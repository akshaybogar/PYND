from PIL import Image, ImageDraw, ImageFont
from random import randint
from quote_engine import QuoteModel

def resize_image(img, width):
    wpercent = (width/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    return img.resize((width,hsize), Image.ANTIALIAS)

def get_randomx(rmg):
    x_min = (rmg.size[0] * 8) // 100
    x_max = (rmg.size[0] * 50) // 100
    return randint(x_min, x_max)

def get_randomy(rmg, line_height, lines):
    y_min = (rmg.size[1] * 4) // 100
    y_max = (rmg.size[1] * 90) //100
    y_max -= (len(lines)*line_height)
    return randint(y_min, y_max)

def text_wrap(text, font, max_width):
    lines = []
    if font.getsize(text)[0]  <= max_width:
        lines.append(text)
    else:
        words = text.split(' ')
        i = 0
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i]+ " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines

def get_font(txt, author, ran_x, rmg):
    font_path = 'font/arialbd.ttf'
    font = ImageFont.truetype(font=font_path, size=20)
    text = str(QuoteModel(txt, author))
    lines = text_wrap(text, font, rmg.size[0]-ran_x)
    line_height = font.getsize('hg')[1]
    return [lines, line_height, font]

def draw_text(x, y, lines, line_height, rmg, font):
    draw = ImageDraw.Draw(rmg)
    color = 'rgb(200, 200, 200)'
    for line in lines:
        draw.text((x,y), line, fill=color, font=font)
        y = y + line_height
    return rmg
