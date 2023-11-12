from sympy import Symbol, solve
from numpy import pi

x = Symbol('x') 

r = 0.015
l = 0.7
energy = 600
# energy = Symbol('energy')

name = ["chromoly steel", "toolsteel", "Beryllium Copper", "malleable Iron", "pure titanium"\
    ,"aluminum bronze", "high-speed steel", "pure tungsten", "carbon fiber"]
y = [500, 1400, 1110, 480, 380, 250, 1000, 750, 2500]
e = [205, 200, 131, 172, 116, 110, 200, 750, 500]
unitprice = [4, 2, 13, 3, 61, 9, 8, 110, 22]
density = [7850, 7810, 8250, 7150, 4510, 7640, 78160, 19250, 2000]
sol = []
price = []
weight = []

for j in range(0, len(y)):
    y[j] = y[j] * 1000000
    e[j] = e[j] * 1000000000
    m = 4*(pow(r, 3) - pow(x, 3))* y[j]/3  # 극한모멘트
    p = 4 * m / l # 하중
    i = pi * (pow(r, 4) - pow(x, 4)) / 4 # 2차모멘트
    d = p*pow(l,3)/(48 * e[j] * i) # 변형
    bd = 0.1 # 최대변형
    equation = (bd - (1/2)*d)*p - energy
    print(name[j])
    ans = solve(equation)[1]
    mass = density[j] * (pi * l * (0.015**2 - ans**2))
    weight.append(mass * 9.81)
    price.append(mass * unitprice[j])
    sol.append(ans)

print(name)
print(sol)
print(price)
print(weight)

# ro = 7850
# y = 500000000 # yield stress
# e = 205000000000 # 탄성계수



# print((bd - (1/2)*d)*p - energy)


print(ro, y, e, m, p, j , d)


