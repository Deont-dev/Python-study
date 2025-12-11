"""
문제: 꼬리문자열
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181841

[문제 요약]
문자열들이 담긴 리스트가 주어졌을 때, 모든 문자열들을 순서대로 합친 문자열을 꼬리 문자열이라고 합니다. 꼬리 문자열을 만들 때 특정 문자열을 포함한 문자열은 제외시키려고 합니다. 예를 들어 문자열 리스트 ["abc", "def", "ghi"]가 있고 문자열 "ef"를 포함한 문자열은 제외하고 꼬리 문자열을 만들면 "abcghi"가 됩니다.

문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때, str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성해주세요.

[나의 풀이]
def solution(str_list, ex):
    answer = ''
    c = str_list
    for i in c:
        if ex not in i:
            answer += i
    return answer

포함 문제는 in / not in 으로 조건을 항상 생각해보기 

[다른 풀이 / 대안 접근]
def solution(str_list, ex):
    return ''.join(s for s in str_list if ex not in s)

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    print(solution(샘플입력))