from entity.MECServer import MECServer
from entity.BS import BS
from entity.UserEquipment import UETools
from util.EnergyUtil import EnergyUtil
from util.GameBase import GameBase


import numpy as np
import matplotlib.pyplot as plt

class PrintBar:
    
    #初始化决策方案
    def getAll_local_offload(self, UEList, mec, bs):
        gb= GameBase(mec,bs)
        n= gb.getTaskNum(UEList)  #获取所有任务数量
        policylist = gb.createPolicySpace(n) #创建所有的方案组合
                        
        policy = policylist[len(policylist)-1]  #全卸载执行  
        gb.updateTasksStatesByPolicy(policy, UEList) #根据当前卸载方案组合,修改各个任务的状态 
        
        euitl = EnergyUtil()
        T_Local=[]
        T_Up=[]
        T_Bh=[]
        T_Mec=[]
        T_Offload=[]
        
        E_Local=[]
        E_Wait=[]
        E_Up=[]
        E_Bh=[]
        E_Mec=[]
        E_Offload=[]
        
        T_Local_Pre=[]  #本地时间开销(*偏好)
        E_Local_Pre=[]  #本地能耗(*偏好)
        T_Offload_Pre=[] #卸载时间开销(*偏好)
        E_Offload_Pre=[] #卸载能耗(*偏好)
        for ue in UEList:
            for task in ue.tasklist:
                task.printTask()
                t_local, t_up, t_bh, t_mec, t_offload =  euitl.time_task_offload2(task, ue, mec, bs, UEList)            
                
                e_local, e_wait, e_up, e_bh, e_mec, e_offload =  euitl.energy_task_offload2(task, ue, mec, bs, UEList)
                
                E_Local_Pre.append(e_local * task.preference)
                T_Local_Pre.append(t_local * (1-task.preference))
                E_Offload_Pre.append(e_offload * task.preference)
                T_Offload_Pre.append(t_offload * (1-task.preference))
                
                T_Local.append(t_local)                
                T_Up.append(t_up)
                T_Bh.append(t_bh)
                T_Mec.append(t_mec)
                T_Offload.append(t_offload)
                
                E_Local.append(e_local)
                E_Wait.append(e_wait)
                E_Up.append(e_up)
                E_Bh.append(e_bh)
                E_Mec.append(e_mec)
                E_Offload.append(e_offload)
        
        
        print("--------------Time consumption--------------")
        print("T_Local:", T_Local)
        print("T_Up:", T_Up)
        print("T_Bh:", T_Bh)
        print("T_Mec:", T_Mec)
        #for i in range(n):
        #    print("-------------")
        #    print("t_local:", T_Local[i])
        #    print("t_trans_up:", T_Up[i])
        #    print("t_trans_bh:", T_Bh[i])
        #    print("t_mec:", T_Mec[i])
        #    print("t_offload:", T_Offload[i])
            
        self.printBar_Time(n, T_Local, T_Up, T_Bh, T_Mec )        
        
        print("--------------Energy consumption--------------")
        print("E_Local:", E_Local)
        print("E_Wait:", E_Wait)
        print("E_Up:", E_Up)
        print("E_Bh:", E_Bh)
        print("E_Mec:", E_Mec)
        #for i in range(n):
        #    print("-------------")
        #    print("e_local:", E_Local[i])
        #    print("e_wait:", E_Wait[i])
        #    print("e_up:", E_Up[i])
        #    print("e_bh:", E_Bh[i])
        #    print("e_mec:", E_Mec[i])
        #    print("e_offload:", E_Offload[i])
            
                
        self.printBar_Energy(n, E_Local, E_Wait, E_Up, E_Bh, E_Mec )   
        
        
        print("--------------Overhead--------------")
        print("E_Local_Pre:", E_Local_Pre)
        print("E_Offload_Pre:",E_Offload_Pre)
        print("T_Local_Pre:",T_Local_Pre)
        print("T_Offload_Pre:",T_Offload_Pre)
        #for i in range(n):
        #    print("-------------")
        #    print("e_local_pre:", E_Local_Pre[i])
        #    print("e_offload_pre:", E_Offload_Pre[i])
        #    print("t_local_pre:", T_Local_Pre[i])
        #    print("t_offload_pre:", T_Offload_Pre[i])            
                
        self.printBar_Overhead(n, E_Local_Pre, E_Offload_Pre, T_Local_Pre, T_Offload_Pre)      
        
  
    #绘制柱状图(时间)
    def printBar_Time(self, N, T_Local, T_Up, T_Bh, T_Mec ):
        v = list(map(lambda x: x[0]+x[1], zip(T_Bh, T_Up)))  #两个相加,T_MEc再叠加
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        
        p1 = plt.bar(ind, T_Local, width, color='#02AAF0')
        p2 = plt.bar(ind+width, T_Mec, width, color='#A7D603', bottom=v)
        p3 = plt.bar(ind+width, T_Bh, width, color='#DCAC05', bottom=T_Up)
        p4 = plt.bar(ind+width, T_Up, width, color='#B676DF')
        
        
        plt.ylabel('Time consumption',fontsize=18)
        plt.xlabel('Computing tasks',fontsize=18)
        plt.xticks(ind + width/2., (ind),fontsize=18)
        plt.yticks(np.arange(0, 110,10), fontsize=18)
        plt.legend((p1[0], p2[0],p3[0],p4[0]), ('T - Local', 'T - MEC', 'T - Backhaul', 'T - Uplink'),fontsize=18, ncol=2)
        plt.show()


    #绘制柱状图(能耗)
    def printBar_Energy(self, N, E_Local, E_Wait, E_Up, E_Bh, E_Mec ):
        v1 = list(map(lambda x: x[0]+x[1], zip(E_Wait, E_Up)))
        v2 = list(map(lambda x: x[0]+x[1], zip(v1, E_Bh)))
        
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        
        p1 = plt.bar(ind, E_Local, width, color='#02AAF0')
        p5 = plt.bar(ind+width, E_Wait, width, color='#F64304')
        p4 = plt.bar(ind+width, E_Up, width, color='#B676DF', bottom=E_Wait)
        p3 = plt.bar(ind+width, E_Bh, width, color='#DCAC05', bottom=v1)
        p2 = plt.bar(ind+width, E_Mec, width, color='#A7D603', bottom=v2)
        
        plt.ylabel('Energy consumption',fontsize=18)
        plt.xlabel('Computing tasks',fontsize=18)
        plt.xticks(ind + width/2., (ind),fontsize=18)
        plt.yticks(np.arange(0, 120,10), fontsize=18)
        plt.legend((p1[0], p2[0],p3[0],p4[0], p5[0]), ('E - Local',  'E - MEC', 'E - Backhaul', 'E - Uplink', 'E - Wait'),fontsize=18,loc='upper center', ncol=2)
        plt.show()


    #绘制柱状图(综合)
    def printBar_Overhead(self, N, E_Local_Pre, E_Offload_Pre, T_Local_Pre, T_Offload_Pre):
        ind = np.arange(N)    # the x locations for the groups
        width = 0.35       # the width of the bars: can also be len(x) sequence
        
        p1 = plt.bar(ind, T_Local_Pre, width, color='#0154BB')
        p2 = plt.bar(ind, E_Local_Pre, width, color='#02AAF0', bottom = T_Local_Pre)
        p3 = plt.bar(ind+width, T_Offload_Pre, width, color='#5D8801')
        p4 = plt.bar(ind+width, E_Offload_Pre, width, color='#A7D603', bottom=T_Offload_Pre)
        
        plt.ylabel('Computation overhead', fontsize=18)
        plt.xlabel('Computing tasks',fontsize=18)
        plt.xticks(ind + width/2., (ind), fontsize=18)
        plt.yticks(np.arange(0, 100,10), fontsize=18)
        plt.legend((p1[0], p2[0],p3[0],p4[0]), ('T - Local',  'E - Local', 'T - Offload', 'E - Offload'),fontsize=18, ncol=2)
        plt.show()

if __name__ == '__main__':
    
    #(1) 生成环境变量
    mec = MECServer()     #创建MEC服务器 (服务等级为5级)
    mec.printMEC()
    
    bs = BS() #创建BS基站列表和Channel信道列表
    bs.printBS_Channel()
    
    #(2) 创建用户终端及任务
    uetool = UETools()
    n_UE=5
    max_t = 2
    UEList = uetool.create_UETasks(n_UE, bs.BS, bs.Channel, max_t)
    uetool.printUEList(UEList)  #打印UE列表
    
    pb = PrintBar()    
    pb.getAll_local_offload(UEList, mec, bs)