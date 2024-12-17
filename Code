from PIL import Image
import numpy as np

def convert_image_to_rgb565(image_path, target_pixels):
    image = Image.open(image_path)
    image = image.convert("RGB")
    
    height = 41
    width = target_pixels // height
    
    if width * height != target_pixels:
        width = (target_pixels + height - 1) // height
    
    image = image.resize((width, height), Image.LANCZOS)
    print(f"Resized image size: {image.size}")
    print(f"Total pixels: {width * height}")
    
    rgb_data = np.array(image)
    rgb565 = ((rgb_data[..., 0] >> 3) << 11) | ((rgb_data[..., 1] >> 2) << 5) | (rgb_data[..., 2] >> 3)
    flattened = rgb565.flatten()
    
    return flattened[:target_pixels]

def replace_logo_in_binary(binary_file_path, start_address, end_address, new_logo_data):
    with open(binary_file_path, 'rb') as file:
        binary_data = bytearray(file.read())
    
    expected_size = (end_address - start_address + 1)
    new_logo_bytes = bytearray()
    
    for pixel in new_logo_data:
        new_logo_bytes.append((pixel >> 8) & 0xFF)
        new_logo_bytes.append(pixel & 0xFF)
    
    binary_data[start_address:end_address + 1] = new_logo_bytes
    
    modified_file_path = 'modified_DDF.bin'
    with open(modified_file_path, 'wb') as modified_file:
        modified_file.write(binary_data)
    
    print(f"Logo replaced and modified binary file saved as '{modified_file_path}'.")

def calculate_total_pixels(start_address, end_address):
    size_in_bytes = end_address - start_address + 1
    return size_in_bytes // 2  # RGB565 format, 2 bytes per pixel

def main():
    binary_file_path = 'DDF.bin'
    new_logo_path = 'image.png'
    start_address = 0x0006933b
    end_address = 0x0006a614
    
    total_pixels = calculate_total_pixels(start_address, end_address)
    print(f"Expected number of pixels: {total_pixels}")
    
    rgb565_data = convert_image_to_rgb565(new_logo_path, total_pixels)
    replace_logo_in_binary(binary_file_path, start_address, end_address, rgb565_data)

if __name__ == '__main__':
    main()
