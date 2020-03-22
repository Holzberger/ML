import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
mylink = '../datasets/housesales.txt'

df     = pd.read_csv(mylink, delimiter=",")
df['date'] = df['date'].apply(pd.to_datetime)

# HouseSales
# This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.
# It contains 19 house features plus the price and the id columns, along with 21613 observations.
# It's a great dataset for evaluating simple regression models.

#Attributes:
#1. id INTEGER
#2. date STRING
#3. price REAL
#4. bedrooms INTEGER
#5. bathrooms REAL
#6. sqft_living INTEGER
#7. sqft_lot INTEGER
#8. floors REAL
#9. waterfront INTEGER
#10.view INTEGER
#11. condition INTEGER
#12. grade INTEGER
#13. sqft_above INTEGER
#14. sqft_basement INTEGER
#15. yr_built INTEGER
#16. yr_renovated INTEGER
#17. zipcode INTEGER
#18. lat REAL
#19. long REAL
#20. sqft_living15 INTEGER
#21. sqft_lot15 INTEGER

fig, axs = plt.subplots(3, 2,gridspec_kw={'hspace': 0.5, 'wspace': 0.1})
axs[0,0].hist(df['bedrooms'],bins=33,edgecolor="black",align='left')
axs[0,0].set_title('bedrooms')

axs[0,1].hist(df['yr_built'],bins=20,edgecolor="black",align='left')
axs[0,1].set_title("year built")

axs[1,0].hist(df['price'],bins=100,edgecolor="black",align='left')
axs[1,0].set_title("price")

axs[1,1].hist(df['sqft_living'],bins=50,edgecolor="black",align='left')
axs[1,1].set_title("Squarefoot living room")

axs[2,0].hist(df['bathrooms'],bins=8,edgecolor="black",align='left')
axs[2,0].set_title("bathrooms")

axs[2,1].hist(df['floors'],bins=5,edgecolor="black",align='left')
axs[2,1].set_title("floors")

#plt.savefig('HistogrammHouses.pdf')
#plt.title("age")
#plt.ylabel("number of samples")
#plt.show()