# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 요소 정렬 및 병합
    def mergeTwoList(self, l1, l2):
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoList(l1.next, l2)
        return l1

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 탈출조건
        if not (head and head.next):
            return head

        # 런너 기법을 이용해 중앙 노드 찾기
        half, slow, fast = None, head, head

        while fast and fast.next:
            # half를 중앙 바로 이전 값으로 둔다.
            half, slow, fast = slow, slow.next, fast.next.next

        half.next = None  # 연결리스트를 분할

        # 재귀 호출하여 단일 노드로 모두 분할
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        # 분할된 노드들을 다시 취합하여 반환
        return self.mergeTwoList(l1, l2)

    # 파이썬 내장 정렬 함수 이용

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 연결 리스트를 파이썬 리스트로 변환
        temp = []
        p = head

        while p:
            temp.append(p.val)
            p = p.next

        temp.sort()  # 정렬
        p = head  # 포인터를 헤드로 재이동

        for n in temp:
            p.val = n
            p = p.next

        return head
