from math import exp


class NonsmoothMultipeakFunctionWrapper(object):
    def maximum_decision_variable_values(self):
        return [5, 5]

    def minimum_decision_variable_values(self):
        return [-5, -5]

    def objective_function_value(self, decision_variable_values):
        return (abs(decision_variable_values[0]) + abs(decision_variable_values[1])) * exp(
            -0.0625 * (decision_variable_values[0] ** 2 + decision_variable_values[1] ** 2))
