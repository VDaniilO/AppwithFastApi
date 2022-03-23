from PIL import Image, ImageDraw, ImageFont, ImageFilter

try:
    newImage = Image.open("test.jpg")
except FileNotFoundError:
    print("File not found")

def new_photo(defPhoto):
    updatePhoto = ImageDraw.Draw(defPhoto)

    text = "whater_mark"
    font = ImageFont.truetype("arial.ttf", size = 40)

    updatePhoto.text((800, 540), text, font = font)
    defPhoto.save('watermarked.jpg')

new_photo(newImage)
