def caesar(s,n):
    s=list(s)
    n1=n%26
    for i in range(len(s)):
 
        if s[i].isupper():#대문자이면
            if ord(s[i])+n1 > ord('Z'):
                s[i] =chr(ord('A')+ ord(s[i])-ord('Z')+n1-1)
            else:
                s[i]=chr(ord(s[i])+n1)
        elif s[i].islower(): #소문자이면
            if ord(s[i])+n1 > ord('z'):
                s[i]=chr(ord('a') + ord(s[i])-ord('z')+n1-1)
            else:
                s[i]=chr(ord(s[i])+n1)
    return s
#출력확인용 예시입니다.
s1="ejf 1rjas gmzwy vzu irb2q zhfm ejf cdnt xzl"
for i in range(26) :
    ss=caesar(s1,i)
    print(ss)

