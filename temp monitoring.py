# Austin Daybell
# Temp monitoring
import math
 
# original temperature list
temps = [50.35, 51.75, 53.08, 57.00, 59.25, 61.19, 65.10, 64.22, 58.35, 55.98, 53.50, 50.95, 50.00]
numTemps = len(temps) 
 
for i in range(0,numTemps): 
    rawValue = temps[i]
    intValue = math.floor(rawValue)
    temps[i] = intValue

 
# print updated temps list, min temp value and max temp value
print("temps =",temps)
print("min =",min(temps))
print("max =",max(temps))
 
 
 
# calculate and display the average list value
average = math.fsum(temps) / numTemps
print(str.format("average = {:.2f}",average))
