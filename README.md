# DDF-350 Transmitter Splash Screen Replacement

This Python script enables you to replace the splash screen logo of the DDF-350 transmitter by modifying its firmware binary file.

## Features

Converts an input PNG image to monochrome (grayscale).
Verifies image dimensions against the specified width and height.
Embeds the grayscale image data into the binary file at a given offset.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Pillow(PIL library for image processing)

You can install the required libraries using pip:

```bash
pip install pillow
