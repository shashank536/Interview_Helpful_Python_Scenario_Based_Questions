"""Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n."""


class Generator:
    def __init__(self, n):
        self.n = n

    def divisiblebySeven(self):
        for i in range(0, self.n + 1):
            if i % 7 == 0:
                yield i


obj = Generator(n=100)
for i in obj.divisiblebySeven():
    print(i)
