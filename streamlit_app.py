import streamlit as st
import pandas as pd 
import time
import altair as alt

st.header('My App')

@st.cache_data
def load_data():
    return pd.read_csv('https://github.com/dataprofessor/population-dashboard/raw/master/data/us-population-2010-2019-reshaped.csv', index_col=0)

df = load_data()

# Year selection
# Using st.number_input
#selected_year = st.number_input('Enter a year',
#                                placeholder='Enter a year from 2010-2019',
#                                value=2019)

# Using st.selectbox
selected_year = st.selectbox('Select a year',
                             list(df.year.unique())[::-1])

# Display data subset
df_selected_year = df[df.year == selected_year]
st.dataframe(df_selected_year, height=250, use_container_width=True)

# Display chart
st.bar_chart(df_selected_year,
             x='states',
             y='population')

st.header("Compare US state populations over time")
states = st.multiselect("Pick your states", list(df.states.unique())[::-1])
date_range = st.slider(
    "Pick your date range",
    2010, 2019, (2010, 2019))

st.write(date_range[0])

if states:
    chart_data = df[df['states'].isin(states)]
    # chart_data = chart_data[chart_data['year'].between(daterange[0],daterange[1])]
    chart_data = chart_data[(chart_data['year'] >= daterange[0]) & (chart_data['year'] <= daterange[1])]

    chart_data['year'] = chart_data['year'].astype(str)

    st.write(chart_data)

    # c = (
    #    alt.Chart(chart_data)
    #     .mark_line()
    #     .encode(x=alt.X('year:T'), 
    #             y=alt.Y('population'),
    #             color='states',)
    # )
    
    
    # c = (
    #    alt.Chart(chart_data)
    #     .mark_line()
    #     .encode(x=alt.X('year:T'), 
    #             y=alt.Y('population',scale=alt.Scale(domain=[30000000,50000000])))
    # )
    
    # st.altair_chart(c, use_container_width=True)

# st.write(chart_data)

# ca_data = df.loc[df['states'] == "California"]
# ca_chart_data = pd.DataFrame(ca_data, columns=["year", "population"])
# ca_chart_data['year'] = ca_chart_data['year'].astype(str)

# c = (
#    alt.Chart(ca_chart_data)
#     .mark_line()
#     .encode(x=alt.X('year:T'), 
#             y=alt.Y('population',scale=alt.Scale(domain=[37000000,40000000])))
# )

# # st.write(ca_data['population'].min())
# # st.write(ca_data['population'].max())

# st.subheader("California population over time")
# st.altair_chart(c, use_container_width=True)
