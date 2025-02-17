import math
import random
from qubots.base_problem import BaseProblem

class BraninFunctionProblem(BaseProblem):
    """
    Branin Function Optimization Problem

    The Branin function is defined as:
      f(x1, x2) = a * (x2 - b*x1^2 + c*x1 - r)^2 + s*(1-t)*cos(x1) + s

    Where:
      a = 1
      b = 5.1 / (4 * π^2)
      c = 5 / π
      r = 6
      s = 10
      t = 1 / (8 * π)

    Decision variables:
      x1 ∈ [-5.0, 10.0]
      x2 ∈ [0.0, 15.0]

    Objective:
      Minimize f(x1, x2).

    Candidate solution representation:
      A list of two floats [x1, x2].
    """
    
    def __init__(self):
        # Fixed parameters for the Branin function.
        self.a = 1
        self.PI = 3.14159265359
        self.b = 5.1 / (4 * self.PI ** 2)
        self.c = 5 / self.PI
        self.r = 6
        self.s = 10
        self.t = 1 / (8 * self.PI)
        # Domain bounds
        self.bounds = [(-5.0, 10.0), (0.0, 15.0)]
    
    def evaluate_solution(self, solution) -> float:
        """
        Given a candidate solution [x1, x2], compute the Branin function value.
        Returns a large value (infinity) if the solution is out of bounds.
        """
        if not isinstance(solution, (list, tuple)) or len(solution) != 2:
            raise ValueError("Solution must be a list or tuple of two floats: [x1, x2].")
        x1, x2 = solution
        # Check domain bounds.
        if not (self.bounds[0][0] <= x1 <= self.bounds[0][1]) or not (self.bounds[1][0] <= x2 <= self.bounds[1][1]):
            return float('inf')
        # Compute the Branin function value.
        f = self.a * (x2 - self.b * x1**2 + self.c * x1 - self.r) ** 2 \
            + self.s * (1 - self.t) * math.cos(x1) + self.s
        return f

    def random_solution(self):
        """
        Generate a random candidate solution within the defined domain.
        """
        x1 = random.uniform(self.bounds[0][0], self.bounds[0][1])
        x2 = random.uniform(self.bounds[1][0], self.bounds[1][1])
        return [x1, x2]
