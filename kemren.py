import os
import time
R = '\033[31m' # merah
G = '\033[32m' # hijau
C = '\033[36m' # biru
W = '\033[0m'  # putih

string = "happy birthday to you, patrick"
cek1 = 0
cek2 = 1
cake = '''
                       *
                    _|_|_
                   |     |
                 +---------+
      *          |         |
     _|_|_     +-------------+
    |     |    |             |
    +-----+    +-------------+
\033[32m===================================
'''
cake1 = '''
                     *
                    _|_|_
                   |     |
                 +---------+
        *        |         |
     _|_|_     +-------------+
    |     |    |             |
    +-----+    +-------------+
\033[32m===================================
'''
while True:
    os.system('clear')
    depan = string[:cek1]
    if string[cek1].islower():
        tengah1 = string[cek1].upper()
    else:
        tengah1 = string[cek1].lower()
    if string[cek2].islower():
        tengah2 = string[cek2].upper()
    else:
        tengah2 = string[cek2].lower()
    belakang = string[cek1 + 2:]
    if cek1%3 == 0:
        kemren = ' /'
    elif cek1%3 == 1:
        kemren = " |"
    else:
        kemren = ' -'
    if cek1%2 == 0:
        print(cake)
    else:
        print(cake1)
    if cek2 == 0:
        string_baru =tengah2 +  depan[1:] + tengah1 + belakang + kemren
        print(R + "~~> " + C + string_baru + W)
    else: 
        string_baru = depan + tengah1 + tengah2 + belakang + kemren
        print(R + "~~> " + C + string_baru + W)
    time.sleep(0.1)
    cek1 += 1
    cek2 += 1
    if cek2 == len(string):
        cek2 = 0
    if cek1 == len(string):
        cek1 = 0
            
    
