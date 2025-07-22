import tkinter as tk
import random as rand
from PIL import Image, ImageTk
import sys
import os
from pathlib import Path
from playsound3 import playsound

# needed to add pngs to exe
def resource_path(relative_path):
    try:
        # for exe
        base_path = sys._MEIPASS
    except Exception:
        # for dev
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_images_folder():
    # always use the directory where the executable is located
    if getattr(sys, 'frozen', False):
        # running as exe
        exe_dir = os.path.dirname(sys.executable)  # ← This uses where the EXE is located
    else:
        # running as script (for dev)
        exe_dir = os.path.dirname(os.path.abspath(__file__))
    
    images_dir = os.path.join(exe_dir, "images")
    os.makedirs(images_dir, exist_ok=True)
    return images_dir

class Bouncer:
    def __init__(self):
        self.root = tk.Tk()

        self.setup_window()

        self.width = 320
        self.height = 240

        self.speed = 3

        # # comment out this, uncomment below to force a corner hit
        # # initial pos, center of screen
        # self.x = self.root.winfo_screenwidth()/2 - self.width/2
        # self.y = self.root.winfo_screenheight()/2 - self.width/2

        # #small variance in starting pos
        # self.x += rand.randint(-100, 100)
        # self.y += rand.randint(-100, 100)

        # # speed, random direction
        # dir = [self.speed, -self.speed]
        # self.dx = rand.choice(dir)
        # self.dy = rand.choice(dir)

        # comment out the above, uncomment this to force a corner hit
        self.x = 100
        self.y = 100
        self.dx = -3
        self.dy = -3

        self.images = []
        self.load_images()
        self.current_image_index = 0

        self.canvas = tk.Canvas(self.root, highlightthickness=0, bg='#123456')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.root.bind('<Escape>', self.quit_app)

    def load_images(self):

        images_folder = get_images_folder()
        suffixes = [".png", ".jpg", ".jpeg", ".gif", ".bmp"]
        print(f"looking for images in: {images_folder}")

        for file in Path(images_folder).iterdir():
            # filters for only images
            if file.suffix.lower() in suffixes:
                img = Image.open(file)
                img = img.resize((self.width, self.height), Image.Resampling.NEAREST)
                photo = ImageTk.PhotoImage(img)
                self.images.append(photo)
                print(f"loaded image: {file.name}")
        # random order :)
        rand.shuffle(self.images)

        # if no images found, use some rectangles
        if not self.images:
            print("no images found, creating default")
            colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
            for color in colors:
                img = Image.new('RGB', (self.width, self.height), color)
                photo = ImageTk.PhotoImage(img)
                self.images.append(photo)

    def setup_window(self):
        #remove window decorations
        self.root.overrideredirect(True)
        # always on top
        self.root.wm_attributes('-topmost', True)
        # make #123456 transparent
        self.root.wm_attributes('-transparentcolor', '#123456')

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # set window to fullscreen
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

    def update_pos(self):

        # update pos
        self.x += self.dx
        self.y += self.dy

        collision = False
        corner = False

        top = bool(self.y + self.height >= self.screen_height)
        right = bool(self.x + self.width >= self.screen_width)
        bottom = bool(self.y <= 0)
        left = bool(self.x <= 0)

        # bounce on collision
        if right:
            self.dx = -self.dx
            collision = True
            if top or bottom:
                corner = True
        if top:
            self.dy = -self.dy
            collision = True
            if left or right:
                corner = True
        if left:
            self.dx = -self.dx
            collision = True
            if top or bottom:
                corner = True
        if bottom:
            self.dy = -self.dy
            collision = True
            if left or right:
                corner = True

        if collision:
            self.change_image()
            if corner:
                sound_path = resource_path('taco_baco.mp3')
                playsound(sound_path)

    def change_image(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.images)

    def draw(self):
        self.canvas.delete("all")

        # force a redraw of the background with the transparent color, prevents weird trails
        self.canvas.create_rectangle(
            0, 0, 
            self.screen_width, self.screen_height, 
            fill = '#123456', 
            outline = ''
        )

        self.canvas.create_image(
            self.x, self.y,
            image = self.images[self.current_image_index],
            anchor = "nw"
        )

    def animate(self):
        # main animation loop
        self.update_pos()
        self.draw()

        # schedule next frame (roughly 60 FPS)
        self.root.after(17, self.animate)

    def quit_app(self, event = None):
        self.root.destroy()

    def run(self):
        self.animate()
        self.root.mainloop()

if __name__ == "__main__":
    screensaver = Bouncer()
    screensaver.run()