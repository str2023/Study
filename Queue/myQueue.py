# 원형큐 구현해보기 Queue Implementation
# 리스트 이용해서 사이즈가 정해진 원형큐 구현

class CircularQueue:
    # 큐 생성 및 초기화
    def __init__(self,size):
        self.myQueue = [0] * size   # 원형큐는 공백과 포화 상태를 구분하기 위해 완충지대가 필요하므로 실제 데이터가 들어갈 공간은 size - 1
        self.size = size
        self.front = 0  # 처음 값의 인덱스. 출력할 때마다 +1
        self.rear = 0   # 마지막 값의 인덱스. 값이 추가될 때마다 +1
            
    # 큐가 꽉 차있는가 검사
    def isFull(self):
        if self.front == (self.rear + 1) % self.size: # 원형큐이므로 rear는 front보다 1 작을 때 가득 참. 
            print("Queue is Full.")
            return True
        else:
            return False
        
    # 큐가 완전히 비어있는지 검사
    def isEmpty(self):
        if self.front == self.rear: #front와 rear가 같다면 비어있음
            print("Queue is Empty.")
            return True
        else:
            return False
    
    # 데이터 삽입
    def enqueue(self, data):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.size   # 원형큐이므로 인덱스는 반복
            self.myQueue[self.rear] = data
    
    # 데이터 삭제
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.size
            returnValue = self.myQueue[self.front]
            self.myQueue[self.front] = 0
            return returnValue
    
    # 데이터 출력
    def print(self):
        if not self.isEmpty():
            tmp = self.front
            while self.rear != tmp: # 처음값의 인덱스부터 차례로 순회하며 마지막 값까지 출력
                tmp = (tmp + 1)% self.size
                print(self.myQueue[tmp], end=' ')