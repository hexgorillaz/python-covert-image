import os
from PIL import Image

def convert_to_png(image_path, png_path):
    try:
        # Open the image and convert it to RGBA
        image = Image.open(image_path).convert("RGBA")

        # Save the image as a PNG file
        image.save(png_path)
        print(f"Successfully converted {image_path} to {png_path}")
    except Exception as e:
        print(f"Failed to convert {image_path} to {png_path}")
        print(e)

def main():
    # Set the input and output directories
    input_dir = r"M:\GORILLA\HexPIX\_working\images\labs_openai_com"
    output_dir = r"M:\GORILLA\HexPIX\_working\images\open"

    # Make sure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over all the files in the input directory
    for file in os.listdir(input_dir):
        # Get the full path of the input and output files
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, file.rsplit(".", 1)[0] + ".png")

        # Convert the image to PNG format
        convert_to_png(input_file, output_file)

if __name__ == "__main__":
    main()
