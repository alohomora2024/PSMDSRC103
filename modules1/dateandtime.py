import time

def pause():
    for i in range(10, 0, -1):
        print(f"The program will end in {i}…")
        time.sleep(1)