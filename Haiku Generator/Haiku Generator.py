from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    print("Creating your haiku...\n")

    prompt = (
        f"Write a 3-line haiku about {topic}. "
        f"Include the name {name} in the haiku. "
        f"Follow the 5-7-5 syllable structure."
    )

    haiku = call_gpt(prompt)

    print(haiku)

if __name__ == '__main__':
    main()
