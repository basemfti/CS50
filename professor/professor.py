import random

def main():
    level = get_level()
    problems = generate_math_problems(level)
    score = 0
    for problem in problems:
        if solve_problem(problem):
            score += 1
    print(f"score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ['1', '2', '3']:
            return int(level)
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3.")

def generate_math_problems(level):
    problems = []
    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        problems.append((X, Y))
    return problems

def solve_problem(problem):
    X, Y = problem
    Z = X + Y
    tries = 0
    while tries < 3:
        answer = input(f"{X} + {Y} =")
        try:
            if int(answer) == Z:
                return True
            else:
                print("EEE")
                tries += 1
        except ValueError:
            print("EEE")
            tries += 1
    print(f"The correct answer is: {Z}")
    return False

if __name__ == "__main__":
    main()
