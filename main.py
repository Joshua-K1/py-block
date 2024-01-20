import argparse
import datetime as dt
from chain_ops import establish_chain, return_last_block 

def main():
   # Create new blockchain
   
   # Check that chain exists
   chain_file_data = establish_chain()

   # Return last block
   last_block = return_last_block()
   print(last_block)





if __name__ == "__main__":
   # parser = argparse.ArgumentParser(description="Process external arguments")
   # parser.add_argument("-message", type=str, require=True, help="Message to add to blockchain")
   # 
   # args = parser.parse_args()

   main()
