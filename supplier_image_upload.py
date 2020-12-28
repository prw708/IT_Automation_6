#!/usr/bin/env python3

import os
import requests

username = "student"
src_dir = "/home/" + username + "/supplier-data/images"
dest_url = "http://localhost/upload/"

for item in os.listdir(src_dir):
    filename, ext = os.path.splitext(item)
    if ext == ".jpeg":
        with open(src_dir + "/" + item, "rb") as file:
            response = requests.post(dest_url, files={"file": file})
            try:
                if response.raise_for_status() == None:
                    print("Item successfully submitted: " + str(response.status_code))
            except requests.exceptions.HTTPError:
                print("Error: " + str(response.status_code))
            file.close()
