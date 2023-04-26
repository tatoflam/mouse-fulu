import pyautogui
import time

def main():
    
    pyautogui.moveTo(500, 500)
    
    vpos = 200
    hpos = 200
    move_sec = 2
    sleep_sec = 20
    while True:
        pyautogui.move(vpos, hpos, duration=move_sec)
        vpos *= -1
        hpos *= -1
        time.sleep(sleep_sec)

if __name__ == "__main__":
    main()