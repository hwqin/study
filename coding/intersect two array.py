##
'''
Intersection Of Two Sorted Arrays
+20
40
Easy
10 mins
166.1k
653
Problem statement
You are given two arrays 'A' and 'B' of size 'N' and 'M' respectively.
Both these arrays are sorted in non-decreasing order. You have to find the
intersection of these two arrays.

Intersection of two arrays is an array that consists of all the common
elements occurring in both arrays.

Note :
1. The length of each array is greater than zero.
2. Both the arrays are sorted in non-decreasing order.
3. The output should be in the order of elements that occur in the original arrays.
4. If there is no intersection present then return an empty array.

'''
# increasing order
result = []
# i1, i2 to iterate through arr1 and arr2
# if arr1[i1] < arr[i2] -> i1 += 1
# if arr1[i1] > arr[i2] -> i2 += 1
# if ==, append (element), i1 +=1 and i2 +=1
#
def find_intersection(A, B):
    i = 0  # Pointer for A
    j = 0  # Pointer for B
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return intersection
