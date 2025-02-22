from linear_search import linear_search
from linear_search import global_linear_search

print(linear_search(3, [1,2,3]) == 2)
print(linear_search(4, [1,2,3]) == None)
print(linear_search(13, [1,2,3]) == None)

print((global_linear_search("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5]))
print(global_linear_search("s", ["b", "a", "n", "a", "n", "a", "s"]) == [6])
print(global_linear_search("n", ["b", "a", "n", "a", "n", "a", "s"]) == [2, 4])

print(global_linear_search("x", ["b", "a", "n", "a", "n", "a", "s"]) == [])
print(global_linear_search(2, ["b", "a", "n", "a", "n", "a", "s", 2]) == [7])