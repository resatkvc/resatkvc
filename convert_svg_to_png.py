import cairosvg
import os

def convert_svg_to_png(svg_path, png_path):
    """Convert SVG file to PNG"""
    try:
        cairosvg.svg2png(url=svg_path, write_to=png_path)
        print(f"Converted {svg_path} to {png_path}")
    except Exception as e:
        print(f"Error converting {svg_path}: {e}")

# Convert the SVG files to PNG
convert_svg_to_png('assets/line-knowledge.png', 'assets/line-knowledge.png')
convert_svg_to_png('assets/radar-motivation.png', 'assets/radar-motivation.png')
convert_svg_to_png('profile-3d-contrib/profile-night-green.svg', 'profile-3d-contrib/profile-night-green.png')

print("Conversion completed!") 