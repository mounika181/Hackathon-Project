import pandas as pd
import sqlite3
orders=pd.read_csv("orders.csv")
users=pd.read_json("users.json")
conn=sqlite3.connect(":memory:")
with open ("restaurants.sql","r")as f:
    sql_script=f.read()
conn.executescript(sql_script)
restaurants=pd.read_sql("SELECT * FROM restaurants",conn)
print("Orders loaded:",orders.shape)
print("Users loaded:",users.shape)
print("Restaurants loaded:",restaurants.shape)
merged_df = orders.merge(users,on="user_id",how="left")
final_df = merged_df.merge(restaurants,on="restaurant_id",how="left")
final_df.to_csv("final_food_delivery_dataset.csv",index=False)
print("Final dataset saved successfully")
