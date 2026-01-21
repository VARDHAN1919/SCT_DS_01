import matplotlib.pyplot as plt
import pandas as pd
iphone=pd.read_csv("iphone.csv")
colors=["red","blue","green","yellow","brown","pink","orange"]
plt.bar(iphone["Model"],iphone["Sales"],color=colors)
plt.xlabel("iPhone Model")
plt.ylabel("Sales (Million Units)")
plt.title("iPhone Sales by Model")
plt.xticks(rotation=90,ha="center",fontsize=10)
plt.show()