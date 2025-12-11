"""
문제: 숫자조작1
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181926

[문제 요약]
여기에 문제 요약 작성

[나의 풀이]
def solution(n, control):
    c = list(control)
    for i in c:
        if i == "w":
            n += 1
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
        else:
            n -= 10
    return n 

[다른 풀이 / 대안 접근]
🔹 패턴 1: 문자열은 리스트로 만들 필요 없음
문자열 자체가 for-loop 가능.
문자열은 본질적으로 iterable이기 때문에
c = list(control)
for i in c:
→ 이것과
for i in control:
은 완전히 동일하게 동작함.
불필요한 연산이므로 안 쓰는 것이 더 깔끔함
🔹 패턴 2: 상태 제어는 if-elif 대신 “매핑(dictionary)”
→ 이 패턴은 백엔드, ML 모델 라우팅, 이벤트 핸들러 등 거의 모든 곳에서 쓰임.
move = {"w": 1, "s": -1, "d": 10, "a": -10}

🔹 패턴 3: 누적 계산은 sum + 컴프리헨션 가능
문자열 → 변환 → 합산
→ Pandas, Numpy에서도 그대로 이어지는 사고방식.
🔹 패턴 4: else로 특정 케이스를 처리하지 말고, 가능한 명시적으로 처리
가독성 + 유지보수성 향상.

def solution(n, control):
    move = {"w": 1, "s": -1, "d": 10, "a": -10}
    return n + sum(move[i] for i in control)

[접근 방법(Detail)]
- 아이디어 상세 설명
- 시간복잡도: O(n)

"""

