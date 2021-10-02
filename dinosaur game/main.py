from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np


class Coordinates():
    replaybutton =(360, 214)
    dinosaur = (149, 239 )


def restart_game():
    pyautogui.click(Coordinates.replaybutton)
    # to keep our bot safe from bird we always keep it down so
    pyautogui.keyDown('down')


def press_space():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')

    time.sleep(0.05)

    # printing the "Jump" statement on the
    # terminal to see the current output
    print("jump")
    time.sleep(0.50)

    # releasing the Space Key
    # pyautogui.keyUp('space')
    #
    # # again pressing the Down Key to keep my Bot always down
    # pyautogui.keyDown('down')


def image_grab():
    # defining the coordinates of box in front of dinosaur
    box = (Coordinates.dinosaur[0]+30, Coordinates.dinosaur[1],
           Coordinates.dinosaur[0]+120, Coordinates.dinosaur[1]+2)

    # grabbing all the pixels values in form of RGB tupples
    image = ImageGrab.grab(box)

    # converting RGB to Grayscale to
    # make processing easy and result faster
    grayImage = ImageOps.grayscale(image)

    # using numpy to get sum of all grayscale pixels
    a = np.array(grayImage.getcolors())

    # returning the sum
    print(a.sum())
    return a.sum()


restart_game()
while True:
    if (image_grab() != 435):
        press_space()
        time.sleep(0.1)



