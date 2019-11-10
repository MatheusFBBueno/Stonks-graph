import json
import requests
import matplotlib.pyplot as plt
import time

total=0
data={'ABEV':None,'VALE':None,'TTWO':None,'WEGE':None}
sma={'ABEV':None,'VALE':None,'TTWO':None,'WEGE':None}
def graph():
    global total
    global data
    global sma

    atual=[data['ABEV'].json(),data["VALE"].json(),data['TTWO'].json(),data['WEGE'].json()]
    sma_atual=[sma['ABEV'].json(),sma["VALE"].json(),sma['TTWO'].json(),sma['WEGE'].json()]
            
    #fechamento
    for i  in range(len(atual)):
        timeseries=atual[i]["Time Series (5min)"]
        close= [float(item["4. close"]) for item in timeseries.values()]
        
        ativo=''
        if i==0:
            ativo='ABEV'
        elif i==1:
            ativo="VALE"
        elif i==2:
            ativo="TTWO"
        else:
            ativo="WEGE"

        valores=[]

        for i in range(len(close)):
            valores.append(i)
    
    #volume    
    for i  in range(len(atual)):
        timeseries=atual[i]["Time Series (5min)"]
        close= [float(item["5. volume"]) for item in timeseries.values()]
        
        ativo=''
        if i==0:
            ativo='ABEV'
        elif i==1:
            ativo="VALE"
        elif i==2:
            ativo="TTWO"
        else:
            ativo="WEGE"

        valores=[]

        for i in range(len(close)):
            valores.append(i)
            
        plt.plot(valores,close[::-1])
        plt.savefig("images/"+ativo+'_volume'+str(total)+'.png')
        plt.close()
    #media movel simples
    for i in range(len(sma_atual)):
        timeseries=sma_atual[i]["Technical Analysis: SMA"]
        close= [float(dado["SMA"]) for dado in timeseries.values()]
        
        ativo=''
        if i==0:
            ativo='ABEV'
        elif i==1:
            ativo="VALE"
        elif i==2:
            ativo="TTWO"
        else:
            ativo="WEGE"

        valores=[]

        for i in range(len(close)):
            valores.append(i)
            
        plt.plot(valores,close[::-1])
        plt.savefig("images/"+ativo+'_sma'+str(total)+'.png')
        plt.close()
    
    total+=1
#funçoes que realizam as requisições, executam uma pausa para não passar o limite do alpha vantage
def req_abev():
    global data
    global sma
    data['ABEV']= requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=ABEV3.SA&interval=5min&apikey=G6IBSDLXJ0V0KXQW")
    sma["ABEV"]= requests.get("https://www.alphavantage.co/query?function=SMA&symbol=ABEV3.SA&interval=5min&time_period=10&series_type=close&apikey=G6IBSDLXJ0V0KXQW")
    time.sleep(50)
def req_vale():
    global data
    global sma
    data["VALE"]= requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=VALE3.SA&interval=5min&apikey=18947984687123")
    sma["VALE"]= requests.get("https://www.alphavantage.co/query?function=SMA&symbol=VALE3.SA&interval=5min&time_period=10&series_type=close&apikey=419874984189541")
    time.sleep(50)
def req_ttwo():
    global data
    global sma
    data["TTWO"]=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TTWO&interval=5min&apikey=129849840984984984")
    sma["TTWO"]= requests.get("https://www.alphavantage.co/query?function=SMA&symbol=TTWO&interval=5min&time_period=10&series_type=close&apikey=132186498749849")
    time.sleep(50)
def req_wege():
    global data
    global sma
    data["WEGE"]=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=WEGE3.SA&interval=5min&apikey=2321684684818")
    sma["WEGE"]=requests.get("https://www.alphavantage.co/query?function=SMA&symbol=WEGE3.SA&interval=5min&time_period=10&series_type=close&apikey=98098406941965481")
    time.sleep(50)

while True:
    req_ttwo()
    req_vale()
    req_wege()
    req_abev()
    graph()
    time.sleep(60)#pausa para fechar 5 minutos