set_satu = {1,2,3}
set_dua = {4,5,6}
set_satu.add(4)
set_dua.add(7)
print(set_satu)
print(set_dua)
set_satu.update({5,6})
set_dua.update({8,9})
print(set_satu)
print(set_dua)
set_satu.discard(6)
set_dua.remove(4)
print(set_satu | set_dua)
print(set_satu & set_dua)
print(1 in set_satu)