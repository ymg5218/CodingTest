def solution(genres, plays):
    # 장르 별 누적 재생 수를 카운트하기 위한 딕셔너리
    genresPlayDict = {}

    # 같은 장르끼리 묶기 위한 딕셔너리
    genresDict = {}

    for idx in range(len(genres)):
        if genres[idx] in genresDict:
            genresDict[genres[idx]].append([idx, plays[idx]])
            genresPlayDict[genres[idx]] += plays[idx]

        else:
            genresDict[genres[idx]] = [[idx, plays[idx]]]
            genresPlayDict[genres[idx]] = plays[idx]

    # 누적 재생 수를 기준으로 모든 장르를 정렬한 결과를 담기 위한 배열
    genresSortByTotalPlays = []

    for key, value in genresPlayDict.items():
        genresSortByTotalPlays.append([key, value])

    # 누적 재생 수 기반 정렬
    genresSortByTotalPlays.sort(reverse=True, key=lambda x: x[1])

    # 같은 장르끼리 클러스터링한 노래들 중에서 정렬한 결과를 담기 위한 배열
    genresSortByPlays = []

    for key, value in genresDict.items():
        genresSortByPlays.append([key, value])

    # genreCnt = 장르 종류 가짓수
    genresCnt = len(genresSortByPlays)

    # 각 장르 내에서 재생 수 기준 오름차순, 같다면 인덱스 번호 기준 내림차순
    # 이렇게 정렬하면 genresSortByPlays에서 pop() 하여 우선순위가 높은 노래 순으로 추출 가능
    for i in range(genresCnt):
        temp = genresSortByPlays[i][1]
        # 각 장르별로 재생 수 기반 오름차순, 재생 수가 같다면 인덱스 번호 기준 내림차순
        temp.sort(key=lambda x: (x[1], -x[0]))
        genresSortByPlays[i][1] = temp

    # 베스트앨범 노래들을 담을 배열
    answer = []

    # genresCnt = 장르 종류 가짓수
    for i in range(genresCnt):
        # 누적 재생 수가 많은 장르의 노래가 최우선순위
        nowGenre = genresSortByTotalPlays[i][0]
        # 같은 장르끼리 클러스터링한 배열에서 현재 수록하고 싶은 장르를 탐색
        for j in range(genresCnt):
            if genresSortByPlays[j][0] == nowGenre:
                cnt = 0
                # 베스트앨범에는 같은 장르를 최대 2개 수록 가능함 and 2개 이하라면 1개만 수록하도록 함
                while cnt < 2 and genresSortByPlays[j][1]:
                    # 각 장르에서 베스트앨범에 우선순위로 수록될 노래를 추출하여 answer에 추가함
                    answer.append(genresSortByPlays[j][1].pop()[0])
                    cnt += 1
                break

    return answer

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [100, 500, 100, 100, 500]

    print(solution(genres, plays))