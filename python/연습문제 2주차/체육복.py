def solution(n, lost, reserve):
    resSet = set(reserve)-set(lost) 
    lostSet = set(lost)-set(reserve) 
    
    for i in resSet: 
        if i-1 in lostSet: 
            lostSet.remove(i-1) 
        elif i+1 in lostSet: 
            lostSet.remove(i+1) 
    
    return n-len(lostSet)