from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    b_sum = 0 
    while bridge:
        time += 1
        print(bridge , truck_weights )

        b_sum -= bridge.popleft()

        print(b_sum)

        if truck_weights:
            if b_sum + truck_weights[0] > weight:
                bridge.append(0)
            else:
                b_sum += truck_weights[0]

                bridge.append(truck_weights.pop(0))

    return time

solution(2,10,[7,4,5,6])