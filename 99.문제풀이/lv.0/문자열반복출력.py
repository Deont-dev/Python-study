"""
문제: 문자열 반복해서 출력하기
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181950

[문제 요약]
문자열 str과 정수 n이 주어집니다.
str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

[나의 풀이]
str, n = input().strip().split(' ')
n = int(n)
print(str*n)

[다른 풀이 / 대안 접근]
s, t = input().split()
print(s*int(t))

이건 주어진 내용을 수정해서 표현한건데 n = int(n) 줄을 없애고 그냥 프린트문 안에 조건을 넣는게 인상깊었음

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    pass