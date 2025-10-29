from pymouse import PyMouse
from PIL import ImageGrab
import time
m = PyMouse()

target_color = (0x4b, 0xdb, 0x6a)  #4bdb6a

def find_color_on_screen(target_rgb):

    screenshot = ImageGrab.grab()
    pixels = screenshot.load()
    width, height = screenshot.size

    for y in range(height):
        for x in range(width):
            if pixels[x, y][:3] == target_rgb:
                return (x, y)
    return None

def main():
    print("looking")
    while True:
        pos = find_color_on_screen(target_color)
        if pos:
            print(f"found color at: {pos}")
            m.click(pos[0], pos[1])
        time.sleep(0.5)

if __name__ == "__main__":
    main()
