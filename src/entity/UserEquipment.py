#User Equipment (UE)
import random
        
class UE:         
        
    #Create a UE object
    def initUE(self, uid, BSlist, ChannelList):
        self.uid = uid   
        self.bsid = random.randint(0,len(BSlist)-1) 
        self.channelid=random.randint(0,len(ChannelList)-1)
        self.tempchannelid=self.channelid 
        self.transmitgain = random.uniform(0.01, 1.0)  #Channel gain between UE and BS
        self.QoE=random.randint(0,5-1)   #QoE
        self.fi = random.uniform(1.1, 2.5)  #Local computation power
        self.wi = self.fi * 0.3  #local energy cost
        self.w0 = self.fi*0.1  #local energy cost in idle status
        self.tasklist=[]       #List of computation tasks



class Task:
    
    def __init__(self, id):
        self.tid = id      
        self.computingsize = random.uniform(50,200)  #amount of computation 
        self.datasize = random.uniform(50,200)      #amount of input dataset
        self.preference = random.uniform(0.3,0.7)      #preference between energy consumption and computation delay, 0.5-1: energy consumption, 0-0.5: computation latency
        self.ai = 0     #offloading policy (0,1)
    
      
class UETools:
    
    #create UE and tasks
    #n_UE: number of UEs, max_t: Maximum number of tasks per UE
    def create_UETasks(self, n_UE, BSlist, ChannelList, max_t):
        #create UE
        UEList = []
        for i in range(n_UE):  
            ue = UE()
            ue.initUE(i, BSlist, ChannelList)
            UEList.append(ue) 
        
        #Randomly create tasks list for each user
        for ue in UEList:
            n_task =random.randint(1,max_t) 
            ue.tasklist = self.createTaskList(n_task, max_t)
        return UEList    
    
    
    #Create tasks list for each user
    def createTaskList(self, n_task, max_t):            
        Tasklist=[]
        id_list = random.sample(range(max_t), n_task)
        id_list.sort()
        for id in id_list:
            task = Task(id)
            Tasklist.append(task)
        return Tasklist    
                 
            
    def getTaskNum(self,UEList):
        nlist=[]
        n=0
        for ue in UEList:
            n += len(ue.tasklist)
            nlist.append(len(ue.tasklist))
        return n, nlist
    
    
    def getTaskrange(self, nlist, UEid):
        start = sum (nlist[0:UEid])
        end =start + nlist[UEid]
        return start, end
                