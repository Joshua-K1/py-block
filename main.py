import argparse
from chain_ops import list_chain_blocks, add_block

def main():
   list_chain_blocks()
   add_block()

if __name__ == "__main__":
   # parser = argparse.ArgumentParser(description="Process external arguments")
   # parser.add_argument("-message", type=str, require=True, help="Message to add to blockchain")
   # 
   # args = parser.parse_args()

   main()
