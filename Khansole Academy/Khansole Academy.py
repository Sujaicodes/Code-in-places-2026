import random

def main():
    print("Khansole Academy")
    print()

    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)

    correct_answer = num1 + num2

    print(f"What is {num1} + {num2}?")
    print()

    user_answer = int(input("Your answer: "))
    print()

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print()
        print(f"The expected answer is {correct_answer}")

if __name__ == '__main__':
    main()
