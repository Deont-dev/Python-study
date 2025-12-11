"""
문제: 접미사 구하기 
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181908

[문제 요약]
어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.


[나의 풀이]
def solution(my_string, is_suffix):
    return 1 if my_string[-len(is_suffix):] == is_suffix else 0

def solution(my_string, is_suffix): 
    a = list(my_string) 
    for i in range(len(my_string)): 
        if is_suffix in a[1:i]: 
            return 1 
    return 0                  > 틀린함수

    for i in range(len(my_stirng)):
        if my_string[i:] == is_suffix:
            return 1
    return 0




[다른 풀이 / 대안 접근]
이 문제에서 반드시 배우고 가야 할 패턴
패턴 1) 문자열 접두사/접미사 검사
접미사: s.endswith(x)
접두사: s.startswith(x)
슬라이싱 접미사: s[-len(x):] == x
슬라이싱 접두사: s[:len(x)] == x
데이터 분석과 NLP에서도 매우 자주 쓰는 패턴.
패턴 2) 리스트로 쪼개면 문자열 의미가 사라진다
"banana" → ['b','a','n','a','n','a']
suffix/prefix 문제는 문자열 단위 비교가 핵심
→ 리스트 변환은 대부분 잘못된 접근.
패턴 3) 포함 여부 in vs 종료 여부 endswith
"abc" in "xxxabc" → 부분 포함
"xxxabc".endswith("abc") → 접미사 여부 (이 문제에서 필요한 것)
🌟 4. 네 코드 구조 자체를 어떻게 고치면 될까?
지금 형태를 최대한 유지하면서 올바른 방식으로 바꾸면:
def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if my_string[i:] == is_suffix:    # i부터 끝까지 → suffix 후보
            return 1
    return 0
즉, my_string[i:]가 가능한 모든 suffix이므로
그 중 하나라도 is_suffix와 같다면 정답.
하지만 위 방식은 endswith보다 비효율적이므로 실전에서는 endswith를 쓰는 게 정답.

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    print(solution(샘플입력))