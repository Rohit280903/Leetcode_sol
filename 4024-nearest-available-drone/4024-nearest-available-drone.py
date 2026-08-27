class Solution:
    def nearestDrone(self, drones, t):
        minDist = float('inf')
        idx = -1

        for i in range(len(drones)):
            dist = abs(t[0] - drones[i][0]) + abs(t[1] - drones[i][1])

            if dist <= drones[i][2] and minDist > dist:
                minDist = dist
                idx = i

        return idx