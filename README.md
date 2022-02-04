
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=mopil1102)](https://solved.ac/mopil1102/)  &nbsp;&nbsp;&nbsp;&nbsp;
<img src="http://mazandi.herokuapp.com/api?handle=mopil1102&theme=cold"/>


# 📜 Tips
### 신기한 파이썬 기능
  - 한국어 변수, 함수명 사용 가능
  - 함수 리턴값 여러개 가능
  - 분기 리턴 결과가 타입이 달라도 됨
    ```python
    if a:
      return True
    else:
      return "맞았습니다"
    ```
  - 수학적 대소비교 가능 ( 0 <= x <= 3 )
  - for문에 iterable 한 객체는 다 들어올 수 있음
    ```python
    for i in (x-1, x+1, x*2): # 튜플, 리스트 가능
      print(i)
    ```
  - 루트 적용하기 : ```Math.sqrt()```, ``` n ** 0.5```
  - 한 줄에 리스트 요소 다 출력하기 : ```print(" ".join(str(i) for i in result)) ```
  - 한 줄에 if문 넣기 : ```print("정답" if test() else "틀림")```
  - 리스트 초기화 하기1 : ``` arr = [0] * 10 ```
  - 문자열 + 연산자 사용 가능 : ```"happy" + "birthday"```
  - 리스트 + 연산자 사용 가능 : ```[1, 2, 3] + [4, 5]```
  - 리스트에 타입 다른 요소 넣기 가능 : ```[1, "hello", 3, 'a']```
  - 문자열에 숫자 있는지 판단하기 : String 내장 메서드로 제공됨 ```s.isdigit()```
  - 2차원 리스트 1차원 리스트로 변환하기 : ```sum(arr, []) # arr : 2차원 리스트```
  - for-else 문 : for문을 다 돌았을 때 break로 빠져나오지 못하면 else문 수행 되는 문법이 존재함
  <br>

<br>

## Etc
[시간복잡도]
  <br>시간제한 1초인 경우
  - N < 500 : O(N<sup>3</sup>) (3중 반복문)
  - N < 2000 : O(N<sup>2</sup>) (2중 반복문)
  - N < 10만 : O(NlogN)
  - N < 1000만 : O(N)
 <br>
 
[정렬]

  - ```sorted(list, reverse=bool) : return 정렬된 객체```
  - ```list.sort(reverse=bool)```
  <br>
  
[딕셔너리 정렬]
  ```python
  d = sorted(d.items(), key = lambda x: x[1]) # x[]에 따라 key, value로 정렬할 건지 기준을 정해주면 됨
  # items()는 key, value를 튜플 페어로 만들어서 리스트에 넣어서 반환함
  ```
  <br>

[조합, 중복조합]
  ```python
  import itertools
  for c in itertools.combinations(['A','B','C'], 2):  # A,B,C 세 개의 원소 중 두 개를 뽑는 경우의 수 = 3가지
    print(c)  # ('A','B') / ('A','C') / ('B','C')

  for cr in itertools.combinations_with_replacement(['A','B','C'], 2):
    print(c)    # 중복 가능이므로 ('A','A') 등도 포함.
  ```
  <br>
  
[리스트 IndexError 무시하기]
 - try ~ except로 예외처리
  <br>

[코드 한 줄로 리스트 요소 모두 출력하기]
  ```python
  result = [1,2,3]
  print(" ".join(str(i) for i in result))
  ```
  <br>
  
[사용자입력 빠르게 받기]
  ```python
  import sys
  input = sys.stdin.readline # rstrip()을 나중에 붙혀줘야 개행문자 제거 됨
  ```
  <br>
  
 [최대 공약수와 최소 공배수]
  ```python
  import math
  
  # 최소 공배수(LCM)을 구하는 함수
  def lcm(a,b):
    return a * b // math.gcd(a,b) # 최대 공약수 구하는건 math 라이브러리에 있음
    
  ```
  <br>
  
[유클리드 호제법]
  - 자연수 a,b의 최대 공약수는 b, a%b의 최대 공약수와 동일하다
  - 재귀로 gcd함수 구현
   ```python
    def gcd(a, b):
      if a % b == 0:
        return b
      else:
        return gcd(b, a % b)
   ```
   <br>

