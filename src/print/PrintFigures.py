import matplotlib.pyplot as plt
import numpy as np
import random

class PrintFigures:
    
    #10 generate random color
    def getRandomColor(self):
        R = list(range(256))  #np.arange(256)
        B = list(range(256))
        G = list(range(256))
        R = np.array(R)/255.0
        G = np.array(G)/255.0
        B = np.array(B)/255.0
        #print(R)
        random.shuffle(R)   
        random.shuffle(G)
        random.shuffle(B)
        colors = []
        for i in range(256):
            colors.append((R[i], G[i], B[i]))        
        return colors
    
    #生成随机颜色2 指定颜色列表
    def getRandomColor2(self):
        colors =['#008EF5','#99CC00','#7C0050', '#F20404', '#1D6902','#DCAC05', '#02AAF0']   #五种颜色
        #colors =['#FF6D01','#F4003F','#7F00F6', '#1D6902']   #心形图案的三种颜色
        return colors   
 
 
    #生成点的形状
    def getRandomMarker(self):
        markers = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', '8', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']
        #markers = ['*','o','x', 's']   #心形图案的三种图标
        #markers=['D', 'o', 'x', 'v','s']
        random.shuffle(markers) #随机排序
        '''
        (1)marker -- 折点形状
        (2)markeredgecolor 或 mec -- 折点外边颜色
        (3)markeredgewidth 或 mew -- 折点线宽
        (4)markerfacecolor 或 mfc --折点实心颜色
        (5)markerfacecoloralt 或 mfcalt
        (6)markersize 或 ms --折点大小
                      折点形状选择:
        ================    ===============================
        character           description
        ================    ===============================
        ``'-'``             solid line style
        ``'--'``            dashed line style
        ``'-.'``            dash-dot line style
        ``':'``             dotted line style
        ``'.'``             point marker
        ``','``             pixel marker
        ``'o'``             circle marker
        ``'v'``             triangle_down marker
        ``'^'``             triangle_up marker
        ``'<'``             triangle_left marker
        ``'>'``             triangle_right marker
        ``'1'``             tri_down marker
        ``'2'``             tri_up marker
        ``'3'``             tri_left marker
        ``'4'``             tri_right marker
        ``'s'``             square marker
        ``'p'``             pentagon marker
        ``'*'``             star marker
        ``'h'``             hexagon1 marker
        ``'H'``             hexagon2 marker
        ``'+'``             plus marker
        ``'x'``             x marker
        ``'D'``             diamond marker
        ``'d'``             thin_diamond marker
        ``'|'``             vline marker
        ``'_'``             hline marker
        '''
        return markers   
    
    
    #生成点的形状
    def getRandomLineStyle(self):
        ls = ['-','--',':','-.']  #线型
        '''
        -      实线(solid)
        --     短线(dashed)
        -.     短点相间线(dashdot)
                      ：    虚点线(dotted)
        '', ' ', None
        '''
        random.shuffle(ls) #随机排序
        return ls
    
    
    #绘制多条折线图
    # 输入参数:points:数据点集合; length:数据点长度
    def printMultiLine(self, x, ylist, xlabel, ylabel, labels):
        print(x)
        print(ylist)
        colors = self.getRandomColor2()  #获得随机颜色
        markers = self.getRandomMarker() #获得随机形状
        ls = self.getRandomLineStyle()   #获得随机线条样式
        plt.figure()
        for y in ylist:
            plt.plot(x, y, color =  colors[ylist.index(y)%len(colors)], label=labels[ylist.index(y)%len(ls)], marker =  markers[ylist.index(y)%len(markers)],markeredgewidth=3, linewidth=2)
        plt.xlabel(xlabel,fontsize=17)
        plt.ylabel(ylabel, fontsize=17)
        #plt.xlim(0,20)  #设置坐标轴范围
        #plt.ylim(0,5000)  #设置坐标轴范围       
        #xmin, xmax = plt.xlim()   # return the current xlim
        #ymin, ymax = plt.ylim()
        #plt.xlim(xmin=int(xmin* 1.0), xmax=int(xmax *1.1))  #设置坐标轴范围
        #plt.ylim(ymin = int(ymin * 1.0), ymax=int(ymax * 1.1))
        plt.legend(loc = 'upper left', fontsize=17)  #图例及字体大小
        plt.xticks(fontsize=17)  #刻度字体大小 
        plt.yticks(fontsize=17)
        plt.show()
        
        
    #绘制多条折线图
    # 输入参数:points:数据点集合; length:数据点长度
    def printMultiLine2(self, x, ylist, xlabel, ylabel, labels, filename):
        #print(x)
        #print(ylist)
        colors = self.getRandomColor()  #获得随机颜色
        markers = self.getRandomMarker() #获得随机形状
        ls = self.getRandomLineStyle()   #获得随机线条样式
        plt.figure()
        for y in ylist:
            #plt.plot(x, y, color =  colors[ylist.index(y)%len(colors)], label=labels[ylist.index(y)], marker =  markers[ylist.index(y)%len(markers)], markeredgewidth=2, linewidth=1.5)
            plt.plot(x, y, color =  colors[ylist.index(y)%len(colors)], label=labels[ylist.index(y)], marker =  markers[ylist.index(y)%len(markers)], markeredgewidth=1, linewidth=1)
        plt.xlabel(xlabel,fontsize=14)
        plt.ylabel(ylabel, fontsize=14)
        #plt.xlim(0,20)  #设置坐标轴范围
        #plt.ylim(0,5000)  #设置坐标轴范围       
        #xmin, xmax = plt.xlim()   # return the current xlim
        ymin, ymax = plt.ylim()
        #plt.xlim(xmin=int(xmin* 1.0), xmax=int(xmax *1.1))  #设置坐标轴范围
        plt.ylim(ymin = int(ymin * 1.0), ymax=int(ymax * 1.1))
        #plt.legend(loc = 'upper right', fontsize=10, ncol=3)  #图例及字体大小
        #plt.legend(loc = 'upper right', fontsize=10, ncol=5)  #图例及字体大小
        plt.xticks(fontsize=14)  #17刻度字体大小 
        plt.xticks(range(len(x)))  #连续数字
        #xtick = [i for i in range(len(x)) if (i % 10 ==0)]
        xtick = [i for i in range(len(x)) if (i % 5 ==0)]
        plt.xticks(xtick)
        plt.yticks(fontsize=14)
        #plt.savefig('../results/'+filename+'.png')
        plt.show()    
        
        
    #绘制多条折线图
    # 输入参数:points:数据点集合; length:数据点长度
    def printMultiLine3(self, x, ylist, xlabel, ylabel, labels, filename):
        #print(x)
        #print(ylist)
        colors = self.getRandomColor2()  #获得随机颜色
        markers = self.getRandomMarker() #获得随机形状
        ls = self.getRandomLineStyle()   #获得随机线条样式
        plt.figure()
        for y in ylist:
            plt.plot(x, y, color =  colors[ylist.index(y)%len(colors)], label=labels[ylist.index(y)], marker =  markers[ylist.index(y)%len(markers)], markeredgewidth=3, linewidth=2)
        plt.xlabel(xlabel,fontsize=17)
        plt.ylabel(ylabel, fontsize=17)
        #plt.xlim(0,20)  #设置坐标轴范围
        #plt.ylim(0,5000)  #设置坐标轴范围       
        #xmin, xmax = plt.xlim()   # return the current xlim
        ymin, ymax = plt.ylim()
        #plt.xlim(xmin=int(xmin* 1.0), xmax=int(xmax *1.1))  #设置坐标轴范围
        plt.ylim(ymin = int(ymin * 1.0), ymax=int(ymax * 1.1))
        plt.legend(loc = 'upper right', fontsize=13, ncol=3)  #图例及字体大小
        plt.xticks(fontsize=17)  #刻度字体大小 
        plt.xticks(range(len(x)))
        plt.yticks(fontsize=17)
        plt.savefig('../results/'+filename+'.png')
        #plt.show()    
        
        
       