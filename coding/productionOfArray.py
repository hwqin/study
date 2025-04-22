
'''
Problem statement
You have been given an integer array/list (ARR) of size N.
You have to return an array/list PRODUCT such that PRODUCT[i] is equal to the product of
all the elements of ARR except ARR[i]

 Note :
Each product can cross the integer limits, so we should take modulo of the operation. 

Take MOD = 10^9 + 7 to always stay in the limits.
Follow up :
Can you try solving the problem in O(1) space?
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <= 100
0 <= N <= 10^5
0 <= ARR[i] <= 10^5

Time Limit: 1 sec
Sample Input 1 :
2
3
1 2 3
3
5 2 2
Sample Output 1 :
6 3 2
4 10 10
Explanation for Sample Output 1 :
 Test case 1 : Given array = {1, 2, 3] 
 Required array = [2 * 3, 1 * 3, 1 * 2] = [6, 3, 2]
 Test case 2 : Given array = {5, 2, 2] 
 Required array = [2 * 2, 5 * 2, 5 * 2] = [4, 10, 10]
 
'''

# Follow up: O(1) space solution (excluding the output array)
def product_except_self_o1_space(arr):
    
    n = len(arr)
    if n == 0:
        return []
    
    MOD = 10**9 + 7
    product = [1]*n
    prefix_product = 1
    for i in range(n):
        product[i] = prefix_product
        prefix_product = (arr[i] * prefix_product) % MOD
        
    surfix_product =1
    for j in range(n-1, -1, -1):
        product[j] = (product[j] * surfix_product) %MOD
        surfix_product = (surfix_product * arr[j]) % MOD

    return product

arr1 = [1, 2, 3, 4, 5]
print (product_except_self_o1_space(arr1))
