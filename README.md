# Map production experiment 2023.2.26
This is the repository for the map production experiment(the second semester in my junior year). We get the main idea from the paper "[Improving the Forecasting of Winter Wheat Yields in Northern China with Machine Learning–Dynamical Hybrid Subseasonal-to-Seasonal Ensemble Prediction](https://doi.org/10.3390/)". Only for their work can we do such a thing. We are very grateful to them.
# The Main result of the experiment( may be useful for you)
## 1. 6 years of winter wheat yield data in the north of China from 2005 to 2010
Those data contain the meteorological data and the yield data of each county (393 counties in total). 
### The meteorological data
The meteorological data are Tmx, Tmn, Tmp and Pre (the maximum, minimum, and average temperature and precipitation of each county in each month) which is from the [Climatic Research Unit (University of East Anglia) and Met Office](https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.06/). We put them in the "dataset" folder in the same order as the "county.csv". For example, in the "0.csv", you will find the data is organized as follows:
```
(month:) 1,2,3,4,5,6,7,8,9,10,11,12 in 2005 and so on
(Tmx:) xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx ...
(Tmn:) xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx ...
(Tmp:) xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx ...
(Pre:) xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx,xxx ...
```
You can read those data by the following code:
```python
    import pandas as pd
    import numpy as np
    data = pd.read_csv("dataset/0.csv",header=None)
    data = np.array(data)
    Tmx = data[1:,1:13]
    Tmn = data[1:,13:25]
    Tmp = data[1:,25:37]
    Pre = data[1:,37:49]
```
> If you want to know more about how to get data like this from the original data (0.5 digree * 0.5 digree resultion grid data for the earth serface), you can read the "process.py" .

### The yield data
The yield data are the yield of each county each year. The data are from the [China National Grain and Oils Information Center](http://www.cngoc.org.cn/). The data are in the "yield.csv".

> For convenience, we make the metadata for them. The "county.csv" is the metadata to organize all the data mationed above and you can find the location of each conty in the "county.csv". The "county.csv" is organized as follows:
```
idx longitude  latitude
0,   116.46,     39.92
1,   116.46,     39.92
...
```
## 2. The prediction model
We use the simple multiple perceptron model to predict the yield of each county. The model is in the "model.py". The model's performance is not good enough. We will try to improve it in the future. : )
You can use it in "use.py". This script will load the best model and predict the yield of each county in 2011.
# Thanks for your attention
If you have any questions, please put them in the "issue" or contact me by email.
> the data is too large to upload, so we put them in the Baidu cloud disk. Jusy unzip the "dataset.zip" and put it into the "dataset" folder. Some changes may be needed in the "process.py" and "model.py" to make it work. 
 