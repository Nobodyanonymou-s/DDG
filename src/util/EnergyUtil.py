#Calculating the energy consumption of a single task
from util.CommunicationUtil import CommunicationUtil

class EnergyUtil:
    
    #Calculate the energy consumption for a local task
    def energy_task_local(self, task, ue):        
        e_local = task.computingsize *ue.wi
        return e_local
    
    #Calculate the time consumption for a local task
    def time_task_local(self, task, ue):        
        t_local = task.computingsize  / ue.fi
        return t_local


    #Calculate the time consumption for an offload task
    def time_task_offload(self, task, ue, mec, bs, UEList):        
        t_mec = task.computingsize / mec.fs[ue.QoE]
        cutil = CommunicationUtil()
        r_up = cutil.getr_up(ue, bs, UEList)
        t_up = task.datasize / r_up   #Transmission time of the task in the uplink segment
        t_bh=0  #Transmission time of the task in the backhaul segment
        if(ue.bsid>0):  
            t_bh = task.datasize / bs.r_bh[ue.QoE]
        t_offload = t_up + t_bh + t_mec   #Waiting time for task offloading       
        return t_offload
            
    
    #Calculate the energy consumption for an offload task
    def energy_task_offload(self, task, ue, mec, bs, UEList):        
        t_offload = self.time_task_offload(task, ue, mec, bs, UEList)         
        e_wait = t_offload * ue.w0 
        e_trans_up = task.datasize * bs.u_up[ue.channelid] * pow(ue.QoE+1,1/3)
        e_trans_bh = 0
        if(ue.bsid>0):  
            e_trans_bh = task.datasize * bs.u_bh[ue.QoE]
        e_mec= task.computingsize * mec.us[ue.QoE]  
        e_offload = e_wait + e_trans_up + e_trans_bh + e_mec        
        return e_offload
        
        
    def task_energy_time(self, task, ue, mec, bs, UEList):        
        e_local = 0.0 if task.ai==1 else self.energy_task_local(task, ue)
        e_offload =0.0 if task.ai==0 else  self.energy_task_offload(task, ue, mec, bs, UEList)
        t_local = 0.0 if task.ai==1 else self.time_task_local(task, ue)
        t_offload = 0.0 if task.ai ==0 else self.time_task_offload(task, ue, mec, bs,UEList)
        return t_local, t_offload, e_local, e_offload


    def getAllTaskEnergy(self, t, UEList, mec, bs):
        E_list =[]
        for ue in UEList:
            e_local, e_offload = self.energy_ue(t, ue, mec, bs)
            if(e_local != 0 or e_offload != 0):
                E_list.append([ue.uid, e_local, e_offload])
        return E_list