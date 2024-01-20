from writer import write_chain
from logger import event_logger
import datetime as date
import json
import os 

chain_file = './chain/chain.json'

def establish_chain():
   event_logger.info("Establishing if chain exists")

   if os.path.exists(chain_file) and os.path.getsize(chain_file) == 0:
      event_logger.info("Chain file exists but is empty")
      # Read in file and create genesis block

   elif os.path.exists(chain_file) and os.path.getsize(chain_file) > 0:
      event_logger.info("Chain exists and has a size greater than 0")
      # Read in file, read previous block and append new block

   else: 
      event_logger.info("Chain file does not exist")
      # Creat file?

def create_genesis_block():
   block = {
         "index": "",
         "date": "",
         "data": "Genesis Block",
         "prev_hash": ""
      }

   return block
