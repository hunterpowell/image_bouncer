# Bouncer Screensaver

A fun, customizable bouncing screensaver that displays your own images bouncing around the screen with transparent background support.

## Features

- **Custom Images**: Add your own images to bounce around
- **Fallback Graphics**: Shows colorful rectangles if no images are provided
- **Transparent Background**: Works as an overlay on your desktop
- **Portable**: Single executable file that works anywhere

## Installation

### Option 1: Download Release
Download the latest `bouncer.exe` from the [Releases](../../releases) page.

### Option 2: Build from Source
```bash
git clone https://github.com/yourusername/bouncer-screensaver.git
cd bouncer-screensaver
pip install -r requirements.txt
pyinstaller bouncer.spec
```

## Usage

1. **Run the screensaver**: Double-click `bouncer.exe`
2. **Add custom images**: 
   - An `images` folder will be created next to the executable
   - Add your `.png`, `.jpg`, `.jpeg`, `.gif`, or `.bmp` files to this folder
   - Restart the screensaver to see your images
3. **Exit**: Press `ESC` to close the screensaver

## Requirements

- Windows (tested on Windows 10)
- For building from source:
  - Python 3.7+
  - tkinter
  - Pillow (PIL)
  - playsound3
  - PyInstaller

## How It Works

- Images are automatically resized to 320x240 pixels
- Each time an image hits a screen edge, it changes to the next image
- The screensaver runs fullscreen with a transparent background

## Building

To create your own executable:

```bash
pip install pillow playsound3 pyinstaller
pyinstaller bouncer.spec
```

The built executable will be in the `dist` folder.
