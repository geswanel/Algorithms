from collections import deque

def deque_basics():
    d = deque()
    d.append(1)
    d.appendleft(2)
    d.pop()
    d.popleft()


class RecentCounter:
    def __init__(self):
        self.recent_requests = deque()
        self.__TIME_WINDOW = 3000

    def ping(self, t: int) -> int:
        self.recent_requests.append(t)
        while self.recent_requests[0] < t - self.__TIME_WINDOW:
            self.recent_requests.popleft()
        return len(self.recent_requests)


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        banned = [False] * len(senate)
        cnt = {"D": senate.count("D"), "R": senate.count("R")}
        i = 0
        while cnt["D"] > 0 and cnt["R"] > 0:
            next_senator = senate[i % n]   # D or R
            i += 1
            if not banned[(i - 1) % n]:
                j = i
                while j < n + i - 1 and (senate[j % n] == next_senator or banned[j % n]):
                    j += 1
                if j < n + i - 1 and senate[j % n] != next_senator and not banned[j % n]:
                    banned[j % n] = True
                    cnt["D" if next_senator == "R" else "R"] -= 1
            
            #print(senate, banned, sep="\n")
        
        return "Radiant" if cnt["D"] == 0 else "Dire"





import unittest

class QueueTest(unittest.TestCase):
    def test_predictPartyVictory(self):
        sol = Solution()
        senate = "RD"
        self.assertEqual(sol.predictPartyVictory(senate), "Radiant")

        senate = "RDD"
        self.assertEqual(sol.predictPartyVictory(senate), "Dire")

        senate = "RRDDD"
        self.assertEqual(sol.predictPartyVictory(senate), "Radiant")

        senate = "RDRDDRD"
        self.assertEqual(sol.predictPartyVictory(senate), "Dire")

        senate = "R"
        self.assertEqual(sol.predictPartyVictory(senate), "Radiant")
    


if __name__ == "__main__":
    unittest.main()