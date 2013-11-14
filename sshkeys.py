import os
import sys

if len(sys.argv) <= 2:
    print 'Usage: python sshkeys.py [username] [hostname] [port]'
    print 'Usage: [port] is voluntary'
    sys.exit()

path = "/Users/hakloev/.ssh/id_rsa.pub"
user = str(sys.argv[1])
host = str(sys.argv[2])

if (len(sys.argv) == 4):
    port = str(sys.argv[3])
else:
    port = "22"

def getPublicKey():
    if os.path.exists(path):
        print "id_rsa exists"
    else:
        print "id_rsa doesn't exist, creating now!"
        os.system('ssh-keygen')

def postKey():
    os.system('cat ' + path + ' | ssh -p ' + port + ' '+  user + '@' + \
    host + " 'mkdir -p .ssh; cat >> .ssh/authorized_keys'")
    
getPublicKey()
postKey()
