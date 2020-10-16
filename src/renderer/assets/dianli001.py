# -*- coding:utf-8 -*-
import warnings
warnings.filterwarnings("ignore", category=Warning)
import pandas as pd
import datetime as dt
import numpy as np
import openpyxl as op
import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

#基础数据读取
sht1=pd.read_excel(os.path.join(basedir, '8760h_PEBS_base.xlsx'),'电力电量平衡')

# 径流式水电平均出力读取
Rhydropower=[]
Rhydropower=sht1.iloc[[78],[2,3,4,5,6,7,8,9,10,11,12,13]].values                      #径流式电站过程
Rhydropower=Rhydropower[0]


# 核电平均出力读取
Nuclear=[]
Nuclear=sht1.iloc[[89],[2,3,4,5,6,7,8,9,10,11,12,13]].values                         #核电电站过程
Nuclear=Nuclear[0]


#其他平均出力读取
Other=[]
Other=sht1.iloc[[90],[2,3,4,5,6,7,8,9,10,11,12,13]].values
Other=Other[0]


Thermal=[]                                                    #火电可用容量读取
Thermal=sht1.iloc[[64],[2,3,4,5,6,7,8,9,10,11,12,13]].values
Thermal=Thermal[0]


HydroFpower=[]
HydroFpower=sht1.iloc[[71],[2,3,4,5,6,7,8,9,10,11,12,13]].values   #水电强迫出力读取
HydroFpower=HydroFpower[0]


Hydropower=[]                                                    #水电可调容量读取
Hydropower=sht1.iloc[[72],[2,3,4,5,6,7,8,9,10,11,12,13]].values
Hydropower=Hydropower[0]

ThermalRateofoutput=[]                                                    #火电技术最小出力率
ThermalRateofoutput=sht1.iloc[[65],[2,3,4,5,6,7,8,9,10,11,12,13]].values
ThermalRateofoutput=ThermalRateofoutput[0]

#装机读取

Hydrocapacity=sht1.iloc[[22],[2]].values[0][0]
Pumpedcapacity=sht1.iloc[[23],[2]].values[0][0]
Thermalcapacity=sht1.iloc[[24],[2]].values[0][0]
Windcapacity=sht1.iloc[[25],[2]].values[0][0]
Photovoltaic=sht1.iloc[[26],[2]].values[0][0]
Photoheatcapacity=sht1.iloc[[27],[2]].values[0][0]
Nuclearcapacity=sht1.iloc[[28],[2]].values[0][0]
Othercapacity=sht1.iloc[[29],[2]].values[0][0]
EnergyStoragecapacity=sht1.iloc[[30],[2]].values[0][0]      #储能装机

#光热参数
Photoheattime=sht1.iloc[[91],[2]].values[0][0]              #光热储存小时
Photoheattrans=sht1.iloc[[92],[2]].values[0][0]             #光热转换效率
PhotoheatEfficiency=sht1.iloc[[93],[2]].values[0][0]        #光热发电效率
Photoheatmin=sht1.iloc[[87],[2]].values[0][0]               #光热最小出力率

#化学储能
EnergyStorageEfficiency=sht1.iloc[[94],[2]].values[0][0]    #储能效率
EnergyStoragetime=sht1.iloc[[95],[2]].values[0][0]          #储能小时

#抽水蓄能电站
Pumpedstoragehydroelectricitycapacity=sht1.iloc[[83],[2,3,4,5,6,7,8,9,10,11,12,13]].values         #抽水蓄能电站可用容量
Pumpedstoragehydroelectricitycapacity=Pumpedstoragehydroelectricitycapacity[0]

Baseload=Nuclear+Other+Rhydropower+HydroFpower                  #基荷包括核电、其他、径流式水电、调节水电强迫出力

#print(Nuclear[0],Other[0],Rhydropower[0],Baseload)

#残余负荷曲线计算
sht2=pd.read_excel(os.path.join(basedir, '8760h_PEBS_base.xlsx'),'计算过程')

no=sht2['排序']
Loadprofile1=sht2['负荷']
Windpower1=sht2['风电出力']
Photovoltaic1=sht2['光伏出力']

Loadprofile2=Loadprofile1-Windpower1-Photovoltaic1      #残余负荷曲线计算

AM=24*31
BM=24*30
CM=24*28

Jan=AM                   #744
Feb=Jan+CM               #672
Mar=Feb+AM               #744
Api=Mar+BM               #720
May=Api+AM               #744
Jun=May+BM               #720
Jul=Jun+AM                #744
Aug=Jul+AM                  #744
Sep=Aug+BM                #720
Oct=Sep+AM               #744
Noc=Oct+BM                #720
Dec=Noc+AM               #744

qiepianlen=[744,672,744,720,744,720,744,744,720,744,720,744]
#残余负荷曲线分月

Loadprofile2_1=Loadprofile2.iloc[0:Jan]
Loadprofile2_2=Loadprofile2.iloc[Jan:Feb]
Loadprofile2_3=Loadprofile2.iloc[Feb:Mar]
Loadprofile2_4=Loadprofile2.iloc[Mar:Api]
Loadprofile2_5=Loadprofile2.iloc[Api:May]
Loadprofile2_6=Loadprofile2.iloc[May:Jun]
Loadprofile2_7=Loadprofile2.iloc[Jun:Jul]
Loadprofile2_8=Loadprofile2.iloc[Jul:Aug]
Loadprofile2_9=Loadprofile2.iloc[Aug:Sep]
Loadprofile2_10=Loadprofile2.iloc[Sep:Oct]
Loadprofile2_11=Loadprofile2.iloc[Oct:Noc]
Loadprofile2_12=Loadprofile2.iloc[Noc:Dec]

Loadprofile2=[Loadprofile2_1,Loadprofile2_2,Loadprofile2_3,Loadprofile2_4,Loadprofile2_5,Loadprofile2_6,
              Loadprofile2_7,Loadprofile2_8,Loadprofile2_9,Loadprofile2_10,Loadprofile2_11,Loadprofile2_12]

Windpower1_1 = Windpower1.iloc[0:Jan]
Windpower1_2 = Windpower1.iloc[Jan:Feb]
Windpower1_3 = Windpower1.iloc[Feb:Mar]
Windpower1_4 = Windpower1.iloc[Mar:Api]
Windpower1_5 = Windpower1.iloc[Api:May]
Windpower1_6 = Windpower1.iloc[May:Jun]
Windpower1_7 = Windpower1.iloc[Jun:Jul]
Windpower1_8 = Windpower1.iloc[Jul:Aug]
Windpower1_9 = Windpower1.iloc[Aug:Sep]
Windpower1_10 = Windpower1.iloc[Sep:Oct]
Windpower1_11 = Windpower1.iloc[Oct:Noc]
Windpower1_12 = Windpower1.iloc[Noc:Dec]

Windpower2 = np.array([Windpower1_1, Windpower1_2, Windpower1_3, Windpower1_4, Windpower1_5, Windpower1_6,
                       Windpower1_7, Windpower1_8, Windpower1_9, Windpower1_10, Windpower1_11, Windpower1_12])



Photovoltaic1_1 = Photovoltaic1.iloc[0:Jan]
Photovoltaic1_2 = Photovoltaic1.iloc[Jan:Feb]
Photovoltaic1_3 = Photovoltaic1.iloc[Feb:Mar]
Photovoltaic1_4 = Photovoltaic1.iloc[Mar:Api]
Photovoltaic1_5 = Photovoltaic1.iloc[Api:May]
Photovoltaic1_6 = Photovoltaic1.iloc[May:Jun]
Photovoltaic1_7 = Photovoltaic1.iloc[Jun:Jul]
Photovoltaic1_8 = Photovoltaic1.iloc[Jul:Aug]
Photovoltaic1_9 = Photovoltaic1.iloc[Aug:Sep]
Photovoltaic1_10 = Photovoltaic1.iloc[Sep:Oct]
Photovoltaic1_11 = Photovoltaic1.iloc[Oct:Noc]
Photovoltaic1_12 = Photovoltaic1.iloc[Noc:Dec]

Photovoltaic2 = np.array([Photovoltaic1_1, Photovoltaic1_2, Photovoltaic1_3, Photovoltaic1_4, Photovoltaic1_5, Photovoltaic1_6,
                 Photovoltaic1_7, Photovoltaic1_8, Photovoltaic1_9, Photovoltaic1_10, Photovoltaic1_11,
                 Photovoltaic1_12])

#去除基荷

Loadprofile3=[]                                        #去掉基荷残余负荷

def cal4sub(Baseload,Loadprofile2):
    for num,shuzu in zip(Baseload,Loadprofile2):

        Loadprofile3.append(np.subtract(shuzu,num))

    return Loadprofile3

Loadprofile3 =np.array( cal4sub(Baseload,Loadprofile2))


#print(type(Loadprofile3))


from numpy import trapz
#调节水电

#1、确定可调容量    Hydropower

#2、各月电量计算
HElec_capacity=[]
HElec_capacity=sht1.iloc[[74],[2,3,4,5,6,7,8,9,10,11,12,13]].values
HElec_capacity=HElec_capacity[0]

#3、水电放线


def fangxian(xia,shang,list):

    #if xia<0:
        #xia=0
    y=np.clip(list,xia,shang)-xia
    mianji=np.trapz(y)
    return mianji

def paixian(list1,dianliang,ketiao):                        #对水电进行月调节

    c_hydroProcesssum=[]
    i=0
    while i <12:
        a = 0
        low = a
        high=np.max(list1[i])+ketiao[i]
        while True:
            mid=(low+high)/2
            am=mid
            bm = am + ketiao[i]
            bbm = fangxian(am, bm, list1[i])
            bbm=float(bbm)
            ccm=bbm-dianliang[i]
            ccm = float(ccm)
            if abs(ccm) <1:
                #print('水电位置为',am)
                am=int(am)
                c_hydroProcess=np.clip(list1[i],am,np.max(list1[i]))-am    # 负荷每小时调节能力  #每个步长函数与两条直线的高度
                #print('调节能力使用了',np.max(c_hydroProcess))
                c_hydroProcesssum.append(c_hydroProcess)                  #全年水电调节过程
                #continue
                #return c_hydroProcess
                break

            elif ccm>=1:

                #print('low=min',ccm,low,mid,high)
                low = mid
            elif ccm<-1:

                #print('high=mid',ccm,low,mid,high)
                high = mid
        i=i+1



    #print(c_hydroProcesssum)
    return c_hydroProcesssum
Hydropower1=np.array(paixian(Loadprofile3,HElec_capacity,Hydropower))          #Hydropower1 1号水电全年出力过程

#print('1号水电出力过程结果为',Hydropower1)


#初步弃电判断
#print(type(np.array(Loadprofile3[0])))
#print(type(Hydropower1))


Loadprofile4=[]
Loadprofile4=np.array(Loadprofile3)-Hydropower1                  #满足基荷、风电、光伏、水电1号电站后的残余负荷


def jueduizhi(a,b):                            #残余的负荷和火电的装机
    c=[]
    for i,j in zip(a,b):
        c.append(np.clip(i,0,j))
    return c

ThermalPower=jueduizhi(Loadprofile4,Thermal)#np.clip(Loadprofile4,0,Thermal)
#print(ThermalPower)

def ydpanduan(a,b):
    c=[]
    for i,j in zip (a,b):
        c.append(np.subtract(i,j))
    return c

yudian=np.array(ydpanduan(Loadprofile4,ThermalPower))                                    #火电能力后是否存在余电

#print("这里是",yudian)

#
#yudian=yudian[0]

#print("而这里这里是",yudian)
#print(np.shape(yudian))

###############################
###############################说明每一天的弃电都在什么时候
###############################
# j=0                                                                                    #判断电源是否有电量不足
# p=[]
# while j<12:
#     m=0
#     n=[]
#     elec = yudian[j:j+1]
#     #print('elec的数据是',elec, type(elec))
#     for k in range(len(elec)):
#         #print('k type is',type(k))
#         for num in elec[k]:
#             elec[k]=list(elec[k])
#             #print('eleck type is',type(elec[k]))
#             #num=int(num)
#             #print('num type is',type(num))
#             #print('elec[k] num is',elec[k])
#             if num>0:
#                 m=m+1
#                 n.append(num)
#     #print('第', j + 1, '月，有',m, '天缺电', np.sum(n), '亿千瓦时')
#     j=j+1
#     p.append(np.sum(n))
#
# pp=np.sum(p)

#if pp>0:
    #print('系统存在缺电，请重新进行初步电力电量平衡')
#else:
    #print('继续计算')
'''
def listnum(list1,num1):
    for list11 num11 in zip(list1,num1)
        c=np.append(list11*num11)
    return c

ThermalPowerCircumscribes_min=listnum()'''

#print(ThermalPower)
#print(ThermalRateofoutput)


ThermalPowermax=[]
ThermalPowerCircumscribes_min=[]
ThermalPowerCircumscribes=[]
failurePower=[]
failurePowerall=[]
ThermalPowerCircumscribes1=[]
ThermalPowerCircumscribes_min1=[]


for i in range(12):
    ThermalPowermax=np.max(ThermalPower[i])
    ThermalPowerCircumscribes_min=ThermalPowermax*ThermalRateofoutput[i]           #火电最小技术出力要求
    ThermalPowerCircumscribes_min1.append(ThermalPowerCircumscribes_min)
    ThermalPowerCircumscribes=np.clip(ThermalPower[i],ThermalPowerCircumscribes_min,ThermalPowermax)    #火电最低出力过程
    ThermalPowerCircumscribes1.append(ThermalPowerCircumscribes)                       #火电最小出力率
    failurePower=ThermalPowerCircumscribes-ThermalPower[i]                             #弃电计算，这个弃电是个正的
    failurePowerall.append(failurePower)

#print('初步弃电量为',failurePowerall)

from itertools import chain

failurePowerall=np.array(failurePowerall)                                           #12个月分开
failurePowerall1=np.array(list(chain(*failurePowerall)))                            #完整的一年
#print('初步弃电量为',failurePowerall1)

Windfailure=Windpower2/(Windpower2+Photovoltaic2)*failurePowerall
Photovoltaicfailure=Photovoltaic2/(Windpower2+Photovoltaic2)*failurePowerall

#大于火电最小技术出力率部分


#print('风电弃电率为',Windfailure,'光伏弃电率',Photovoltaicfailure)

#抽水蓄能及储能计算

def zushucha(aa,a):
    b=[]
    for zu,shu in zip(aa,a):
        b.append(np.subtract(aa,a))

    return b

#1、光热

Photovoltaic28760=np.array(list(chain(*Photovoltaic2)))                  #变成8760h过程

AvailableThermal=[]                                                      #可被抽的火电计算
ThermalPowerCircumscribes_min1=np.array(ThermalPowerCircumscribes_min1)   #最小出力计算
ThermalPowerCircumscribes1=np.array(ThermalPowerCircumscribes1)

#AvailableThermal=np.array(cal4sub(ThermalPowerCircumscribes_min1,ThermalPowerCircumscribes1))

AvailableThermal=zushucha(ThermalPowerCircumscribes1,ThermalPowerCircumscribes_min1)
AvailableThermal=AvailableThermal[0]                                       #可被抽的火电序列

#print('ashi1',AvailableThermal,'_____________')


# print("剩余点",yudian)


yudian=np.array(list(chain(*yudian)))                                         #可利用的余电计算，即距离负荷不足的区间
AvailableThermal=np.array(list(chain(*AvailableThermal)))
# np.set_printoptions(threshold=np.inf)
# print("南要的结果:\n",AvailableThermal)
#光热
PhotoheatAvailable=yudian+AvailableThermal                               #光热可发量

#光热储存小时Photoheattime
#光热转换效率Photoheattrans
#光热发电效率PhotoheatEfficiency
#装机 Photoheatcapacity

Photoheatmin_1=Photoheatmin*Photoheatcapacity

PhotoheatProcess1=[]                                              #发电过程
Photoheatsave=[]                                                  #储光过程
Photoheatcapacity1=Photoheatcapacity*(1-Photoheatmin)

iheat=0
sheat=0

while iheat<8760:
    sheat1=sheat+PhotoheatEfficiency*Photovoltaic28760[i]-PhotoheatAvailable[i]
    if sheat1>=Photoheatcapacity1:
        sheat1=Photoheatcapacity1
        PhotoheatProcess=abs(PhotoheatAvailable[i])
        #print('1')
    elif sheat1<=0:
        sheat1=0
        PhotoheatProcess=sheat+Photovoltaic28760[i]
        #print('2')
    elif  0<sheat1<Photoheatcapacity1 :
        sheat1=sheat+PhotoheatEfficiency*Photovoltaic28760[i]+PhotoheatAvailable[i]
        PhotoheatProcess=abs(PhotoheatAvailable[i])
        #print('3')
    PhotoheatProcess1.append(PhotoheatProcess)
    #print('s1 is',sheat1)
    Photoheatsave.append(sheat1)
    sheat=sheat1
    #print( PhotoheatProcess)
    iheat=iheat+1

#print(Photoheatsave,PhotoheatProcess1)


#2、化学储能

#
AvailablePower=failurePowerall1-yudian-AvailableThermal+PhotoheatProcess1              #可利用的电量
#print(np.shape(failurePowerall1),np.shape(yudian),np.shape(AvailableThermal))

#储能效率EnergyStorageEfficiency
#储能小时EnergyStoragetime
#装机EnergyStoragecapacity

                                                                                       #暂定储能小时为4小时
EnergyStorageStart=1/2*EnergyStoragecapacity*EnergyStoragetime                         #库容，初始库容按照一半考虑
EnergyStorage1=[]                                                                      #过程
                                                                                       #暂定储能效率为90%
Storagemid=0
Energy=0                                                                               #拟定抽的是正的  发电是负的
while Energy<8760:
    if AvailablePower[Energy]>0:                         #抽水
        if Storagemid+EnergyStorageEfficiency*AvailablePower[Energy]>=EnergyStoragecapacity:
            Storagemid1=EnergyStoragecapacity
        else:
            Storagemid1=Storagemid+EnergyStorageEfficiency*AvailablePower[Energy]

    else:                               #发电
        if Storagemid+AvailablePower[Energy]<0:
            Storagemid1=0

        else:
            Storagemid1=Storagemid+AvailablePower[Energy]
    EnergyStorage1.append(Storagemid1-Storagemid)
    Storagemid=Storagemid1
    Energy=Energy+1

#print(EnergyStorage1)



##---------------------------------------------------------------
#3、抽水蓄能

AvailablePower2=AvailablePower-EnergyStorage1     #可利用的电量
EnergyStorageStart=1/2*EnergyStoragecapacity*EnergyStoragetime  #库容，初始库容按照一半考虑
EnergyStorage2=[]   #过程

Storagemid=0
Energy=0                                                                               #拟定抽的是正的  发电是负的

while Energy<8760:
    if AvailablePower2[Energy]>0:                         #抽水
        if Storagemid+EnergyStorageEfficiency*AvailablePower2[Energy]>=EnergyStoragecapacity:
            Storagemid2=EnergyStoragecapacity
        else:
            Storagemid2=Storagemid+EnergyStorageEfficiency*AvailablePower2[Energy]

    else:                               #发电
        if Storagemid+AvailablePower2[Energy]<0:
            Storagemid2=0

        else:
            Storagemid2=Storagemid+AvailablePower2[Energy]
    EnergyStorage2.append(Storagemid2-Storagemid)
    Storagemid=Storagemid2
    Energy=Energy+1

#print("抽水蓄能的",EnergyStorage2)




##---------------------------------------------------------------
#4水电第二次计算



#print(data)

#print("Loadprofile3是什么",Loadprofile3)
#pandas -------Series

#把12个数组转换成8760的一维数组
Loadprofile3dataget=[]
for data in Loadprofile3:
    Loadprofile3dataget.append(data.values.tolist())


aaa=Loadprofile3dataget
bbb=[]
for data in aaa:
    bbb=bbb+data

#print("这里是啥",len(bbb))
#print("-----------------------------#########################################-------------------------------------")
#print("PhotoheatProcess1是什么",PhotoheatProcess1)


Loadprofile221= np.array(bbb) -PhotoheatProcess1+EnergyStorage1+EnergyStorage2

#print("-----------------------------#########################################-------------------------------------")     #221已经没问题
#print("Loadprofile221的长度是不是8760",len(Loadprofile221))
#print("daozheli",Loadprofile221)
#print("-----------------------------#########################################-------------------------------------")
#
#
qiepianlen=[744,672,744,720,744,720,744,744,720,744,720,744]
data4qiepian=[]

def qiepian4Hydropower221():
    start=0
    for end in qiepianlen:
        qieend=start+end
        #print("这次切片的开始是",start,"这次切片的结束是",qieend)
        data4qiepian.append(Loadprofile221[start:qieend])
        start=start+end

    #print("data4qiepian的len应该是12，",len(data4qiepian))




def qiepian412ge(listname):  #吧8760单维数组，切片成为12个组
    datagetname=[]
    start=0
    for end in qiepianlen:
        qieend=start+end
        #print("这次切片的开始是",start,"这次切片的结束是",qieend)
        datagetname.append(listname[start:qieend])
        start=start+end
    return datagetname

qiepian4Hydropower221()

#print("切完之后的数据为",data4qiepian)

Hydropower221=np.array(paixian(data4qiepian,HElec_capacity,Hydropower))          #Hydropower1 1号水电全年出力过程
# print("Hydropower221的长度是不是8760",len(Hydropower221))
# print("daozheli",Hydropower221)
#
# print("-----------------------------#########################################-------------------------------------")

#print(Hydropower221)
##---------------------------------------------------------------


#5火电的第二次计算

#5.1 火电的初算

Loadprofile222=[]
####221
Loadprofile222=np.array(data4qiepian)-Hydropower221                  #满足基荷、风电、光伏、水电1号电站后的参与负荷


ThermalPower221=jueduizhi(data4qiepian,Thermal)#np.clip(Loadprofile4,0,Thermal)


#print(ThermalPower221)
#print(ThermalPower)
yudian221=np.array(ydpanduan(data4qiepian,ThermalPower221))                                    #火电能力后是否存在余电
# yudian221=yudian221[0]
#print("余电221应该是对的8",yudian221)


##5.2 火电的最低要求



#
# ThermalPowermax=[]
# ThermalPowerCircumscribes_min=[]
# ThermalPowerCircumscribes=[]
# failurePower=[]
# failurePowerall=[]
# ThermalPowerCircumscribes1=[]
# ThermalPowerCircumscribes_min1=[]
#
#
# for i in range(12):
#     ThermalPowermax=np.max(ThermalPower[i])
#     ThermalPowerCircumscribes_min=ThermalPowermax*ThermalRateofoutput[i]           #火电最小技术出力要求
#     ThermalPowerCircumscribes_min1.append(ThermalPowerCircumscribes_min)
#     ThermalPowerCircumscribes=np.clip(ThermalPower[i],ThermalPowerCircumscribes_min,ThermalPowermax)    #火电最低出力过程
#     ThermalPowerCircumscribes1.append(ThermalPowerCircumscribes)                       #火电最小出力率
#     failurePower=ThermalPowerCircumscribes-ThermalPower[i]                             #弃电计算，这个弃电是个正的
#     failurePowerall.append(failurePower)
#



ThermalPowermax_3=[]
ThermalPowerCircumscribes_min_3=[]
ThermalPowerCircumscribes_3=[]
failurePower_3=[]
failurePowerall_3=[]
ThermalPowerCircumscribes1_3=[]
ThermalPowerCircumscribes_min1_3=[]


for i in range(12):
    ThermalPowermax_3=np.max(ThermalPower221[i])  #这每次只有一个， 12个
    ThermalPowerCircumscribes_min_3=ThermalPowermax_3*ThermalRateofoutput[i]           #火电最小技术出力要求
    ThermalPowerCircumscribes_min1_3.append(ThermalPowerCircumscribes_min_3)
    ThermalPowerCircumscribes_3=np.clip(ThermalPower221[i],ThermalPowerCircumscribes_min_3,ThermalPowermax_3)    #火电最低出力过程
    ThermalPowerCircumscribes1_3.append(ThermalPowerCircumscribes_3)                       #火电最小出力率
    failurePower_3=ThermalPowerCircumscribes_3-ThermalPower221[i]                             #弃电计算，这个弃电是个正的
    failurePowerall_3.append(failurePower_3)

#print("能到这里吗",ThermalPowerCircumscribes_3,failurePowerall_3)
#failurePowerall_3   火电上调，增加的弃电
#ThermalPowerCircumscribes1_3  火电过程
#print("火电过程应该是12",ThermalPowerCircumscribes1_3)
#print("他是12维",ThermalPower221)
# ###--------------------
# #6输出结果
#
# #要看这两个
#
#

#print(Windpower1.type)

res=Loadprofile1-Windpower1    -Photovoltaic1
res2array=res.values
#print("这里是啥",len(res2array))



res212gezu=qiepian412ge(res2array)


# print("这东西是啥",len(ThermalPowerCircumscribes_3))

# ###################################
# ##ThermalPowerCircumscribes_3转换成单list
# ThermalPowerCircumscribes_3_list=[]
# for data in ThermalPowerCircumscribes_3:
#     ThermalPowerCircumscribes_3_list.extend(data)
#
# print("ThermalPowerCircumscribes_3_list的长度应该是8760，是不是",len(ThermalPowerCircumscribes_3_list))

resfinal=res212gezu-Hydropower221-ThermalPowerCircumscribes1_3  #这里的操作 本来就是12维度的

#
#
reslast= resfinal  -qiepian412ge(PhotoheatProcess1)-qiepian412ge(EnergyStorage1)-qiepian412ge(EnergyStorage2)             #qiepian412ge这个函数将单维的数组转换为12组的多维



#输出的第一个参数
aaa=reslast[0].tolist()
quedian=[]
qidian=[]
for data in aaa:
    if data >0:
        quedian.append(data)
        qidian.append(0)
    else:
        quedian.append(0)
        qidian.append(data)



#输出的第二个参数

print(aaa)
print(quedian)
print(qidian)
#-PhotoheatProcess1-EnergyStorage1-EnergyStorage2
#print("正的是缺电，负的是弃电",reslast)
#+++缺电直接表示
#---

# qidianpanbo="res里面的负"
#
# Windfailure221=Windpower1/(Windpower1+Photovoltaic1)*qidianpanbo
# Photovoltaicfailure221=Photovoltaic1/(Windpower1+Photovoltaic1)*qidianpanbo
#
#
# Windpower221=Windpower1-Windfailure221
# Photovoltaic221=Photovoltaic1-Photovoltaicfailure221


#############################
#输出10个结果
# 缺电===>res里面正的数据
#
# 各个电源===>Hydropower221，ThermalPower221，PhotoheatProcess1，EnergyStorage1，EnergyStorage2,Windpower221,Photovoltaic221
#
# 弃电===>Windfailure221,Photovoltaicfailure221
