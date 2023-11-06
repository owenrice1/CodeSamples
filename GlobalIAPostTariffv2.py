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

plt.hlines(12,0, 45)
plt.hlines(7,0, 45)

ax = plt.gca()
ax.set_aspect(1)

plt.ylim([0, 30])
plt.xlim([0, 45])


#dashed lines#
plt.vlines(10.5, 0, 7, linestyles='dashed', color='black')
plt.vlines(34.5, 0, 7, linestyles='dashed', color='black')
plt.vlines(18, 0, 12, linestyles='dashed', color='black')
plt.vlines(27, 0, 12, linestyles='dashed', color='black')

#axes labels#

tocallx = [r'$Q_{1}$',r'$Q_{3}$',r'$Q_{4}$',r'$Q_{2}$']
xpuntas = [10.5, 18, 27, 34.5]
ax.set_xticks(xpuntas, labels=tocallx, minor=False)
tocally = [r'$P_{W}$',r'$P_{W+T}$']
ypuntas = [7, 12]

ax.set_yticks(ypuntas, labels=tocally, minor=False)

#welfare zones#

Dcsx=[0,27,0,0]
Dcsy=[30,12,12,30]
plt.fill(Dcsx,Dcsy,color='aquamarine')

Dpsx=[0,18,0,0]
Dpsy=[0,12,12,0]
plt.fill(Dpsx,Dpsy,color='orange')

Dfprx=[18,18,27,27,18]
Dfpry=[0,7,7,0,0]
plt.fill(Dfprx, Dfpry, color='yellow')

Dtaxx=[18,18,27,27,18]
Dtaxy=[7,12,12,7,7]
plt.fill(Dtaxx, Dtaxy, color='lightskyblue')

Dwl1x=[10.5,18,18,10.5]
Dwl1y=[7,7,12,7]
plt.fill(Dwl1x,Dwl1y, color='crimson')

Dwl2x=[27,34.5,27,27]
Dwl2y=[7,7,12,7]
plt.fill(Dwl2x,Dwl2y, color='crimson')


#annotations#
plt.text(20.75, 8.5, "    Tax\nRevenue", size = 8)
plt.text(20.75, 2.5, " Foreign\nProducer\nRevenue", size = 8)
plt.text(6, 18, "Consumer\n  Surplus", size = 8)
plt.text(4, 9, "Producer\n  Surplus", size = 8)
plt.text(14, 8,"DWL",size = 8)
plt.text(28, 8," DWL",size = 8)

#curve labels

plt.text(43.5, 1.5,r'$D_{D}$', size = 8)
plt.text(43.5, 7.5,r'$S_{W}$', size = 8)
plt.text(42.7, 12.5,r'$S_{W+T}$', size = 8)
plt.text(43.5, 28,r'$S_{D}$', size = 8)

plt.title(STitle)
plt.xlabel(Sxlabel)
plt.ylabel(Sylabel)

plt.show()
