import csv 
import os
import json

chain_file = './chain/chain.json'

def write_chain(chain) -> None:
   if os.path.exists(chain_file) and os.path.getsize(chain_file) == 0:
      print("File exists and has a size of 0")

      with open(chain_file, 'a') as file:
         json.dump({}, file, ensure_ascii=False)

   elif os.path.exists(chain_file) and os.path.getsize(chain_file) > 0: 
      print("File exists and has content")
      # Write next row of file

      with open(chain_file, mode='a', newline='') as file: 
         csv_writer = csv.writer(file)
         csv_writer.writerow(chain)

   else:
      print("File does not exist")
      # En
