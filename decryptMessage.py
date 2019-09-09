from fractions import gcd
import base64
from Crypto.Util.number import *
from Crypto.PublicKey import RSA

reply = "jJiCjvamYL7yYOq+yGC+1tze7r7o0Ga+xtDeasrcvsZi4NBm5L5o6OjCxtZC+g=="
x = 2
def egcd(x, y):
    if x == 0:
        return (y, 0, 1)
    g, b, a = egcd(y%x,x)
    return (g, a - (y//x) * b, b)

def modinv(a, n):
    g, x, y = egcd(a, n)
    return x%n

def decryt(msg, x, n):
    longMsg = bytes_to_long(base64.b64decode(msg))
    xInverse = modinv(x,n)
    print()
    print("Modular Inverse of X = ", xInverse)
    print()
    return long_to_bytes((longMsg*xInverse)%n)

def Main():

    with open("pub.pem","r") as myfile:
        key = RSA.importKey(myfile.read())
    decryptMsg = decryt(reply,x,key.n)
    print(decryptMsg.decode("utf-8"))
    print()
if __name__ == "__main__":
    Main()


