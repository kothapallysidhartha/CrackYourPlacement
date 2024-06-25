#User function Template for python3

class Solution:
    def printNos(self, n):
        # Code here
        while n:
            print(n,end=" ")
            self.printNos(n-1)
            
            break
        #


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printNos(N)
        print()
# } Driver Code Ends