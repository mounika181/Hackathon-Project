import pandas as pd
df=pd.read_csv("final_food_delivery_dataset.csv")

gold_city=(df[df["membership"]=="Gold"].groupby("city")["total_amount"].sum().sort_values(ascending=False).head(1))
print("City with highest gold revenue:")
print(gold_city)

top_cuisine=(df.groupby("cuisine")["total_amount"].mean().sort_values(ascending=False).head(1) )
print(top_cuisine)

count_users=(df.groupby("user_id")["total_amount"].sum().gt(1000).sum())
print(count_users)

df["rating_range"]=pd.cut(df["rating"],bins=[3.0,3.5,4.0,4.5,5.0],labels=["3.0-3.5","3.6-4.0","4.1-4.5","4.6-5.0"])
top_rating=df.groupby("rating_range")["total_amount"].sum().idxmax()
print(top_rating)

print(df[df["membership"]=="Gold"].groupby("city")["total_amount"].mean().idxmax())

print(round(df[df.membership=='Gold'].order_id.nunique() / df.order_id.nunique()*100))

print(df.groupby('restaurant_name_x').agg(o=('order_id','nunique'),aov=('total_amount','mean')).query('o<20').sort_values('aov',ascending=False))

print(df.groupby(['membership','cuisine'])['total_amount'].sum().idxmax())

print(df.assign(q=pd.to_datetime(df['order_date']).dt.to_period('Q')).groupby('q')['total_amount'].sum().idxmax)

print(df[df['membership']=='Gold'].shape[0])

print(round(df[df['city']=='Hyderabad']['total_amount'].sum()))

print(df['user_id'].nunique())

print(round(df[df['membership']=='Gold']['total_amount'].mean(),2))

print(df[df['rating']>=4.5].shape[0])

print(df[(df['membership']=='Gold')&(df['city']==df[df['membership']=='Gold'].groupby('city')['total_amount'].sum().idxmax())].shape[0])

print(df.shape[0])