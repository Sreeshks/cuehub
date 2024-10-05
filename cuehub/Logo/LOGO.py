from PIL import Image

# ASCII characters used based on pixel brightness (dark to light)
# Adding 'u', 'e', and 'a' to the list so that they can appear in the ASCII art.
ASCII_CHARS = [' ', '+', '+', '+', '+', '*', '*', '*', '*', '*', '*']

# ANSI color codes
RED = "\033[31m"     # Red color for 'e'
GREY = "\033[90m"    # Light grey color for 'a'
RESET = "\033[0m"    # Reset color

def resize_image(image, new_width=90):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.45)  # Adjusting for character width
    return image.resize((new_width, new_height))

def grayscale_image(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // 25]  # Scale pixel value to character index
    return ascii_str

def apply_color(ascii_str):
    # Apply red color to 'e' and light grey to 'a', leaving other characters as they are
    colored_str = ""
    for char in ascii_str:
        if char == '+':
            colored_str += f"{RED}{char}{RESET}"  # Apply red to 'e'
        elif char == '*':
            colored_str += f"{GREY}{char}{RESET}"  # Apply light grey to 'a'
        else:
            colored_str += char
    return colored_str

def convert_image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {image_path}. {e}")
        return
    
    # Resize and convert to grayscale
    image = resize_image(image, new_width)
    image = grayscale_image(image)
    
    # Convert pixels to ASCII characters
    ascii_str = pixels_to_ascii(image)
    
    # Format the string into the correct width
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join(ascii_str[i:(i + new_width)] for i in range(0, ascii_str_len, new_width))
    
    # Apply color to 'e' and 'a'
    colored_ascii_img = apply_color(ascii_img)
    
    return colored_ascii_img

# Test the function with an image file path
image_path = "logo.png"
ascii_image = convert_image_to_ascii(image_path, new_width=100)
print(ascii_image)

# Optionally, write the ASCII art to a file (without colors since terminal handles color)
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)
