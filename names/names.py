import time
from trie import Trie
import math
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# Average time to compute: 6.8 seconds
# Total time complexity: O(n^2)
# Total space complexity worst case: O(n)
# O(n)
# for name_1 in names_1:
    # O(n) 
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Average time to compute: 0.21 seconds
# Total time complexity: O(2nk) = O(nk) or O(n)
# Total space complexity worst case: O(mn) where m is longest string
# Total space is usually less than other methods 
# as strings that are a prefix of others do not cause additional storage
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

# [STRECTH]
# Average time to compute: 0.007 seconds
# Total time complexity: O(2n) = O(n)
# Total space complexity: O(n)
# table = dict()
# # O(n)
# for name_1 in names_1:
#     # O(1)
#     table[name_1] = True
# # O(n)
# for name_2 in names_2:
#     #O(1)
#     if name_2 in table:
#         duplicates.append(name_2)

# [STRETCH 2]

# Average time to compute: 0.07 seconds
# Total time complexity: O(nlog(n))
# Total space complexity: O(n)
store = list()

# O(n)
for name_1 in names_1:
    store.append(name_1)

# O(log(n))
store.sort()

# O (log(n))
def bin_search(arr, val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = math.floor((start + end) / 2)
        if arr[mid] > val:
            end = mid - 1
        elif arr[mid] < val:
            start = mid + 1
        else:
            return True
    return False

for name_2 in names_2:
    if bin_search(store, name_2):
        duplicates.append(name_2)

# Best space complexity: Solution 2
# Best time complexity: Solution 3

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

