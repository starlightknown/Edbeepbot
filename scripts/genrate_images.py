from PIL import Image, ImageFont, ImageDraw
from quotes import quotes

FONT_COLOR = "#000000"
FONT_FACE = "Gabriola.ttf"
CENTER = [1822, 1645]
INPUT_FOLDER = "../template_images/"
OUTPUT_FOLDER = "../media/"

def make_cert(name):
    """function to generate certificate"""
    WIDTH, HEIGHT = CENTER
    FONT_SIZE=250
    FONT_FILE = ImageFont.truetype(FONT_FACE, size=FONT_SIZE)

    image_source = Image.open(INPUT_FOLDER + 'eddie.jpg')
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=FONT_FILE)

    while not (name_height<1500 and name_width<2000):
        FONT_SIZE -= 10
        FONT_FILE = ImageFont.truetype(FONT_FACE, size=FONT_SIZE)
        name_width, name_height = draw.textsize(name, font=FONT_FILE)

    text_location = (WIDTH-(name_width//2), HEIGHT-(name_height//2))
    draw.text(text_location, name, fill=FONT_COLOR, font=FONT_FILE)

    image_source.save(OUTPUT_FOLDER + name.replace("\n","").replace("  ","")+".jpg")
    print('printing certificate of: '+name)


for quote in quotes:
    make_cert(quote)