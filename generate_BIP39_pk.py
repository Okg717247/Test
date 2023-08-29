from bip32utils import BIP32Key
from bip32utils import BIP32_HARDEN
import os, bip39

import hashlib

    # Read the BIP39 seed word list 
    # (english seed words here)
with open('english.txt') as f:
    bip39_list = f.readlines()    
bip39_list = [w.strip('\n') for w in bip39_list]

passphrase = ''

account_number = 0   

pk_list = []

mnemonic = 'wine anxiety behind atom enroll gown dragon acoustic autumn couple firm comfort'.split(' ')

for k in range(0,12):
    mnemonic_phrase = mnemonic.copy()
    for j in range(0, len(bip39_list)):
        mnemonic_phrase[k]  = bip39_list[j]     
        try:       
            seed = bip39.phrase_to_seed(' '.join(mnemonic_phrase), passphrase=passphrase)
            
            key = BIP32Key.fromEntropy(seed)
            for account_number in range(0,2):
                for i in range(0, 20):
                    pk = key.ChildKey(44 + BIP32_HARDEN).ChildKey(0 + BIP32_HARDEN).ChildKey(account_number + BIP32_HARDEN).ChildKey(0).ChildKey(i).PrivateKey().hex()      
                    pk_list.append(pk)
        except Exception as ex:
            print(ex)
                
    if (j % 10 == 0) and (j != 0):    
        print(f'{round(100*(j+1) / len(bip39_list),2)} %')
        with open('bip39_pks.txt', 'a') as f:
            f.write('\n'.join(pk_list))
            pk_list.clear()
            
with open('bip39_pks.txt', 'a') as f:
    f.write('\n'.join(pk_list))
    pk_list.clear()
        


