import hashlib


def findCoinHashID(key, search_num):
    i=0
    Finished = False
    while not Finished:
        key_check = key + str(i)
        result = hashlib.md5(key_check.encode()).hexdigest()
        first_digits = result[:len(search_num)]
        if (first_digits)== search_num:
            Finished = True
            return i
        i+=1

key = 'ckczppom'


print (findCoinHashID(key, '00000'))
print (findCoinHashID(key, '000000'))