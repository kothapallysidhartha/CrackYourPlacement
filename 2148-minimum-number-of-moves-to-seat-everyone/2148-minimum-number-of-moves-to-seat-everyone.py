class Solution:
    def minMovesToSeat(self, seats, students):
        ans = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])
        return ans
