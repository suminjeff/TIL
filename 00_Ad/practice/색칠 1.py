import sys
sys.stdin = open('색칠 1.txt', 'r')
input = sys.stdin.readline
W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

area = (c+1)*(x2-x1)*(y2-y1)
if f <= W//2:
    if f <= x1:
        print(W*H - area)
    else:
        print(W*H - (area+(min(f, x2)-x1) * (y2-y1) * (c+1)))
else:
    if W <= x1+f:
        print(W*H - area)
    else:
        print(W*H - (area + (min(W, f+x2) - (f+x1)) * (y2-y1)*(c+1)))




# arr = [[1]*W + [0]*W for _ in range(H)]
# for i in range(H):
#     for j in range(2*W):
#         if f <= j < f+f:
#             arr[i][j] += 1
#         elif j < f:
#             arr[i][j] = 0
# if c > 0:
#     for i in range(H//(c+1), H, H//(c+1)):
#         for j in range(i, i+H//(c+1)):
#             for k in range(f, 2*W):
#                 arr[j][k] += arr[j-H//(c+1)][k]
# ans = W * H
# for i in range(H-y2, H-y1):
#     for j in range(f+x1, f+x2):
#         ans -= arr[i][j]
# print(ans)



