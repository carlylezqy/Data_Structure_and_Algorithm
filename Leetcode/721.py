import HashTable as ht
import UnionFindSet as ufs
import sys


accounts = [
["David","David0@m.co","David4@m.co","David3@m.co"],
["David","David5@m.co","David5@m.co","David0@m.co"],
["David","David1@m.co","David4@m.co","David0@m.co"],
["David","David0@m.co","David1@m.co","David3@m.co"],
["David","David4@m.co","David1@m.co","David3@m.co"]]

#accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

hashtable_size = len(accounts) * 30
table = ht.HashTable(hashtable_size)
user_dict = []

for i, v in enumerate(accounts):
    user_dict.append(v[0])
    accounts[i][0] = i
    for e_idx in range(1, len(v)):
        hash_index = hash(v[e_idx]) % ((sys.maxsize + 1) * 2)
        table.put(hash_index, v[e_idx])
        accounts[i][e_idx] = hash_index

uts_table = ufs.UnionFindSet(range(len(user_dict)))
for v in accounts:
    for idx in range(1, len(v)):
        uts_table.union(v[idx-1], v[idx])

#print(table.hashtable)
print(uts_table.father_dict)
#print(uts_table.get_root())

output = []
for v in uts_table.get_root():
    user_info = []
    temp = []
    user_info.append(user_dict[v])
    for e_hidx in uts_table.get_leaf(v):
        temp.append(table.get(e_hidx))
    temp.sort()
    for i in temp:
        user_info.append(i)
    output.append(user_info)

print(output)