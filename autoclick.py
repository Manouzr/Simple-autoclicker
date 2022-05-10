import keyboard

from pynput.mouse import Button, Controller
import time
import os
mouse = Controller()

def main():
    print("Manou autoclick")
    global cps
    cps = float(input("enter CPS here : "))
    cps = 1/(cps+2)
    clique()
        
        

def clique():
    while True:
        try:
            if keyboard.is_pressed('a'):
                while True:
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    time.sleep(cps)
                    if keyboard.is_pressed('r'):
                        break
            else:
                if keyboard.is_pressed("alt"):
                    clique()
        except:
            if keyboard.is_pressed('u'):
                clique()


if __name__ == "__main__":
    main()
