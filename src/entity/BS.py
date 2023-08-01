#Base stations (BS) 
#including MBS, SBS, Channel
class BS:    
    #Initialization 
    def __init__(self):
        self.BS= ['MBS', 'SBS1', 'SBS2', 'SBS3']
        self.Channel =['C0','C1','C2','C3']
          
        #Transmission rate and cost of uplink (between UE and SBS/MBS) 
        self.p_up = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500] 
        self.u_up = [0.15, 0.20, 0.30, 0.35, 0.55, 0.65, 0.74, 0.85, 0.95, 1.0] #Transmission cost
        
        #Transmission rate and cost of backhaul (between SBS and MBS)
        self.r_bh = [35, 40, 45, 50, 55]
        self.u_bh = [0.03, 0.07, 0.10, 0.15, 0.20] 
        
        self.noisepower= 254 #Channel noise
        self.bandwidth = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] #Channel bandwidth 