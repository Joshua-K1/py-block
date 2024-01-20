import argparse
import datetime as dt
from chain_ops import establish_chain, return_last_block, list_chain_blocks
from cryptography import calc_hash 

def main():
   list_chain_blocks()

   hash_string = calc_hash(return_last_block())
   print(hash_string)

if __name__ == "__main__":
   # parser = argparse.ArgumentParser(description="Process external arguments")
   # parser.add_argument("-message", type=str, require=True, help="Message to add to blockchain")
   # 
   # args = parser.parse_args()

   main()
