#!/usr/bin/env python3

import requests
import sys

import data

username = "student"
src_dir = "/home/" + username + "/supplier-data/descriptions"
dest_url = "http:///fruits/"


def main(argv):
    fruits = []
    fruits = data.get_data(src_dir)
    for item in fruits:
        response = requests.post(dest_url, json=item)
        try:
            if response.raise_for_status() == None:
                print("Item successfully submitted: " + str(response.status_code))
        except requests.exceptions.HTTPError:
            print("Error: " + str(response.status_code))

if __name__ == "__main__":
    main(sys.argv)
