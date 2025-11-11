import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Tears stream down your face", 0.15),
        ("When you lose something you cannot replace", 0.13),
        ("Tears stream down your face, and I", 0.15),
        ("Tears stream down your face", 0.15),
        ("I promise you I will learn from my mistakes", 0.10),
        ("Tears stream down your face, and I......", 0.20),
    ]
    delays = [4.5, 1.5, 2.6, 8.2, 2.3, 3]
    
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        sing_lyric(lyric, delays[i], speed)

if __name__ == "__main__":
    sing_song()
