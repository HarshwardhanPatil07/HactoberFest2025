def word_frequency(text):
    # Split the text into words
    words = text.split()
    frequency = {}

    # Count the frequency of each word
    for word in words:
        word = word.lower()  # Convert to lowercase for uniformity
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Example usage
if __name__ == "__main__":
    sample_text = "Hello world! Welcome to Hacktoberfest. Hello again!"
    freq = word_frequency(sample_text)
    print(freq)
