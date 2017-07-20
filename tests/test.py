from math import  sin, pi
import numpy,random


def test(y):
    x = numpy.ones(y)
    z = x - 0.5
    print(x)
    print(z)

test(5)
print(abs(4-9))
n=4
zn=numpy.ones(n)
xx= zn.fill(3)
print(zn)
ns = numpy.random.uniform(0, 1, (n, 2))
ns2= ns[1,:]
decision_variable = s = numpy.random.uniform(0, 1, 2)
total=numpy.ones(2)
result = numpy.ones(2)
result[0] = sin(decision_variable[0]) * (sin(0 * decision_variable[0] ** 2 / pi)) ** (20)
result[1] = sin(decision_variable[1]) * (sin(1 * decision_variable[1] ** 2 / pi)) ** (20)
print(total)
print(result)
print("--------------------------")
print(ns)
print(ns2)
print(random.random())
delta = [1,2,3,4]
for i in range (n):
     delta.append(.5 * zn[i])

print(delta)
