import argparse
from chain import Blockain
from block import Block
import datetime as dt

def main():
   print("Main")

   # Create new blockchain
   blockchain = Blockain()

   blockchain.add_block(Block(1, dt.datetime.now(), "Transaction 1", ""))
   blockchain.add_block(Block(2, dt.datetime.now(), "Transaction 2", ""))
   blockchain.add_block(Block(3, dt.datetime.now(), "Transaction 3", ""))

   for block in blockchain.chain: 
      print("Block #: " + str(block.index)) 
      print("Timestamp: " + str(block.timestamp)) 
      print("Data: " + str(block.data)) 
      print("Prev Hash: " + str(block.previous_hash)) 



if __name__ == "__main__":
   # parser = argparse.ArgumentParser(description="Process external arguments")
   # parser.add_argument("-message", type=str, require=True, help="Message to add to blockchain")
   # 
   # args = parser.parse_args()

   main()
