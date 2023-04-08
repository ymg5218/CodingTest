# 14653


def find():
    global send_name, no_read, people
    if send_name[Q - 1] in people:
        people.remove(send_name[Q - 1])
    for index in range(K-1, -1, -1):
        if no_read[index] != no_read[Q - 1]:
            del no_read[index]
            del send_name[index]
    send_name = list(set(send_name))
    
    for val in send_name:
        if val in people:
            people.remove(val)
    if "A" in people:
        people.remove("A")
    print(people)
            

if __name__ == "__main__":
    N,K,Q = map(int, input().split()) # N,K 값 받아옴
    people = [] # 톡방 전체 인원
    no_read = [] # R 값 저장할 배열 선언
    send_name = [] # 메시지 송신자 저장
    for i in range(0,K):
        R,P = input().split()
        no_read.append(R)
        send_name.append(P)
    for j in range(0,N):
        people.append(chr(65+j))
    
    find()