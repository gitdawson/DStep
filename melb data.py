
import pandas as pd
import matplotlib.pyplot as plt

mydata = pd.read_csv("C:/Users/dstephens/Downloads/melb_data.csv")

groupd = mydata.groupby(["SellerG"]).agg(Total_Value=('Price', 'sum')).sort_values(by='Total_Value',ascending=False).head(5)

# Create custom labels that show both percentage and value
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(pct*total/100.0)
        return f'${val:,.0f}\n({pct:.1f}%)'
    return my_autopct

plt.figure(figsize=(10, 8))
plt.pie(groupd['Total_Value'], labels=groupd.index, autopct=make_autopct(groupd['Total_Value']))
plt.title('Sales Output by Seller')

plt.legend()

plt.show()

