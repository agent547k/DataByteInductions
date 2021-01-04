import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList)
plt.xlabel('Month')
plt.ylabel('Profit')
plt.xticks(monthList)
plt.title('Graph')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()