def solution(bridge_length, weight, truck_weights):
    answer = 0
    proceed = 0
    onBridge = [0] * bridge_length

    while len(onBridge):
        
        answer += 1
        proceed -= onBridge.pop(0)

        if truck_weights:
            if (proceed + truck_weights[0]) <= weight:
                proceed += truck_weights[0]
                onBridge.append(truck_weights.pop(0))
            else:
                onBridge.append(0)

    return answer