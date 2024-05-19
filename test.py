from collections import OrderedDict

d = {'apple': 3, 'banana': 2, 'cherry': 1}

o = OrderedDict(reversed(True))

# 키를 기준으로 정렬된 OrderedDict 객체 생성
sorted_d = OrderedDict(sorted(d.items(), key=lambda x: x[0]))
print(sorted_d)

# 값(value)를 기준으로 정렬된 OrderedDict 객체 생성
sorted_d = OrderedDict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_d)

print(type(sorted_d))