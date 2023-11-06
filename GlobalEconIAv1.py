import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

#Titles#
STitle = "Market for Tin-Plated Steel in US" #check country#
Sxlabel = "Quantity \n(mn tonnes)" #check unit#
Sylabel = "Price \n($USD)"

#Creation of lines at Equilibrium#
IMofD = -0.6666
ICofD = 30
IMofS = 0.6666
ICofS = 0


IQty = (ICofS-ICofD)/(IMofD-IMofS)
IPrice = IMofD*IQty + ICofD




apricexpoints = ([0,IQty])
apriceypoints = ([IPrice,IPrice])

aqtyxpoints = ([IQty,IQty])
aqtyypoints = ([0,IPrice])

x = np.linspace(0,4*IQty)

DCurve = (x*IMofD)+ICofD
SCurve = (x*IMofS)+ICofS
plt.plot(x, DCurve, color = 'black')
plt.plot(x, SCurve, color = 'black')

#plt.hlines(12,0, 45)
plt.hlines(7,0, 45)

ax = plt.gca()
ax.set_aspect(1)

plt.ylim([0, 30])
plt.xlim([0, 45])


#dashed lines#
plt.vlines(10.5, 0, 7, linestyles='dashed', color='black')
plt.vlines(34.5, 0, 7, linestyles='dashed', color='black')
#plt.vlines(18, 0, 12, linestyles='dashed', color='black')
#plt.vlines(27, 0, 12, linestyles='dashed', color='black')

#axes labels#

#tocallx = [r'$Q_{1}$',r'$Q_{3}$',r'$Q_{4}$',r'$Q_{2}$']
tocallx = [r'$Q_{1}$',r'$Q_{2}$']
#xpuntas = [10.5, 18, 27, 34.5]
xpuntas = [10.5, 34.5]
ax.set_xticks(xpuntas, labels=tocallx, minor=False)
#tocally = [r'$P_{W}$',r'$P_{W+T}$']
tocally = [r'$P_{W}$']
#ypuntas = [7, 12]
ypuntas = [7]
ax.set_yticks(ypuntas, labels=tocally, minor=False)

#welfare zones#

Dcsprex=[0,34.5,0,0]
Dcsprey=[30,7,7,30]
plt.fill(Dcsprex,Dcsprey,color='aquamarine')

Dpsprex=[0,10.5,0,0]
Dpsprey=[0,7,7,0]
plt.fill(Dpsprex,Dpsprey,color='orange')

Dfprprex=[10.5,10.5,34.5,34.5,10.5]
Dfprprey=[0,7,7,0,0]
plt.fill(Dfprprex, Dfprprey, color='yellow')

#curve labels

plt.text(43.5, 1.5,r'$D_{D}$', size = 8)
plt.text(43.5, 7.5,r'$S_{W}$', size = 8)
plt.text(43.5, 28,r'$S_{D}$', size = 8)

#annotations

plt.text(20.75, 2.5, " Foreign\nProducer\nRevenue", size = 8)
plt.text(8, 14, "Consumer\n  Surplus", size = 8)
plt.text(1, 3.5, "Producer\n  Surplus", size = 8)



plt.title(STitle)
plt.xlabel(Sxlabel)
plt.ylabel(Sylabel)

plt.show()
