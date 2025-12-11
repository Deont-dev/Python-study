"""
문제: a와b출력하기
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181951

[문제 요약]
정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.
[내 풀이]
a, b = map(int, input().strip().split(' '))
print("a =", a)
print("b =", b)
[다른 풀이]
a, b = map(int, input().strip().split(' '))
print(f"a = {a}\nb = {b}")
포매팅을 이용했는데 나도 포매팅이용하다가 줄바꿈을 어떻게 사용해야할지를 잘 모르겠어서 프린트문의 끝부분이 무조건 줄바꿈이라는걸 이용해서
프린트문 두개 사용해서 나타냈었는데 그냥 이스케이프사용해서 줄바꿈하는 방법 가지고 가면 좋을거같음
[접근 방법]
- 아이디어 a와 b를 나타내고 거기에 해당하는 값까지 같이 출력해야되니 그냥 a와 b를 나타내는 프린트문 출력해보자  
- 시간복잡도: O(n)

"""

a, b = map(int, input().strip().split(' '))
print("a =", a)
print("b =", b)

if __name__ == "__main__":
    # 예시 테스트
    a, b = map(int, input().strip().split(' '))
    print("a =", a)
    print("b =", b)