"""
문제: 배열만들기3
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181895

[문제 요약]
여기에 문제 요약 작성

[나의 풀이]
def solution(arr, intervals):
    answer = []
    # intervals 의 리스트 요소 빼기
    for start,end in intervals:
        #뺀 요소로 슬라이싱 하기
        answer += arr[start:end+1]
    return answer

리스트안의 리스트를 빼서 각 요소별 갯수대로 문자 배분할수있음

[다른 풀이 / 대안 접근]
✅ 너의 코드
def solution(arr, intervals):
    answer = []
    for start, end in intervals:
        answer += arr[start:end+1]
    return answer
🎯 왜 완벽한가?
✔ 1. for start, end in intervals
intervals의 각 요소가 [start, end] 구조이기 때문에
언패킹이 정확히 맞아떨어짐 → 가장 깔끔한 코드 구조.
✔ 2. 슬라이싱 구간: arr[start:end+1]
b 구간을 포함하려면 end+1까지 해야 한다.
문제 요구와 100% 일치.
✔ 3. 리스트 확장: +=
여기서 append를 쓰면 리스트가 중첩되므로
+= 사용이 맞는 패턴.
✔ 4. 전체 concat 흐름이 문제 요구와 동일
intervals 순서대로 구간을 차례대로 붙이기 → 정확.
🔥 더 파이써닉한 참고 버전 (너무 잘했지만 참고로)
(1) 리스트 컴프리헨션 + sum
def solution(arr, intervals):
    return sum((arr[s:e+1] for s, e in intervals), [])
(2) extend 사용
def solution(arr, intervals):
    answer = []
    for s, e in intervals:
        answer.extend(arr[s:e+1])
    return answer
🧠 이번 문제의 핵심 패턴 (꼭 기억)
✔ 리스트 구간 추출 → arr[start:end+1]
✔ intervals는 "쌍"이므로 unpacking → for start, end in intervals
✔ 여러 리스트 이어 붙이기 → answer += ... 또는 answer.extend(...)
이 3개 패턴은 앞으로 프로그래머스 배열 문제에서 반복적으로 쓰인다.
원하면 이 패턴을 확실히 굳히는 유사문제 2~3개 더 내줄게!
나의 말:
궁금한건 리스트안에 리스트를 빼고 그걸 문자 두개로 치환하는게 파이썬만의 장점을 이용한건가?
ChatGPT의 말:
좋은 질문이다.
지금 네가 말하는 건 **“리스트 안의 리스트를 꺼내서(start, end로 언패킹), 그걸 바로 슬라이싱에 넣어서 arr[start:end+1] 형태로 쓰는 패턴”**을 의미하지?
이건 정말로 파이썬이 가진 장점(특히 언패킹 + 슬라이싱 + 동적 타입 지원) 중 하나야.
다른 언어에서는 이렇게 깔끔하게 안 된다.

🔥 왜 이것이 “파이썬만의 강력한 장점”인가?
1️⃣ 리스트 언패킹(unpacking)을 자연스럽게 지원
intervals 요소가 [start, end] 형태일 때:
for start, end in intervals:
이렇게 “변수 두 개”에 리스트 안의 값을 분해해서 받을 수 있어.
Java / C / C++ / JS에서는 이런 식으로 자동 언패킹이 되지 않는다.

예를 들어 JS에서는 이렇게 해야 한다:

for (let interval of intervals) {
    let start = interval[0];
    let end = interval[1];
}
파이썬은 그냥:
for start, end in intervals:
→ 훨씬 간결하고 오류가 줄어듦.
2️⃣ 슬라이싱이 직관적 & 강력
파이썬은:
arr[start:end+1]
이렇게만 하면 구간을 그대로 잘라낸 새 배열이 만들어진다.
JS에서는:

arr.slice(start, end+1)
C/C++에서는 직접 복사하는 루프를 짜야 한다.
파이썬의 슬라이싱은 문법 레벨에서 지원되는 매우 강력한 기능이고,
리스트 확장(+= / .extend())과 함께 쓰면 더 날카로운 무기가 된다.

3️⃣ 리스트 확장 += / extend 도 파이썬이 제공하는 고급 기능
answer += arr[start:end+1]
이 한 줄은
“배열 뒤에 다른 배열의 요소를 펼쳐서 붙여라” 라는 의미인데
타 언어에서는:
push 반복문 필요
또는 배열 concat 필요 (메모리 복사 더 많음)
파이썬은 built-in 레벨에서 이걸 처리해줘서 훨씬 간결하다.
⚡ 결론
✔ 리스트 언패킹
✔ 직관적인 슬라이싱
✔ += 를 통한 리스트 확장
이 3개가 파이썬이 데이터 처리에서 특히 강력한 이유야.

"""

def solution(입력변수):
    pass


if __name__ == "__main__":
    # 예시 테스트
    print(solution(샘플입력))