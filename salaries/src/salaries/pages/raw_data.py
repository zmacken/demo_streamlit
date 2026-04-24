import streamlit as st
from salaries.utils.constants import DATA_PATH
import pandas as pd
from salaries.utils.helpers import get_salaries_df


def raw_data():
    st.markdown("## Raw Data")
    st.dataframe(get_salaries_df())

if __name__ == "__main__":
    raw_data()