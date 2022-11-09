
list1 = [1,2,3,4,5]
list2 = ["apple","banana","lemon"]
list3 = [1,2,3,4,5,6,7,8,9,10]
list4 = [1,2,["apple","banana"]] # [0] = 1, [1]=2, [2] = apple,banana
#[2][0] = apple, [2][1] = banana

print(list1) # 배열 전체출력
print(list2[1]) # 배열의 1번자리 출력
print(list3[-1]) # 0번째 배열의 뒷자리가 없으므로 맨 뒤 배열 위치 출력
print(list4[2][0])

# ************************************************************************

list5 = [4,5,6]
print(list1+list5) # 배열 더하기 가능 ( 이어붙이기 )
print(list1*3) # 배열 곱하기 가능 

list2[1] = "melon" #1번째 배열을 melon문자열로 대체
list2.append("melon") # 배열의 맨뒤에 melon문자열 추가

# ***********************************************************************

list6 = [10,23,45,92,8,3,2,1]
list6.sort() # 정렬 ( 작은수부터 큰수로 정렬)
print(list6) 
print(list6.index(45)) # 정렬 후, 정수 45의 인덱스번호 출력
print(list6.count(92)) # 정수 92가 몇개 있는가