# 에러 a = "Life" is good!!" # 큰따옴표를 큰 따옴표로 감싸면 에러가 안난다.
a = 'Life" is good!!' # 큰따옴표를 작은 따옴표로 감싸면 에러가 안난다.
# 에러 a = 'Life' is good!!' # 작은따옴표를 작은 따옴표로 감싸면 에러가 뜬다.
b = "Life' is not good!!" # 작은따옴표를 큰 따옴표로 감싸면 에러가 안난다.
c = "I\' m hungry!!" # 굳이 따옴표를 따옴표로 감싸고 싶으면 백슬래쉬를 넣어준다
d = "Life is too short \nYou need python" # 개행
e = "Life is too short \tYou need python" # 탭
f = "Life is too short \\You need python" # 백슬래쉬를 그냥 쓰고 싶을때

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)