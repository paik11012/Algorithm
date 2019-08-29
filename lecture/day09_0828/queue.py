myque = []  # 변수라 리스트이며 global쓰지 않아도 된다
def enqueue(item):
    # global myque  # local변수를 global로 선언해줘야 함
    myque.append(item)
    # myque = item
#
# def dequeue(item):
#     return myque.pop(0)


print(myque)
enqueue(100)
enqueue(200)
enqueue(300)
print(myque)  # 100이 결국 나옴
# print('dequeue',dequeue())  # 큐 첫번째 요소 삭제