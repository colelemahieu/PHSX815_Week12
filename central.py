# central limit theorem demo using a Rayleigh distribution

#import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from Random import Random
from math import *

# instantiate Random class
random = Random()

# default number experiments, measurements
Nexp = 100
Nmeas = 50

# user can input value for experiment or measurement number
if "-Nexp" in sys.argv:
    p = sys.argv.index("-Nexp")
    Ne = int(sys.argv[p+1])
    if Ne  > 0:
        Nexp = Ne
if "-Nmeas" in sys.argv:
    p = sys.argv.index("-Nmeas")
    Nt = int(sys.argv[p+1])
    if Nt > 0:
        Nmeas = Nt

# sample from a Rayleigh distribution for Nmeas
# calculate the average value and do it again
averages = []
for i in range(0, Nexp):
    sum = 0
    for j in range(0, Nmeas):
        x = random.rayleigh()
        sum = sum + x
    avg = float(sum) / Nmeas
    averages.append(avg)

# repeat this with 10 times as many samples per experiment
averages2 = []
for i in range(0, Nexp):
    sum = 0
    for j in range(0, 10*Nmeas):
        x = random.rayleigh()
        sum = sum + x
    avg2 = float(sum) / (10*Nmeas)
    averages2.append(avg2)


# Gaussian fits
(mu, sigma) = norm.fit(averages)
(mu2, sigma2) = norm.fit(averages2)

# plotting
plt.figure()
n, bins, patches = plt.hist(averages, bins=10, density=1)
y = mlab.normpdf(bins, mu, sigma)
l = plt.plot(bins, y, "darkgreen", linewidth=2)
plt.title("Rayleigh Distribution Sample Averages")
plt.xlabel("Averages")
plt.ylabel("Relative Frequency")

# plotting labels
left, right = plt.xlim()
bottom, top = plt.ylim()
plt.text(left+0.025*(right-left), 0.95*top, "Exp Num = %i" %(Nexp), fontweight="bold")
plt.text(left+0.025*(right-left), 0.90*top, "Meas Num = %i" %(Nmeas), fontweight="bold")
plt.text(right-0.175*(right-left), 0.95*top, "$\\mu$ = %.3f" %(mu), fontweight="bold")
plt.text(right-0.175*(right-left), 0.90*top, "$\\sigma$ = %.3f" %(sigma), fontweight="bold")

# second plot and labels
plt.figure()
n2, bins2, patches2 = plt.hist(averages2, bins=10, density=1)
y2 = mlab.normpdf(bins2, mu2, sigma2)
l2 = plt.plot(bins2, y2, "darkgreen", linewidth=2)
plt.title("Rayleigh Distribution Sample Averages")
plt.xlabel("Averages")
plt.ylabel("Relative Frequency")

left2, right2 = plt.xlim()
bottom2, top2 = plt.ylim()
plt.text(left2+0.025*(right2-left2), 0.95*top2, "Exp Num = %i" %(Nexp), fontweight="bold")
plt.text(left2+0.025*(right2-left2), 0.90*top2, "Meas Num = %i" %(10*Nmeas), fontweight="bold")
plt.text(right2-0.175*(right2-left2), 0.95*top2, "$\\mu$ = %.3f" %(mu2), fontweight="bold")
plt.text(right2-0.175*(right2-left2), 0.90*top2, "$\\sigma$ = %.3f" %(sigma2), fontweight="bold")

plt.show()





        
        

