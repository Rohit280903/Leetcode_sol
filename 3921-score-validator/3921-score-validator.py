class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        for elem in events:
            if elem == "WD" or elem == "NB":
                score += 1
            elif elem == "W":
                counter += 1
                if counter == 10:
                    break
            else:
                score += int(elem)
        return [score, counter]