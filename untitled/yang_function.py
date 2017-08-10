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
        L1 = math.exp(- (decision_variable[0]/a)**10 - (decision_variable[1]/a)**10)
        L2 = 2 * math.exp( - (decision_variable[0] - 0)**2 - (decision_variable[1] - 0)**2)
        L3 = (math.cos(decision_variable[0]))**2 * (math.cos(decision_variable[1]))**2
        F= ( L1 - L2) * L3
        return F

