import matplotlib.pyplot as plt

c1 = [0.19, 0.53, 0.65, 0.72, 0.76]
c10 = [0.20, 0.53, 0.69, 0.72, 0.76]
c50 = [0.23, 0.56, 0.71, 0.76, 0.79]
c100 = [0.24, 0.59, 0.73, 0.79, 0.81]
c150 = [0.24, 0.61, 0.74, 0.80, 0.83]
c200 = [0.25, 0.61, 0.74, 0.80, 0.83]

k1 = [0.02, 0.05, 0.08, 0.09, 0.11]
k10 = [0.02, 0.07, 0.09, 0.11, 0.13]
k50 = [0.02, 0.07, 0.11, 0.14, 0.16]
k100 = [0.03, 0.08, 0.13, 0.16, 0.18]
k150 = [0.03, 0.09, 0.13, 0.17, 0.19]
k200 = [0.03, 0.09, 0.14, 0.17, 0.20]

x = [10, 50, 100, 150, 200]

plt.plot(x, c1, label="Un estudiante")
plt.plot(x, c10, label="Diez estudiantes")
plt.plot(x, c50, label="Cincuenta estudiantes")
plt.plot(x, c100, label="Cien estudiantes")
plt.plot(x, c150, label="Ciento cincuenta estudiantes")
plt.plot(x, c200, label="Doscientos estudiantes")

plt.legend()

plt.show()

plt.plot(x, k1, label="Un estudiante")
plt.plot(x, k10, label="Diez estudiantes")
plt.plot(x, k50, label="Cincuenta estudiantes")
plt.plot(x, k100, label="Cien estudiantes")
plt.plot(x, k150, label="Ciento cincuenta estudiantes")
plt.plot(x, k200, label="Doscientos estudiantes")

plt.legend()

plt.show()
