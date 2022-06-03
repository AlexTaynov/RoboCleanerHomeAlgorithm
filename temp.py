import math


def arithmetical_mean(a, b):
    return (a + b) / 2.0


def geometric_mean(a, b):
    return math.sqrt(a * b)


def harmonic_mean(a, b):
    return 2.0 * a * b / (a + b)

list_x = [0, 1, 0, 2, 0, 2, 1]
list_y = [0, 1, 1, 0, 2, 2, 0]

# x = [273, 283, 288, 293, 313, 333, 353, 373]
# y = [29.4, 33.3, 35.2, 37.2, 45.8, 55.2, 65.6, 77.3]

x = [1, 2, 3, 4, 5]
y = [0, 0, 0, 0, 0]

for i in range(len(x)):
    y[i] += 5 * math.log(x[i]) + 2
    i += 1

# 0 - arithmetical
# 1 - geometric
# 2 - harmonic

formulas = [
    'y = ax+b',
    'y = ax^b',
    'y = ab^x, y = ae^(px), p = ln(x)',
    'y = a/x + b',
    'y = 1/(ax+b)',
    'y = x/(ax+b)',
    'y = aln(x) + b'
]

min = len(x) + 1
status = -1

for i in range(len(list_x)):
    x_s = 0
    y_s = 0
    if (list_x[i] == 0):
        x_s = arithmetical_mean(x[0], x[len(x) - 1])
    elif (list_x[i] == 1):
        x_s = geometric_mean(x[0], x[len(x) - 1])
    else:
        x_s = harmonic_mean(x[0], x[len(x) - 1])

if (list_y[i] == 0):
    y_s = arithmetical_mean(y[0], y[len(y) - 1])
elif (list_y[i] == 1):
y_s = geometric_mean(y[0], y[len(y) - 1])
else:
y_s = harmonic_mean(y[0], y[len(y) - 1])

y_ss = 0

if (x_s in x) == False:
    index = 0
for j in range(len(x)):
    if (x_s < x[j]):
    index = j - 1
break
y_ss = y[index] + (y[index + 1] - y[index]) / (x[index + 1] - x[index]) * (x_s - x[index])

else:
for j in range(len(y)):
    if (x_s == x[j]):
    y_ss = y[j]
break

dif = abs(y_s - y_ss)
if (dif < min):
    min = dif
status = i
print("x_s =", round(x_s, 1), "|y_s =", round(y_s, 1), "|y_ss =", round(y_ss, 1), "|dif =", round(dif, 1),
      "|formula_number =", i + 1)

print()
print("min_dif =", round(min, 1), " formula number", status + 1)
print(formulas[status])

if (formulas[status] == 'y = ax+b'):
    n = len(x)
# сумма x_i
sumXi = 0
for i in range(n):
    sumXi += x[i]
# сумма y_i
sumYi = 0
for i in range(n):
    sumYi += y[i]
# cумма квадратов иксов
sumXi2 = 0
for i in range(n):
    sumXi2 += x[i] * x[i]
# сумма y_i*x_i
sumXY = 0
for i in range(n):
    sumXY += x[i] * y[i]

a = (n * sumXY - sumYi * sumXi) / (n * sumXi2 - sumXi * sumXi)
b = (sumYi - a * sumXi) / n
print('y=', a, '* x + ', b, )

if (formulas[status] == 'y = ax^b'):
    n = len(x)
# сумма натуральных лог y_i
sum_ln_Yi = 0
for i in range(n):
    sum_ln_Yi += math.log(y[i])
# сумма натуральных лог x_i
sum_ln_Xi = 0
for i in range(n):
    sum_ln_Xi += math.log(x[i])
# сумма произведения нат лог y_i и x_i
sum_ln_XY = 0
for i in range(n):
    sum_ln_XY += math.log(x[i]) * math.log(y[i])
# сумма квадратов нат лог x_i
sum_ln_Xi2 = 0
for i in range(n):
    sum_ln_Xi2 += math.log(x[i]) * math.log(x[i])

b = (n * sum_ln_XY - sum_ln_Yi * sum_ln_Xi) / (n * sum_ln_Xi2 - math.pow(sum_ln_Xi, 2))
a = (sum_ln_Yi - b * sum_ln_Xi) / n
a = math.exp(a)

print('y= ', a, '* x ^ ', b)

if (formulas[status] == 'y = aln(x) + b'):
    n = len(x)
# сумма ln x_i
sum_ln_Xi = 0
for i in range(n):
    sum_ln_Xi += math.log(x[i])
# сумма y_i
sumYi = 0
for i in range(n):
    sumYi += y[i]
# сумма y_i*ln x_i
sum_Yi_ln_Xi = 0
for i in range(n):
    sum_Yi_ln_Xi += y[i] * math.log(x[i])
# сумма квадратов ln x_i
sum_ln_Xi2 = 0
for i in range(n):
    sum_ln_Xi2 += math.pow(math.log(x[i]), 2)

a = (n * sum_Yi_ln_Xi - sumYi * sum_ln_Xi) / (n * sum_ln_Xi2 - math.pow(sum_ln_Xi, 2))
b = (sumYi - a * sum_ln_Xi) / n
print('y = ', a, ' * ln(x) + ', b)

if (formulas[status] == 'y = 1/(ax+b)'):
    n = len(n)
# сумма отношения x_i/y_i
sumXY = 0
for i in range(n):
    sumXY += x[i] / y[i]
# сумма x_i
sumXi = 0
for i in range(n):
    sumXi += x[i]
# сумма квадратов x_i
sumXi2 = 0
for i in range(n):
    sumXi2 += math.pow(x[i], 2)
# сумма 1/y_i
sumYi = 0
for i in range(n):
    sumYi += 1 / y[i]

a = (n * sumXY - sumXi * sumYi) / (n * sumXi2 - math.pow(sumXi, 2))
b = (sumYi - a * sumXi) / n
print('y = 1/( ', a, ' * x + ', b, ' )')

if (formulas[status] == 'y = a/x + b'):
    n = len(n)
# сумма отношения y_i/x_i
sumYX = 0
for i in range(n):
    sumYX += y[i] / x[i]
# сумма y_i
sumYi = 0
for i in range(n):
    sumYi += y[i]
# сумма 1/x_i
sumXi = 0
for i in range(n):
    sumXi += 1 / x[i]
# сумма (1/x_i)^2
sumXi2 = 0
for i in range(n):
    sumXi2 += 1 / math.pow(x[i], 2)

a = (n * sumYX - sumYi * sumXi) / (n * sumXi2 - math.pow(sumXi, 2))
b = (sumYi - a * sumXi) / n
print('y = ', a, ' / x + ', b, ' )')

if (formulas[status] == 'y = x/(ax+b)'):
    n = len(n)
# сумма отношения 1/y_i*x_i
sumYX = 0
for i in range(n):
    sumYX += 1 / (y[i] * x[i])
# сумма
1 / y_i
sumYi = 0
for i in range(n):
    sumYi += 1 / y[i]
# сумма 1/x_i
sumXi = 0
for i in range(n):
    sumXi += 1 / x[i]
# сумма (1/x_i)^2
sumXi2 = 0
for i in range(n):
    sumXi2 += 1 / math.pow(x[i], 2)

b = (n * sumYX - sumYi * sumXi) / (n * sumXi2 - math.pow(sumXi, 2))
a = (sumYi - b * sumXi) / n
print('y = x/(', a, '* x + ', b, ' )')
