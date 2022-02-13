# step 1 : create a blockchain class

import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        
        self.new_block(previous_hash  = "0",proof=100)
        
# step 2 : write a function to build new blocks

    def new_block(self,proof,previous_hash = None):
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions' : self.pending_transactions,
            'proof' : proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1]),
        }
        self.pending_transactions = []
        self.chain.append(block)
        
        return block

# step 3 : write functions to create new transactions & get the last block    
    @property
    def last_block(self):
        
        return self.chain[-1]
    
    def new_transaction(self,match,team_a,team_b):
        transaction = {
            'Match' : match,
            'Team A' : team_a,
            'Team B' : team_b
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

# step 4 : write a function to "hash" our blocks

    def hash(self,block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        
        return hex_hash
    
# step 5 : create a new blockchain & send some money

blockchain = Blockchain()
t1 = blockchain.new_transaction("1","EVOS Esports","PSG Esports")
t2 = blockchain.new_transaction("2","King Of Gamers Club","Valencia CF Esports")
t3 = blockchain.new_transaction("3","Bruriram United Esports","Bacontime")

blockchain.new_block(12345)
t4 = blockchain.new_transaction("4","Earena","Goldcity Esports")
t5 = blockchain.new_transaction("5","Bruriram United Esports","Valencia CF Esports")
t6 = blockchain.new_transaction("6","Bacontime","PSG Esports")
blockchain.new_block(6789)

print("Blockchain : ",blockchain.chain)

