# -*- coding: utf-8 -*-

from js import document, alert # type: ignore

import copy
import random
import datetime


        
def sumOfBallsInsideHat(insideHat, *args):
    
    document.getElementById('sumOfballs').textContent = sum(ball for ball in insideHat.values()) 

def sumOfBallsInsideExpectedHat(expectedHat, *args):
    document.getElementById('sumOfExpectedBalls').textContent = sum(ball for ball in expectedHat.values())
    
def insideHatSummary(insideHat, *args):
    document.getElementById('insideHatSummary').textContent = ', '.join([f'{key.replace("_", " ")}: {value}' for key, value in insideHat.items()])
    
def expectedHatSummary(expectedHat, *args):

    document.getElementById('expectedHatSummary').textContent = ', '.join([f'{key.replace("_", " ")}: {value}' for key, value in expectedHat.items()])
        
def addInsideHat(insideHat, *args):
    
    ballColor = f'{document.getElementById("addBallDiv").dataset.color}'
    ballType = f'{document.getElementById("addBallDiv").dataset.type}'
    ball = f'{ballColor}_{ballType}'
    numberOfBalls = document.getElementById("insideHatBallNumber").value
    
    
    if numberOfBalls != '':
    
        if ball not in insideHat:
            alert(f'{int(numberOfBalls)} piece(s) of \'{ball.replace("_", " ")}\' ball added to the hat')
            insideHat[ball] = int(numberOfBalls)
        
        else:
            
            alert(f'\'{ball.replace("_"," ")}\' is already in the hat!, number of them updated.')
            insideHat.update({ball: int(numberOfBalls)})
        
        document.getElementById("insideHatBallNumber").value = ''
        
        
        
        
        return
    
    alert('Please enter a number of balls')
    
    
        
def addToExpectedHat(insideHat, expectedHat, *args):
    ballColor = f'{document.getElementById("expectedBallDiv").dataset.color}'
    ballType = f'{document.getElementById("expectedBallDiv").dataset.type}'
    ball = f'{ballColor}_{ballType}'
    numberOfBalls = document.getElementById("expectedHatBallNumber").value
    
    if numberOfBalls != '':
        
        if int(numberOfBalls) > insideHat[ball]:
            alert(f'You can\'t add more than {insideHat[ball]} {ball.replace("_", " ")} ball(s) to the expected list')
            
        
        else:
        
            if ball not in expectedHat:
                alert(f'{int(numberOfBalls)} piece(s) of \'{ball.replace("_", " ")}\' ball added to the expected list')
                expectedHat[ball] = int(numberOfBalls)
                
            else:
                alert(f'\'{ball.replace("_"," ")}\' is already in the expected list!, number of them updated.')
                expectedHat.update({ball: int(numberOfBalls)})
            
            
            expectedHatSummary(expectedHat)
        
        document.getElementById("expectedHatBallNumber").value = ''   
        return
    alert('Please enter a number of balls')
            

    
def calculateExperiments(insideHat, expectedHat, *args):
    
    def draw(hat, number_of_balls_drawn):
        insideHatContent = [ball for ball, number in hat.items() for _ in range(number)]
        random.shuffle(insideHatContent)
        choices = []
        
        if number_of_balls_drawn >= len(insideHatContent):
            choices = insideHatContent
            insideHatContent = []
        else:
            for _ in range(number_of_balls_drawn):
                choices.append(insideHatContent.pop(random.randrange(0, len(insideHatContent))))
                
        return choices
    
    
    number_of_balls_drawn = int(numberOfBallsDrawnInput.value)
    number_of_experiments = int(numberOfExperimentsInput.value)
    
    
    expectedHatContent = [ball for ball, number in expectedHat.items() for _ in range(number)]
    
    counts = 0
    
    for _ in range(number_of_experiments):
        hatcopy = copy.deepcopy(insideHat)
        
        draws = draw(hatcopy, number_of_balls_drawn)
        
        flag = True
        
        for ball in expectedHatContent:
            if ball in draws:
                draws.remove(ball)
            else:
                flag = False
                
        if flag:
            counts += 1
            
    probability = (counts / number_of_experiments) * 100
    
    document.getElementById("output").textContent = f'''
Probability of drawing expected balls. {number_of_balls_drawn} balls per experiment. After {number_of_experiments} experiments are drawn is {probability:.2f} %
'''
    document.getElementById("numberOfExperimentsInput").value = ''
    
    document.getElementById("resetButton").style.display = 'block'


def reset(*args):
    document.getElementById('insideHatBallNumber').value = ''
    document.getElementById('expectedHatBallNumber').value = ''
    document.getElementById('numberOfBallsDrawnInput').value = ''
    document.getElementById('numberOfExperimentsInput').value = ''
    document.getElementById('output').textContent = ''
    document.getElementById('sumOfballs').textContent = ''
    document.getElementById('sumOfExpectedBalls').textContent = ''
    document.getElementById('insideHatSummary').textContent = ''
    document.getElementById('expectedHatSummary').textContent = ''
    document.getElementById('resetButton').style.display = 'none'
    
    insideHat.clear()
    expectedHat.clear()
    expectedBallTypes.clear()

def changeAddBallTypes(direction, *args):
    document.getElementById("insideHatBallNumber").value = ''
    addBallDiv = document.getElementById('addBallDiv')
    addBallImg = document.getElementById('addBallImg')
    addBallImgName = document.getElementById('addBallImgName')
    
    FILETYPE = '.svg'
    
    addBallColor = addBallDiv.dataset.color
    addBallType = addBallDiv.dataset.type
    
    
    
    for index, (color, ballTypes) in enumerate(addBallTypes.items()):
        for i, ballType in enumerate(ballTypes):
            if color == addBallColor and ballType == addBallType:
                
                if direction == 'right':
                    i += 1
                    if i == len(ballTypes):
                        index += 1
                        if index == len(addBallTypes):
                            index = 0
                        i = 0
                        
                else:
                    i -= 1
                    if i == -1:
                        index -= 1
                        if index == -1:
                            index = len(addBallTypes) - 1
                        i = len(ballTypes) - 1
                

                addBallDiv.dataset.color = list(addBallTypes.keys())[index]
                
                addBallDiv.dataset.type = addBallTypes[list(addBallTypes.keys())[index]][i]
                
                addBallImg.src = f'./src/img/{addBallDiv.dataset.color}/{addBallDiv.dataset.type}{FILETYPE}'
                addBallImgName.textContent = f'{addBallDiv.dataset.type.replace("_", " ")}'
                return
                        
                        

                    
def changeExpectedBallTypes(direction, *args):
    
    expectedBallDiv = document.getElementById('expectedBallDiv')
    expectedBallImg = document.getElementById('expectedBallImg')
    expectedBallImgName = document.getElementById('expectedBallImgName')
    
    FILETYPE = '.svg'

    expectedBallColor = expectedBallDiv.dataset.color
    expectedBallType = expectedBallDiv.dataset.type
    
    for index, (color, ballTypes) in enumerate(expectedBallTypes.items()):
        for i, ballType in enumerate(ballTypes):
            if color == expectedBallColor and ballType == expectedBallType:
                
                if direction == 'right':
                    i += 1
                    if i == len(ballTypes):
                        index += 1
                        if index == len(expectedBallTypes):
                            index = 0
                        i = 0
                        
                else:
                    i -= 1
                    if i == -1:
                        index -= 1
                        if index == -1:
                            index = len(expectedBallTypes) - 1
                        i = len(ballTypes) - 1
                

                expectedBallDiv.dataset.color = list(expectedBallTypes.keys())[index]
                
                expectedBallDiv.dataset.type = expectedBallTypes[list(expectedBallTypes.keys())[index]][i]
                
                expectedBallImg.src = f'./src/img/{expectedBallDiv.dataset.color}/{expectedBallDiv.dataset.type}{FILETYPE}'
                expectedBallImgName.textContent = f'{expectedBallDiv.dataset.type.replace("_", " ")}'
                return
    
    
            
def nextSection(id, next):
    
    
    if next == 'expectedSection':
        insideHatSummary(insideHat)
        
        for key in insideHat:
            color, *expectedBallType = key.split('_')
            if color not in expectedBallTypes:
                expectedBallTypes[color] = [] 
            expectedBallType = '_'.join(expectedBallType)
            expectedBallTypes[color].append(expectedBallType)
        
        
        expectedBallDiv = document.getElementById('expectedBallDiv')
      
        expectedBallDiv.dataset.color = list(expectedBallTypes.keys())[0]
        expectedBallDiv.dataset.type = expectedBallTypes[expectedBallDiv.dataset.color][0]
        document.getElementById('expectedBallImg').src = f'./src/img/{expectedBallDiv.dataset.color}/{expectedBallDiv.dataset.type}.svg'
        document.getElementById('expectedBallImgName').textContent = f'{expectedBallDiv.dataset.type.replace("_", " ")}'
            
    if next == 'drawSection':
        sumOfBallsInsideHat(insideHat)
        sumOfBallsInsideExpectedHat(expectedHat)
    
    if next == 'experimentSection':
        if int(numberOfBallsDrawnInput.value) > sum(ball for ball in insideHat.values()) :
            alert('Number of balls drawn cannot be greater than the number of balls in the hat')
            numberOfBallsDrawnInput.value = ''
            return
        if numberOfBallsDrawnInput.value == '':
            alert('Please enter the number of balls drawn')
            return
    
    if next == 'startSection':
        reset()
        
        
    
    section = document.getElementById(id)
    section.style.display = "none"
    
    nextElementSection = document.getElementById(next)
    nextElementSection.style.display = "block"   
        

def pressButtons(*args):
    
    document.getElementById('startSectionButton').onclick = lambda *args: nextSection('startSection', 'addSection')
    document.getElementById('addSectionButton').onclick = lambda *args: nextSection('addSection', 'expectedSection')
    document.getElementById('expectedSectionButton').onclick = lambda *args: nextSection('expectedSection', 'drawSection')
    document.getElementById('drawSectionButton').onclick = lambda *args: nextSection('drawSection', 'experimentSection')
    document.getElementById('resetButton').onclick = lambda *args: nextSection('experimentSection', 'startSection')
    
    document.getElementById('addBallLeftArrow').onclick = lambda *args: changeAddBallTypes('left')
    document.getElementById('addBallRightArrow').onclick = lambda *args: changeAddBallTypes('right')
    
    document.getElementById('insideHatButton').onclick = lambda *args: addInsideHat(insideHat)
    
    document.getElementById('expectedBallRightArrow').onclick = lambda *args: changeExpectedBallTypes('right')
    document.getElementById('expectedBallLeftArrow').onclick = lambda *args: changeExpectedBallTypes('left')
        
    document.getElementById('expectedHatButton').onclick = lambda *args: addToExpectedHat(insideHat, expectedHat)
    
    document.getElementById('experimentSectionButton').onclick = lambda *args: calculateExperiments(insideHat, expectedHat)
    
if __name__ == "__main__":
    insideHat: dict[str, int] = {}
    expectedHat: dict[str, int] = {}
    
    addBallTypes = {
        'blue': ['dots', 'horizontal_striped', 'plain' , 'vertical_striped'],
        'cyan': ['dots', 'horizontal_striped', 'plain' , 'vertical_striped'],
        'green': ['dots', 'horizontal_striped', 'plain' , 'vertical_striped'],
        'orange': ['dots', 'horizontal_striped', 'plain' , 'vertical_striped'],
        'pink': ['dots', 'horizontal_striped', 'plain' , 'vertical_striped'],
        'purple': ['dots', 'horizontal_striped', 'plain' , 'vertical_striped'],
        'red': ['dots', 'horizontal_striped', 'plain' , 'vertical_striped'],
        'yellow': ['dots', 'horizontal_striped', 'plain' , 'vertical_striped'],
    }
    
    expectedBallTypes: dict[str, int] = {}
    
    numberOfBallsDrawnInput = document.getElementById('numberOfBallsDrawnInput')
    numberOfExperimentsInput = document.getElementById("numberOfExperimentsInput")
    
    pressButtons()
    
     
    if runFooter := True:
        document.getElementById('footer').textContent = f'© 2020 - {datetime.datetime.now().year} - sericakitty.github.io. All Rights Reserved.'
        runFooter = False
    
   
    

   