"""
문제: 홀짝구분하기
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181944

[문제 요약]
자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

[나의 풀이]
a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

[다른 풀이 / 대안 접근]
n=int(input())
print(f"{n} is {'eovdedn'[n&1::2]}")
신박한 방법 : n&1 이 1이면 홀수 0이면 짝수니까 짝수일경우 인덱스가[0::2] 이렇게 될거고 이 인덱스는 0부터 2칸씩 띄어서 끝까지 다읽기

print(f"{N} is {'even' if N % 2 == 0 else 'odd'}")
이건 if조건문 한줄로 바꾼 표현식 이용하는거 [수행할문장 if 조건 else 수행할문장]

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    pass