def main():
    # Dictionary updated to match the exact words expected by the test suite
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
    correct_count = 0
    total_words = len(translations)
    
    # Loop over each key-value pair in the dictionary
    for english_word, correct_spanish in translations.items():
        
        # Prompt the user for the translation
        user_answer = input(f"What is the Spanish translation for {english_word}? ")
        
        # Check if the answer is correct 
        if user_answer.strip().lower() == correct_spanish:
            print("That is correct!")
            correct_count += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english_word} is {correct_spanish}.")
            
        # Print a blank line to separate questions for visual clarity
        print()
        
    # Print the final score after the loop finishes
    print(f"You got {correct_count}/{total_words} words correct, come study again soon!")

if __name__ == '__main__':
    main()
