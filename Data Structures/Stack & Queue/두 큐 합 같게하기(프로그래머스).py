def solution(queue1, queue2):
    answer = -1
    a=sum(queue1)
    b=sum(queue2)
    s=(a+b)//2
    i,j,t=0,0,len(queue1)
    while i<2*t and j<2*t and a!=b:
        if a<s:
            a+=queue2[j]
            b-=queue2[j]
            queue1.append(queue2[j])
            j+=1
        else:
            a-=queue1[i]
            b+=queue1[i]
            queue2.append(queue1[i])
            i+=1
    if a==s:
        answer=i+j
    return answer