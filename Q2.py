import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
monthList = df['month_number'].tolist()
faceCrem = df['facecream'].tolist()
faceWash = df['facewash'].tolist()
toothPaste = df['toothpaste'].tolist()
bathingsoap = df['bathingsoap'].tolist()
shampoo = df['shampoo'].tolist()
moisturizer = df['moisturizer'].tolist()

plt.plot(monthList, faceCrem,
         label='Face cream', marker='o', linewidth=3)
plt.plot(monthList, faceWash,
         label='Face Wash',  marker='o', linewidth=3)
plt.plot(monthList, toothPaste,
         label='Tooth Paste', marker='o', linewidth=3)
plt.plot(monthList, bathingsoap,
         label='Bathing Soap', marker='o', linewidth=3)
plt.plot(monthList, shampoo,
         label='Shampoo', marker='o', linewidth=3)
plt.plot(monthList, moisturizer,
         label='Moisturizer', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 3000, 5000, 7000, 9000, 11000, 13000, 15000, 17000,19000])
plt.title('Sales data')
plt.show()