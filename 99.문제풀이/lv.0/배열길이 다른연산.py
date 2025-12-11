"""
문제: 배열길이에 따른 다른 연산	
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181854

[문제 요약]
정수 배열 arr과 정수 n이 매개변수로 주어집니다. arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.

[나의 풀이]
def solution(arr, n):
    result = []
    a = len(arr)
    if a % 2 == 1:
        for i in range(a):
            if i % 2 == 0:
                result.append(arr[i]+n)
            else:result.append(arr[i])
    if a % 2 == 0:
        for i in range(a):
            if i % 2 == 1:
                result.append(arr[i]+n)
            else:result.append(arr[i])
    return result

[다른 풀이 / 대안 접근]
🎯 이 문제에서 반드시 가져가야 할 패턴 4가지
✅ 패턴 1: “조건에 따라 배열 전체를 순회하며 index 기반으로 값 변환”
문제의 핵심은:
배열 전체는 유지한다.
그러나 특정 인덱스만 변환한다.
즉,
result[i] = arr[i] + n   # 특정 조건일 때만
이 구조가 매우 중요하다.
일반화 패턴:
result = []
for i in range(len(arr)):
    if 조건(i):
        result.append(arr[i] + n)
    else:
        result.append(arr[i])
이건 데이터 전처리, ETL, Pandas에서 조건 변환할 때 가장 많이 쓰는 패턴이다.
✅ 패턴 2: “홀수/짝수 인덱스 조건 처리”
문제에서 길이에 따라 조건이 바뀌지만, 본질은:
if i % 2 == 0:  # 짝수 인덱스
if i % 2 == 1:  # 홀수 인덱스
이 패턴은 문자열 처리, 배열 필터링, 인덱스 기반 연산에서 자주 등장함.
실전 사례
feature engineering에서 짝수 column만 변환
UI grid에서 짝수 행만 색 바꾸기
데이터 전처리에서 even/odd row 검증
✅ 패턴 3: 슬라이싱(arr[::2], arr[1::2])은 “부분 추출”이지 “전체 변환”이 아니다
네가 처음에 시도한 방식은:
arr[1::2]
arr[::2]
이건 전체 배열을 변환하는 문제에 잘못 적용한 패턴이야.
이 문제를 통해 배워야 할 핵심 교정:
슬라이싱은 “그 구간의 요소만 잘라낸 새로운 리스트를 만드는 것”이다.
전체를 유지하며 변환하려면 반드시 index 기반 반복(for i in range)이어야 한다.
이 교정은 이후 많은 문제에서 틀리는 걸 막아준다.
✅ 패턴 4: append([]) ⇒ 중첩 리스트가 된다 (리턴 형태 주의)
처음 네 코드에서:
result.append([ ... ])
하면 결과는:
[[변환값들]]
즉, 이중 리스트가 된다.
이 문제에서는:
변환된 원소 하나씩 append해서 1차원 리스트 유지해야 한다.
올바른 패턴
result.append(arr[i] + n)
잘못된 패턴
result.append([arr[i] + n])
이 패턴은 모든 리스트 문제에서 매우 자주 실수하는 부분이라서
지금 정확히 짚고 가는 게 중요하다.
🧠 패턴 요약 테이블
패턴	설명	이 문제에서 어떻게 적용되는가
Index 기반 전체 변환 패턴	배열 길이만큼 순회하며 조건 적용	특정 인덱스 요소에만 n 더함
짝/홀 인덱스 조건	i % 2 == 0/1	길이에 따라 어느 인덱스에 더할지 결정
슬라이싱은 부분 추출	arr[::2]는 새 배열	전체 배열 변환 문제에 사용하면 안 됨
append([]) = 2D 리스트 경고	리스트 안에 리스트가 들어감	결과 형태가 틀리는 원인이 됨
✨ 가장 중요한 패턴 하나만 뽑으라면?
👉 “조건에 따라 index를 검사하며 원본 리스트를 변환하는 패턴”
이 패턴은 앞으로 문제를 100개 풀어도 계속 나오고,
나중에 Pandas에서도 이렇게 쓰게 된다:
df['col'] = df['col'].apply(lambda x: x+n if 조건 else x)
즉,
조건 + 인덱스 기반 변환 → 원소별 변환 패턴
이게 이 문제의 핵심 학습 포인트.

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    print(solution(샘플입력))