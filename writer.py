import csv 
import os


class Writer:
   def __init__(self, entry, log_file):
      self.entry = entry
      self.log_file = log_file


   def write_chain(self) -> None:
      if os.path.exists(self.log_file) and os.path.getsize(self.log_file) == 0:
         print("File exists and has a size of 0")

         with open(self.log_file, mode='a', newline='') as file: 
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Block', 'Timestamp', 'Data', 'Previous Hash'])

      elif os.path.exists(self.log_file) and os.path.getsize(self.log_file) > 0: 
         print("File exists and has content")
         # Write next row of file

      else:
         print("File does not exist")
         # End

      

