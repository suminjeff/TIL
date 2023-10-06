import matplotlib.pyplot as plt

# 예제1: x, y가 가을 때

plt.plot([1, 2, 3, 4])
# plt.show()

# 이때까지 그렸던 plot 지우기
plt.clf()


# 예제2: x, y가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
# plt.show()
plt.clf()

# 예제3: 제목 + 각 축의 설명
plt.plot(x, y)
plt.title("Test Graph")
plt.xlabel("x label")
plt.ylabel("y label")
plt.grid(True)
