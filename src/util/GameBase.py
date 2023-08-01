from util.EnergyUtil import EnergyUtil
import random

class GameBase:
    def __init__(self, mec, bs):
        self.mec = mec
        self.bs = bs
    
    
    def createPolicySpace(self, n):       
        n_policy = pow(2,n)       
        policylist=[]
        for i in range(n_policy):
            i2 =('{0:0'+str(n)+'b}').format(i) 
            i3 = [int( i2[item: item+1] ) for item in range(0, len(i2), 1)]
            policylist.append(i3)
        return policylist
    

    def initialRandomPolicy(self,n):
        n2 = random.randint(0,n-1)
        i2 =('{0:0'+str(n)+'b}').format(n2) 
        policy = [int( i2[item: item+1] ) for item in range(0, len(i2), 1)]
        return policy
    
            
    def updateTasksStatesByPolicy(self,policy, UEList):  
        i=0
        for ue in UEList:
            isoffload = False  
            for task in ue.tasklist:
                task.ai=policy[i]  
                i =i+1 
                if task.ai == 1:
                    isoffload=True
                    ue.channelid=ue.tempchannelid 
            if(isoffload==False):
                ue.channelid=-1
                        
    def getOverheadByPolicy(self, policy, UEList):
        self.updateTasksStatesByPolicy(policy, UEList)  
        euitl = EnergyUtil()
        overheadList=[]  
        timeconList=[]   
        energyconList=[] 
        for ue in UEList:
            overhead=0  
            timecon=0  
            energycon=0 
            for task in ue.tasklist:
                t_local, t_offload, e_local, e_offload =  euitl.task_energy_time(task, ue, self.mec, self.bs, UEList)            
                if task.ai==0:
                    timecon += t_local
                    energycon += e_local
                    overhead += (task.preference * e_local)  + ((1-task.preference) * t_local)
                else:     
                    timecon += t_offload
                    energycon += e_offload
                    overhead += (task.preference * e_offload)  + ((1-task.preference) * t_offload)
            overheadList.append(overhead)
            timeconList.append(timecon)
            energyconList.append(energycon)        
        return overheadList, timeconList, energyconList            