import copy
from math import sqrt, exp
import random
from GitProject.FireFly.FireflyAlgorithem.objective_function.nonsmooth_multipeak_function import NonsmoothMultipeakFunctionWrapper
from GitProject.FireFly.FireflyAlgorithem.objective_function.michaelwicz_function_wrapper import MichaelwiczFunctionWrapper

class FA(object):

    class Firefly(object):

        def __init__(self, objective_function, fireflies_location, light_intensity):
            # objective_function: the Function that we need to find its optimized value
            # firefly_location: the coordinate for each firefly (variable) in the generation
            # light_intensity: the result of the objective function

            self.objective_function= objective_function
            self.fireflies_location= fireflies_location
            self.light_intensity= light_intensity

        def update_light_intensity(self):
            # A(1) compute light intensity according to the objective function
            # fill the list of "light_intensity" with objective function value of each firefly

            self.light_intensity = self.objective_function.objective_function_value(self.fireflies_location)

        def copy_objective_function(self):
            # copy the values in another argument to save the original value from changing
            #return a copy of function varibles

            copy_object= copy.deepcopy(self)
            return copy_object

    def __init__(self, objective_function , number_of_variables, objective):

        # objective_function: the Function that we need to find its optimized value
        # number_of_variables: number of variables in the objective function (hence: Diminution)
        # objective: the objective of using the objective function either maximization or minimization

        #my objective function:


        self.objective_function= objective_function
        self.number_of_variables= number_of_variables
        self.objective= objective
 # delta
    def get_decision_variable_value_by_randomization(self, decision_variable_index):
        #B initial random values of the objective function for each firefly
        # return the random values given to the objective function variables

        return (self.objective_function.maximum_decision_variable_values()[decision_variable_index] - self.objective_function.minimum_decision_variable_values()[decision_variable_index]) * 0.05

    def best_function_value_from_list(self, function_values):
        # max(function_values) or min(function_values)
        #return the best value of the funcation accourding to its objective, after evaluating each firefly (choose the best firefly light intensity)

        if self.objective == "maximization":
            best_function_value = max(function_values)
        elif self.objective == "minimization":
            best_function_value = min(function_values)

        return best_function_value

    def search(self, number_of_fireflies, max_generation, randomization_parameter_alpha,
               absorption_coefficient_gamma):
        #1 number_of_fireflies: fireflies number (number of proposed sloutions)
        # max_generation: number of the itrations
        # randomization_parameter_alpha: alpha
        # absorption_coefficient_gamma:
        # return the location (decision_variable) of the best firefly and the light intesity (objective_function) of the best firefly

        self.__initialize_fireflies(number_of_fireflies)
        #alpha_damp = 0.98
        for generation in range(max_generation):

            for firefly in self.__fireflies:
                firefly.update_light_intensity()


            self.__move_fireflies(randomization_parameter_alpha, absorption_coefficient_gamma)



        solution_firefly = self.__select_best_firefly_by_light_intensity(self.__fireflies)

        #print

        return {"best_decision_variable_values": solution_firefly.fireflies_location,
                "best_objective_function_value": solution_firefly.light_intensity}

    def __initialize_fireflies(self, number_of_fireflies):
        #2
        # fill in the array "__fireflies" with values based on B

        self.__fireflies = []
        # assign each firefly with a random initial value for its objective function ( or light intensity)

        for i in range(number_of_fireflies):
            decision_variable_values = [self.get_decision_variable_value_by_randomization(variable_index) for variable_index in range(self.number_of_variables)]
            firefly = FA.Firefly(self.objective_function, decision_variable_values, 0)
            self.__fireflies.append(firefly)

    def __select_best_firefly_by_light_intensity(self, fireflies):
        #3 rank fireflies (sloutions) according to the value of "objective" either MAX of MIN
        # return the value of "best_firefly" with the (max) or (min) value from (light_intensity) list in A(1)

        if self.objective == "maximization":
            best_firefly = max(fireflies, key = lambda firefly : firefly.light_intensity)
        elif self.objective == "minimization":
            best_firefly = min(fireflies, key = lambda firefly : firefly.light_intensity)

        return best_firefly

    def __remove_matching_element_from_fireflies_copy(self, fireflies_copy, firefly):
        #4 remove the firefly that we are comparing from the set of all fireflies
        #remove the firely tha I am comparing from the list of all fireflies using light intensity
        matching_fireflies_copy_element = next((fireflies_copy_element for fireflies_copy_element in fireflies_copy if fireflies_copy_element.light_intensity == firefly.light_intensity), None)
        fireflies_copy.remove(matching_fireflies_copy_element)

    def __move_fireflies(self, randomization_parameter_alpha, absorption_coefficient_gamma):
        #5 move firfly accourding to the equation
        # fill in "new_location_coordinate" which is for updating the fireflies move (move formula)
       # alpha_damp = 0.98
        delta=[]
        e = []
        attractiveness_beta_at_distance_0 = 1

        for variable_index in range(self.number_of_variables):
            delta.append(0.05 * (self.objective_function.maximum_decision_variable_values()[variable_index] - self.objective_function.minimum_decision_variable_values()[variable_index]))
            e.append(delta[variable_index] * random.random())


        fireflies_copy = [firefly.copy_objective_function() for firefly in self.__fireflies]

        fireflies = self.__fireflies

        for firefly_i in self.__fireflies:

            self.__remove_matching_element_from_fireflies_copy(fireflies_copy, firefly_i)

            for firefly_j in fireflies_copy:

                if firefly_i.light_intensity < firefly_j.light_intensity:

                    distance_of_two_fireflies = self.__distance_of_two_fireflies(firefly_i, firefly_j)

                    attractiveness_beta = attractiveness_beta_at_distance_0 * exp(-absorption_coefficient_gamma * distance_of_two_fireflies**2)

                    for variable_index in range(self.number_of_variables):
                        new_location_coordinate = firefly_i.fireflies_location[variable_index] * (1 - attractiveness_beta) \
                                                  + firefly_j.fireflies_location[variable_index] * attractiveness_beta \
                                                  + randomization_parameter_alpha * random.random() #e[variable_index]
                        new_location_coordinate = self.__constrain_within_range(new_location_coordinate, variable_index)

                        firefly_i.fireflies_location[variable_index] = new_location_coordinate





    def  __constrain_within_range(self, fireflies_location, variable_index):
        #6 make sure the values of the fireflies location fall within the pre- determined range of the objective function
        # return fireflies location within the specify range

        if fireflies_location < self.objective_function.minimum_decision_variable_values()[variable_index]:
            return self.objective_function.minimum_decision_variable_values()[variable_index]
        elif fireflies_location > self.objective_function.maximum_decision_variable_values()[variable_index]:
            return self.objective_function.maximum_decision_variable_values()[variable_index]
        else:
            return fireflies_location

    def __distance_of_two_fireflies(self, firefly_1, firefly_2):
        #7 compute the distence between any two fireflies
        #return the distence betweeen two fireflies (distance r)

        sum_of_squares_of_distance = 0
        dmax = 0

        for variable_index in range(self.number_of_variables):
            dmax_ = (self.objective_function.maximum_decision_variable_values[variable_index] - self.objective_function.minimum_decision_variable_values[variable_index])**2
            dmax += dmax_

        dmax = sqrt(dmax)

        for variable_index in range(self.number_of_variables):
            square_of_distance = (firefly_1.fireflies_location[variable_index] - firefly_2.fireflies_location[variable_index])**2
            sum_of_squares_of_distance += square_of_distance

        return sqrt(sum_of_squares_of_distance)

if __name__ == '__main__':
    nonsmooth_multipeak_function_wrapper = NonsmoothMultipeakFunctionWrapper()
    michaelwicz_function_wrapper = MichaelwiczFunctionWrapper()

    # damnation of the function
    number_of_variables = 2
    objective = "minimization"

    firefly_algorithm = FA( michaelwicz_function_wrapper, number_of_variables, objective)

    number_of_fireflies = 6
    maximun_generation = 10
    randomization_parameter_alpha = 0.8
    absorption_coefficient_gamma = 1.0

    result = firefly_algorithm.search(number_of_fireflies=number_of_fireflies, max_generation= maximun_generation,
                                      randomization_parameter_alpha=randomization_parameter_alpha,
                                      absorption_coefficient_gamma=absorption_coefficient_gamma)
    print("the result", result)
    print("the result[0]", result["best_decision_variable_values"][0])
    print("the result[1]", result["best_decision_variable_values"][1])

    # TODO: Improve accuracy:
    #FA.assertAlmostEqual(result["best_decision_variable_values"][0], 2.8327, delta=5)
    #FA.assertAlmostEqual(result["best_decision_variable_values"][1], -0.0038, delta=5)
    #FA.assertAlmostEqual(result["best_objective_function_value"], 3.4310, delta=5)
