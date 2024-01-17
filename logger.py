import csv 
import os


class Logger:
   def __init__(self, entry, log_file):
      self.entry = entry
      self.log_file = log_file


   def write_log(self) -> None:
      if os.path.exists(self.log_file):
         print("File exists")
      else: 
         print("File does not exist")
      

