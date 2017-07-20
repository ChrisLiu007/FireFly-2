import numpy

from tests.mich import mich

def FireF(no_fireflies, Max_generation):
    # algorithm parameters
    alpha = 0
    beta_0 = 0
    gamma = 0


    #objective function parameters
    diminsion = 0
    Ub = 0
    Lb = 0
    Objective_Function_Value = mich()


    # initalize fireflies
    Fireflies_objective_value = numpy.zeros(no_fireflies)
    Light_intensity = numpy.zeros(no_fireflies)
    Fireflies_Location = numpy.random.uniform(0,1,(no_fireflies,diminsion)) * (Ub - Lb)+ Lb


