def load_words_from_file(filepath):
    """
    Reads words from a file and returns them as a list.
    Assumes one word per line.
    """
    words = []
    with open(filepath, 'r') as file:
        for line in file:
            cleaned_word = line.strip()
            if cleaned_word: # Make sure it's not an empty line
                words.append(cleaned_word)
    return words

def main():
    # Load the words from the specific file in your project folder
    word_list = load_words_from_file("words.txt")
    
    # 1. Count the appearance of each word using a dictionary
    word_counts = {}
    for word in word_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
            
    # 2. Find the length of the longest word to align the colons perfectly
    max_length = 0
    for word in word_counts:
        if len(word) > max_length:
            max_length = len(word)
            
    # 3. Print the histogram
    for word, count in word_counts.items():
        # Multiply the 'x' character by the count to create the bar
        bar = 'x' * count
        
        # Use an f-string to print the formatted row
        print(f"{word:<{max_length}} : {bar}")

if __name__ == '__main__':
    main()
