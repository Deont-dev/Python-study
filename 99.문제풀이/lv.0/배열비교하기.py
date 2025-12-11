"""
문제: 배열비교하기	
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181856

[문제 요약]
여기에 문제 요약 작성

[나의 풀이]
- def solution(arr1, arr2):
    len1=len(arr1)
    len2=len(arr2)
    # 길이 크기비교
    if len1 > len2:
        return 1
    elif len1 < len2:
        return -1
    
    s1 = sum(arr1)
    s2 = sum(arr2)
    if len1 == len2:
        if s1 > s2:
            return 1
        elif s1 < s2:
            return -1
        else: return 0
        
        

[다른 풀이 / 대안 접근]
이 문제에서 반드시 가져가야 하는 패턴
⭐ 패턴 1: “우선순위 기반 비교 구조”
문제에서 두 값을 비교할 때는 먼저 1번 조건,
같으면 2번 조건, 그것도 같으면 3번 조건으로 가는 계층적 조건 구조를 써야 한다.
이건 매우 매우 자주 등장하는 패턴:
if criterion1_A > criterion1_B:
    return 1
elif criterion1_A < criterion1_B:
    return -1
else:
    # criterion1 같을 때만 criterion2 비교
    if criterion2_A > criterion2_B:
        ...
⭐ 패턴 2: zip은 리스트를 돌 때만 의미가 있다
잘못된 예:
zip(a, b)  # a와 b가 길이(int)일 때
올바른 예:
for x, y in zip(arr1, arr2):
    ...
⭐ 패턴 3: 합 비교는 sum()으로 한 번에 해결한다
절대 이런 식으로 하지 않음:
for i in range(len(arr1)):
    ar += arr1[i]
파이썬에서는 무조건:
sum(arr1)
이게 정석이자 최적화된 방식.
⭐ 패턴 4: 비교는 “누적 중”이 아니라 “누적 후 한 번만” 한다
누적 중 비교 → ❌
최종 합 비교 → ✔
🔥 네가 지금 꼭 알아야 할 핵심
문제를 복잡하게 풀려고 하는 경향이 있어.
이 문제는 정렬도 필요 없고 반복문도 거의 필요 없다.
정답의 구조는 딱 이것:
길이 비교
(길이 같으면) 합 비교
동일하면 0
끝.

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    print(solution(샘플입력))