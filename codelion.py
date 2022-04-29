# import random

# lunch = random.choice(["된장찌개", "피자", "제육볶음"])
# dinner = random.choice(["김밥","쫄면","돈까스"])

# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# print(information)
# print(information.get("취미"))

# information = {"특기":"피아노", "사는곳":"서울"}
# print(information.get("특기"))
# print(information.get("사는곳"))

# information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
# foods = ["된장찌개", "피자", "제육볶음"]
# print(information.get("취미"))

# information["특기"] = "피아노"
# information["사는곳"] = "서울"
# del information["좋아하는 음식"] #이 key와 value 삭제된다 

# print(information)

# print(len(information))

# information.clear()

# print(information)



# for x in range(30):
#     print(x)

# foods = ["된장찌개", "피자", "제육볶음"]
# for x in range(3):
#     print(foods[x])
# for x in foods:
#     print(x)

# information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
# for x, y in information.items():
#     print(x) #x에는 key값이
#     print(y) #y에는 value 값이 들어간다. 


#집합 - set -> 순서가 없고, 중복 없다 
#미리 만든 list set으로 감싸서 만든다. 
#집합끼리 합집합 -> | / 교집합 -> & / 차집합 -> -
