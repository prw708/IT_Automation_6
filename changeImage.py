#!/usr/bin/env python3

import os
from PIL import Image

username = "student"
src_dir = "/home/" + username + "/supplier-data/images"
dest_dir = "/home/" + username + "/supplier-data/images"

for item in os.listdir(src_dir):
    filename, ext = os.path.splitext(item)
    try:
        if ext == ".tiff":
            with Image.open(src_dir + "/" + item) as im:
                im = im.resize((600,400))
                im = im.convert("RGB")
                im.save(dest_dir + "/" + filename + ".jpeg", "JPEG")
    except OSError as err:
        print("OSError: {}".format(err))
