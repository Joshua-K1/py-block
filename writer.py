import csv 
import os

chain_file = './log/chain.csv'

def write_chain(chain) -> None:
   if os.path.exists(chain_file) and os.path.getsize(chain_file) == 0:
      print("File exists and has a size of 0")

      with open(chain_file, mode='a', newline='') as file: 
         csv_writer = csv.writer(file)
         csv_writer.writerow(['Block', 'Timestamp', 'Data', 'Previous Hash'])

   elif os.path.exists(chain_file) and os.path.getsize(chain_file) > 0: 
      print("File exists and has content")
      # Write next row of file

      with open(chain_file, mode='a', newline='') as file: 
         csv_writer = csv.writer(file)
         csv_writer.writerow(chain)

   else:
      print("File does not exist")
      # End
