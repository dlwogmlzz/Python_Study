# 리스트에 대해서
odd = [1, 3, 5, 7, 9]
print(type(odd))

# 배열안에 숫자와 문자를 다 담을 수 있고, 리스트안에 다른 리스트를 담을 수 있다.
a = [1, 2, ['lee', 'jaehee'], 3, 4, 5, '6', '7', 'Fuck You']
print(a[2]) # 3번째 리스트를 출력
print(a[6] + a[7]) # 67
print(a[0] + a[5]) # 1 + 5 = 6
print(a[2][1]) # 3번째 리스트에 2번째 'jaehee'출력
print(a[-7][0]) # 반대쪽 6번째 리스트의 첫번째 자리 'lee'출력
print(a[8][5])

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3 + b * 3)

# 숫자와 문자 더하기, 형변환을 해야됌
print(str(7) + 'hi')

# 리스트 위치 바꾸기
c = [7, 8, 9]
c[2] = 10
print(c)

# 리스트 삭제
del c[2:]
print(c)

# 리스트 요소 추가 - append
c.append(9)
print(c)

# 오름차순 리스트 정렬 - sort
d = [10, 2, 3, 5, 9, 7, 1]
e = ['z', 'a', 'h', 'j', 't', 'b', 'c']
d.sort()
e.sort()
print(d)
print(e)

# 내림차순 리스트 정렬 - reverse
d.reverse()
print(d)

# 인덱스 반환
f = [1, 2, 3]
print(f.index(4))

