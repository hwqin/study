'''
Problem statement
For a given array with N elements, you need to find the length of the longest subsequence from the array
such that all the elements of the subsequence are sorted in strictly increasing order.

Strictly Increasing Sequence is when each term in the sequence is larger than the preceding term.

For example:
[1, 2, 3, 4] is a strictly increasing array, while [2, 1, 4, 3] is not.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input :
6
5 4 11 1 16 8
Sample Output 1 :
3
Explanation of Sample Input 1:
Length of longest subsequence is 3 i.e. [5, 11, 16] or [4, 11, 16].

'''

def longestIncreaseSubseq(A):
    if A is None or len(A) == 0:
        return 0

    n = len(A)
    dm = [1] * n #max subsequence length, default to 1, as each element at least contains 1 element subsequence
    
    for i in range(1, n):
        for j in range(i):
            if (A[i]> A[j]):
                tempm = dm[j] + 1
                dm[i] = max(dm[i], tempm)
                # print(dm[i]); optionally, remember the index of previous number's index in sequence if tempm > dm[i]
    print (dm)
    return max(dm)

arr = [5, 4, 11, 1, 16, 8]

print(longestIncreaseSubseq(arr))