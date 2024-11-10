from PIL import Image
import os
import easygui
from easygui import *

def resizer():
    print("Please select the image you want to compress")
    image_file = easygui.fileopenbox()
    if not image_file:
        msgbox("No file selected. Exiting.")
        return  # Exit if no file is selected

    filepath = os.path.join(os.getcwd(), image_file)

    # Create the "compressed" folder if it doesn't exist
    compressed_folder = os.path.join(os.getcwd(), "compressed")
    if not os.path.exists(compressed_folder):
        os.makedirs(compressed_folder)
        print(f"Compressed folder created at: {compressed_folder}")
    else:
        print(f"Compressed folder already exists at: {compressed_folder}")

    filename, filextension = os.path.splitext(image_file)
    img = Image.open(filepath)
    text = "Enter quality on a scale of 10 to 100 (default value is 50)"

    if filextension == ".jpeg" or filextension == ".jpg":
        qual = integerbox(text, 50, lowerbound=10, upperbound=100)
        # Save the compressed image to the "compressed" folder
        save_path = os.path.join(compressed_folder, filename + "_compressed" + ".jpeg")
        img.save(
            save_path,
            "JPEG",
            optimize=True,
            quality=qual
        )
        msgbox(f"Your compressed image has been saved in the 'compressed' folder at {save_path}")

    elif filextension == ".png":
        img.convert("P", palette=Image.ADAPTIVE, colors=256)
        # Save the compressed image to the "compressed" folder
        save_path = os.path.join(compressed_folder, filename + "_compressed" + ".png")
        img.save(
            save_path,
            optimize=True,
            quality=10
        )
        msgbox(f"Please note that due to the file format being png it may not get compressed much.\nYour compressed image has been saved in the 'compressed' folder at {save_path}")
        
    else:
        print("Invalid filetype")
        msgbox("Invalid file type selected. Please choose a valid image format (.jpeg, .jpg, .png).")

    return

resizer()
