import unittest
import FA
from objective_function.nonsmooth_multipeak_function import NonsmoothMultipeakFunctionWrapper

class testFA(unittest.TestCase):
    print("hhh")
    def test_find_glocal_maximum_for_nonsmooth_multipeak_function(self):
        nonsmooth_multipeak_function_wrapper = NonsmoothMultipeakFunctionWrapper()

        number_of_variables = 2
        objective = "maximization"

        firefly_algorithm = FA(nonsmooth_multipeak_function_wrapper, number_of_variables, objective)

        number_of_fireflies = 10
        maximun_generation = 10
        randomization_parameter_alpha = 0.2
        absorption_coefficient_gamma = 1.0


        result = firefly_algorithm.search(number_of_fireflies=number_of_fireflies,
                                          maximun_generation=maximun_generation,
                                          randomization_parameter_alpha=randomization_parameter_alpha,
                                          absorption_coefficient_gamma=absorption_coefficient_gamma)
        print("the result[0]", result)
        print("the result[0]", result["best_decision_variable_values"][0])
        print("the result[1]", result["best_decision_variable_values"][1])


    if __name__ == '__main__':
        unittest.main()


