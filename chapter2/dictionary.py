# 딕셔너리
dic = {'name': 'jaehee', 'phone': '010-0000-1111', 'birth': '1022'}
print(type(dic))
print(dic)

a = {1: 'a'}
# key와 value 추가
a[2] = 'b'

print(a)

# 딕셔너리 삭제 - key를 지운다.
b = {1: 'a', 2: 'b', 'name' : 'lee', 3: [1, 2, 3]}
del b['name'], b[1]
print(b)

grade = {'lee' : 100, 'kang' : '60'}
print(grade['lee']) 

# Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다
c = {1: 'a', 1: 'b'}
print(c) # b가 출력됨
# d = {[1, 2] : 'hi'} # TypeError: unhashable type: 'list'
# print(d)

# key만 출력
e = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(e.keys())
print(e.values())

# 리스트로 변형해서 출력
print(list(e.keys()))

for f in e.keys():
	print(f)

# key와 value 쌍으로 출력
print(e.items())

# key와 value 쌍 지우기
e.clear()
print(e)

g = {'name': 'kim', 'phone': '010-9999-8888', 'birth': '0929'}
# print(g['name'])
print(g.get('name'))

# yoyo가 없으면 값이 없어요라는 메시지 출력
print(g.get('yoyo', '값이 없어요'))
# birth라는 key값이 g에 있으면 True
print('birth' in g)

