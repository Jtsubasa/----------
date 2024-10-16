import tkinter as tk
import pygame
import random
from PIL import Image, ImageTk
import sys
import keyboard

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

PLAYER_X = 300
PLAYER_Y = 550

class Main:
    
    def quit(self):
        input

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Shooting Game")
    cv = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
    cv.pack()

    main = Main()
    main.simulation.loop()
    root.mainloop()