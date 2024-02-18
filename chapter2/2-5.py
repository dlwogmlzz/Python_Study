a = "baseball"
print(a.count('b')) # b의 갯수
print(a.find('e')) # e위치 찾기
print(a.find('x')) # x위치 찾기1(find) -> -1이 출력됨(없는문자)
# print(a.index('x')) # x위치 찾기2(index) -> 에러가 출력됨(없는문자)
print("=" * 50)
# 문자열 삽입
b = ", ".join('player') # p, l, a, y, e, r 출력
c = " to the ".join('동그라') + ('미') # 동 to the 그 to the 라미 출력
print(b)
print(c)

# 소문자 대문자 바꾸기
d = 'upper'
print(d.upper())
e = 'LOWER'
print(e.lower())

# 공백지우기
f = " fox " # 왼쪽
g = " google " # 오른쪽
h = " hot " # 양쪽

print(f.lstrip())
print(g.rstrip())
print(h.strip())

# 문자열 바꾸기 - replace
i = "My name is Lee won woo"
print(i.replace("won woo", "jae hee"))

# 문자열 나누기 - split
print(i.split()) # 띄워쓰기를 기준으로 나눈다, 안띄워져 있으면 그대로 출력됨
j = "a:b:c:d:e:f:g:h:i:j:k:l:m:n:o:p:q:r:s:t:u:v:w:x:y:z"
print(j.split(":")) # 콜론을 기준으로 띄워준다.

