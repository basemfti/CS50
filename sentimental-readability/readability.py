from cs50 import get_string


def main():
    # Get input text
    text = get_string("Text: ")

    # Calculate letters, words, and sentences
    leter = letters(text)
    word = words(text)
    sent = sentences(text)


   
    l = float(leter) / word * 100
    s = float(sent) / word * 100

    # Calculate index
    index = round(0.0588 * l - 0.296 * s - 15.8)

    # Print grade level
    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


def letters(text):
    # Count alphabetic characters
    j = 0
    for ch in text:
        if ch.isalpha():
            j += 1
    return j


def words(text):
    # Count words (spaces + 1)
    j = 1
    for ch in text:
        if ch == ' ':
            j += 1
    return j


def sentences(text):
    # Count sentences (ends with ., !, ?)
    j = 0
    for ch in text:
        if ch in ['.', '!', '?']:
            j += 1
    return j


if __name__ == "__main__":
    main()
