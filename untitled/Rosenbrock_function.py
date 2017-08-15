import math
import numpy

class Rosenbrock_function:
    def compute(self, decision_variable, dimensions):
        sum =0
        for i in range (dimensions-1):
            xi=decision_variable[i]
            xnext=decision_variable[i+1]
            new = 100*(xnext-(xi**2))**2 + (xi-1)**2
            sum = sum +new

        return sum