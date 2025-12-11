"""
문제: 대소문자 바꾸기
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181949

[문제 요약]
영어 알파벳으로 이루어진 문자열 str이 주어집니다. 각 알파벳을 대문자는 소문자로 소문자는 대문자로 변환해서 출력하는 코드를 작성해 보세요.

[나의 풀이]
- print(input().swapcase())
swapcase() 함수는 대문자는 소문자, 소문자는 대문자로 바꿔주는 파이썬 내장함수다.

[다른 풀이 / 대안 접근]
- print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))
join함수
if는 그냥 한줄일때 저렇게 표현가능
for문은 리스트 컴프리헨션 쓴건데 [표현식 for 항목 in 반복가능개체]
이 풀이방안은 빈곳에다가 조건문 사용해서 새로운 출력을 만드는 방안

str = input()
a = ''

for s in str :
    if(s.isupper()) :
        a = a + s.lower()
    else : 
        a = a + s.upper()

print(a)


[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

str = input()
print(str.swapcase())


if __name__ == "__main__":
    # 예시 테스트
    str = input()
    print(str.swapcase())