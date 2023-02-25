import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import numpy as np
from process import *

# define the dataset class
class MyDataset(Dataset):
    def __init__(self, data, label):
        self.data = data
        self.label = label

    def __getitem__(self, index):
        return self.data[index], self.label[index]

    def __len__(self):
        return len(self.data)

# define loader function
# year in range of [0,6]
# 0 means 2005, 1 means 2006, 2 means 2007, 3 means 2008, 4 means 2009, 5 means 2010
def getLoader(year, batch_size):
    trainData, trainLabel, testData, testLabel = splitData(year)
    trainData = torch.from_numpy(trainData).float()
    trainLabel = torch.from_numpy(trainLabel).float()
    testData = torch.from_numpy(testData).float()
    testLabel = torch.from_numpy(testLabel).float()

    trainDataset = MyDataset(trainData, trainLabel)
    testDataset = MyDataset(testData, testLabel)

    trainLoader = DataLoader(trainDataset, 
                            batch_size=batch_size, 
                            shuffle=True)
    
    testLoader = DataLoader(testDataset, 
                            batch_size=batch_size, 
                            shuffle=True)

    return trainLoader, testLoader


def LoadDataFromFiles():
    # load data
    data = np.array([])
    for i in range(0, 393):
        if i == 0:
            data = loadData(str(i))
        else:
            data = np.concatenate((data, loadData(str(i))), axis=1)

    data = data.transpose()
    data = data.reshape(2358,9,4)

    label = loadTxt("label")
    label = label.reshape(label.shape[0]*6, 1)
    return data, label

# year in range of [0,6]
# 0 means 2005, 1 means 2006, 2 means 2007, 3 means 2008, 4 means 2009, 5 means 2010
def splitData(year):
    splitList = getSplitList(year)
    data, label = LoadDataFromFiles()

    trainData = np.array([])
    trainLabel = np.array([])
    testData = np.array([])
    testLabel = np.array([])

    testData = data[splitList]
    testLabel = label[splitList]

    trainData = np.delete(data, splitList, axis=0)
    trainLabel = np.delete(label, splitList, axis=0)

    return trainData, trainLabel, testData, testLabel


# get the last year as the test data
def getSplitList(year):
    splitList = []
    for i in range(year, 393*6, 6):
        splitList.append(i)
    splitList = np.array(splitList)
    return splitList









    


