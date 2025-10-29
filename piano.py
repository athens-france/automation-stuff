from pymouse import PyMouse
from PIL import ImageGrab
import time

m = PyMouse()
target_color = (0x00, 0x00, 0x00) 

def find_color_on_screen(target_rgb):
    screen = ImageGrab.grab()
    screen_width, screen_height = screen.size
    width = 200
    height = 350

    left = (screen_width - width) // 2 - 50
    top = (screen_height - height) // 2 + 90
    right = left + width
    bottom = top + height

    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    pixels = screenshot.load()

    for y in range(height):
        for x in range(width):
            if pixels[x, y][:3] == target_rgb:
                return (left + x, top + y)
    return None

def main():
    print("looking for black")
    while True:
        pos = find_color_on_screen(target_color)
        if pos:
            print(f"found color at: {pos}")
            m.click(pos[0], pos[1])

if __name__ == "__main__":
    main()
