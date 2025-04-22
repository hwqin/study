'''
Problem statement
Aahad and Harshit always have fun by solving problems.
Harshit took a sorted array consisting of distinct integers 
and rotated it clockwise by an unknown amount. For example,
he took a sorted array = [1, 2, 3, 4, 5] and if he rotates it by 2,
then the array becomes: [4, 5, 1, 2, 3].

After rotating a sorted array, Aahad needs to answer Q queries asked by Harshit,
each of them is described by one integer Q[i]. which Harshit wanted him to search in the array.
For each query, if he found it, he had to shout the index of the number, otherwise, he had to shout -1.

For each query, you have to complete the given method where 'key' denotes Q[i].
If the key exists in the array, return the index of the 'key', otherwise, return -1.

Note:

Can you solve each query in O(logN) ?
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= N <= 10^6
-10^9 <= A[i] <= 10^9
1 <= Q <= 10^5
-10^9 <= Q[i] <= 10^9

Time Limit: 1sec
Sample Input 1:
4
2 5 -3 0
2
5
1
'''

def findkey(key, array, sindex, endindex):
    length = len(array)
    if length == 0:
        return -1
    
    if sindex > endindex:
        return -1
    
    start_num = array[sindex]
    if sindex == endindex:
        return sindex if (start_num == key) else -1
    end_num = array[endindex]
    
    mindex = int((sindex + endindex) / 2)
    middle_num = array[mindex]
    if key == middle_num:
        return mindex
    
    '''
    if start_num < end_num:
        # whole sub array is increasing order
        if key < middle_num: # left half
            return findkey(key, array, sindex, mindex - 1)
        else: # right half
            return findkey(key, array, mindex + 1, endindex)
    else:
    ''' 

    if middle_num > end_num:
        # max value and min value in second half
        if key < start_num:
            return findkey(key, array, mindex + 1, endindex)
        else:
            return findkey(key, array, sindex, mindex - 1)
    else:
        # max and min value in first half
        if key > end_num:
            return findkey(key, array, sindex, mindex - 1)
        else:
            return findkey(key, array, mindex + 1, endindex)

array = [2, 5, -3, 0]

print (findkey(-3, array, 0, 3))


def findkey2(key, array, sindex, endindex):
    length = len(array)
    if length == 0:
        return -1
    
    if sindex > endindex:
        return -1
    
    start_num = array[sindex]
    if sindex == endindex:
        return sindex if (start_num == key) else -1
    end_num = array[endindex]
    
    mindex = int((sindex + endindex) / 2)
    middle_num = array[mindex]
    if key == middle_num:
        return mindex

    if middle_num > end_num:
        # max value and min value in second half, first half is sorted
        if start_num<= key < middle_num:
            return findkey(key, array, sindex, mindex - 1)
        else:
            return findkey(key, array, mindex + 1, endindex)
    else:
        # max and min value in first half, second half is sorted
        if middle_num < key <= end_num:
            return findkey(key, array, mindex + 1, endindex)
        else:
            return findkey(key, array, sindex, mindex - 1)
