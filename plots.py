import pandas as pd
import plotly_express as px
import plotly.express 
df=pd.read_csv("Covid.csv")

fig= px.scatter(df,x="date",y="cases",color="country")
fig.show()