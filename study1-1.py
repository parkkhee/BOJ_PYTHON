def solution(s):
    answer=""
    cnt=1
    s=s+" "
    n=len(s)
    for i in range(n-1):
        if s[i]==s[i+1]:
            cnt+=1
        else:
            answer+=s[i]
            if cnt>1:
                answer+=str(cnt)
            cnt=1
    return answer

print(solution("KKHSSSSSSSEEE"))
