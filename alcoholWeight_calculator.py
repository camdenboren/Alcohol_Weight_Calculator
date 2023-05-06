##########################################################################################################################
#  Alcohol Weight Calculator                                                                                             #
#                                                                                                                        #
#  Uses power and exponential trendlines (found in excel) to accurately estimate the weight of various types of alcohol  #
#  -can be used for either individual ingredients or mixed drinks                                                        #
#                                                                                                                        #
#  Written by Camden Boren @ 2:45AM 5/5/2023                                                                             #
##########################################################################################################################

import math
import decimal

def alcoholWeight(alcoholType,percentage):
    if (alcoholType == 'hard' or alcoholType == 'whiskey' or alcoholType == 'vodka' or alcoholType == 'gin' 
            or alcoholType == 'rum' or alcoholType == 'everclear' or alcoholType == 'grain alcohol'):
        alcoholNum = 1
        return 3062.9*pow(percentage,-1.161), alcoholNum
    elif (alcoholType == 'flavored' or alcoholType == 'liquer' or alcoholType == 'baileys' or alcoholType == 'schnapps' 
            or alcoholType == 'kahlua' or alcoholType == 'liqueur'):
        alcoholNum = 2
        return (235.94*math.exp(percentage*-.044)), alcoholNum
    elif (alcoholType == 'carbonated' or alcoholType == 'fermented' or alcoholType == 'beer' or alcoholType == 'wine' 
            or alcoholType == 'malt beer' or alcoholType == 'seltzer'):
        alcoholNum = 3
        return 1772.6*pow(percentage,-0.996), alcoholNum
    else:
        alcoholNum = 0
        return '***error***', alcoholNum    

alcoholTypeArray = []
weightArray = []
volumeArray = []
densityArray = []
numPartsArray = []
percentageArray = []
calculatedWeightArray = []

scalar = 0
n = 1

# user input
numIngredients = int(input('\nEnter the total number of ingredients in the drink: '))
numDrinks = float(input('Enter the quantity of units of alcohol you want this drink to contain: '))
if numIngredients > 1:
    for m in range(numIngredients):
        numPartsArray.append(float(input('Enter the desired number of parts of alcohol #' + str(n) + ': ')))
        n += 1

for i in range(numIngredients):
    volumeNum = 0
    alcoholType = input('\nEnter alcohol type: ')
    percentage = float(input('Enter Alcohol Percentage of drink: '))
    weight, alcoholNum = alcoholWeight(alcoholType,percentage)
    weight = decimal.Decimal(str(weight))
    weight = float(weight.quantize(decimal.Decimal('.1'), rounding=decimal.ROUND_HALF_UP))
    if numIngredients == 1:
        print(f'Weight of {numDrinks} standard unit(s) of {alcoholType} (of strength {percentage}%) is {numDrinks*weight}g\n')

    # array insertions for mixed drinks
    if numIngredients > 1:
        if alcoholNum == 1 or alcoholNum == 2 :
            volumeNum = (40/percentage)*44.355
            volumeArray.append(volumeNum)
        elif alcoholNum == 3:
            volumeNum = (5/percentage)*354.84
            volumeArray.append(volumeNum)
        else:
            volumeArray.append(0)
        alcoholTypeArray.append(alcoholType)
        density = weight/volumeNum
        densityArray.append(density)
        weightArray.append(weight)
        percentageArray.append(percentage)
        if i == 0:
            calculatedWeightArray.append(weight)
        else:
            calculatedWeightArray.append((((volumeArray[0]*numPartsArray[i])/numPartsArray[0])*density))

# calculates the scalar, the final weight of each ingredient, then displays them
if numIngredients > 1:
    temp = 0
    counter = 0
    for j in calculatedWeightArray:
        temp += (calculatedWeightArray[counter]/weightArray[counter])
        counter += 1
    scalar = numDrinks/temp        

    print('\nThe weight of each ingredient in the mixed drink is:')
    counter = 0
    finalWeight = 0
    for j in calculatedWeightArray:
        finalWeight = decimal.Decimal(str(scalar*calculatedWeightArray[counter]))
        finalWeight = float(finalWeight.quantize(decimal.Decimal('.1'), rounding=decimal.ROUND_HALF_UP))
        print(f'    -{alcoholTypeArray[counter]}: {finalWeight}g')
        counter += 1
    print('\n')