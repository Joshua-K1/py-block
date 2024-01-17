import os

#@TODO: Parser argument for specifying a log file location

class Logger:
   def __init__(self, location=None):
      if location is None: location = "./log/log.json"
      self.location = location

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
