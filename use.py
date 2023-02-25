from model import *
from dataset import *
import numpy as np

# # load model pth file
model = MyModel()
model.load_state_dict(torch.load("bestmodel.pth"))

# load data
# 预测2011年的数据
train_data, train_label, test_data, test_label = splitData(5) 


pre_result = []
for i in range(0, 393):
    data = test_data[i]
    data = data.reshape(1,36)
    data = torch.from_numpy(data).float()
    pre = model(data)
    pre_result.append(pre.item())

# save the result as csv
np.savetxt("pre_result.csv", pre_result, delimiter = ',')