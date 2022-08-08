# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = temp = ListNode()
        carry = 0

        while l1 or l2 or carry:
            # 두 입력 값의 합 계산
            temp_sum = 0
            if l1:
                temp_sum += l1.val
                l1 = l1.next
            if l2:
                temp_sum += l2.val
                l2 = l2.next

            # 캐리 값 합산 로직
            if carry > 0:
                temp_sum += carry
                carry = 0

            # 추가 캐리 계산
            if temp_sum > 9:
                carry = temp_sum // 10

            temp.val = temp_sum - 10*carry

            if not l1 and not l2 and carry == 0:
                break

            temp.next = ListNode()
            temp = temp.next

        return root

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = temp = ListNode()
        carry = 0

        while l1 or l2 or carry:
            # 두 입력 값의 합 계산
            temp_sum = 0
            if l1:
                temp_sum += l1.val
                l1 = l1.next
            if l2:
                temp_sum += l2.val
                l2 = l2.next

            # 파이썬의 내장함수 및 다중 할당을 이용해서 코드 간결화
            carry, val = divmod(temp_sum+carry, 10)

            # 시작 노드를 root.next로 해서, 브레이크 분기문 제거
            temp.next = ListNode(val)
            temp = temp.next

        return root.next

    # 마지막 풀이
    # 자료형을 변환하여 풀이
    # 연결리스트를 역순으로 뒤집는 함수
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            temp, node.next = node.next, prev
            prev, node = node, temp

        return prev

    # 연결리스트를 파이썬 리스트로 변환한다.
    def toList(self, node: ListNode) -> list:
        result = list()

        while node:
            result.append(node.val)
            node = node.next

        return result

    # 다시 역순의 연결리스트로 변환한다.
    def toReversedLinkedList(self, result: list) -> ListNode:
        prev = None
        for n in result:
            node = ListNode(n)
            node.next = prev
            prev = node  # 역순이므로, 앞 노드를 잠시 보관해둔다.

        return node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        result_sum = int("".join(str(w) for w in a)) + \
            int(''.join(str(w) for w in b))

        return self.toReversedLinkedList(str(result_sum))
