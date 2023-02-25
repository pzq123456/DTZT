import torch
from torch import nn
from dataset import *
import matplotlib.pyplot as plt

# define the model
# input size: 9*4
# output size: 1
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1 = nn.Linear(36, 64)
        self.fc2 = nn.Linear(64, 128)
        self.fc3 = nn.Linear(128, 256)
        self.fc4 = nn.Linear(256, 512)
        self.fc5 = nn.Linear(512, 256)
        self.fc6 = nn.Linear(256, 128)
        self.fc7 = nn.Linear(128, 64)
        self.fc8 = nn.Linear(64, 32)
        self.fc9 = nn.Linear(32, 16)
        self.fc10 = nn.Linear(16, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.relu(self.fc3(x))
        x = self.relu(self.fc4(x))
        x = self.fc5(x)
        x = self.relu(self.fc6(x))
        x = self.relu(self.fc7(x))
        x = self.relu(self.fc8(x))
        x = self.relu(self.fc9(x))
        x = self.fc10(x)
        return x


    
# define the train function
def train(model, trainLoader,epoch, learning_rate,testLoader):
    loss_list = []

    print("train")
    model.train()
    loss = nn.MSELoss()
    test_loss = 100
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
    for i in range(epoch):
        for batch, (data, label) in enumerate(trainLoader):
            data = data.view(-1,36)
            pre = model(data)
            loss_value = loss(pre, label)
            loss_list.append(loss_value.item())

            # backward
            optimizer.zero_grad()
            loss_value.backward()
            optimizer.step()
            if batch % 100 == 0:
                test_loss2 = test(model, testLoader)
                if(test_loss2 < test_loss):
                    print("test loss: ", test_loss2)
                    print("save model:"+str(test_loss2))
                    torch.save(model.state_dict(), "bestmodel.pth")
                    test_loss = test_loss2

    return loss_list

# define the test function
def test(model, testLoader):
    num_batches = len(testLoader)
    test_loss = 0
    model.eval()
    loss = nn.MSELoss()
    with torch.no_grad():
        for batch, (data, label) in enumerate(testLoader):
            data = data.view(-1,36)
            pre = model(data)
            loss_value = loss(pre, label)
            test_loss += loss_value.item()
        test_loss /= num_batches
    return test_loss


# define the main function
def main():

    # define the model
    model = MyModel()
    # get loader
    trainLoader, testLoader = getLoader(0, 64)
    # train
    lossarr = train(model, trainLoader, 40, 0.0025,testLoader)

    # plot the loss
    plt.plot(lossarr, label="loss", color="red", linewidth=1, linestyle="-")
    plt.show()

if __name__ == "__main__":
    main()
