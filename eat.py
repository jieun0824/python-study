import random
import time

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
    
print(lunch)

set_lunch = set(lunch)

#메뉴 삭제 기능

while True:
    print(set_lunch)
    item = input("음식을 삭제해주세요 : ")

    if(item == "q"):
        break
    else:
        set_lunch = set_lunch - set([item]) 
        #차집합은 집합끼리만 할 수 있는 연산이기 때문에 item을 집합 형태로 바꿔야한다. 
  
print(set_lunch, "중에서 선택합니다.")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print(random.choice(list(set_lunch)))
