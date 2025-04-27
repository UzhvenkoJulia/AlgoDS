# 12.4. Рейки (100%)

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.element_count = 0

    def is_empty(self):
        return self.head is None

    def push(self, n):
        node = Node(n)
        node.next = self.head
        self.head = node
        self.element_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("empty")
        temp = self.head
        self.head = self.head.next
        value = temp.data
        del temp
        self.element_count -= 1
        return value

    def back(self):
        if self.is_empty():
            raise IndexError("empty")
        return self.head.data


def main():
    while True:
        n = int(input())
        if n == 0:
            break

        while True:
            arr = list(map(int, input().split()))

            if arr[0] == 0:
                print()
                break

            stack = Stack()
            current = 1
            is_possible = True

            for i in range(n):
                while current <= n and (stack.is_empty() or stack.back() != arr[i]):
                    stack.push(current)
                    current += 1

                if not stack.is_empty() and stack.back() == arr[i]:
                    stack.pop()
                else:
                    is_possible = False
                    break

            print("Yes" if is_possible else "No")


if __name__ == "__main__":
    main()