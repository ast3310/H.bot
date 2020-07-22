from abc import ABC, abstractmethod

class AND(): 
    def get_result(self, permission_first, permission_second):
        return permission_first.check() and permission_second.check()


class OR(): 
    def get_result(self, permission_first, permission_second):
        return permission_first.check() or permission_second.check()


class NOT():
    def get_result(self, permission):
        return not permission.check()


class OperatorContext(ABC):
    @abstractmethod
    def execute():
        pass


class DualOperatorContext(OperatorContext):
    def __init__(self, operator, permission_first, permission_second):
        self.operator = operator()
        self.permission_first = permission_first
        self.permission_second =permission_second

    def execute():
        return operator.get_result(self.permission_first, self.permission_second)


class SingleOperatorContext(OperatorContext):
    def __init__(self, operator, permission):
        self.operator = operator()
        self.permission = permission

    def execute():
        return operator.get_result(self.permission)


class BasePеrmission():
    def check(message):
        pass
    
    def __and__(self, permission):
        context = DualOperatorContext(AND, permission, self)
        return context.execute()
    
    def __rand__(self, permission):
        context = DualOperatorContext(AND, self, permission)
        return context.execute()