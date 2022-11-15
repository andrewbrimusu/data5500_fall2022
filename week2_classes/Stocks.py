class Stocks(object):

    def __init__(self, start, end):
        self.startDate = start
        self.endDate = end

        #init stock sectors and other variables
        self.numAgents = 7
        self.numHighAgents = 2
        self.sectorsTxt = ['it','energy','financials','industrials','healthcare','consumerdisc','consumerstaples']
        self.it = ['CTSH','ADP','PYPL','YHOO','AVGO','EBAY','BRCM','GLW','MU','VMW']
        self.energy = ['PSX','APC','HAL','WMB','VLO','MPC','BHI','SE','DVN','APA']
        self.financials = ['CB','MMC','BBT','CME','STT','EQR','AFL','ALL','DFS','BEN']
        self.industrials = ['PCP','EMR','AAL','CSX','DE','ITW','ETN','NSC','WM','CMI']
        self.healthcare = ['SYK','BDX','HUM','VRTX','CAH','HCA','ILMN','BAX','MYL','BXLT']
        self.consumerdisc = ['CMCSK','TSLA','CBS','CCL','LVS','VIAB','FOX','TRI','DISH','VIA']
        self.consumerstaples = ['MDLZ','COST','CL','KHC','KMB','RAI','KR','GIS','ADM','EL']
        self.sectors = [self.it,self.energy,self.financials,self.industrials,self.healthcare,self.consumerdisc,self.consumerstaples]

        self.agentGetPricesRef=agentGetPricesRef