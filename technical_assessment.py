def tingkat_kemahiran_maksimal(N, M, A, B):
    tingkat_kemahiran = M
    
    for i in range(N-1, -1, -1):
        if tingkat_kemahiran >= A[i]:
            tingkat_kemahiran += B[i]
        else:
            break
    
    return tingkat_kemahiran

def cek_list(list):
    for i in list:
        if 1<=i<=1000 :
            return True
    return False

print("Input: ")
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if (1<=N) and (M<=100) and (cek_list(A) == True) and (cek_list(B) == True) and (len(A) == N) and (len(B) == N):
    print(f"Output: {tingkat_kemahiran_maksimal(N, M, A, B)}")
else:
    print("Format Input Salah")
    
# N, M = 4, 2
# A = [8, 9, 3, 2]
# B = [5, 4, 1, 3]

# N, M = 5, 3
# A = [8, 4, 5, 6, 7]
# B = [9, 8, 7, 5, 6]

# N, M = 5, 9
# A = [2, 3, 6, 7, 8]
# B = [3, 4, 2, 2, 3]