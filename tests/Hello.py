import random
import numpy,math
from untitled.second import second
from untitled.michaelwicz_function import Michaelwicz_function

class Hello:
    def __init__(self,x):
        self.x=x
        print(x)


if __name__ == '__main__':
    no_fireflies=5
    beta0 = 1  # minimum value of beta
    gamma = 1  # Absorption coefficient
    alpha = 0.2
    Ub = 4
    Lb = 0
    delta = 0.05 * (Ub - Lb)
    dimension = 2
    objective_function = Michaelwicz_function()
    x= Hello("-----------------------------------")
    y= random.random()
    #print(y)
    #t= second(40,10,2)
    #print(  numpy.zeros(40))
    fireflies = numpy.zeros(no_fireflies)
    Light_intensity = numpy.zeros(no_fireflies)
    fireflies_location = numpy.random.uniform(0, 1, (no_fireflies, dimension)) * (Ub - Lb) + Lb
    print("fireflies:",fireflies)
    print("Light_intensity:",Light_intensity)
    print("fireflies_location:",fireflies_location)
    x = Hello("-----------------------------------")
    for i in range(0, no_fireflies):
        fireflies[i] = objective_function.compute(fireflies_location[i, :], dimension)
        Light_intensity[i] = fireflies[i]

    #print("fireflies:", fireflies)
    print("Light_intensity:", Light_intensity)
    x = Hello("-----------------------------------")
    # Ranking fireflies by their light intensity
    Light_intensity = numpy.sort(fireflies)
    light_intensity_sorted_index = numpy.argsort(fireflies)
    fireflies_location = fireflies_location[light_intensity_sorted_index, :]
    print("Light_intensity:", Light_intensity)
    print("fireflies_location:",fireflies_location)
    x = Hello("-----------------------------------")
    light_intensity_best = Light_intensity[0]
    fireflies_location_best = fireflies_location[0, :]
    print("Light_intensity best:", light_intensity_best)
    print("fireflies_location best:", fireflies_location_best)
    x = Hello("-----------------------------------")
    light_intensity_copy = Light_intensity
    #fireflies_location = numpy.clip(fireflies_location, Lb, Ub)
    distance_betweet_Fi_Fj = numpy.sqrt(numpy.sum((fireflies_location[1, :] - fireflies_location[0, :]) ** 2))
    print("f-f=",(fireflies_location[1, :] - fireflies_location[0, :]) ** 2)
    print(distance_betweet_Fi_Fj)
    dmax = (Ub-Lb)* math.sqrt(dimension)
    for i in range(no_fireflies):
        for j in range(no_fireflies):
            #print("out i=", i)
            #print("out j=", j)
            #print("________________________________________________")
            if Light_intensity[i] > light_intensity_copy[j]:
                print("in i=",i)
                print("in j=",j)
                print("Light_intensity[i]",Light_intensity[i])
                print("Light_intensity[j]", light_intensity_copy[j])

                distance_betweet_Fi_Fj = numpy.linalg.norm(fireflies_location[i,:] - fireflies_location[j,:]) / dmax
                print("distance_betweet_Fi_Fj", distance_betweet_Fi_Fj)
                print("________________________________________________")
                beta = beta0 * math.exp(-gamma * distance_betweet_Fi_Fj ** 2)
                e = delta * numpy.random.uniform(-1, +1, dimension)
                #print("distance_betweet_Fi_Fj",distance_betweet_Fi_Fj)
                a = numpy.random.uniform(0, 1, (dimension, dimension))
                #b = fireflies_location[j, :] - fireflies_location[i, :]
                #fireflies_location = fireflies_location[i, :] + beta * numpy.multiply(a, b) + alpha * e

                # check the poundries
                #fireflies_location = fireflies_location.append(numpy.clip(fireflies_location, Lb, Ub))

                #Light_intensity[i] = objective_function.compute(fireflies_location[i, :], dimension)

                #print("Light_intensity",Light_intensity[i])
    print("distance_betweet_Fi_Fj",numpy.sum(distance_betweet_Fi_Fj))
