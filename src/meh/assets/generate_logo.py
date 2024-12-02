from PIL import Image, ImageDraw, ImageFont
import os

def create_logo():
    # Create a new image with a transparent background
    # Make canvas larger to accommodate text
    size = (800, 1000)  # Increased height for text
    img = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw a stylized camera lens/eye
    center = (size[0] // 2, size[1] // 2 - 100)  # Moved up to make room for text
    radius = 300
    
    # Outer circle (lens body)
    draw.ellipse([
        center[0] - radius, 
        center[1] - radius,
        center[0] + radius, 
        center[1] + radius
    ], outline=(50, 120, 190), width=15)

    # Inner circle (iris)
    inner_radius = radius * 0.7
    draw.ellipse([
        center[0] - inner_radius,
        center[1] - inner_radius,
        center[0] + inner_radius,
        center[1] + inner_radius
    ], outline=(70, 150, 220), width=10)

    # Center circle (pupil)
    pupil_radius = radius * 0.3
    draw.ellipse([
        center[0] - pupil_radius,
        center[1] - pupil_radius,
        center[0] + pupil_radius,
        center[1] + pupil_radius
    ], fill=(90, 180, 250))

    # Add text "MEH"
    try:
        font_size = 200  # Increased font size
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except OSError:
        font = ImageFont.load_default()

    text = "MEH"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    text_position = (
        center[0] - text_width // 2,
        center[1] + radius + 50  # Increased spacing from the circle
    )
    
    draw.text(text_position, text, font=font, fill=(50, 120, 190))

    # Save in different formats and sizes
    os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
    
    # Save full size PNG with transparency
    img.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png"))
    
    # Save a smaller version for favicon
    favicon_size = (32, 32)
    favicon = img.resize(favicon_size, Image.Resampling.LANCZOS)
    favicon.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), "favicon.png"))

if __name__ == "__main__":
    create_logo()
