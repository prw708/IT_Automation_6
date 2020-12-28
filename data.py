#!/usr/bin/env python3

import os
import re

def get_data(src_dir):
    data = []
    for item in os.listdir(src_dir):
        filename, ext = os.path.splitext(item)
        if ext == ".txt":
            with open(src_dir + "/" + item, "r") as file:
                contents = {}
                lines = file.readlines()
                contents["name"] = lines[0].strip()
                match = re.search(r"([0-9]+) lbs", lines[1].strip())
                contents["weight"] = int(match.group(1))
                contents["description"] = lines[2].strip()
                contents["image_name"] = filename + ".jpeg"
                data.append(contents)
                file.close()
    return data
