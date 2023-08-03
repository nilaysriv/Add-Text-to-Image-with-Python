import os
import openpyxl
from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(font_file, font_size, image_path, text, x, y, color="black"):
    try:
        # Load an input
        image = Image.open(image_path)

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # Load the font
        font = ImageFont.truetype(font_file, font_size)

        # Calculate text size
        text_bbox = draw.textbbox((0, 0), text, font=font)

        # Add text to the image
        draw.text((x, y), text, font=font, fill=color)

        # Save the output image
        output_path = os.path.splitext(image_path)[0] + "_" + text + ".jpg"
        image.save(output_path)
        print(f"Text added to the image and saved as {output_path}")

    except Exception as e:
        print("Error:", e)

def main():
    font_file = input("Enter the absolute path to the font file (e.g., /path/to/font.ttf): ")
    font_size = int(input("Enter the font size: "))
    image_path = input("Enter the path to the image: ")

    #Excel file
    excel_file = input("Enter the path to the Excel file: ")
    wb = openpyxl.load_workbook(excel_file)
    sheet = wb.active

    #Coordinates and color
    x = int(input("Enter the x-coordinate of the text: "))
    y = int(input("Enter the y-coordinate of the text: "))
    color = input("Enter the color of the text (e.g., black, white, red): ")

    for row in sheet.iter_rows():
        text = row[0].value

        # Add the text to the image with the same coordinates and color
        add_text_to_image(font_file, font_size, image_path, text, x, y, color)

if __name__ == "__main__":
    main()
