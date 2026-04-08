_list = [1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 9]
new_list = []
for x in _list:
    if _list.count(x) == 1:
        new_list.append(x)
print("Danh sách mới:", new_list)

