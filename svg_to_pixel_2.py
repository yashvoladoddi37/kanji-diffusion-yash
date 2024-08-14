import os
from PIL import Image
import xml.etree.ElementTree as ET
import cairosvg

def remove_numbers_from_svg(svg_path):
    # Parse the SVG file
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Define the SVG namespace
    ns = {'svg': 'http://www.w3.org/2000/svg'}

    # Locate and remove all text elements
    for text in root.findall('.//svg:text', ns):
        for parent in root.iter():
            if text in parent:
                parent.remove(text)
                break

    # Save the modified SVG with a new name
    modified_svg_path = svg_path.replace('.svg', '_modified.svg')
    tree.write(modified_svg_path)
    return modified_svg_path

def svg_to_png_jpg(svg_path, png_path, jpg_path, size=(256, 256)):
    try:
        # First, strip the numbers from the SVG
        modified_svg_path = remove_numbers_from_svg(svg_path)

        # Convert the cleaned SVG to PNG with a white background using cairosvg
        cairosvg.svg2png(url=modified_svg_path, write_to=png_path, output_width=size[0], output_height=size[1], 
                         background_color="white")

        # Open the resulting PNG and convert it to JPG
        with Image.open(png_path) as img:
            # Convert to grayscale
            img = img.convert('L')
            
            # Apply a threshold to ensure pure black and white
            threshold = 250  # Adjust this value if needed
            img = img.point(lambda x: 0 if x < threshold else 255, '1')
            
            # Create a white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            
            # Paste the black and white image onto the white background
            background.paste(img, (0, 0))
            
            # Save the final image as a high-quality JPG
            background.save(jpg_path, 'JPEG', quality=95)

        # Clean up the temporary modified SVG file
        os.remove(modified_svg_path)

        print(f"Converted {svg_path} to {png_path} and {jpg_path}")
    except Exception as e:
        print(f"Error converting {svg_path}: {str(e)}")

# Set the paths to your directories
svg_dir = 'D:\\sakana-ai\\sakana-ai-2\\kanji-svg-path'
png_dir = 'D:\\sakana-ai\\sakana-ai-2\\kanji-png-path'
jpg_dir = 'D:\\sakana-ai\\sakana-ai-2\\kanji-jpg-path'

# Make sure the output directories exist
os.makedirs(png_dir, exist_ok=True)
os.makedirs(jpg_dir, exist_ok=True)

# Loop through all SVG files in the directory
for svg_filename in os.listdir(svg_dir):
    if svg_filename.endswith('.svg'):
        svg_path = os.path.join(svg_dir, svg_filename)
        png_path = os.path.join(png_dir, svg_filename.replace('.svg', '.png'))
        jpg_path = os.path.join(jpg_dir, svg_filename.replace('.svg', '.jpg'))

        svg_to_png_jpg(svg_path, png_path, jpg_path)
