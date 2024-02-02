from abc import ABC, abstractmethod
## Abstract class for math problems
class MathProblem(ABC):
    @abstractmethod
    def get_problem(self):
        pass

    @abstractmethod
    def get_solution(self):
        pass

    @abstractmethod
    def check_answer(self, answer):
        pass