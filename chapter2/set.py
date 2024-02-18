# 집합

s1 = set('hello')
print(s1) # 중복 제거 , 순서가 정해져 있지않고, 실행시킬때마다 순서가 달라진다.
# print(s1[0]) # 에러발생

# 그래서 list로 바꿔주고 출력한다.
s2 = set([1, 2, 3])
s2 = list(s2)
print(s2[0])

# tuple로도 변환가능 
s2 = tuple(s2)
print(s2)

s3 = {1, 2, 3, 4, 5, 6, 7}
s4 = {4, 5, 6, 7, 8, 3, 9}
# 교 집합
print(s3 & s4)
print(s3.intersection(s4))

# 합집합
print(s3 | s4)
print(s3.union(s4))

# 차집합
print(s3 - s4) # s3을 기준으로 같은거 빼고 나머지
print(s4.difference(s3))


# 값 1개 추가 - add
s5 = set([10, 20, 30, 40, 50])
s5.add(60)
print(s5)

# 값 여러값 추가 - update
s6 = set([1, 2, 3, 4, 5])
s6.update([6, 7, 8, 9, 10])
print(s6)

# 특정값 제거 - remove
s6.remove(5)
print(s6)

# 언제 많이 사용하는가?
s7 = [1, 1, 2, 2, 3, 3, 4, 5, 4, 6]
# set으로 중복제거, list로 쓰고 싶을때
s7 = list(set(s7))
print(s7)