__author__ = 'hyw356'
import math,re
from numpy import matlib
import numpy
from GitProject.FireFly.untitled.michaelwicz_function import Michaelwicz_function
from GitProject.FireFly.untitled.second import second
#from TestFire.FFA import FFA
My_list= []

for member in dir(re):
    if "find" in member:
        My_list.append(member)


#print sorted(My_list)
MF= Michaelwicz_function()
#print ("the result",MF.compute([.5,.6],2))
x = numpy.random.uniform(0,1,4)
xx = numpy.sort(x)
y = numpy.argsort(x)
#print (x)
#print("xx",xx)
#print(y)
x= x[y]
#print(x)
xxx = numpy.random.uniform(0,1,4)
numpy.random.seed()
print(math.exp(.5698))
xxx = xxx[y]
#print(math.cos(.5698))
scale = numpy.ones(2) * abs(4 - 0)
#print(scale)
a=[[1,2],[3,4]]
b=[[11,3],[13,14]]
#print(numpy.multiply(a,b))
#print(numpy.random.uniform(0,1,(2,2)))
#print(numpy.clip(b, 0, 4))
#print("___________________________________________________-")
s= second(40,10,2)
print("___________________________________________________-")
#print (s)
#print ("the result",MF.compute([.5,.6],2))
valuesa = numpy.random.uniform(1,10,(5,2))
valuesb = numpy.random.uniform(1,10,(5,2))
for i in range(3):
    y=numpy.random.uniform(0, 1, (1))
    z = numpy.matlib.repmat(y,i,2)
#print("z=",z)
#for i in range (3):
 #   print("i=",z[i])

#print (valuesa)
#print (valuesb)
#print(numpy.where(valuesa>valuesb))

#for x in numpy.nditer(valuesb):
 #   for y in numpy.nditer(valuesa):
  #      print ("hi")
d=2
f=5
F=[]
x= numpy.random.uniform(0,1,(f,d))
for i in range (f):
    for j in range (d):

        x =numpy.append(x,x)
        #F= F.append(x[i])
        #if numpy.greater(valuesa[i], valuesb[j]):

#print("x=" ,x)
#print("F=" ,F)
dimension =2
no_fireflies =5
fireflies_location = numpy.random.uniform(0, 1, (no_fireflies, dimension)) * (4 - 0) + 0
fireflies = numpy.zeros(no_fireflies)
Light_intensity = numpy.zeros(no_fireflies)
#print(valuesb[valuesb > valuesa])
if -7.78739477403e-35 < -1.18094111732e-12:
#    print("true")

#for i in range (no_fireflies):
    for j in range(no_fireflies):
        #print("Light_intensity", Light_intensity)
        #print("fireflies_location", fireflies_location)
        for i in range(0, no_fireflies):
            fireflies[i] = MF.compute(fireflies_location[i, :], dimension)
            Light_intensity[i] = fireflies[i]
#print("Light_intensity",Light_intensity)
#print("fireflies_location",fireflies_location)





#print("value")
class Algorithm:


    class firflay:
        def __init__(self, cost , position):
           self.cost= cost
           self.position= position

    class best_soluation:
        def __init__(self,cost, position):
            self.cost = cost
            self.position = position


    def __init__(self, fireflies_no, maxGenration, dimension):
        self.fireflies_no = fireflies_no
        self.maxGenration = maxGenration
        self.dimension = dimension

    def intialization(self):
        fireflay_pop = numpy.matlib.repmat(self.firflay,self.fireflies_no,1)
        




#t= FFA("F1",0,4,2,5,10)