import random

NUM_PAIRS = 3

# NOTE: Your starter code might already import or define clear_terminal(). 
# If it does, you can delete this helper function to avoid duplicates!
def clear_terminal():
    # A simple way to clear the screen by printing blank lines
    print('\n' * 20)

def get_valid_index(displayed_list, first_index=-1):
    """
    Prompts the user for an index and validates it based on game rules.
    Loops until a valid index is provided.
    """
    while True:
        user_input = input("Enter an index: ")
        
        # 1. Check if input is a valid number
        try:
            idx = int(user_input)
        except ValueError:
            print("Not a number. Try again.")
            continue
            
        # 2. Check if the index is in bounds
        if idx < 0 or idx >= len(displayed_list):
            print("Invalid index. Try again.")
            continue
            
        # 3. Check if the user entered the same index twice in a turn
        if idx == first_index:
            print("You entered the same index twice. Try again.")
            continue
            
        # 4. Check if the number has already been matched/revealed
        if displayed_list[idx] != '*':
            print("This number has already been matched. Try again.")
            continue
            
        return idx

def main():
    # Milestone #1: Create the truth list
    truth_list = []
    for i in range(NUM_PAIRS):
        truth_list.append(i)
        truth_list.append(i)
        
    # Milestone #2: Shuffle the list
    random.shuffle(truth_list)
    # print(truth_list) # (Commented out as instructed for the final program)
    
    # Milestone #3: Create a displayed list
    displayed_list = ['*'] * (NUM_PAIRS * 2)
    
    # Milestone #6: Play multiple turns until all '*' are gone
    while '*' in displayed_list:
        print(displayed_list)
        
        # Milestone #4: Get two valid indices from the user
        index1 = get_valid_index(displayed_list)
        # Pass the first index so the function can check if the user repeats it
        index2 = get_valid_index(displayed_list, first_index=index1) 
        
        # Milestone #5: Check if the two indices match
        if truth_list[index1] == truth_list[index2]:
            # Update displayed list
            displayed_list[index1] = truth_list[index1]
            displayed_list[index2] = truth_list[index2]
            print("Match!")
            clear_terminal()
        else:
            print(f"Value at index {index1} is {truth_list[index1]}")
            print(f"Value at index {index2} is {truth_list[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue... ")
            clear_terminal()
            
    # When the loop finishes, the game is won
    print(displayed_list)
    print("Congratulations! You won!")

if __name__ == '__main__':
    main()
