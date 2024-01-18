import os
import datetime

#@TODO: Parser argument for specifying a log file location

class Logger:
   def __init__(self, location=None, date=None):
      if location is None: location = "./log/log.json"
      self.location = location

      if date is None: date = datetime.datetime.now()
      self.date = date

   def log_file_check(self) -> bool:
      if os.path.exists(str(self.location)):
         return True
      else: 
         return False
   
   def write_log(self) -> None: 
      if self.log_file_check(): 
         print("File exists, can write log")
      else: 
         print("File doesn't exist")
