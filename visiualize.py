from process import *
import matplotlib.pyplot as plt
import numpy as np

def plotmap():
    # 读取数据
    pre,tmp,tmx,tmn,lat,lon= readData()
    pre1 = pre[0,:,:]
    tmp1 = tmp[0,:,:]
    tmx1 = tmx[0,:,:]
    tmn1 = tmn[0,:,:]

    # numpy array flip up and down
    pre1 = np.flipud(pre1)
    tmp1 = np.flipud(tmp1)
    tmx1 = np.flipud(tmx1)
    tmn1 = np.flipud(tmn1)

    # 画图 subplot 2*2 title 为数据名称
    plt.subplot(2,2,1)
    plt.title("pre")
    plt.imshow(pre1,cmap='rainbow')
    plt.subplot(2,2,2)
    plt.title("tmp")
    plt.imshow(tmp1)
    plt.subplot(2,2,3)
    plt.title("tmx")
    plt.imshow(tmx1)
    plt.subplot(2,2,4)
    plt.title("tmn")
    plt.imshow(tmn1)
    plt.show()

# plotline
def plotline():
    # load data
    data = loadCSV("0")
    # visualize data line subplots with title and color
    # main title of the figure
    plt.suptitle("the data of 0 point")
    plt.subplot(2,2,1)
    plt.title("pre")
    # label the x and y axis
    plt.xlabel("time/mouthly")
    plt.ylabel("mm/month")
    plt.plot(data[0],color='red',label='pre',linewidth=1,linestyle='--',marker='*',markerfacecolor='blue',markersize=3)
    plt.subplot(2,2,2)
    plt.title("tmp")
    plt.xlabel("time/mouthly")
    plt.ylabel("celsius")
    plt.plot(data[1],color='green',label='tmp',linewidth=1,linestyle='--',marker='*',markerfacecolor='blue',markersize=3)
    plt.subplot(2,2,3)
    plt.title("tmx")
    plt.xlabel("time/mouthly")
    plt.ylabel("celcius")
    plt.plot(data[2],color='blue',label='tmx',linewidth=1,linestyle='--',marker='*',markerfacecolor='blue',markersize=3)
    plt.subplot(2,2,4)
    plt.title("tmn")
    plt.xlabel("time/mouthly")
    plt.ylabel("celcius")
    plt.plot(data[3],color='brown',label='tmn',linewidth=1,linestyle='--',marker='*',markerfacecolor='blue',markersize=3)
    plt.show()

if __name__ == "__main__":
    plotline()

