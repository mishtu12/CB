K=int(input("org1 "))
L=int(input("org2 "))
M=int(input("org3 "))
t=K+L+M #total_population
kk = (K/t)*((K-1)/(t-1)*1)
kl = (K/t)*(L/(t-1)*2)
km = (K/t)*(M/(t-1))*2
ll = (L/t)*((L-1)/(t-1))*(3/4)
lm = (L/t)*((M)/(t-1))
p=kk+kl+km+ll+lm
print(p)