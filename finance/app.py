import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get current user ID
    user_id = session["user_id"]

    # Query to get all stocks grouped by symbol for the user
    stocks = db.execute(
        "SELECT symbol, price, SUM(shares) AS totalShares "
        "FROM transactions WHERE user_id = ? GROUP BY symbol",
        user_id
    )


    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    if not user_cash:
        return apology("Unable to retrieve user cash", 400)

    cash = user_cash[0]["cash"]

    total = cash
    for stock in stocks:
        total += stock["price"] * stock["totalShares"]


    # Render portfolio page
    return render_template(
        "index.html",
        stocks=stocks,
        cash=usd(cash),
        total=usd(total)  # Ensure the total is formatted as currency
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol")

        elif not shares or  not shares.isdigit()or int(shares) <=0:
            return apology("must provide a positive integer ")
        quote=lookup(symbol)
        if quote is None:
            return apology("symbol not found")


        price = quote["price"]
        total_cost = int(shares) * price

        # Query user's cash
        cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                          user_id=session["user_id"])[0]["cash"]

        if cash < total_cost:
            return apology("not enough cash")

        # Update user's cash
        db.execute("UPDATE users SET cash = cash - :total_cost WHERE id = :user_id",
                   total_cost=total_cost, user_id=session["user_id"])

        # Insert transaction record
        db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)",
                   user_id=session["user_id"], symbol=symbol.upper(), shares=shares, price=price)

        # Flash success message
        flash(f"Bought {shares} shares of {symbol.upper()} for {total_cost}!")
        return redirect("/")

    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY timestamp DESC", user_id=session["user_id"])

    return render_template("history.html", transactions=transactions)  # Fixed variable name here



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method=="POST":
       symbol=request.form.get("symbol")
       if not symbol:
           return apology("Missing symbol",400)

       quote=lookup(symbol)

       if not quote:
         return apology("Invalid symbol",400)
       return render_template("quote.html",quote=quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Clear any existing session data
    session.clear()

    if request.method == "POST":
        # Get and sanitize form inputs
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        confirmation = request.form.get("confirmation").strip()

        # Validate inputs
        if not username:
            return apology("must provide username", 400)
        elif not password:
            return apology("must provide password", 400)
        elif not confirmation:
            return apology("must confirm password", 400)
        elif password != confirmation:
            return apology("passwords do not match", 400)

        # Check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if rows:
            return apology("username already exists", 400)

        # Insert the new user into the database
        try:
            hashed_password = generate_password_hash(password)
            db.execute(
                "INSERT INTO users (username, hash) VALUES (?, ?)", username, hashed_password
            )
        except Exception as e:
            return apology(f"An error occurred: {str(e)}", 500)

        # Get the new user's id and log them in
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]

        # Redirect to the homepage
        return redirect("/")
    else:
        # Render the registration page
        return render_template("register.html")






@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id= :user_id GROUP BY symbol HAVING total_shares>0", user_id=session["user_id"])

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()  # Fixing the typo here
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol")
        elif not shares or int(shares) <= 0:
            return apology("must provide a positive integer number of shares")
        else:
            shares = int(shares)

        for stock in stocks:
            if stock["symbol"] == symbol:
                if stock["total_shares"] < shares:  # Corrected reference to "total_shares"
                    return apology("not enough shares")
                else:
                    quote = lookup(symbol)
                    if quote is None:
                        return apology("symbol not found")
                    price = quote["price"]
                    total_sale = shares * price
                    db.execute("UPDATE users SET cash = cash + :total_sale WHERE id = :user_id", total_sale=total_sale, user_id=session["user_id"])
                    db.execute("INSERT INTO transactions (user_id, symbol, shares, price) VALUES (:user_id, :symbol, :shares, :price)", user_id=session["user_id"], symbol=symbol, shares=-shares, price=price)
                    flash(f"Sold {shares} shares of {symbol} for {usd(total_sale)}!")
                    return redirect("/")

        return apology("symbol not found")

    else:
        return render_template("sell.html", stocks=stocks)

