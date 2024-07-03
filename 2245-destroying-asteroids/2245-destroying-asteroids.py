class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        c=0
        for i in asteroids:
            if i<=mass:
                mass+=i
                c+=1
        if c==len(asteroids):
            return True
        else:
            return False

        