import netCDF4
import numpy as np
import math

# 辅助函数
def getLocation(oriLat,oriLon):
    lat = HelpF1(oriLat,0.75,0.25)
    lon = HelpF1(oriLon,0.75,0.25)
    return lat,lon

def HelpF1(x,top,button):
    R,I =math.modf(x)
    print(I)
    print(R)
    gap1 = abs(R - top)
    gap2 = abs(R - button)
    if gap1 >= gap2 :
        return I+button
    else:
        return I+top


data = np.loadtxt("data\metadata.txt", encoding="UTF-8")

    

# f1 = netCDF4.Dataset('data\cru_ts4.06.2001.2010.pre.dat.nc')
# f2 = netCDF4.Dataset('data\cru_ts4.06.2001.2010.tmp.dat.nc')
# f3 = netCDF4.Dataset('data\cru_ts4.06.2001.2010.tmx.dat.nc')
# f4 = netCDF4.Dataset('data\cru_ts4.06.2011.2020.tmn.dat.nc')

# lat, lon = f1.variables['lat'], f1.variables['lon']

# # print("=======================")
# # print(f1.variables.keys())
# # print("=======================")
# # print(f2.variables.keys())
# # print("=======================")
# # print(f3.variables.keys())
# # print("=======================")
# # print(f4.variables.keys()) 

# pre = f1.variables['pre'] # 逐月降水量 10年
# tmp = f2.variables['tmp'] # 月均温 
# tmx = f3.variables['tmx'] # 月最高温
# tmn = f4.variables['tmn'] # 月最低温

# print(pre[0,lat[0],lon[0]],pre.units)
# print(tmp[0,lat[0],lon[0]],tmp.units)
# print(tmx[0,lat[0],lon[0]],tmx.units)
# print(tmn[0,lat[0],lon[0]],tmn.units)


# print(getLocation(123.634343,85.1131231))

# getLocation(11,22)