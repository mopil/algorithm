
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=mopil1102)](https://solved.ac/mopil1102/)  &nbsp;&nbsp;&nbsp;&nbsp;
<img src="http://mazandi.herokuapp.com/api?handle=mopil1102&theme=cold"/>

# 📑자료실

[코테 집중 백준 문제집 모음](https://github.com/tony9402/baekjoon)
<br>
[최근 기업 알고리즘 출제 동향](https://github.com/tony9402/baekjoon/blob/main/CodingTest.md)
<br>


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
  - 한 줄에 리스트 요소 다 출력하기 : ```print(" ".join(str(i) for i in result)) ```
  - 한 줄에 if문 넣기 : ```print("정답" if test() else "틀림")```
  - 문자열에 숫자 있는지 판단하기 : String 내장 메서드로 제공됨 ```s.isdigit()```
  - 2차원 리스트 1차원 리스트로 변환하기 : ```sum(arr, []) # arr : 2차원 리스트```
  - for-else 문 : for문을 다 돌았을 때 break로 빠져나오지 못하면 else문 수행 되는 문법이 존재함
  - 문자열 뒤집기 : ```arr_string[::-1]```
  - 최대 재귀한도 해제하기 : ```sys.setrecursionlimit(10000)```
  - 리스트, 딕셔너리, 튜플 모두 해당 자료형 이름으로 원소가 같은지, 다른지 비교 가능
    ```python
    arr1, arr2 = [1,2,3], [1,2,3]
    print(arr1 == arr2)
    ```
  <br>


## Etc
[시간복잡도]
  <br>시간제한 1초인 경우
  - N < 500 : O(N<sup>3</sup>) (3중 반복문)
  - N < 2000 : O(N<sup>2</sup>) (2중 반복문)
  - N < 10만 : O(NlogN)
  - N < 1000만 : O(N)
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

