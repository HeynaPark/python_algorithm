def solution(numlist, n):
    answer = []
    d = []
    
    for num in numlist:
        d.append(num-n)
    
    d.sort()
    d.sort(key=abs)  
    # sort를 두번 해야 풀리는...
    # print(d)
    
    for i in range(len(d)):
        if -1*(d[i]) in d:
            answer.append(n-d[i])
        else:
            answer.append(n+d[i])
    
    
    
    
    return answer
