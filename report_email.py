#!/usr/bin/env python3

import sys
import datetime
from operator import itemgetter

import reports
import emails
import data

username = "student"

def process_data(fruits):
  new_fruits = []
  new_fruits_string = ""
  for item in fruits:
    new_fruits.append((item["name"], item["weight"]))
  sorted(new_fruits, key=itemgetter(0))
  for item in new_fruits:
    new_fruits_string += "name: " + item[0] + "<br/>" + "weight: " + str(item[1]) + " lbs<br/><br/>"
  return new_fruits_string

def main(argv):
  src_dir = "/home/" + username + "/supplier-data/descriptions"
  fruits = data.get_data(src_dir)
  summary = process_data(fruits)
  print(summary)

  # PDF
  filename = "/tmp/processed.pdf"
  today = datetime.date.today().strftime("%B %d, %Y")
  title = "Processed Update on " + today

  reports.generate_report(filename, title, summary)

  # Email
  sender = "automation@example.com"
  recipient = username + "@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate_email(sender, recipient, subject, body, filename)
  emails.send_email(message)


if __name__ == "__main__":
  main(sys.argv)
