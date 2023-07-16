import math
class Module:
    def __init__(self, name, *args) -> None:
        self.name = name
        if len(args) == 1:
            self.rel = args[0]
        elif len(args) == 2:
            self.f_rate = args[0]
            self.op_time = args[1] 
            self.rel = math.exp(-self.f_rate*self.op_time)
        else:
            raise("Just Error")
        self.failure = 1 - self.rel
        
    def __mul__(self, other):
        new_rel = self.rel * other.rel
        return Module("New_System", new_rel)
    def __or__(self, other):
        new_rel = 1 - (other.failure * self.failure)
        return Module('New_System',new_rel)
    def __repr__(self) -> str:
        return (self.name + " has a reliability of " +  str(self.rel))