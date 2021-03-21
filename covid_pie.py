import tkinter as tk
from tkinter import ttk
import matplotlib.pylab as plt
import numpy as np
import json
import urllib.request as req
url='https://api.rootnet.in/covid19-in/stats/history'
rep=req.urlopen(url).read().decode()
info=json.loads(rep)

def onclick():
    x=[]
    y=[]
    z=[]
    a=[]
    if str(state.get())=='India':
        for i in range(len(info['data'])):
            x.append( info['data'][i]['summary']['discharged'])
            y.append(info['data'][i]['summary']['deaths'])
            z.append(info["data"][i]['summary']['total'])
            a.append(info['data'][i]['summary']['confirmedCasesIndian'])
        total=sum(x)+sum(y)+sum(z)+sum(a)
        temp1=(sum(x)/total)*100
        temp2=(sum(y)/total)*100
        temp3=(sum(z)/total)*100
        temp4=(sum(a)/total)*100
        arr=np.array([temp1,temp2,temp3,temp4])

        plt.title("Covid-19 Data INDIA")
        mylab=['Discarged='+str(sum(x)),'Deaths='+str(sum(y)),'Total='+str(sum(z)),'ConfirmedCaseIndia='+str(sum(a))]
        plt.pie(arr,labels=mylab,shadow=True)
        #plt.legend()
        plt.show()
    else:
        
        for i in range(len(info['data'])):
            for j in range(len(info['data'][i]['regional'])):
            
                if (state.get()) == (info['data'][i]['regional'][j]['loc']):
                
                    x.append( info['data'][i]['regional'][j]['discharged'])
                    y.append(info['data'][i]['regional'][j]['deaths'])
                    z.append(info["data"][i]['regional'][j]['totalConfirmed'])
        total=sum(x)+sum(y)+sum(z)
        temp1=(sum(x)/total)*100
        temp2=(sum(y)/total)*100
        temp3=(sum(z)/total)*100
        arr=np.array([temp1,temp2,temp3])
        mylab=['Discarged='+str(sum(x)),'Deaths='+str(sum(y)),'TotalConfirmed='+str(sum(z))]
        #myexplode = [0.1, 0.1, 0.1, 0.1]
        plt.title("Covid-19 Data "+state.get())
        plt.pie(arr,labels=mylab,shadow=True)
        #plt.legend()
        plt.show()





window=tk.Tk()
window.title('COVID-19')
window.geometry('500x300')

ttk.Label(window, text = "COVID-19 PIE CHART",  
          background = 'green', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
ttk.Label(window, text = "Select the state :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
  
n=tk.StringVar()
state=ttk.Combobox(window,width=27,textvariable=n)
state['value']=('India',
                "Andhra Pradesh",
                'Delhi',
                "Haryana",
                "Karnataka",
                 "Kerala",
                "Maharashtra",
                "Punjab",
                "Rajasthan",
                 "Tamil Nadu",
                "Telengana",
                "Chandigarh",
                "Jammu and Kashmir",
                "Uttar Pradesh",
                "Uttarakhand",
                "West Bengal")
state.grid(column=1,row=5)
state.current(0)
but=ttk.Button(window,text='Pie Chart',command=onclick)
but.grid(column=1,row=7)

window.mainloop()

                
