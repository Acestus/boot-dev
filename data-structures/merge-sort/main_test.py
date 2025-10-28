Boot.dev
Dashboard
Courses
Training
Billing
Community
Leaderboard

gem bag

Sorcerer

Level 64
user avatarprofile role frame
streak embersstreak embers

Back

Next

Merge Sort

Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort. It's a divide and conquer algorithm.:

    Divide: divide the large problem into smaller problems, and recursively solve the smaller problems
    Conquer: Combine the results of the smaller problems to solve the large problem

In merge sort we:

    Divide the array into two (equal) halves (divide)
    Recursively sort the two halves
    Merge the two halves to form a sorted array (conquer)

Click to hide video
Your browser does not support playing HTML5 video. You can instead. Here is a description of the content: Merge sort

Algorithm

The algorithm consists of two separate functions, merge_sort() and merge().

merge_sort() divides the input array into two halves, calls itself on each half, and then merges the two sorted halves back together in order.

The merge() function merges two already sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each only have one element. Those single element lists will be merged into a sorted list of length two, and we can build from there.

In other words, all the "real" sorting happens in the merge() function.
merge_sort() pseudocode

Input: A, an unsorted list of integers

    If the length of A is less than 2, it's already sorted so return it
    Split the input array into two halves down the middle
    Call merge_sort() twice, once on each half
    Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls

merge() pseudocode

Inputs: A and B. Two sorted lists of integers

    Create a new final list of integers.
    Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
    Use a loop to compare the current elements of A and B. If an element in A is less than or equal to its respective element in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j. Continue until all items from one of the lists have been added.
    After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
    Return the final list.

Assignment

Our LockedIn influencers are complaining that when they sort their followers by follower count, it gets really slow if they have more than 1,000 followers (because we're using Bubble Sort). Let's speed it up for them with merge sort.

Complete the merge_sort and merge functions according to the described algorithms.

Boots

Need help? I, Boots the Master of Mondays, can assist... for a price.

    Next Tab

    Alt+Shift+]

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
from main import *
import time

run_cases = [([3, 2, 1], [1, 2, 3]), ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])]

submit_cases = run_cases + [
    ([], []),
    ([7], [7]),
    ([4, -7, 1, 0, 5], [-7, 0, 1, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expected: {expected_output}")
    start = time.time()
    result = merge_sort(input1)
    end = time.time()
    timeout = 1.00
    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        print(f"Actual: {result}")
        print("Fail")
        return False
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
        print(f"Actual: {result}")
        print("Fail")
        return False

