import hashlib
import datetime as date
from block import Block

class Blockain:
   def __init__(self):
       self.chain = [self.create_genesis_block()]

   def create_genesis_block(self):
      return Block(0, date.datetime.now(), "Genesis Block", "0")
