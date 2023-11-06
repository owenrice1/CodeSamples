import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
#Titles#
STitle = "Market for All Goods and Services in Australia"
Sxlabel = "Real Output \n(Y)"
Sylabel = "Average \n Price Level \n($AUD)"

up = u'\u2191'
down = u'\u2193'
#Graph Production#
plt.title(STitle)
plt.xlabel(Sxlabel)
plt.ylabel(Sylabel)
#plt.grid()
plt.ylim([0, 30])
plt.xlim([0, 30])

#standin axis points#
tocallx = [r'$Y_{1}$',r'$Y_{F}$', r'$Y_{F1}$',r'$Y_{2}$',r'$Y_{F2}$']
xpuntas = [11, 20, 20.88, 17.962, 23.2]
ax.set_xticks(xpuntas, labels=tocallx, minor=False)
tocally = [r'$P_{L1}$',r'$P_{L}$',r'$P_{L2}$', r'$P_{L3}$']
ypuntas = [9, 10, 13.12, 10.9]
ax.set_yticks(ypuntas, labels=tocally, minor=False)
#end of standin axis points#

#lines#

#sras1#
x = np.linspace(0,21.846,60)
xex = np.linspace(0,24.846,60)
y=5**(x-20)+9
plt.plot(x,y, color='orangered')
plt.plot(xex,y, color='orangered', linestyle='dashed')
##
#lras1#
plt.axvline(x=20, ymin=0, ymax=0.95, color='peru')
#lras2#
plt.axvline(x=23.2, ymin=0, ymax=0.95, color='peru')

#ADS#
def f(x):
    y2=30-x
    return y2
def f2(x):
    y3=20-x
    return y3
def f3(x):
    y4=34-x
    return y4
def f4(x):
    y5=27-x
    return y5
x2 = np.linspace(12,26)
x3 = np.linspace(2,16)
x4 = np.linspace(16,28)
x5 = np.linspace(9,23)

plt.plot(x2,f(x2), color='dodgerblue')
plt.plot(x3,f2(x3), color='dodgerblue')
plt.plot(x4,f3(x4), color='dodgerblue')
plt.plot(x5,f4(x5), color='dodgerblue')
##

#dashedlines#
plt.hlines(10,0,20, color='black', linestyles='dashed')
plt.hlines(13.12,0,20.88, color='black', linestyles='dashed')
plt.hlines(10.7,0,23.2, color='black', linestyles='dashed')

plt.vlines(11, 0, 9, color='black', linestyles='dashed')
plt.vlines(20.88, 0, 13.12, color='black', linestyles='dashed')
plt.vlines(17.962, 0, 9.038, color='black', linestyles='dashed')




#line labels#
plt.text(19.5,29, "$LRAS_{1}$", size = 8)
plt.text(22.75,29, "$LRAS_{2}$", size = 8)
plt.text(24.3,29, "$SRAS_{2}$", size = 8)
plt.text(21.346, 29, "$SRAS_{1}$", size = 8)
plt.text(26,3,"$AD_{1}$", size = 8)
plt.text(16,3,"$AD_{2}$", size = 8)
plt.text(22.5,3,"$AD_{3}$", size = 8)
plt.text(28,5,"$AD_{4}$", size = 8)

#arrows#
plt.annotate("", xy = (3,17), xytext=(13,17), arrowprops = dict(arrowstyle='->'))
plt.annotate("", xy = (11,16), xytext=(4,16), arrowprops = dict(arrowstyle='->'))
plt.annotate("", xy = (18,16), xytext=(11,16), arrowprops = dict(arrowstyle='->'))
plt.annotate("", xy = (23.1,20), xytext=(20.1,20), arrowprops = dict(arrowstyle='->'))


#annotated changes#
plt.annotate(down + "C   " + down + "I", xy = (6,17.25))
plt.annotate(up + "G", xy = (7.5,15.15))
plt.annotate(up + "C   " + up + "I", xy = (15.5,15.15))
plt.annotate(up + "I", xy = (22,20.2))

plt.show()
