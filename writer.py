import csv 
import os

log_file = './log/chain.csv'

def write_chain() -> None:
   if os.path.exists(log_file) and os.path.getsize(log_file) == 0:
      print("File exists and has a size of 0")

      with open(log_file, mode='a', newline='') as file: 
         csv_writer = csv.writer(file)
         csv_writer.writerow(['Block', 'Timestamp', 'Data', 'Previous Hash'])

   elif os.path.exists(log_file) and os.path.getsize(log_file) > 0: 
      print("File exists and has content")
      # Write next row of file

   else:
      print("File does not exist")
      # End
