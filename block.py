import hashlib

class Block: 
   def __init__(self, index, timestamp, data, previous_hash):
      self.index = index
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

   def calc_hash(self) -> str:
      hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)

      return hashlib.sha256(hash_string.encode()).hexdigest()

   def return_dict(self):
      dict = {
      "Index": str(self.index),
      "Timestamp": str(self.timestamp),
      "Data": str(self.data),
      "PreviousHash": str(self.previous_hash)
   }

      return dict

