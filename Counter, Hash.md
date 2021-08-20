## Counter

collections.Counter

컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체

```python
import collections
lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee']
print(collections.Counter(lst))
'''
결과
Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})
'''
```





## Hash

hash란

사람은 누구든지 "이름" = "홍길동", "생일" = "몇 월 몇 일" 등으로 구별할 수 있다. 파이썬은 영리하게도 이러한 대응 관계를 나타낼 수 있는 자료형을 가지고 있다. 요즘 사용하는 대부분의 언어도 이러한 대응 관계를 나타내는 자료형을 갖고 있는데, 이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.

파이썬에서는 이러한 자료형을 딕셔너리(Dictionary)라고 하는데, 단어 그대로 해석하면 사전이라는 뜻이다. 즉 "people"이라는 단어에 "사람", "baseball"이라는 단어에 "야구"라는 뜻이 부합되듯이 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형이다. 예컨대 Key가 "baseball"이라면 Value는 "야구"가 될 것이다.

```python
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
```

hash("무언가")는 고유한 정수형을 반환한다.

