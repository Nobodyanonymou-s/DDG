#COG with dynamic game strategy
 
from util.GameBase import GameBase
import random


class COGAlgorithm:
    def __init__(self, mec, bs):
        self.gb= GameBase(mec,bs)
        self.QTable={}
    

    def initialGame(self, n, UEList):        
        initialpolicy = self.gb.initialRandomPolicy(n)
        overheadList, _, energyconList = self.gb.getOverheadByPolicy(initialpolicy, UEList)
        policyname = str(initialpolicy).replace('[','').replace(',','').replace(']','') 
        self.QTable[policyname]=energyconList
        print("initial COPC:", initialpolicy, ", cost:", overheadList)
        return initialpolicy, overheadList
    
    
    #Start the game iteration
    def gameIteration(self, nlist, currentPolicy, currentOverHead, UEList):
        overHeadList=[]  
        optimizedPolicy=None
        optimizedOverHead =0 
        iteration=0
        allcount=0
        while True:
            iteration  += 1
            print("The ", iteration, "-th game iteration")
            
            id_list = random.sample(range(len(nlist)), len(nlist))
            currentPolicy1=currentPolicy.copy()
            currentOverHead1= currentOverHead 
            overheadList=[]
            print("current COPC:", currentPolicy1, ", cost:",currentOverHead1)
            for id in id_list: 
                uts = nlist[id]  
                subpolicy = self.gb.createPolicySpace(uts)   
                ue_begin= sum(nlist[0:id]) 
                ue_end = sum(nlist[0:id])+uts 
                for subp in subpolicy:                    
                    newpolicy = currentPolicy1.copy()
                    newpolicy[ue_begin: ue_end] = subp                     
                    policyname = str(newpolicy).replace('[','').replace(',','').replace(']','')      
                    if policyname in self.QTable:
                        overhead = self.QTable[policyname]
                    else:
                        allcount +=1
                        overhead, _, _ = self.gb.getOverheadByPolicy(newpolicy, UEList)  
                    print("local COPC:", newpolicy, ", cost:",overhead)
                    if(overhead[id] < currentOverHead1[id]): 
                        currentPolicy1 = newpolicy
                        currentOverHead1 = overhead
                
                print("current COPC:", currentPolicy1, ",cost:",currentOverHead1)
                policyname = str(currentPolicy1).replace('[','').replace(',','').replace(']','')
                overheadList.append([policyname ,currentOverHead1])  
                overHeadList.append(currentOverHead1)
                self.QTable[policyname]=currentOverHead1   
                
            #Determine whether NE is reached
            isNE=True
            for i in range(len(overheadList)-1):
                if overheadList[i] != overheadList[i+1]:
                    isNE = False
                    break
            
            if isNE == True:                
                print("Achieve NE solution!")                
                print("Final COPC:", currentPolicy1, ", cost:",currentOverHead1)
                optimizedPolicy = currentPolicy1
                optimizedOverHead = currentOverHead1
                break
            else:   
                currentPolicy, currentOverHead = currentPolicy1, currentOverHead1    
        
        print("Number of game iterations: ", iteration )
        print("Number of COPC policies: ", allcount)                     
        return  optimizedPolicy, optimizedOverHead, overHeadList        
                    