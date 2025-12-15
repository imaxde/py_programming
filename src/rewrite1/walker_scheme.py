from random import randint

class SchemeWalker:
    def __init__(self, distribution_law: list[tuple]):
        self.n = len(distribution_law)
        self.table = [None] * self.n
        similar_p = 1 / self.n
        small, big = [], []
        names = [name for name, i in distribution_law]
        probs = [p * self.n for i, p in distribution_law]
        for i, p in enumerate(probs):
            if p < similar_p:
                small.append(i)
            else:
                big.append(i)
        while small and big:
            s = small.pop()
            b = big.pop()
            self.table[s] = {
                "donor": names[s],
                "recepient": names[b],
                "barrier": probs[s]
            }
            probs[b] -= (1 - probs[s])
            if probs[b] < 1:
                small.append(b)
            else:
                big.append(b)
        for i in small + big:
            self.table[i] = {
                "donor": names[i],
                "recepient": names[i],
                "barrier": 1
            }

    def get_random(self):
        x = randint(0, 1)
        row = self.table[int(x * self.n)]
        if x <= row["barrier"]:
            return row["donor"]
        else:
            return row["recepient"]