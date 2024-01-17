import argparse
from chain import Blockain
from block import Block
from writer import Writer
from logger import Logger
import datetime as dt

#@TO DO:New Block hash needs to be generated before dict is added to chain

def main():
   # Create new blockchain
   blockchain = Blockain()
   logger = Logger()
   logger.write_log()

   block = Block(4, dt.datetime.now(), "Transaction 4", "")
   block = block.return_dict()

   blockchain.add_block(Block(1, dt.datetime.now(), "Transaction 1", ""))
   blockchain.add_block(Block(2, dt.datetime.now(), "Transaction 2", ""))
   blockchain.add_block(Block(3, dt.datetime.now(), "Transaction 3", ""))

   for block in blockchain.chain: 
    print("Block #: " + str(block.index)) 
    print("Timestamp: " + str(block.timestamp)) 
    print("Data: " + str(block.data)) 
    print("Prev Hash: " + str(block.previous_hash)) 

   # Print as CSV
   print(str(block.index) + "," + str(block.timestamp) + "," + str(block.data) + "," + str(block.previous_hash))
   log_entry = str(block.index) + "," + str(block.timestamp) + "," + str(block.data) + "," + str(block.previous_hash)
   
   cw = Writer(log_entry, "./log/chain.csv")
   cw.write_chain()

if __name__ == "__main__":
   # parser = argparse.ArgumentParser(description="Process external arguments")
   # parser.add_argument("-message", type=str, require=True, help="Message to add to blockchain")
   # 
   # args = parser.parse_args()

   main()
