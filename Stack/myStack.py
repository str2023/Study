# 스택 구현해보기 Stack Implementation
# 리스트 이용해서 사이즈가 정해진 스택 구현
class Stack:
    def __init__(self, size):
        self.stack = [0] * size # 0으로 초기화된 size 크기의 리스트 생성
        self.top = -1 # 스택의 가장 마지막 원소의 인덱스를 나타내는 top을 -1로 초기화. 값이 들어가면 +1
        self.size = size # 크기 정보

    # 스택이 꽉 차 있는지 검사
    def isFull(self):
        if self.top == self.size - 1: # top이 크기보다 1 작으면 가득 참
            print("Stack is Full.")
            return True
        else:
            return False
    
    # 스택이 완전히 비어있는지 검사
    def isEmpty(self):
        if self.top == -1:  # top이 -1이면 스택은 비어있음
            print("Stack is Empty.")
            return True
        else:
            return False
    
    # 스택에 요소를 추가
    def push(self,data):
        if not self.isFull():   # 스택이 가득 차있지 않다면 top에 1을 더한 인덱스에 값을 초기화
            self.top += 1
            self.stack[self.top] = data
        
    # 가장 마지막에 들어온 요소를 반환하고 제거
    def pop(self):
        if not self.isEmpty():  # 스택이 비어있지 않다면 가장 마지막 값을 리턴하고 0으로 초기화한 뒤 top을 1 낮춤 
            returnValue = self.stack[self.top]
            self.stack[self.top] = 0
            self.top -= 1
            return returnValue
    
    # 스택에 저장된 모든 요소를 출력
    def print(self):
        if not self.isEmpty():
            for i in range(self.top+1):
                print(self.stack[i], sep=', ')