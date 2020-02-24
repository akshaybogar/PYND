from PIL import Image
from random import randint
import os
from . import MemeHelper as mh

class MemeEngine():
    def __init__(self, save_loc):
        self.save_loc = save_loc

    def make_meme(self, img_path, txt, author, width=500):
        try:
            img = Image.open(img_path)
            rmg = mh.resize_image(img, width)
            ran_x = mh.get_randomx(rmg)
            lines, line_height, font = mh.get_font(txt, author, ran_x, rmg)
            ran_y = mh.get_randomy(rmg, line_height, lines)
            rmg = mh.draw_text(ran_x, ran_y, lines, line_height, rmg,
                                        font)
            file_path = r'{}/{}.jpg'.format(self.save_loc, randint(0, 1000000))
            if not os.path.exists(self.save_loc):
                os.makedirs(self.save_loc)
            rmg.save(file_path)
            return file_path
        except IOError as error:
            print('Error occured while opening image')
