# 예외처리


f = open('calculator.txt','w')
try:
    a = 4/0
    f.write(a)  
except ZeroDivisionError as e :
    print(e, "가 발생하였습니다.")
except IndexError as e :
    pass
finally:
    f.close()