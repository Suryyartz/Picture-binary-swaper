# pip install pillow

from PIL import Image

def encode_png_to_monochrome(input_image, output_file, width, height, offset):
    """
    Overwrite a binary file with data from a grayscale PNG image, starting at the specified offset.
    """
    # Open the input PNG image
    img = Image.open(input_image).convert("L")  # Ensure the image is in grayscale mode ("L")
    
    # Check dimensions
    if img.size != (width, height):
        raise ValueError(f"Image dimensions do not match the expected size: {width}x{height}")
    
    # Get the raw pixel data
    raw_data = img.tobytes()

    # Open the binary file in read/write mode
    with open(output_file, 'r+b') as f:
        # Seek to the given offset
        f.seek(offset)
        # Write the image data into the binary file
        f.write(raw_data)

if __name__ == "__main__":
    # Example usage
    input_bin_file = "DDF.bin"  # Binary file to overwrite
    modified_image = "lumo.png"  # Modified PNG file to write back
    offset = 0x000692A4  # Offset in the binary file
    width, height = 105, 50  # Dimensions of the image

    # Encode the PNG data back into the binary file
    encode_png_to_monochrome(modified_image, input_bin_file, width, height, offset)
