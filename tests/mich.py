import numpy
from math import sin,pi

class mich:

    def Compute(self, decision_variable, dimension):

        total=numpy.zeros(dimension)
        result = numpy.zeros(dimension)
        for i in range(0,dimension):
            result = sin(decision_variable[i]) * (sin(i*decision_variable[i]**2/pi))**(20)
            total = total + result

        return -total





if __name__ == '__main__':

    v=numpy.random.uniform(0, 1, (2))
    t = mich()
    tt=t.Compute(v,2)
    print(tt)


