# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode()

        # 재귀를 이용
        # 뒤에서 부터 역참조하도록 구현
        def reverse_recursively(first, second):

            # nonlocal new_head
            if second.next:
                reverse_recursively(second, second.next)
            else:
                # 내부함수에서 외부 함수의 변수에 바로 접근하는 경우,
                # 불변 객체(int, string)라면 읽기만 허용된다.
                # 혹은 내부 함수 안에서 새로운 주소로 객체가 할당된다.
                # 그러나, 이 값을 외부 함수의 변수에는 반영할 수 없다.
                # list 와 같은 컬렉션 객체를 활용한다면, 새롭게 생성된 객체(값)를
                # 그 컬렉션이 가진 포인터로 가리키도록 만들 수는 있다.
                new_head.next = second

            first.next = None  # circular 참조 에러 방지
            second.next = first

        if not head or not head.next:
            return head
        reverse_recursively(head, head.next)

        return new_head.next

    # 책에서 제공하는 재귀 풀이
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):

            # 더 이상 진행할 노드가 없다면,
            if not node:
                return prev  # 마지막 노드가 헤드가 된다.

            # 기존에 가리키던 노드는 temp에 담아두고, 다음 시행에 전달
            temp, node.next = node.next, prev

            return reverse(temp, node)

        return reverse(head)  # 가장 마지막 노드가 담길 prev 가 반환된다.

    # 반복 구조를 이용한 뒤집기 풀이
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node, prev = head, None

        while node:
            # 기존의 다음 노드는 temp에 담고,
            # 이전 노드를 다음 노드로 연결하며 스왑
            temp, node.next = node.next, prev
            prev, node = node, temp

        return prev
