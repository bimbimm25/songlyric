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
        ("The winner takes it all......", 0.11),
        ("The game is on again", 0.09),
        ("A lover or a friend", 0.11),
        ("A big thing or a small", 0.12),
        ("The winner takes it all....", 0.10),
        ("So the winner, takes it all", 0.20),
        ("And the loser, has to fall", 0.20)
    ]
    delays = [0, 3.7, 2.2, 1.5, 1.5, 2.5, 2.6]
    
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        sing_lyric(lyric, delays[i], speed)

if __name__ == "__main__":
    sing_song()
