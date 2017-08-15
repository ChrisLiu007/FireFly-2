import math
import numpy

class Yang_Function:
    def compute(self, decision_variable, dimensions):
        a= 15
        X1=0
        Y1=0
        Z1=1
        for i in range (dimensions):
            X= -(decision_variable[i]/a)**10
            X1= X1 + X

        for i in range (dimensions):
            Y= -(decision_variable[i])**2
            Y1= Y1+ Y

        for i in range (dimensions):
            Z = (math.cos(decision_variable[i]))**2
            Z1 = Z1 *Z

        FF= (math.exp(X1) - (2*math.exp(Y1))) * Z1

        return FF

