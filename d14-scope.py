# Description: https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        result = []
        for i in self.__elements:
            for j in self.__elements:  # don't need to run over all indices
                result.append(abs(i - j))
                
        self.maximumDifference = max(result)

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)