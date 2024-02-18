# 숫자 포맷팅
a = "I eat %d apples." % 100
print(a)

# 숫자 & 문자열 포맷팅 1
b = "I eat %s bananas" % "200"
print(b)

number = 5
day = "ten"

c = "I ate %d apples. so I was sick for %s days." % (number, day)
print(c)
d = "I have %d%% apples" % 30 # 몇퍼센트(%)를 표시하고 싶을때 %두개
print(d)
e = "%10s" % "hi" # 출력하면 전체 10칸안에 마지막 두칸 hi 출력
print(e)
f = "%-10sJaehee." % "hi" # 10칸에 맨앞에 hi 그뒤에 7칸이 추가돼서 Jaehee.가 들어감.
print(f)

# 소수점
g = "%0.4f" % 3.123456789 # 소수점 4째짜리까지 표시해라(반올림적용됌)
print(g)

# 숫자 & 문자열 포맷팅 2(.format)
h = "I eat {0} bananas".format(5)
i = "I eat {0} bananas".format("two")

number2 = 4
day2 = "five"
j = "I ate {1} bananas. so I was sick for {0} days.".format(number2, day2)
k = "I ate {number3} Oranges. so I was sick for {day3} days.".format(number3=7, day3="eight")
l = "I ate {0} Grapes. so I was sick for {day4} days.".format(20, day4="ten")
print(j)
print(k)
print(l)

m = "{0:<10}".format("hello") # 총 10칸을 만들어서 앞글자부터 hello가 들어간다. 왼쪽정렬
print(m)
n = "{0:>10}".format("hello") # 총 10칸을 만들어서 마지막에 hello가 들어간다. 오른쪽정렬
print(n)
o = "{0:^10}".format("hello") # 총 10칸을 만들어서 중간에 hello가 들어간다. 가운데정렬 캐럿문자(^)
print(o)
p = "{0:=^10}".format("next") # 총 10칸을 만들어서 중간에 hello채우고, 나머지 사이에 =를 넣는다.
print(p)

# 중괄호 표현
q = "{{ q }}".format()
print(q)

# 숫자 & 문자열 포맷팅 3(f)
name = "이재희"
age = 33
r = f'나의 이름은 {name} 입니다. 나이는 {age + 7}살입니다.'
print(r)
s = f'{"hi":=^10}'
print(s)

