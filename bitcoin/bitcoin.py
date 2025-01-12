import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        return float(data['bpi']['USD']['rate_float'])
    except (requests.RequestException, KeyError, ValueError):
        print("Failed to retrieve Bitcoin price.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    cost_in_usd = bitcoins * bitcoin_price

    print(f"${cost_in_usd:,.4f}")

if __name__ == "__main__":
    main()
