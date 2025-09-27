from PIL import Image, ImageDraw, ImageFont
import os

def create_sample_image(filename, text, color, size=(400, 300)):
    """Create a sample image with text"""
    # Create a new image with the specified size and color
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a default font, fallback to basic if not available
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Get text bounding box to center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Calculate position to center the text
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw the text
    draw.text((x, y), text, fill='white', font=font)
    
    # Save the image
    img.save(f'static/images/{filename}')

def main():
    # Create the images directory if it doesn't exist
    os.makedirs('static/images', exist_ok=True)
    
    # Create sample images
    sample_images = [
        ('sample1.jpg', 'Sample Image 1', '#FF6B6B'),
        ('sample2.jpg', 'Sample Image 2', '#4ECDC4'),
        ('sample3.jpg', 'Sample Image 3', '#45B7D1'),
        ('sample4.jpg', 'Sample Image 4', '#96CEB4'),
        ('sample5.jpg', 'Sample Image 5', '#FFEAA7'),
        ('sample6.jpg', 'Sample Image 6', '#DDA0DD'),
    ]
    
    print("Creating sample images...")
    for filename, text, color in sample_images:
        create_sample_image(filename, text, color)
        print(f"Created: {filename}")
    
    print("\nSample images created successfully!")
    print("You can now run the Flask app to see them in the gallery.")

if __name__ == "__main__":
    main()
