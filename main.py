import streamlit as st
from custom_moduls import Jabama
import pandas as pd
from persiantools.jdatetime import JalaliDate

jab = Jabama()
st.title("Jabama Ramsar")
st.write("----")
today = JalaliDate.today()
st.markdown("#### Date - تاریخ:")

st.markdown("###### Start - از تاریخ:")
col = st.columns(3)
year_s = col[0].number_input("Year - سال", 1403, 1405, today.year)
mounth_s = col[1].number_input("Mounth - ماه", 1, 12, today.month)
day_s = col[2].number_input("Day - روز", 1, 31, today.day)

st.markdown("###### End - پایان تاریخ:")
col1 = st.columns(3)
year_e = col1[0].number_input(label="Year - سال", min_value=1403, max_value=1406, value=today.year)
mounth_e = col1[1].number_input("Mounth - ماه", 1, 13, today.month)
day_e = col1[2].number_input("Day - روز", 1, 31, day_s+1 if day_s < 31 else 1)

col = st.columns(2)
capacity = col[0].slider("Capacity - تعداد افراد", 0, 5, 0, help="تعداد افراد (بهتر است که صفر باشد)")
pages = col[1].number_input("Pages - تعداد صفحات", 0, 300, 0, help="تعداد صفحات اولی که اطلاعات را از انها میخواند. در صورت صفر بودن تمام صفحات را میخواند. و زمان بیشتری طول میکشد")

sub_btn = st.button("Submit", use_container_width=True)

if sub_btn:
    checkIn = str(year_s) + '-' + str(mounth_s) + '-' + str(day_s)
    checkOut = str(year_e) + '-' + str(mounth_e) + '-' + str(day_e)

    pages = 300 if pages == 0 else pages
    capacity = None if capacity == 0 else capacity

    with st.spinner("Please wait..."):
        mean_p, prices, url = jab.get_data(checkIn, checkOut, capacity, pages)
    
    col = st.columns(2)
    col[0].markdown(f"## Mean Price: {int(mean_p)}")
    col[1].metric('Mean: ', int(mean_p)/1000000, 'Million Toman', 'off')
    st.markdown(f"[site]({url+ str(1)})")
    st.markdown(f"### Number of Prices: {len(prices)}")

    df = pd.DataFrame(prices)
    st.dataframe(df.style.highlight_min(axis=0, color='yellow'), hide_index=True)