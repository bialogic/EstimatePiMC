from RndPoint import RandomPoint
import numpy as np
import matplotlib.pyplot as pl
                    
piPoints = []

# initialise parameters
numberOfPoints = 200
circleRadius = 100
radiusSquared = pow(circleRadius, 2)
simulationCount = 1000
circleCount = 00

# Execute each simulation
for steps in range(simulationCount):
    circleCount = 0
  
    # Generate all points for the current simulation
    for points in range(numberOfPoints):
        point = RandomPoint(circleRadius)
        dataPoints = point.DataPoints()
    
        if point.PointLiesInCircle():
            circleCount += 1
      
    piPoints.append(4 * circleCount/numberOfPoints)
  
# Draw a histogram showing the approximations for the value of pi
meanPiValue = np.mean(piPoints) 
stdDevPiValue = np.std(piPoints)
n, b, p = pl.hist(piPoints, bins=30, color='#99b2e0')
yLimit = max(n)
pl.axis([2.6, 3.8, 0, yLimit*11/10])
pl.axvline(meanPiValue, color='b', linestyle='dashed', linewidth=2)
pl.title('Approximating Pi with Monte Carlo')
pl.text(2.7, yLimit*10/11, "Mean value: " + str(round(meanPiValue, 5)) +
        "\nStd dev: " + str(round(stdDevPiValue, 5)) +
        "\nNo. of points: " + str(simulationCount))
pl.show()



