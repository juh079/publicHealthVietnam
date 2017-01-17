import csv
import math

#with open("/Users/JHuynh/Desktop/tripDataProject/Vietnam service data.csv", "r") as dataFile:
    #dataFileReader = csv.reader(dataFile)
    #dataList = [] #empty list here
    #for row in dataFileReader:
        #if len(row) != 0:
            #dataList = dataList + [row]

#dataFile.close()

#print (dataList)

def averagePercentile(totalPercentile, totalNumberOfSubjects):
    if totalNumberOfSubjects != 0:
        return totalPercentile/totalNumberOfSubjects
    return 0

def analyzeData( dataFile ):
    with open(dataFile, "r") as dataFile:
        dataFileReader = csv.reader(dataFile)
        maleCounter = 0
        femaleCounter = 0
        totalCounter = 0
        totalWeight = 0
        totalHeight = 0
        totalFemaleWeight = 0
        totalFemaleHeight = 0
        totalMaleWeight = 0
        totalMaleHeight = 0
        ageListCounter = [0,0,0,0,0,0,0,0,0,0,0,0] #number of people per age
        ageListWeight = [0,0,0,0,0,0,0,0,0,0,0,0] #holds avg values for each age
        ageListHeight = [0,0,0,0,0,0,0,0,0,0,0,0]
        
        
        for row in dataFileReader:
            if row[3] == '1':
                if row[2] == 'M':
                    maleCounter = maleCounter + 1
                    totalMaleWeight = totalMaleWeight + float(row[4])
                    totalMaleHeight = totalMaleHeight + float(row[5])
                else:
                    femaleCounter = femaleCounter + 1
                    totalFemaleWeight = totalFemaleWeight + float(row[4])
                    totalFemaleHeight = totalFemaleHeight + float(row[5])
                    
                totalCounter = totalCounter + 1
                totalWeight = totalWeight + float(row[4])
                totalHeight = totalHeight + float(row[5])
                
                #add to agegroup category
                index = math.ceil(float(row[1])) - 1
                ageListCounter[index] = ageListCounter[index] + 1 
                ageListWeight[index] = ageListWeight[index] + float(row[4])
                ageListHeight[index] = ageListHeight[index] + float(row[5])                
                
    
    avgMaleHeight = averagePercentile(totalMaleHeight, maleCounter)
    avgMaleWeight = averagePercentile(totalMaleWeight, maleCounter)
    avgFemaleHeight = averagePercentile(totalFemaleHeight, femaleCounter)
    avgFemaleWeight = averagePercentile(totalFemaleWeight, femaleCounter)
    avgHeight = averagePercentile(totalHeight, totalCounter)
    avgWeight = averagePercentile(totalWeight, totalCounter)
    
    for i in range(0,12):
        print( "number of age " + str(i + 1) + " patients: " + str(ageListCounter[i]))
        print( "avg height for age " + str(i + 1) + ": " + str(averagePercentile(ageListHeight[i], ageListCounter[i])))
        print( "avg weight for age " + str(i + 1) + ": " + str(averagePercentile(ageListWeight[i], ageListCounter[i])))
    
    print()
    print( "number of males: " + str(maleCounter) )
    print( "number of females: " + str(femaleCounter) )
    print( "total kids examined: " + str(totalCounter) )
    print( "males average height percentile: " + str(avgMaleHeight) )
    print( "males average weight percentile: " + str(avgMaleWeight) )
    print( "females average height percentile: " + str(avgFemaleHeight) )
    print( "females average weight percentile: " + str(avgFemaleWeight) )
    print( "total average height percentile: " + str(avgHeight) )
    print( "total average weight percentile: " + str(avgWeight) )
    
    dataFile.close()

analyzeData("/Users/JHuynh/Desktop/tripDataProject/Vietnam service data 7:19:16.csv")
print('****************wheeee****************')
analyzeData("/Users/JHuynh/Desktop/tripDataProject/Vietnam service data 7:20:16.csv")
