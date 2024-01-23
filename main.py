import argparse
from chain_ops import list_chain_blocks, add_block

def main(args):

   if args.listBlocks:
      list_chain_blocks()
   if args.addBlock:
      if args.blockData is None:
         print("No block data supplied")
      else:
         add_block(args.blockData)

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description="Process external arguments")
   parser.add_argument("-listBlocks", action="store_true", help="List all blocks in chain")
   parser.add_argument("-addBlock", action="store_true", help="Add new block to the blockchain")
   parser.add_argument("-blockData", type=str, help="Data to be contained within the block")
   
   args = parser.parse_args()

   main(args)
