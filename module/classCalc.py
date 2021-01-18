class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, a: int, b: int) -> int:
        '''This method allows to add integer a and integer b'''
        self.result = 0
        self.result += a + b
        return self.result
    
    def subtract(self, a: int, b: int) -> int:
        """This method allows to subtract integer b from integer a"""
        self.result = 0
        self.result += a - b
        return self.result
    
    def multiply(self, a: int, b: int) -> int:
        """This method allows to multiply integer a and integer b"""
        self.result = 0
        self.result += a * b
        return self.result
    
    def divide(self, a: int, b: int) -> float:
        """This method allows to divide integer a from integer b"""
        self.result = 0
        self.result += a / b
        return self.result
    
    def n_root(self, a: int, n: int) -> float:
        """This method allows to get n root of integer a"""
        self.result = 0
        self.result += a ** (1/n)
        return self.result
    
    def previous_result(self):
        """This method returns previous result of any kind of mathematical manipulation"""
        return self.result
    
    def result_reset(self):
        """This method deletes result memory and puts it back to 0"""
        self.result = 0