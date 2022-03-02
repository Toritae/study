import sys
sys.stdin = open("input.txt", 'r')
l = 0 
while True:
    try:
        for word in input().split():
            if word == '<br>':
                l = 0
                print()
            elif word == '<hr>':
                if l:
                    print('\n'+'-'*80)
                else:
                    print('-'*80)
                l = 0
            else:
                w_l = len(word)
                if l + w_l > 80:
                    l = w_l
                    print()
                    print(word, end=' ')
                else:
                    l += w_l
                    print(word,end=' ')
                if l+1 >80:
                    l =0
                    print()
                else:
                    l += 1
                    print('',end=' ')
    except:
        break