import json
import urllib.request as req
import matplotlib.pylab as plt
url='https://api.rootnet.in/covid19-in/stats/history'
rep=req.urlopen(url).read().decode()
info=json.loads(rep)
x=[]
y=[]
z=[]

for i in range(len(info['data'])):
    x.append( info['data'][i]['summary']['discharged'])
    y.append(info['data'][i]['summary']['deaths'])
    z.append(info["data"][i]['summary']['total'])
plt.subplot(3,1,1)
plt.plot(x,y)
plt.xlabel('Discharged')
plt.ylabel('Deaths')
plt.title("Data of Covid Discharged and Deaths")
plt.subplot(3,1,3)
plt.plot(z,x)
plt.ylabel('Discharged')
plt.xlabel('Total case per day')
plt.title("Data of Covid Total and Discharged")
plt.show()
