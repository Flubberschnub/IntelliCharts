import mathproblem

class TimesTable(mathproblem.MathProblem):
    def __init__(self, num1, num2):
        self.problem = f"{num1} x {num2} = "
        self.solution = num1 * num2

    def get_problem(self):
        return self.problem

    def get_solution(self):
        return self.solution
    
    def check_answer(self, answer):
        return answer == self.solution