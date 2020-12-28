#!/usr/bin/env python3

import sys
import shutil
import psutil
import socket

import emails

username = "student"

def cpu_usage_greater_than(percent_threshold):
  if psutil.cpu_percent(interval=1) > percent_threshold:
    return True
  else:
    return False

def disk_space_less_than(path, percent_threshold):
  total, used, free = shutil.disk_usage(path)
  if (free / total) * 100 < percent_threshold:
    return True
  else:
    return False

def memory_less_than(memory_in_MB):
  if psutil.virtual_memory().available / 1000000 < memory_in_MB:
    return True
  else:
    return False

def localhost_valid(hostname):
  if socket.gethostbyname(hostname) == "127.0.0.1":
    return True
  else:
    return False

def main(argv):
  sender = "automation@example.com"
  recipient = username + "@example.com"
  body = "Please check your system and resolve the issue as soon as possible."
  if cpu_usage_greater_than(80):
    subject = "Error - CPU usage is over 80%"
  elif disk_space_less_than("/", 20):
    subject = "Error - Available disk space is less than 20%"
  elif memory_less_than(500):
    subject = "Error - Available memory is less than 500MB"
  elif not localhost_valid("localhost"):
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
  else:
    subject = None

  if subject is not None:
    message = emails.generate_email(sender, recipient, subject, body, None)
    emails.send_email(message)


if __name__ == "__main__":
  main(sys.argv)
