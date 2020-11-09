from typing import List
class Agent:
    def __init__(self,list1):
        self.valList = list1
    def value(self,option:int)->float:
        return self.valList[option]

def isParetoImprovement(agents:List[Agent],option1:int,option2:int)->bool:
    answer = True
    for i in agents: 
        if i.value(option1) < i.value(option2):
            answer = False
    return answer

def isParetoOptimal(agents:List[Agent], option: int, allOptions:List[int]) -> bool:
    answer = True
    for i in allOptions:
        if i != option and isParetoImprovement(agents,option,i):
            return False
    return answer

Ami = Agent([1,2,3,4,5])
Tami = Agent([3,1,2,5,4])
Rami = Agent([3,5,5,1,1])

agentList = [Ami, Tami, Rami]
print(isParetoImprovement(agentList,2,1))
print(isParetoOptimal(agentList,0,[0,1,2,3,4]))