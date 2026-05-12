S = tuple(input())
ans = ''

# 回文のチェック
def check(A):
    checker = True
    for i in range(len(A)//2):
        if A[i] != A[len(A) - i -1]:
            checker = False
            break
    return checker

for i in range(len(S)):
    for j in range(len(S)-1, -1 ,-1):
        if S[i] == S[j]:
            A = S[i:j+1]
            if check(A) and len(ans) < len(A):
                ans = ''.join(A)
            else:
                break
print(ans)
