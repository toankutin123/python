_list = [1, 2, 3, 4, 5,7,8,9,10]
chan = []
le = []
for x in _list:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)
print("Số chẵn:", chan)
print("Số lẻ:", le) 
