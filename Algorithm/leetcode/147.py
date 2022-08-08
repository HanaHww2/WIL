# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # 성능 및 코드 개선이 필요...
    def insertionSort(self, node, sorted_list):
        p = sorted_list

        # 주어진 노드가 정렬된 리스트에서 위치를 찾도록 순회
        while node.val >= p.val:

            if not p.next:
                p.next = node
                break
            if p.next and p.next.val > node.val:
                temp, p.next = p.next, node
                node.next = temp
                break
            p = p.next

        if node.val < p.val:
            node.next = p
            sorted_list = node
        return sorted_list

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = head
        node, head.next = head.next, None

        while node:
            temp, node.next = node.next, None
            sorted_list = self.insertionSort(node, sorted_list)
            node = temp

        return sorted_list

    ##############
    # 위 코드를 조금 개선
    def insertionSort(self, node, sorted_list):
        p = sorted_list

        # 새로운 노드가 가장 앞에 가는 경우
        if node.val < p.val:
            node.next, sorted_list = p, node
            return sorted_list

        # 주어진 노드가 정렬된 리스트에서 위치를 찾도록 순회
        # 매 반복에서 정렬된 리스트 처음부터 새로운 노드가 삽입될 위치 탐색
        # -> 시간복잡도가 증가한다.
        while p.next and p.next.val <= node.val:
            p = p.next
        temp, p.next = p.next, node
        node.next = temp

        return sorted_list

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = head
        node, head.next = head.next, None

        while node:
            temp, node.next = node.next, None

            sorted_list = self.insertionSort(node, sorted_list)
            node = temp

        return sorted_list

    #######
    # 책에서 제공하는 풀이
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = root = ListNode(0)

        while head:
            while cur.next and cur.next.val <= head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            # 알고리즘 최적화
            # 실제 삽입 정렬과 유사하도록, cur 값과 먼저 비교하여
            # 항상 처음부터 탐색하는 로직 개선
            # head가 현재 cur 보다 작은 경우에만
            if head and cur.val > head.val:
                # 시작점(빈 노드)으로 이동
                cur = root

        return root.next
