from PIL import Image

def create_blank_image(width, height, color=(255, 255, 255), output_path="blank_image.png"):
    """
    Create a blank image with specified dimensions and color
    
    Args:
        width (int): Width of the image in pixels
        height (int): Height of the image in pixels
        color (tuple): RGB color tuple (default: white)
        output_path (str): Path where the image will be saved
    """
    # Create new image with white background
    image = Image.new('RGB', (width, height), color)
    
    # Save the image
    image.save(output_path)
    return image

# Example usage
if __name__ == "__main__":
    # Create a white image (300x200 pixels)
    create_blank_image(300, 200)
    
    # Create a black image (500x500 pixels)
    create_blank_image(500, 500, color=(0, 0, 0), output_path="black_image.png")
    
    # Create a red image (400x300 pixels)
    create_blank_image(400, 300, color=(255, 0, 0), output_path="red_image.png")