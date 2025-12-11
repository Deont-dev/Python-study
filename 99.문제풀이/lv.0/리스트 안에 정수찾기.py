"""
문제: 리스트 안의 정수찾기
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181840

[문제 요약]
정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

[나의 풀이]
def solution(num_list, n):
    answer = 0
    for i in num_list:
        if n == i:
            answer = 1
    return answer

막혔던 부분은 if n in i: 로 조건을 실행했었는데 타입 관련해서 오류가 뜸
이유는 in 은 리스트 목록에서 있는지 없는지 판단하는 내용인데 for문을 써서 리스트에 있는 인수들을 i라는 정수로 뽑았기 때문에 오류가 발생한거임
정수끼리 비교를 해야하니 당연히 연산자 == 를 써야지 오류가 안남

[다른 풀이 / 대안 접근]
def solution(num_list, n):
    return int(n in num_list)

이게 내가 in을 쓸거면 써야했을 문법임

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    print(solution(샘플입력))