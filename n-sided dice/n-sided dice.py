import random

def main():
    sides = int(input("How many sides does your dice have? "))
    
    roll = random.randint(1, sides)
    
    print("Your roll is", roll)

if __name__ == '__main__':
    main()
