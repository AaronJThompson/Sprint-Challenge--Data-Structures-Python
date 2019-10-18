import time
from trie import Trie
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Average time to compute: 6.8 seconds
# Total: O(n^2)
# O(n)
# for name_1 in names_1:
    # O(n) 
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Average time to compute: 0.21 seconds
# Total: O(2nk) = O(nk) or O(n)
# trie = Trie()
# O(nk) where k is average length of string
# for name_1 in names_1:
#     O(k) where k is length of string
#     trie.insert_string(name_1)
#
# O(nk) where k is average length of string 
# for name_2 in names_2:
#     O(k) where k is length of string
#     if trie.check_string(name_2):
#         duplicates.append(name_2)

# Average time to compute: 0.007 seconds
# Total: O(2n) = O(n)
table = dict()
# O(n)
for name_1 in names_1:
    # O(1)
    table[name_1] = True
# O(n)
for name_2 in names_2:
    #O(1)
    if name_2 in table:
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

