import netCDF4
import numpy as np
import math
import matplotlib.pyplot as plt

# 辅助函数
def getLocation(oriLat,oriLon):
    lat = HelpF1(oriLat,0.75,0.25)
    lon = HelpF1(oriLon,0.75,0.25)
    return lat,lon

def getLatIndex(lat):
    return int((lat+89.75)/0.5)

def getLonIndex(lon):
    return int((lon+179.75)/0.5)

def getLocIndex(lat,lon):
    latIndex = getLatIndex(lat)
    lonIndex = getLonIndex(lon)
    return latIndex,lonIndex

def HelpF1(x,top,button):
    R,I =math.modf(x)
    gap1 = abs(R - top)
    gap2 = abs(R - button)
    if gap1 >= gap2 :
        return I+button
    else:
        return I+top

# contact 4 lines of data into one numpy array 
def contactLines(data1,data2,data3,data4):
    data = np.array([data1,data2,data3,data4])
    return data

# 读取数据
def readData():
    f1 = netCDF4.Dataset('DTZT/data/cru_ts4.06.2001.2010.pre.dat.nc')
    f2 = netCDF4.Dataset('DTZT/data/cru_ts4.06.2001.2010.tmp.dat.nc')
    f3 = netCDF4.Dataset('DTZT/data/cru_ts4.06.2001.2010.tmx.dat.nc')
    f4 = netCDF4.Dataset('DTZT/data/cru_ts4.06.2011.2020.tmn.dat.nc')
    pre = f1.variables['pre'] # 逐月降水量 10年
    tmp = f2.variables['tmp'] # 月均温 
    tmx = f3.variables['tmx'] # 月最高温
    tmn = f4.variables['tmn'] # 月最低温
    return pre,tmp,tmx,tmn

# read metadata.txt 
def readMetadata():
    data = np.loadtxt("DTZT/data/metadata.txt", encoding="UTF-8")
    return data

# generate numpy array save path function
# name: the name of the numpy array
def savePath(name):
    path = "DTZT/dataset/"+name+".npy"
    return path

# save numpy array as the savePath function generated path
def saveData(data,name):
    path = savePath(name)
    np.save(path,data)

# load numpy array from the savePath function generated path
def loadData(name):
    path = savePath(name)
    data = np.load(path)
    return data

# process status report function
def reportStart(i):
    print("processing "+str(i)+" data")

def reportEnd(i):
    print("processed "+str(i)+" data")

# main process function
def process():
    pre,tmp,tmx,tmn= readData()
    metadata = readMetadata()
    for i in range(0,1):
        reportStart(i)
        lat,lon = getLocation(metadata[i][0],metadata[i][1])
        latIndex,lonIndex = getLocIndex(lat,lon)
        data1 = pre[:,latIndex,lonIndex]
        data2 = tmp[:,latIndex,lonIndex]
        data3 = tmx[:,latIndex,lonIndex]
        data4 = tmn[:,latIndex,lonIndex]
        data = contactLines(data1,data2,data3,data4)
        print(data)
        # visualize data line subplots 
        plt.subplot(2,2,1)
        plt.plot(data[0],color='red',label='pre',linewidth=1,linestyle='--',marker='*',markerfacecolor='blue',markersize=3)
        plt.subplot(2,2,2)
        plt.plot(data[1],color='green',label='tmp',linewidth=1,linestyle='--',marker='*',markerfacecolor='blue',markersize=3)
        plt.subplot(2,2,3)
        plt.plot(data[2],color='blue',label='tmx',linewidth=1,linestyle='--',marker='*',markerfacecolor='blue',markersize=3)
        plt.subplot(2,2,4)
        plt.plot(data[3],color='brown',label='tmn',linewidth=1,linestyle='--',marker='*',markerfacecolor='blue',markersize=3)
        plt.show()
        # saveData(data,str(i))
        # reportEnd(i)


if __name__ == "__main__":
    process()