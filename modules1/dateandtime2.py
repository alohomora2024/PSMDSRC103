import time

def pause():
    for i in range(10, 0, -1):
        print(f"The program will end in {i}…")
        time.sleep(1)
pause()

def current_time():
    t = time.strftime("%I:%M %p")
    return t
print(current_time())
