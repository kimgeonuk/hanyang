# 클래스

# result = 0
# result2 = 0

# def add(num):
#     global result
#     result = result + num
#     return result

# def add2(num):
#     global result2
#     result2 = result2 + num
#     return result2


# print(add(3))
# print(add(4))

# print(add2(5))
# print(add2(10))



# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

# a = Calculator()
# b = Calculator()
# print(a.add(3))
# print(a.add(4))
# print(b.add(5))
# print(b.add(10))






#사칙연산 클래스


class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def setdata(self,first,second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

# a = FourCal(4,2)
# print(a.add())

# a.setdata(5,10)
# print(a.add())


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if self.first == 0 or self.second ==0:
            return 0
        else:
            return self.first / self.second

a = MoreFourCal(4,0)
print(a.div())

