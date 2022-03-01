from turtle import color
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import plotly 
import plotly.express as px 
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import seaborn as sns
import altair as alt

# just using seaborn to get data 
penguins = sns.load_dataset('penguins')

fig = px.scatter(data_frame = penguins, 
    x = "bill_length_mm",
    y = "body_mass_g", 
    color = "species", 
    labels = dict(bill_length_mm = "Bill length (mm)",
        body_mass_g = "Body mass (g)", 
        species = "Species")
    )

# this code is broken
# fig.update_traces(customdata = penguins,
#     hovertemplate = "Species: %{species}<br>Island: %{island}<br>Sex: %{sex}").format()

fig.show()

tips = px.data.tips()
fig2 = px.bar(tips, x = 'day', y = 'total_bill', 
    color = 'smoker', barmode = 'group',
    facet_col= 'sex',
    category_orders={'day':['Thur', 'Fri', 'Sat', 'Sun']}, 
    width = 500, height = 500)

fig2.show()


mpg = sns.load_dataset("mpg")
fig3 = (
    alt.Chart(mpg)  # data set
    .mark_point()  # geometry
    .encode(x="horsepower", y="mpg", color="origin")  # encodings
)

fig3.show()
