import time
import random

# List of random texts for typing practice
texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a high-level, interpreted programming language.",
    "Practice makes perfect.",
    "Coding is fun!",
    "Type like the wind.",
]

def get_random_text():
    return random.choice(texts)

def calculate_wpm(text, elapsed_time):
    words = text.split()
    word_count = len(words)
    seconds = elapsed_time / 60.0
    wpm = word_count / seconds
    return wpm

def typing_test():
    text = get_random_text()
    print("Type the following:")
    print(text)

    input("Press Enter to start...")
    start_time = time.time()

    user_input = input("Start typing: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Calculate WPM
    wpm = calculate_wpm(text, elapsed_time)
    print(f"\nYour typing speed: {wpm:.2f} WPM")
    
    # Calculate accuracy
    correct_characters = sum(c1 == c2 for c1, c2 in zip(text, user_input))
    accuracy = (correct_characters / len(text)) * 100
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    while True:
        typing_test()
        another_round = input("Do you want to try another round? (yes/no): ").lower()
        if another_round != "yes":
            print("Thanks for practicing!")
            break



