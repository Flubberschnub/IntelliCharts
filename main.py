import random
import mathproblem
import timestable
import time
import math

def load_weights(filename):
    weights = dict()
    with open(filename + '.mwt', 'r') as f:
        for line in f:
            key, val = line.split()
            weights[int(key)] = float(val)
    return weights

def save_weights(weights, filename):
    with open(filename + '.mwt', 'w') as f:
        for key, val in weights.items():
            f.write(str(key) + ' ' + str(val) + '\n')

learningRate = 0.1
desiredAnswerTime = 3

weights = dict()
for i in range(0,13):
    weights[i] = 1

## Normalize weights
total = sum(weights.values())
for key in weights:
    weights[key] /= total

## Option to load weights from file
print("Load weights from file? (y/n)")
if input() == 'y':
    print("Filename:")
    filename = input()
    print("Loading weights for " + filename)
    weights = load_weights(filename)

## Begin Times table game
print("How many questions?")
num_questions = int(input())

print("Starting game in 3...")
## Wait 3 seconds before starting
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

## Start timer
start = time.time()
score = 0
for i in range(0, num_questions):
    ## Choose numbers based on weights
    num1 = random.choices(list(weights.keys()), weights=list(weights.values()))[0]
    num2 = random.choices(list(weights.keys()), weights=list(weights.values()))[0]
    problem = timestable.TimesTable(num1, num2)
    print(problem.get_problem())

    # QUESTION timer
    questionStartTime = time.time()

    answer = int(input())

    questionEndTime = time.time()
    timeElapsed = questionEndTime - questionStartTime

    if problem.check_answer(answer):
        print("Correct!")
        weights[num1] += (weights[num1]) * learningRate * (math.tanh(timeElapsed-desiredAnswerTime))
        weights[num2] += (weights[num2]) * learningRate * (math.tanh(timeElapsed-desiredAnswerTime))
        score += 1
    else:
        print("Incorrect!")
        weights[num1] += (weights[num1]) * learningRate * (1 + math.tanh(timeElapsed))
        weights[num2] += (weights[num2]) * learningRate * (1 + math.tanh(timeElapsed))


        total = sum(weights.values())
        for key in weights:
            weights[key] /= total
## End timer
end = time.time()
print("Time: " + str(end - start))
print("Score: " + str(score) + "/" + str(num_questions))
print("Save weights? (y/n)")
if input() == 'y':
    print("Input name:")
    filename = input()
    save_weights(weights, filename)
