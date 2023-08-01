#Calculating communication overhead
import numpy as np

class CommunicationUtil:
    
    #signal interference to noise ratio
    def getSINR (self, ue, bs, UEList):
        p_k = bs.p_up[ue.channelid] * np.sqrt(ue.QoE+1)   
        i_k =  self.getinterference(ue, bs, UEList)
        sinr = (p_k * ue.transmitgain) / (bs.noisepower + i_k)
        return sinr
    
    
    #Calculating the interference of the current UE and UEs of other BSs on channel k
    def getinterference(self, ue, bs, UEList):
        p_k = bs.p_up[ue.channelid]  #Get the transmission power of channel k  
        i_k=0
        for ue2 in UEList:
            if (ue2.channelid == ue.channelid and ue2.bsid != ue.bsid):
                i_k += p_k *np.sqrt(ue2.QoE+1) * ue2.transmitgain
        return i_k       
    
    
    #Calculating the transmission rate
    def getr_up(self, ue, bs, UEList): 
        sinr = self.getSINR(ue,bs, UEList)
        r_up = bs.bandwidth[ue.channelid] * np.log2( 1 + sinr)
        return r_up 