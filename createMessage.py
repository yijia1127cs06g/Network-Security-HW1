from fractions import gcd
import base64
from Crypto.PublicKey import RSA
from Crypto.Util.number import *

def readFlag(fileName):
    with open(fileName,"r") as myfile:
        text = myfile.read().strip()
    b64Msg = base64.b64decode(text)
    longMsg = bytes_to_long(b64Msg)
    return longMsg

def findCoprime(num):
    for i in range(2,num):
        if gcd(i,num) == 1:
            return i
    else:
        return 1

def createFakeMsg(msg, e, n):
    x = findCoprime(n)
    bytesMsg = long_to_bytes((msg*(x**e))%n)
    return (x,base64.b64encode(bytesMsg))
    

def Main():

    with open("pub.pem","r") as myfile:
        key = RSA.importKey(myfile.read())
    longMsg = readFlag("flag.enc")
    x, msg = createFakeMsg(longMsg, key.e, key.n)
    print()
    print()
    print("n = ", key.n)
    print("e = ", key.e)

    print()
    print()
    print("==Chosen X==")
    print(x)
    print("==Fake message==")
    print(msg.decode())
    

if __name__ == "__main__":
    Main()


