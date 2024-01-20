import datetime as date
from block import Block

class Blockain:
   def __init__(self):
       self.chain = [self.create_genesis_block()]

   def create_genesis_block(self) -> Block:
      return Block(0, date.datetime.now(), "Genesis Block", "0")

   def get_latest_block(self) -> Block:
      return self.chain[-1]

   def add_block(self, new_block):
      new_block.previous_hash = self.get_latest_block().hash
      new_block.hash = new_block.calc_hash()
      self.chain.append(new_block)

   def is_valid(self):
      for i in range(1, len(self.chain)):
         current_block = self.chain[i]
         previous_block = self.chain[i-1]

         if current_block.hash != current_block.calc_hash:
            return False

         if current_block.previous_hash != previous_block.hash:
            return False

      return True
