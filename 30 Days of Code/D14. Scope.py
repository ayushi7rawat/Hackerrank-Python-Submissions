class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=0

    def computeDifference(self):
        mini=min(self.__elements)
        maxi=max(self.__elements)
       
        self.maximumDifference = maxi-mini

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)