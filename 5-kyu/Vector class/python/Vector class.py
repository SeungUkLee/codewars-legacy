# My Solution
import math
class Vector:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        if self.value.__len__() != other.value.__len__():
            raise Exception

        return Vector([x + y for x, y in zip(self.value, other.value)])

    def subtract(self, other):
        if self.value.__len__() != other.value.__len__():
            raise Exception

        return Vector([x - y for x, y in zip(self.value, other.value)])

    def dot(self, other):
        if self.value.__len__() != other.value.__len__():
            raise Exception

        return sum(x * y for x, y in zip(self.value, other.value))

    def norm(self):
        return math.sqrt(sum(pow(x, 2) for x in self.value))

    def equals(self, other):
        if self.value.__len__() != other.value.__len__():
            return False

        for x, y in zip(self.value, other.value):
            if x != y:
                return False
        return True

    def __str__(self):
        res = ""
        for v in self.value:
            res += "{},".format(v)

        return "(" + res[:-1] + ")"

# Best Practice & Clever
"https://www.codewars.com/kata/vector-class/solutions/python"
