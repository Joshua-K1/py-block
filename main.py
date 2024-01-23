import argparse
from chain_ops import list_chain_blocks, add_block

def main(args):

   if args.listBlocks:
      list_chain_blocks()
   add_block()

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Process external arguments")
   parser.add_argument("-listBlocks", action="store_true", help="List all blocks in chain")
   parser.add_argument("-addBlock", action="store_true", help="Add new block to the blockchain")
   
   args = parser.parse_args()

   main(args)
