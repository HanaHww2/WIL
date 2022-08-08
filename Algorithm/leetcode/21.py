# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head1 = list1
        head2 = list2
        result = ListNode(val='')
        temp = result

        while head1 or head2:
            if not head2 or (head1 and head1.val <= head2.val):
                temp.val = head1.val
                head1 = head1.next

            elif not head1 or (head2 and head1.val > head2.val):
                temp.val = head2.val
                head2 = head2.next

            if not (head1 or head2):
                break

            # 매번 새로운 노드를 생성하면서
            # 반환할 연결리스트를 만든다.
            temp.next = ListNode()
            temp = temp.next

        return result

    # 책에서 제공하는 풀이 적용
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # 재귀를 활용하며, 기존 연결리스트의 포인터를 조작하는 방식
        if not list1 or (list2 and list1.val > list2.val):
            # 다중 할당을 활용한 스왑
            list1, list2 = list2, list1

        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1
