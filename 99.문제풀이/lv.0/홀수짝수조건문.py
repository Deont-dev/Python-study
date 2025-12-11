"""
문제: 홀짝따라서 값구하기	
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181935

[문제 요약]
양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

[나의 풀이]
첫번째 트라이 
def solution(n):
    result = []
    for i in range(1,n,2):
        if n % 2 != 0:
            result += n[i]
    for j in range(n):
        if n % 2 == 0:
            result += n[j]**2
    return result                                # 정수를 리스트로 인덱싱하려고 해서 오류 리스트 인덱싱은 정수에서 사용할 수 없음

def solution(n):
    result = 0
    if n % 2 != 0:
        for i in range(1,n+1,2):
            result += i
    else:
        for i in range(0,n+1,2):
            result += i**2
    return result

[다른 풀이 / 대안 접근]
def solution(n):
    if n % 2 != 0:  # 홀수
        return sum(i for i in range(1, n+1, 2))
    else:           # 짝수
        return sum(i*i for i in range(2, n+1, 2))

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""