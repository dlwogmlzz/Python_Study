# 문자열 연산
a = "python"
# 문자열과 문자열은 에러 print(a * a)
print(a * 3) # 문자열과 숫자를 연산할수 있다.

# 등호로 행을 나눌때 ================================
print("=" * 50)
print("Python Program!")
print("=" * 50)

b = " Program!^^"
print(len(b)) # 문자열의 길이

#문자열의 인덱싱 : 무언가를 가리킨다.
print(b[8]) # 인덱스는 0부터 시작 !출력
# print(a[6]) 문자열을 벋어나서, 문자가 없으면 string index out of range 에러
print(b[-1]) # 맨뒤부터 시작 ^출력

#문자열의 슬라이싱 : 무언가를 잘라낸다, 범위를 가져온다.
c = "Coding@@"
d = c[0:8] # 콜론으로 0에서 끝까지 8미만 7까지의 수를 가져온다. c[이상:미만] / c[이상:미만:간격]
print(d)

e = "foodBallPlayer"
f = e[:8] # 처음부터 8번 미만까지
g = e[8:] # 8번부터 마지막까지
h = e[::2] # 처음부터 끝까지 2칸씩 있는 문자를 출력
i = e[::-1] # 거꾸로 스타트
j = e[::-2] # 거꾸로 스타트해서 2칸씩 있는 문자를 출력

print("f = " + f)
print("g = " + g)
print(h)
print(i)
print(j)

k = "20240218pythonstudy"
print(k[10:-5])

L = "토마토기러기스위스오디오스위스기러기토마토" # Palindrom : 역순으로 읽어도 같은말
print(L[::-1])
