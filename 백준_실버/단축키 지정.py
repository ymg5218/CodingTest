# 1283
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())

    dict = {' ' : True}

    for _ in range(N):
        command = input().strip()

        # 띄워쓰기 구분
        command_words = list(command.split())

        # 글자 하나하나 구분
        command_units = list(command)

        is_finish = False

        # 커맨더로 지정할 위치의 인덱스
        result_idx = 0

        # 1. 각 단어의 맨 첫 번째 글자부터 확인
        for idx in range(len(command_words)):
            if is_finish:
                break
            if command_words[idx][0].upper() not in dict:
                dict[command_words[idx][0].upper()] = True
                command_units[result_idx] = "[" + command_units[result_idx] + "]"
                is_finish = True
                break

            result_idx += len(command_words[idx]) + 1
        # 2-1. 각 단어의 맨 첫 번째 글자들이 이미 단축키로 지정되어 있음
        if not is_finish:
            result_idx = -1
            for idx in range(len(command_units)):
                if command_units[idx].upper() not in dict:
                    dict[command_units[idx].upper()] = True
                    command_units[idx] = "[" + command_units[idx] + "]"
                    print(''.join(command_units))
                    is_finish = True
                    break

            if not is_finish:
                if result_idx != -1:
                    command_units[result_idx] = "[" + command_units[result_idx] + "]"
                    dict[command_units[result_idx].upper()] = True

                print(''.join(command_units))
        
        # 2-2. 1단계에서 단축키 설정이 끝났으면 바로 출력
        else:
            print(''.join(command_units))
