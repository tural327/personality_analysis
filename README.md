# Personality analysis and Prediction 
Data token from kaggle description of columns are: <br />
> AcceptedCmp1 - 1 if customer accepted the offer in the 1st campaign, 0 otherwise <br />
AcceptedCmp2 - 1 if customer accepted the offer in the 2nd campaign, 0 otherwise <br />
AcceptedCmp3 - 1 if customer accepted the offer in the 3rd campaign, 0 otherwise <br />
AcceptedCmp4 - 1 if customer accepted the offer in the 4th campaign, 0 otherwise <br />
AcceptedCmp5 - 1 if customer accepted the offer in the 5th campaign, 0 otherwise <br />
Response (target) - 1 if customer accepted the offer in the last campaign, 0 otherwise <br />
Complain - 1 if customer complained in the last 2 years <br />
DtCustomer - date of customer’s enrolment with the company <br />
Education - customer’s level of education <br />
Marital - customer’s marital status <br />
Kidhome - number of small children in customer’s household <br />
Teenhome - number of teenagers in customer’s household <br />
Income - customer’s yearly household income <br />
MntFishProducts - amount spent on fish products in the last 2 years <br />
MntMeatProducts - amount spent on meat products in the last 2 years <br />
MntFruits - amount spent on fruits products in the last 2 years <br />
MntSweetProducts - amount spent on sweet products in the last 2 years <br />
MntWines - amount spent on wine products in the last 2 years <br />
MntGoldProds - amount spent on gold products in the last 2 years <br />
NumDealsPurchases - number of purchases made with discount <br />
NumCatalogPurchases - number of purchases made using catalogue <br />
NumStorePurchases - number of purchases made directly in stores <br />
NumWebPurchases - number of purchases made through company’s web site <br />
NumWebVisitsMonth - number of visits to company’s web site in the last month <br />
Recency - number of days since the last purchase <br />


# Data visualization

We can see main customers was born between 1970-1980

![](https://github.com/tural327/test/blob/main/img/birth.png) <br />

Most of cusomer's have higher education level

![](https://github.com/tural327/test/blob/main/img/edu.png) <br />

Incomes of customers mostly between 35.000 -70.000

![](https://github.com/tural327/test/blob/main/img/income.png) <br />

Customers purches from catalogue, discount, catalogue, directly in stores,through company’s web site

![](https://github.com/tural327/test/blob/main/img/purch.png) <br />


# Data Clustering
I used Kmean algorithm for clustering my data.
Firstly I tried to find best cluser size for my model
```python
wss=[]
K=range(1,10)
for i in K:
    kmean=KMeans(n_clusters=i)
    kmean.fit(df)
    wss.append(kmean.inertia_)
    plt.plot(K,wss,marker='x')
plt.xlabel('K clusters')
plt.ylabel('Erors')
plt.title("Finding optimal K kluster")
```
![](https://github.com/tural327/test/blob/main/img/cluster.png) <br />
