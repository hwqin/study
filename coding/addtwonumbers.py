# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        node1 = l1
        node2 = l2
        result = None
        tail_node = None
        flow_value = 0
        while node1 is not None and node2 is not None:
            value1 = node1.val
            value2 = node2.val
            sum_value = value1 + value2 + flow_value
            if sum_value >= 10:
                sum_value %= 10
                flow_value = 1
            else:
                flow_value = 0

            res_node = ListNode(sum_value)
            if result is None:
                result = res_node
                tail_node = result
            else:
                tail_node.next = res_node
                tail_node = res_node

            node1 = node1.next
            node2 = node2.next
        
        remain_node = None
        if node1 is not None:
            print("node1 is not none")
            remain_node = node1
        elif node2 is not None:
            print("node2 is not none")
            remain_node = node2


        while remain_node is not None:
            value = remain_node.val
            sum_value = value + flow_value
            if sum_value >= 10:
                sum_value %= 10
                flow_value = 1
            else:
                flow_value = 0

            res_node = ListNode(sum_value)
            if tail_node is None:
                result = res_node
                tail_node = result
            else:
                tail_node.next = res_node
                tail_node = res_node

            remain_node = remain_node.next

        if flow_value > 0:
            res_node = ListNode(flow_value)
            tail_node.next = res_node

        return result
    