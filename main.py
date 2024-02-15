import matplotlib.pyplot as plt
lr = 0.01
w1 = w0 = 0
x = [1,3,7]
y = [2,6,14]
plt.scatter(x,y,color='red', alpha=0.9)
def f(x):
  return w1*x + w0

for i in range(len(x)):
    p = x[i]*w1 + w0
    w1 += 2*lr*x[i]*(y[i]-p)
    w0 += 2*lr*x[i]*(y[i]-p)
plt.plot(x, [f(i) for i in x])
plt.grid()
plt.show()


# # этим дополнения пытался взять наиболее подходящие веса, не знаю правильно делал или нет, но вроде получилось лучше.
# import matplotlib.pyplot as plt
# lr = 0.01
# w1 = w0 = 0
# x = [1,3,7]
# y = [2,6,14]
# plt.scatter(x,y,color='red', alpha=0.9)
# def f(x):
#   return w1*x + w0
# while True:
#   for i in range(len(x)):
#     p = x[i]*w1 + w0
#     w1 += 2*lr*x[i]*(y[i]-p)
#     w0 += 2*lr*x[i]*(y[i]-p)
#   if y[i]-p<0.68 and y[i]-p>0:
#     break
# plt.plot(x, [f(i) for i in x])
# plt.grid()
# plt.show()
