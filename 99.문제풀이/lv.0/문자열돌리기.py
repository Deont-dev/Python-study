"""
문제: 문자열 돌리기
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181945

[문제 요약]
문자열 str이 주어집니다.
문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.

[나의 풀이]
str = input()
for i in str:
    print(i)
for문으로 하나씩 출력진행하면 될거같아서

[다른 풀이 / 대안 접근]
"\n".join(input()) 
인풋 사이에 이스케이프 끼워넣기

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

str = input()
for i in str:
    print(i)


if __name__ == "__main__":
    # 예시 테스트
    str = input()
    for i in str:
        print(i)