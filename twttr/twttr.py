
def main():
    user_input = input("input: ")
    # Remove vowels from the input text
    text_without_vowels = shorten(user_input)
    # Output the text without vowels
    print("output:", text_without_vowels)


def shorten(word):
    vowels = "aeiouAEIOU"
    # Use a list comprehension to create a new string with vowels removed
    text_without_vowels = ''.join([char for char in word if char not in vowels])
    return text_without_vowels


if __name__ == "__main__":
    main()


