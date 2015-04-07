# initialiaze and populate the database.
# from pals_curriculum.models import *

"""

What is the purpose of the branches? To skip certain parts of a level or
is it to do certain parts first and gauge which pathes are most interested in
(they would still do all the material, with a choice of the order).

           4-5-12-13-14\ ? (15 or valid unvisited nodes)
          /             |
    1-2-3<     /8-11-----15-16-17
          \6-7<      ___/
               \9-10/

Path Walking Adventure Time Algorithm Step by Step
page 1     |  next_pages = [2] (hit page 1, add 2)           , options = 2
page 2     |  next_pages = [3] (remove 2, add 3)             , options = 3
page 3     |  next_pages = [4,6] (remove 3, add 4 and 6)     , options = 4,6
page 4     |  next_pages = [5,6] (remove 4, add 5)           , options = 5
page 5     |  next_pages = [6,12] (remove 5, add 12)         , options = 12
page 6     |  next_pages = [7,12] (remove 6, add 7)          , options = 7
page 7     |  next_pages = [8,9,12] (remove 7, add 8 and 9)  , options = 8,9,12
page 12    |  next_pages = [8,9,13] (remove 12, add 13)      , options = 13
page 13    |  next_pages = [8,9,14] (remove 13, add 14)      , options = 14
page 14    |  next_pages = [8,9] (remove 14, do not add 15)  , options = 8,9
page 8     |  next_pages = [9,11] (remove 8, add 11)         , options = 11
page 11    |  next_pages = [9] (remove 11)                   , options = 9
page 9     |  next_pages = [10] (remove 11, add 10)          , options = 9
page 10    |  next_pages = [15] (remove 10, add 15)          , options = 15
...15,16
page 17    |  next_pages = [] (remove 17)                    , options = -1

# functional logic (not needed if branches can be skipped)
remove page we are on
if next.indegree > 1 and next_pages is empty: add next to next_pages
elif next.indegree == 1: add next to next_pages
else: do not add

# display logic
if  this.out > 1: display next_pages
elif next.in > 1: display next_pages
else:             display next

They have 3 routes they could go to! FREEDOM AT LAST


Edges
u  v
-  -
1  2
2  3
3  4
4  5
5  12
12 13
14 15
15 16
3  6
6  7
7  8
7  9
9  10
8  11

Some Valid Topological Sorts
All preceding routes must come first in topo sort

1 2 3 4 5 12 13 14 6 7 8 11 9 10 15 16 17
1 2 3 6 7 8 11 9 10 4 5 12 13 14 15 16 17
1 2 3 6 7 8 11 4 5 12 13 14 9 10 15 16 17
1 2 3 4 6 5 12 7 13 9 8 14 11 10 15 16 17

1 2 3 4 6 7 where to next? --> [8, 9, 5]


             5-12-13-14\ ? (15 or valid unvisited nodes)
                        |
                8-11-----15-16-17
                     ___/
                9-10/

"""


adj_list3=[((1,False),[2]),
((2,False),[3]),
((3,False),[4,6]),
((4,False),[5]),
((5,False),[12]),
((12,False),[13]),
((13,False),[14]),
((14,False),[15]),
((6,False),[7]),
((7,False),[8,9]),
((8,False),[11]),
((11,False),[15]),
((9,False),[10]),
((10,False),[15]),
((15,False),[16]),
((16,False),[17]),
((17,False),[])]


adj_list=[(1,[2]),
(2,[3]),
(3,[4,6]),
(4,[5]),
(5,[12]),
(12,[13]),
(13,[14]),
(14,[15]),
(6,[7]),
(7,[8,9]),
(8,[11]),
(11,[15]),
(9,[10]),
(10,[15]),
(15,[16]),
(16,[17]),
(17,[])]

adj_list2=[
(5,[12]),
(12,[13]),
(13,[14]),
(14,[15]),
(8,[11]),
(11,[15]),
(9,[10]),
(10,[15]),
(15,[16]),
(16,[17]),
(17,[])]

def topolgical_sort2(graph_unsorted):
    graph_sorted = []
    graph_unsorted = dict([(t[0][0],t[1] for t in graph_unsorted)])
    while graph_unsorted:
        acyclic = False
        for node, edges in graph_unsorted.items():
            for edge in edges:
                if edge in graph_unsorted:
                    break
            else:
                acyclic = True
                del graph_unsorted[node]
                graph_sorted.append(node)

        if not acyclic:
            raise RuntimeError("A cyclic dependency occurred")
    return list(reversed(graph_sorted))


def topolgical_sort(graph_unsorted):
    graph_sorted = []
    graph_unsorted = dict(graph_unsorted)
    while graph_unsorted:
        acyclic = False
        for node, edges in graph_unsorted.items():
            for edge in edges:
                if edge in graph_unsorted:
                    break
            else:
                acyclic = True
                del graph_unsorted[node]
                graph_sorted.append(node)

        if not acyclic:
            raise RuntimeError("A cyclic dependency occurred")
    return list(reversed(graph_sorted))

print(topolgical_sort(adj_list))
print
print(topolgical_sort(adj_list2))




