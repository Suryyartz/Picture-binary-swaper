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

## Template
You should use this pictures as a temp for ur logo.
![lumo_des](https://github.com/user-attachments/assets/3f3c2083-8d65-49f0-8774-cc5240bb3a86)
![lumo](https://github.com/user-attachments/assets/824c4990-b2d4-4311-866b-e533dd37a689)

All assets, including this logo, are provided for educational purposes only. I do not claim authorship nor endorsement from the original creator. The binary firmware is provided by DumboRC.
