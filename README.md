# 알고리즘 공부 기록

### Algorithm Tier
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=mopil1102)](https://solved.ac/mopil1102/)

## 📜 Tips
#### 파이썬 함수 작명 규칙은 Snake case (언더스코어)

[루트 적용하기]
  - Math.sqrt()
  - n ** 0.5
  <br>
 
[정렬]
  - sorted(list, reverse=bool) : return 정렬된 객체
  - list.sort(reverse=bool)
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
 