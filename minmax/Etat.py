class Etat:
    def __init__(self, n):
        self.piles = n

    def get_next_actions(self):
        res = []
        for i, v in enumerate(self.piles):
            if (v < 3):
                continue
            else:
                for j in range(1, v // 2 + 1):
                    if (v == 2 * j):
                        continue

                    temp = self.piles.copy()
                    temp.pop(i)
                    temp.insert(i, j)
                    temp.insert(i, v - j)
                    res.append(temp)
        return res

    def is_final(self):
        return max(self.piles) < 3

    def __repr__(self):
        return f"{self.piles}"