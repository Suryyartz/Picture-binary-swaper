# DDF-350 Transmitter Splash Screen Replacement

This Python script enables you to replace the splash screen logo of the DDF-350 transmitter by modifying its firmware binary file. It converts an image to the RGB565 format and embeds it into the binary file at a specified memory address range.

## Features

- Converts an input image to the RGB565 format.
- Automatically resizes the image to fit the pixel dimensions specified by the firmware binary's memory range.
- Replaces the logo in the firmware binary and saves the modified file.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- [Pillow](https://python-pillow.org/) (PIL library for image processing)
- NumPy

You can install the required libraries using pip:

```bash
pip install pillow numpy
