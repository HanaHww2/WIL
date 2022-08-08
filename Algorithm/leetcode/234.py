# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string = ''
        while head:
            # 주어진 연결리스트를 문자열(혹은 리스트) 로 변환
            string += str(head.val)
            head = head.next

        # 역순으로 문자열을 뒤집어서 같은지 확인, 최적화가 필요한 과정
        # 1. 전체 비교
        # if string == string[::-1]: return True

        # 2. 절반으로 슬라이싱하여 비교
        length = len(string)
        left, right = string[:math.floor(
            length/2)], string[math.ceil(length/2):]

        if left == right[::-1]:
            return True

        return False

    # 3. 포인터를 이용해 비교
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string = ''
        while head:
            # 주어진 연결리스트를 문자열(혹은 리스트) 로 변환
            string += str(head.val)
            head = head.next

        length = len(string)-1
        idx = 0
        while idx < length/2:
            if string[idx] != string[length-idx]:
                return False
            idx += 1
        return True

    # 데크를 이용한 펠린드롬 체크 (위 2, 3 풀이와 유사한 속도)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = collections.deque()

        while head:
            # 주어진 연결리스트를 문자열(혹은 리스트) 로 변환
            queue.append(head.val)
            head = head.next

        while len(queue) > 1:
            if queue.pop() != queue.popleft():
                return False

        return True
