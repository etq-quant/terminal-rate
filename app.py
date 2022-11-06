import streamlit as st
import pandas as pd
from plot import *


st.set_page_config(
    page_title="US Terminal Rate", layout="wide",
)
st.title("US Terminal Rate")
DATA_PATH = "data/terminal_rate_data.csv"


@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv(DATA_PATH)
    df = df.ffill().dropna()
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")
    return df


df = load_data()

col1, col2 = st.columns(2)
start_date = col1.date_input(
    "Start Date", df.index.min(), df.index.min(), df.index.max()
)
end_date = col2.date_input("End Date", df.index.max(), df.index.min(), df.index.max())

st.write("Date:", start_date, end_date)


start_year, end_year = st.select_slider(
    "Year",
    options=df.index.year.unique(),
    value=(df.index.year.min(), df.index.year.max()),
)
st.write("Year:", start_year, end_year)

tdf = df.loc[start_date:end_date].copy()
tdf = tdf.loc[str(start_year) : str(end_year)].copy()

fig = create_plot(tdf)

start_date = tdf.index.min()
end_date = tdf.index.max()
st.plotly_chart(fig)
