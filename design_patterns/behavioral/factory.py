from abc import ABC,abstractmethod

class Employee(ABC):

    @abstractmethod
    def salary(self)->int:
        pass

class CEO(Employee):

    def salary(self) -> int:
        return 98000

class Manager(Employee):

    def salary(self) -> int:
        return 65000

class Developer(Employee):

    def salary(self) -> int:
        return 40000

class EmployeeFactory:

    
    """
    it has all the power to create employee objects depends on criteria.
    """

    @staticmethod
    def getSalary(types):
        if types.upper()=="CEO":
            return CEO()
        elif types.upper()=="MANAGER":
            return Manager()
        elif types.upper()=="DEVELOPER":
            return Developer()
        else:
            return None

em=EmployeeFactory.getSalary("developer")
print(em.salary())