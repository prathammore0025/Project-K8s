import sys
import time

def display_lyrics():
    lines = [
        "So I'm loving you every night like it's the last night",
        "Like it's the last night",
        "If the world was ending",
        "I'd wanna be next to you...",
        "If the party was over",
        "And our time on Earth was through",
        "I'd wanna hold you just for a while",
        "And die with a smile",
        "If the world was ending",
        "I'd wanna be next to you",
        "Right next to you"
    ]

    delays = [0.9, 0.7, 1.5, 5.2, 1.0, 6.0, 2.8, 2.9, 0.9, 0.7, 2.3]

    for i, (line, delay) in enumerate(zip(lines, delays)):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.05) 
        print() 
        time.sleep(delay) 

    for _ in range(2):
        print(".")
        time.sleep(0.3)  

display_lyrics()
