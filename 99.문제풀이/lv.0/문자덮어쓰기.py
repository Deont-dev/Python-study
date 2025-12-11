"""
문제: 문자덮어쓰기
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181943

[문제 요약]
문자열 my_string, overwrite_string과 정수 s가 주어집니다. 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을 문자열 overwrite_string으로 
바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

[나의 풀이]
def solution(my_string, overwrite_string, s):
    answer = my_string.replace(my_string[s:],overwrite_string)
    if len(my_string) != len(my_string.replace(my_string[s:],overwrite_string)):
        answer = answer + my_string[-1:]
    return answer

replace로 오버라이트 스트링을 s부터 덮어버리려고했는데 오버라이팅 길이가 전체길이랑 다르면 손실되는 데이터 발생되서
문제해결 실패로 뜸

그러면 그냥 인덱싱을 활용해보자는 생각
def solution(my_string, overwrite_string, s):
    answer = my_string[:s]+overwrite_string+my_string[len(my_string[:s]+overwrite_string):]
    return answer

[다른 풀이 / 대안 접근]
- 다른 풀이 아이디어 또는 더 효율적인 방식

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""


if __name__ == "__main__":
    # 예시 테스트
    print(solution(샘플입력))