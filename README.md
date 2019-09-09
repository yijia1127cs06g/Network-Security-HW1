# Network-Security-HW1
## introduction
Given the RSA public key (pub.pem), the encrypted message (flag.enc), and the source code of the decrypter running on the server (decrypter.py).
The goal is to retrieve flag, it should be like FLAG{.......}


## Chosen ciphertext attack
Chosen cipher attack is an attack model that If an attacker can gather information by obtaining the decryption of cipertexts, attacker can then retrieve the plaintext without having the key.

## Given
- flag.enc
- pub.pem
- decrypter.py

## Solution
- createMessage.py: According given public key, generating a fake message to send to decrypt server.
- decryptMessage.py: According reply from decrypt server. decrypt message with the given public key and chosen X
- flag.txt: decrypted message

## Dependency
- pycrypto
