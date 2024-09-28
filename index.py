from PIL import Image
import os

# convert .jpg to .ico


def convert_jpg_to_ico(input_jpg, output_ico):
    try:
        # Open the JPG image
        with Image.open(input_jpg) as img:
            # Convert to ICO
            img.save(output_ico, format="ICO")
            print(f"Successfully converted {input_jpg} to {output_ico}.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    input_jpg_path = "icon.jpg"  # Change this to your input JPG file path
    output_ico_path = "icon.ico"  # Desired output ICO file path

    # Ensure the input file exists
    if not os.path.isfile(input_jpg_path):
        print(f"The file {input_jpg_path} does not exist.")
    else:
        convert_jpg_to_ico(input_jpg_path, output_ico_path)
