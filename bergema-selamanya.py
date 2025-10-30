import sys
from threading import Thread, Lock
import time

lock = Lock()

def animate_text(text, delay):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def lirik_lagu(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)


def animate_lirik():
    lirik = [
        ("Bersandar padaku, taruh di bahuku", 0.15),
        ("Relakan semua, bebas semaumu", 0.14),
        ("Percayalah ini sayang terlewatkan", 0.13),
        ("Kusampaikan dalam nyanyian, bergema sampai selamanya", 0.13),
        ("🎶🎶.... ", 0.3),
        ("Dunia pasti ada akhirnya", 0.1),
        ("Bintang bintang pun ada umurnya", 0.1),
        ("Maka tenang saja kita disini berdua", 0.2),
        ("Nikmati sementara yang ada...", 0.2)
    ]

    delay = [2, 1.5, 1.2, 1.5, 1.5, 20, 3, 2.6, 3.5]
    print("\n== bergema sampai selamanya - nadhif basalamah ==", )
    print()
    for i in range(len(lirik)):
        lyric, speed = lirik[i]
        lirik_lagu(lyric, delay[i], speed)


if __name__ == "__main__":
    animate_lirik()