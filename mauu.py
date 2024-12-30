import sys
import time

def display_lyrics():
    # Define the updated lyrics with lines as elements of the list
    lines = [
        "So I'm loving you every night like it's the last night",
        "Like it's the last night",
        "If the world was ending",
        "I'd wanna be next to you",
        "If the party was over",
        "And our time on Earth was through",
        "I'd wanna hold you just for a while",
        "And die with a smile",
        "If the world was ending",
        "I'd wanna be next to you",
        "Right next to you"
    ]

    # Define delays for each line
    delays = [0.6, 0.7, 1.0, 4.6, 1.0, 3.6, 1.7, 2.0, 0.9, 0.7, 0.8]

    # Loop through each line and each character with delays
    for i, (line, delay) in enumerate(zip(lines, delays)):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.05)  # Delay between characters
        print()  # Move to the next line
        time.sleep(delay)  # Delay between lines

    # Add two lines with a single dot after the lyrics
    for _ in range(2):
        print(".")
        time.sleep(0.3)  # Delay for dramatic effect

# Call the function to display the lyrics
display_lyrics()
