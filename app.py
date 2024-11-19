import streamlit as st
import main
st.title("Bane intervaltider kalkulator")
st.header("For de som har mere i benene en i hovedet")

st.divider()

st.text("Ønsket pace [min/km]")
minutes =st.slider("Minuter",min_value=2, max_value=10, value=4, step=1)
seconds = st.slider("Sekunder",min_value=0, max_value=59, value=0, step=1)
st.text("Lengde [m]")
length = st.slider("Lengde",min_value=100, max_value=10000, value=1000, step=100)

st.divider()

df = main.main_function(minutes, seconds, length)
st.text("Resultat")
st.dataframe(df)


