import sys
import hashlib
import json
from time import time
from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import List

@dataclass
class MediBlock(object):
    '''
    A class to model  blocks of medical transations to be added to the blockchain
    below is how to instantiate the block to be added to the ledger
    '''
    index:int # -  index of the block
    previous_block_hash:str
    nonce:int #  number use once.
    transaction:str # the AES encrypted set of actions  that can be decrypted into  medical operation graph.
    timestamp:datetime = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())   #  -  timestamp when block was created and added

    def hash_block(self) ->str:
        '''
        A method to return a  sha256 has of the complete block
        '''
        block_dict = self.__dict__
        json_str = json.dumps(block_dict, sort_keys=True)
        return hashlib.sha256(json_str.encode('utf-8')).hexdigest()
        




@dataclass
class MediLedger:
    blocks: List[MediBlock] = field(default_factory=list)
    """
    A class to model a simple blockchain ledger for medical transactions
    """
    def add_block(self, block: MediBlock) -> None:
        """Add a MediBlock to the ledger"""
        self.blocks.append(block)

    def get_block(self, index: int) -> MediBlock:
        """Retrieve a block by index"""
        return self.blocks[index]

    def last_block(self) -> MediBlock:
        """Get the most recent block"""
        if self.blocks:
            return self.blocks[-1]
        return None