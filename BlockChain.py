import sys
import hashlib
import json
from time import time
from uuid import uuid4

class BlockChain:

    def  __init__(self):
        self.chain = [] # have a list of all blocks
        self.current_transactions = [] # hold current block

        # Create the genesis block
        genesis_hash = hashlib.sha256(b'genesis_block').hexdigest() # start the chain.
        self.append_block(previous_hash = genesis_hash,
                          nonce= self.proof_of_work(0, genesis_hash, [])
        )
