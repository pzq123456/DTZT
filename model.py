import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision.transforms import ToTensor
import pandas as pd

# Define the model class
# LSTM model 
# in put: 4 features
# output: 1 feature
class LSTM(nn.Module):
    def __init__(self, input_size=4, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size

        self.lstm = nn.LSTM(input_size, hidden_layer_size)

        self.linear = nn.Linear(hidden_layer_size, output_size)

        self.hidden_cell = (torch.zeros(1,1,self.hidden_layer_size),
                            torch.zeros(1,1,self.hidden_layer_size))

    def forward(self, input_seq):
        lstm_out, self.hidden_cell = self.lstm(input_seq.view(len(input_seq) ,1, -1), self.hidden_cell)
        predictions = self.linear(lstm_out.view(len(input_seq), -1))
        return predictions[-1]

# Define the dataset class
# Dataset class
class StockDataset(Dataset):
    def __init__(self, csv_file, transform=None):
        self.stock_frame = pd.read_csv(csv_file)
        self.transform = transform

    def __len__(self):
        return len(self.stock_frame)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        sample = self.stock_frame.iloc[idx, 1:5].values
        sample = sample.astype('float').reshape(-1, 1)

        if self.transform:
            sample = self.transform(sample)

        return sample

# Define the transform class
# Transform class
class ToTensor(object):
    def __call__(self, sample):
        return torch.from_numpy(sample)

# Define the data loader class
# Data loader class
def get_data_loader(csv_file, batch_size):
    dataset = StockDataset(csv_file=csv_file, transform=ToTensor())
    data_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=False)
    return data_loader
    


