from GitProject.FireFly.FireflyAlgorithem.objective_function.abstract_wrapper import AbstractWrapper
from math import sin, pi

class MichaelwiczFunctionWrapper(object):

    def maximum_decision_variable_values(self):
        # becouse I have to variables [-,-], if I have 3 than ub=[-,-,-]
        return [4, 4]

    def minimum_decision_variable_values(self):
        return [0, 0]

    def objective_function_value(self, decision_variable_values):
        return -(sin(decision_variable_values[0]) * (sin(decision_variable_values[0]**2 / pi))**20 + sin(decision_variable_values[1]) * (sin(decision_variable_values[1]**2 / pi))**20)

    def initial_decision_variable_value_estimates(self):
        pass