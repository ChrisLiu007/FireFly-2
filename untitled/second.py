__author__ = 'hyw356'

import numpy
from math import exp, pi, sqrt, sin, floor
from GitProject.FireFly.untitled.michaelwicz_function import Michaelwicz_function
from GitProject.FireFly.untitled.yang_function import Yang_Function
from GitProject.FireFly.untitled.Rosenbrock_function import Rosenbrock_function
from GitProject.FireFly.untitled.DeJong_function import DeJong_function

def second(no_fireflies, maxGeneration, dimension):
    # General parameters

    # FireFlay Algorithm parameters
    alpha = 0.2  # Randomness 0--1 (highly random)
    beta0 = 1  # minimum value of beta
    gamma = 1  # Absorption coefficient
    alpha_damp = 0.98

    # objective function valu parameters
    Ub = 5.12
    Lb = -5.12

    delta = 0.05 * (Ub - Lb)
# Objective function
    objective_function = DeJong_function()
    dmax = (Ub - Lb) * sqrt(dimension)
#Initialization

#Empty Firefly Structure
    fireflies = numpy.zeros(no_fireflies)
    Light_intensity = numpy.zeros(no_fireflies)
    fireflies_location = numpy.random.uniform(Lb, Ub, (no_fireflies, dimension))

#Initialize Best Solution Ever Found
    BestCostEver = numpy.zeros(no_fireflies)
    BestCostEver.fill(float("inf"))
    BestLocationEver = numpy.zeros(no_fireflies)
    BestLocationEver.fill(float("inf"))

    # random locations for fireflies

    for i in range(0, no_fireflies):
        fireflies[i] = objective_function.compute(fireflies_location[i, :], dimension)
        Light_intensity[i] = fireflies[i]
        if (Light_intensity[i] <= BestCostEver).any():
            BestCostEver=Light_intensity[i]
            BestLocationEver = fireflies_location[i]

    light_intensity_best = numpy.zeros(maxGeneration)
    fireflies_location_best = numpy.zeros(maxGeneration)

    for G in range(0,maxGeneration):



         # Make a copy of the fireflies_ location & light_intensity
         light_intensity_copy = Light_intensity
         fireflies_location_copy = fireflies_location



         #Move all fireflies to the better locations

         for i in range (no_fireflies):
             light_intensity_copy[i]= "inf"
             for j in range (no_fireflies):

                 if (Light_intensity[i] > Light_intensity[j]).any():

                     distance_betweet_Fi_Fj= numpy.linalg.norm(fireflies_location[i,:]-fireflies_location_copy[j,:])/dmax
                     beta = beta0 * exp(-gamma*(distance_betweet_Fi_Fj**2))
                     e = delta * numpy.random.uniform(-1,+1,dimension)

                     a = numpy.random.rand(dimension)
                     b = fireflies_location[j,:] - fireflies_location[i,:]
                     fireflies_location_new = fireflies_location[i,:] + beta * numpy.multiply(a,b) + alpha * e

                     #check the poundries
                     fireflies_location_new = numpy.clip(fireflies_location_new, Lb, Ub)



                     Light_intensity_new = objective_function.compute(fireflies_location_new,dimension)
                     #print("Light_intensity_new =", Light_intensity_new )

                     if (Light_intensity_new <= light_intensity_copy[i]).any():
                         light_intensity_copy[i] = Light_intensity_new
                         fireflies_location_copy[i,:] = fireflies_location_new
                         if (light_intensity_copy[i] <= BestCostEver).any():
                             BestCostEver= light_intensity_copy[i]
                             BestLocationEver = fireflies_location_copy[i]
                     #print("BestCostEver=",BestCostEver)
                     #print("BestLocationEve=", BestLocationEver)




                     # Ranking fireflies by their light intensity
          #merge values
         fireflies_location=numpy.concatenate((fireflies_location,fireflies_location_copy),axis=0)
         Light_intensity=numpy.append(Light_intensity,light_intensity_copy)

          #sort the values
         Light_intensity = numpy.sort(Light_intensity)
         light_intensity_sorted_index = numpy.argsort(Light_intensity)
         fireflies_location = fireflies_location[light_intensity_sorted_index, :]

    #return to the acual size
         Light_intensity = Light_intensity[0:no_fireflies]
         fireflies_location = fireflies_location[0:no_fireflies,:]
    #best vlaues
         light_intensity_best[G] = BestCostEver
         #fireflies_location_best[]=BestLocationEver
         alpha = alpha * alpha_damp

    print("best value:",numpy.around(light_intensity_best[G],3))
    print("best Location:", numpy.around(BestLocationEver,3))


#if __name__ == '__main__':








