"""
문제: 덧셈식 출력
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181947

[문제 요약]
두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

[나의 풀이]
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a+b}')

[다른 풀이 / 대안 접근]
a, b = map(int, input().strip().split(' '))
c = a + b
print('{} + {} = {}'.format(a, b, c))
f포매팅 기억안나면 그냥 포맷함수 사용했을텐데 변수하나 추가해서 사용한듯

[접근 방법(Detail)]
- 포매팅활용
- 시간복잡도: O(n)

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    pass