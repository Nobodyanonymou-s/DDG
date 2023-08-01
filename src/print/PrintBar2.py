from entity.MECServer import MECServer
from entity.BS import BS
from entity.UserEquipment import UE,Task
from entity.UserEquipment import UETools
from util.EnergyUtil import EnergyUtil
from util.GameBase import GameBase


import numpy as np
import matplotlib.pyplot as plt

class PrintBar:
    
    def create_UETasks(self):
        #创建UE0        
        ue0 = UE()
        ue0.uid = 0
        ue0.bsid = 1 #SBS1
        ue0.channelid=0
        ue0.tempchannelid=ue0.channelid #临时
        ue0.transmitgain = 0.15  #用户与基站之间的信道增益
        ue0.QoE=3
        ue0.fi = 2.34
        ue0.wi = 0.55  
        ue0.w0 = 0.15
        
        
        task0 = Task(0)
        task0.tid = 0      
        task0.computingsize = 172.45  
        task0.datasize = 28.28      
        task0.preference = 0.24     #偏好
        task0.ai = 1   
        
        task1 = Task(1)
        task1.tid = 1
        task1.computingsize = 119.73
        task1.datasize = 55.23
        task1.preference = 0.31
        task1.ai = 1
        ue0.tasklist=[task0, task1]
        
        
        #创建UE1
        ue1 = UE()
        ue1.uid = 1
        ue1.bsid = 3 #SBS1
        ue1.channelid=0
        ue1.tempchannelid=ue1.channelid #临时
        ue1.transmitgain = 0.15  #用户与基站之间的信道增益
        ue1.QoE=0
        ue1.fi = 2.34
        ue1.wi = 0.55 
        ue1.w0 = 0.17
        
        
        task2 = Task(2)
        task2.tid = 2      
        task2.computingsize = 172.45  
        task2.datasize = 28.28       
        task2.preference = 0.24 
        task2.ai = 1    
        
        task3 = Task(3)
        task3.tid = 3
        task3.computingsize = 60.35
        task3.datasize = 34.25
        task3.preference = 0.32
        task3.ai = 1
        ue1.tasklist=[task2, task3]
        
        
        #创建UE2
        ue2 = UE()
        ue2.uid = 2
        ue2.bsid = 0 
        ue2.channelid=1
        ue2.tempchannelid=ue2.channelid #临时
        ue2.transmitgain = 0.15
        ue2.QoE=0
        ue2.fi = 2.30
        ue2.wi = 0.62  
        ue2.w0 = 0.17
        
        
        task4 = Task(4)
        task4.tid = 4      
        task4.computingsize = 149.61  
        task4.datasize = 98.81      
        task4.preference = 0.48
        task4.ai = 1 
        ue2.tasklist=[task4]   
        
        
        #创建UE3
        ue3 = UE()
        ue3.uid = 3
        ue3.bsid = 2 
        ue3.channelid=2
        ue3.tempchannelid=ue3.channelid #临时
        ue3.transmitgain = 0.15
        ue3.QoE=3
        ue3.fi = 1.64
        ue3.wi = 0.95  
        ue3.w0 = 0.26
        
        
        task5 = Task(5)
        task5.tid = 5
        task5.computingsize = 43.16
        task5.datasize = 106.84
        task5.preference = 0.68
        task5.ai = 1
        ue3.tasklist=[task5]
        
        
        #创建UE4
        ue4 = UE()
        ue4.uid = 4
        ue4.bsid = 1
        ue4.channelid=0
        ue4.tempchannelid=ue4.channelid #临时
        ue4.transmitgain = 0.15
        ue4.QoE=2
        ue4.fi = 1.90
        ue4.wi = 0.96  
        ue4.w0 = 0.19                
        
        task6 = Task(6)
        task6.tid = 6     
        task6.computingsize = 33.01  
        task6.datasize = 131.82      
        task6.preference = 0.57
        task6.ai = 1    
            
        task7 = Task(7)
        task7.tid = 7
        task7.computingsize = 56.03
        task7.datasize = 167.48
        task7.preference = 0.62
        task7.ai = 1
        ue4.tasklist=[task6, task7]
        
        
        #创建UE5
        ue5 = UE()
        ue5.uid = 5
        ue5.bsid = 0 
        ue5.channelid=0
        ue5.tempchannelid=ue5.channelid #临时
        ue5.transmitgain = 0.15
        ue5.QoE=1
        ue5.fi = 1.40
        ue5.wi = 0.86  
        ue5.w0 = 0.14        
        
        task8 = Task(8)
        task8.tid = 8      
        task8.computingsize = 62.74  
        task8.datasize = 142.02      
        task8.preference = 0.63
        task8.ai = 1    
        ue5.tasklist=[task8]
        
        
        #创建UE6
        ue6 = UE()
        ue6.uid = 6
        ue6.bsid = 3
        ue6.channelid=1
        ue6.tempchannelid=ue6.channelid #临时
        ue6.transmitgain = 0.15
        ue6.QoE= 0
        ue6.fi = 1.67
        ue6.wi = 0.78  
        ue6.w0 = 0.16
        
        task9 = Task(9)
        task9.tid = 9
        task9.computingsize = 61.22
        task9.datasize = 139.24
        task9.preference = 0.69
        task9.ai = 1
        ue6.tasklist=[task9]
        
        UEList = [ue0, ue1, ue2, ue3, ue4, ue5, ue6]
        return UEList   
    
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
        
    def getData(self):
        n=10
        #--------------Time consumption--------------
        T_Local = [59.13, 73.23, 47.37, 28.15, 58.30, 36.97, 43.54, 45.12, 50.93, 44.70]
        T_Up    = [13.29, 10.94,  3.13,  3.49,  4.75,  3.28,  4.44,  4.68,  8.40,  6.43]
        T_Bh    = [ 6.55,  7.68,  3.83,  4.28,  0.00,  3.05,  4.07,  4.29,  0.00,  5.56]
        T_Mec   = [18.98, 25.89, 14.12,  8.39, 14.23,  9.02, 16.60, 17.20, 13.94, 12.24]
        self.printBar_Time(n, T_Local, T_Up, T_Bh, T_Mec ) 
        
        #--------------Energy consumption--------------
        E_Local = [35.51, 43.98, 60.64, 36.03, 68.08, 43.17, 63.29, 65.59, 38.20, 33.53]
        E_Wait  = [ 6.22,  6.80,  3.77,  2.89,  4.00,  2.62,  4.78,  4.99,  4.05,  3.32]
        E_Up    = [19.24, 17.28, 27.35, 30.53, 39.75, 27.40, 22.02, 23.25, 39.37, 30.12]
        E_Bh    = [ 3.84,  3.45, 11.23, 11.23,  0.00,  6.36,  8.18,  8.74,  0.00,  7.92]
        E_Mec   = [ 9.78, 12.11, 19.06, 11.33, 24.40, 15.47, 16.60, 17.20, 13.94, 12.24]
        self.printBar_Energy(n, E_Local, E_Wait, E_Up, E_Bh, E_Mec )  
        
        #--------------Overhead--------------
        Pre = [0.54, 0.61, 0.59, 0.62, 0.58, 0.68, 0.57, 0.6, 0.62, 0.69]
        E_Local_Pre = list(map(lambda x: x[0] * x[1], zip(E_Local, Pre)))
        
        E_Offload_Pre = list(map(lambda x: x[0] + x[1], zip(E_Wait, E_Up)))
        E_Offload_Pre = list(map(lambda x: x[0] + x[1], zip(E_Offload_Pre, E_Bh)))
        E_Offload_Pre = list(map(lambda x: x[0] + x[1], zip(E_Offload_Pre, E_Mec)))
        E_Offload_Pre = list(map(lambda x: x[0] * x[1], zip(E_Offload_Pre, Pre)))
        
        T_Local_Pre = list(map(lambda x: x[0] * (1-x[1]), zip(T_Local, Pre)))
        
        T_Offload_Pre = list(map(lambda x: x[0] + x[1], zip(T_Up, T_Bh)))
        T_Offload_Pre = list(map(lambda x: x[0] + x[1], zip(T_Offload_Pre, T_Mec)))
        T_Offload_Pre = list(map(lambda x: x[0] * x[1], zip(T_Offload_Pre, Pre)))
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
        plt.yticks(np.arange(0, 160,10), fontsize=18)
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
        plt.yticks(np.arange(0, 120,10), fontsize=18)
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
    #UEList =  uetool.create_UETasks(n_UE, bs.BS, bs.Channel, max_t)
    #uetool.printUEList(UEList)  #打印UE列表
    
    #(1) 穷举算法
    print("--------------------------穷举博弈----------------------------")
    pb = PrintBar()
    pb.getData()
    #UEList = pb.create_UETasks()    
    #pb.getAll_local_offload(UEList, mec, bs)
    