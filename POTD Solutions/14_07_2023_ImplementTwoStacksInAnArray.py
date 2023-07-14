class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = n

    # Function to push an integer into stack 1
    def push1(self, x):
        # Check if there is space available for stack 1
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow")

    # Function to push an integer into stack 2
    def push2(self, x):
        # Check if there is space available for stack 2
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow")

    # Function to remove an element from top of stack 1
    def pop1(self):
        # Check if stack 1 is empty
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 -= 1
            return x
        else:
            return -1  # Stack 1 is empty

    # Function to remove an element from top of stack 2
    def pop2(self):
        # Check if stack 2 is empty
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 += 1
            return x
        else:
            return -1  # Stack 2 is empty
