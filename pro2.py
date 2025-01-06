def count_words(text):
    """
    Count the number of words in the given text.
    A word is defined as a sequence of characters separated by whitespace.
    """
    # Split the text by whitespace and count the resulting parts
    words = text.split()
    return len(words)


def main():
    print("Welcome to the Word Counter Program!")
    print("Enter a sentence or paragraph to count the words.")

    # Prompt the user for input
    text = input("Enter your text: ").strip()

    # Handle empty input
    if not text:
        print("Error: You entered an empty text. Please provide some input.")
        return

    # Call the word counting function
    word_count = count_words(text)

    # Display the word count
    print(f"\nThe number of words in your text is: {word_count}")


# Entry point of the program
if __name__ == "__main__":
    main()