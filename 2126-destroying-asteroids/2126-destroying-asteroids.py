class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for elem in asteroids:
            if mass < elem:
                return False
            else:
                mass += elem
        return True