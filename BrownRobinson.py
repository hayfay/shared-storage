def indexOfMaxElement(array):
    return sorted([(index, value) for (index, value) in enumerate(array)], key=lambda x: x[1])[-1][0]

def indexOfMinElement(array):
    return sorted([(index, value) for (index, value) in enumerate(array)], key=lambda x: x[1])[0][0]

def BrownRobinson(strategyMatrix, targetError, maxStep):
    currentStrategyA = 0
    currentStrategyB = 0
    algSteps = []
    total = {"solution": [], "answer": []}
    M = len(strategyMatrix)
    N = len(strategyMatrix[0])
    CHOICE_A_INDEX = 0
    CHOICE_B_INDEX = 1
    WIN_A_START = 2
    WIN_B_START = WIN_A_START + M
    TOP_SCORE = WIN_B_START + N
    LOWER_SCORE = TOP_SCORE + 1
    ERROR = LOWER_SCORE + 1
    algSteps.append([0 for i in range(ERROR+1)])
    minTopScore = 0
    maxLowerScore = 0
    for i in range(1, maxStep):
        currentStep = [0 for k in range(ERROR+1)]
        currentStep[CHOICE_A_INDEX] = currentStrategyA + 1
        currentStep[CHOICE_B_INDEX] = currentStrategyB + 1
        for j in range(M):
            currentStep[WIN_A_START + j] = algSteps[i-1][WIN_A_START + j] + strategyMatrix[j][currentStrategyB]
        for j in range(N):
            currentStep[WIN_B_START + j] = algSteps[i-1][WIN_B_START + j] + strategyMatrix[currentStrategyA][j]
        currentStep[TOP_SCORE] = max(currentStep[WIN_A_START:WIN_A_START+M]) / i
        currentStep[LOWER_SCORE] = min(currentStep[WIN_B_START:WIN_B_START+N]) / i
        if i==1:
            minTopScore = currentStep[TOP_SCORE]
            maxLowerScore = currentStep[LOWER_SCORE]
        else:
            if currentStep[TOP_SCORE] < minTopScore:
                minTopScore = currentStep[TOP_SCORE]
            if currentStep[LOWER_SCORE] > maxLowerScore:
                maxLowerScore = currentStep[LOWER_SCORE]
        currentStep[ERROR] = minTopScore - maxLowerScore
        algSteps.append(currentStep)
        if currentStep[ERROR] < targetError:
            print(0.5*(minTopScore + maxLowerScore))
            answer = [[],[]]
            answer.append(currentStep[ERROR])
            answer.append(0.5*(minTopScore + maxLowerScore))
            total["solution"] = algSteps
            total["answer"] = answer
            return total
        currentStrategyA = indexOfMaxElement(currentStep[WIN_A_START:WIN_A_START+M])
        currentStrategyB = indexOfMinElement(currentStep[WIN_B_START:WIN_B_START+N])
    total["solution"].append(algSteps)
    return total
