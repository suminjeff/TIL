def solution(bridge_length, weight, truck_weights):
    que = [0] * (bridge_length + 1)
    front = 0
    rear = bridge_length
    que[rear] = truck_weights.pop(0)
    time = 1
    done = []
    while sum(que) != 0:
        if sum(que) + truck_weights[0] < weight:
            rear = (rear + 1) % (bridge_length + 1)
            que[rear] = truck_weights.pop(0)
        else:
            rear = (rear + 1) % (bridge_length + 1)
            que[rear] = 0
        front = (front + 1) % (bridge_length + 1)
        time += 1
        if que[front] != 0:
            done.append(que[front])
            que[front] = 0
    return time


# bridge_length1 = 2
# weight1 = 10
# truck_weights1 = [7, 4, 5, 6]
# print(solution(bridge_length1, weight1, truck_weights1))

bridge_length2 = 100
weight2 = 100
truck_weights2 = [10]
print(solution(bridge_length2, weight2, truck_weights2))

bridge_length3 = 100
weight3 = 100
truck_weights3 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(bridge_length3, weight3, truck_weights3))
