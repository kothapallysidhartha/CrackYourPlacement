class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        """if n == 0:  # Base case for F(0)
            return 0
        elif n == 1:  # Base case for F(1)
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)  # Recursive case"""

        if n<=1:
            return n
        else:
            return self.fib(n-1)+self.fib(n-2)
