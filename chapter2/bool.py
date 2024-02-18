# bool 자료형의 참과 거짓

'''

	값				참 or 거짓
"python"		"참"
""					"거짓"
[1,2,3]			"참"
[]					"거짓"
(1,2,3)			"참"
()					"거짓"
{'a': 1}		"참"
{}					"거짓"
1						"참"
0						"거짓"
None				"거짓"

'''

a = [1, 2, 3, 4, 5]
while a:
		print(a)
		a.pop()

if [1,2,3]:
		print("참")
else:
		print("거짓")

# 참 속성인지 거짓 속성인지 알아보기
b = bool([1, 2, 3])
c = bool([])
print(b)
print(c)


