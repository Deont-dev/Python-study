"""
문제: 문자열 붙여서 출력하기
레벨: 0
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181946

[문제요약]
두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다.
입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.

[풀이답안]
print(input().strip().replace(' ', ''))

[접근 방법]
- 아이디어 : str1,str2 변수를 붙이는 출력을 함수로 나타내보자
- 풀이답안과 내 답안의 차이 : 둘 다 문제는 없는 코딩이지만 출력이라는 조건으로 print를 생각해내는건 자연스러운거 같고
한줄로 끝낼 수 있을지 없을지에 대한 고민의 차이? 였던거 같다.
- 시간복잡도: O
- input()은 그냥 입력값받는거고, strip()은 양옆공백지우기, replace는 공백을 공백없는걸로 대체해서 프린트문으로 한줄출력

"""

str1, str2 = input().strip().split(' ')

def solve(str1,str2):
    print(str1+str2)

solve('hello','world')

if __name__ == "__main__":
    # 예시 테스트
    solve('hello','world')
    

