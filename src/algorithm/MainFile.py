#绘制出随着用户数量增加,能耗的对比
#对比算法:EA算法,动态博弈,静态博弈
from entity.MECServer import MECServer
from entity.BS import BS
from entity.UserEquipment import UETools
from algorithm.COG import COGAlgorithm
from print.PrintFigures import PrintFigures


def createCompareList():
    mec = MECServer()   
    bs = BS()         
    uetool = UETools()
    #caseList=[20,40,60,80,100,120,140] 
    caseList=[20] 
    for n in caseList:       
        Z_DynamicGame=[]  
        UEList = uetool.create_UETasks(n, bs.BS, bs.Channel, max_t=2)
        n, nlist= uetool.getTaskNum(UEList)  
            
        cog = COGAlgorithm(mec, bs)                       
        initialpolicy, overhead = cog.initialGame(n, UEList)  
        _, z_dg, _ = cog.gameIteration(nlist, initialpolicy, overhead, UEList)
                
createCompareList()