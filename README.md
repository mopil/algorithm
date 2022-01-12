# 알고리즘 공부 기록

### Algorithm Tier
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=mopil1102)](https://solved.ac/mopil1102/)

## 📜 Tips
#### 파이썬 함수 작명 규칙은 Snake case (언더스코어)
[시간복잡도]
  <br>시간제한 1초인 경우
  - N < 500 : O(N<sup>3</sup>) (3중 반복문)
  - N < 2000 : O(N<sup>2</sup>) (2중 반복문)
  - N < 10만 : O(NlogN)
  - N < 1000만 : O(N)
 <br>

[루트 적용하기]
  - Math.sqrt()
  - n ** 0.5
  <br>
 
[정렬]
  - sorted(list, reverse=bool) : return 정렬된 객체
  - list.sort(reverse=bool)
  <br>
  
[딕셔너리 정렬]
  ```python
  d = sorted(d.items(), key = lambda x: x[1]) # x[]에 따라 key, value로 정렬할 건지 기준을 정해주면 됨
  # items()는 key, value를 튜플 페어로 만들어서 리스트에 넣어서 반환함
  ```
  <br>

[문자열 하나하나 잘라서 입력받기]
  - arr = list(input())
  <br>

[중복 제거하기]
  - set() # 집합에 넣었다 빼기
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
  
[파이썬은 함수 리턴값 가능]
  ```python
  def func():
    return 1, 2, 3
  a, b, c = func() # 정확히는 언패킹이라고 함
  ```
  
 
