class Node(object):
    def __init__(self, value):
        self.value = value  # 자신이 관리하는 값
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):  # 초기화 함수
        # 트리 필요한 것 넣기 rootnode
        self.root = None

    def add(self, value):
        # root가 없으면 root에 현재 값을 넣는다
        # Node라는 클래스도 생성해줘야함
        if self.root == None:
            self.root = Node(value)   # node에는 3가지: 자기 값, 왼쪽, 오른쪽 포인터 지니기  1 저장
        else:
            self._add(value, self.root)  # 재귀적 저장 함수  2 루트에 저장

    def _add(self, value, node):
        # value는 저장하려는 숫자. root보다 작으면 왼쪽, 크면 오른쪽에 저장
        if node.value < value:  # 저장하려는 숫자가 더 크면 오른쪽에 저장  node.val >= val
            if node.left == None:   # 비었으면 노드 만들어 저장
                node.left = Node(value)
            else:
                # 이미 left에 무엇인가가 저장되어 있으면 그 아래 저장
                self._add(value, node.left)
        else:
            if node.right == None:
                node.right = Node(value)
            else:
                self._add(value, node.right)

    def printAll(self):
        if self.root == None:
            return
        else:
            self._print(self.root)


    def _print(self, node):
        if node != None:
            print(node.value)  # 자기자신부터 출력 --> 전위법
            self._print(node.left)
            # print(node.value)  # 자신을 중간에 출력 --> 중위법
            self._print(node.right)
            # print(node.value)  # 자신을 마지막에 출력 --> 후위법


t = Tree()
t.add(1)  # 숫자추가
t.add(2)
t.add(3)
t.add(4)

t.printAll()  # 전체 저장값 출력.  / 전위, 중위, 후위 설정