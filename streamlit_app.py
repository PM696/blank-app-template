import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

st.title("🎈 College Classification App")
st.divider()
st.write("This application classifies universities and colleges.")

@st.cache_data
def load_data():
    data = pd.read_csv('ml_dataset.csv')
    return data


# Load the model
model = load_model('my_first_best_pipeline')


def main():
    # Load dataset
    data = load_data()
    subset_cols=['exp_award_value',
        'awards_per_state_value',
        'grad_100_value',
        'counted_pct',
        'ft_pct',
        'pell_value',
        'ft_fac_value',
        'grad_150_value',
        'cohort_size',
        'aid_value']
    df=data[subset_cols]
    

    st.subheader("Data")
    st.write(df.head())

     # Prepare the input data
    input_data = {'Funds per award': exp_award_value,
                  'Awards given per State': awards_per_state_value,
                  'Graduate within time': grad_100_value,
                  'Counted percent': counted_pct,
                  'Percent of fulltime students': ft_pct,
                  'Pell grant amount': pell_value,
                  'Fulltime faculty contributions': ft_fac_value,
                  'Graduate within 1.5 time': grad_150_value,
                  'Cohort size': cohort_size,
                  'Aid value': aid_value}

    input_df = pd.DataFrame({input_data})

    # User input Features
    st.subheader("User Input Features:")

    exp_award_value = st.slider("Funds per award", min_value=float(
        df['exp_award_value'].min()), max_value=float(df['exp_award_value'].max()))
    awards_per_state_value = st.slider("Awards given per State", min_value=float(
        df['awards_per_state_value'].min()), max_value=float(df['awards_per_state_value'].max()))
    grad_100_value = st.slider("Graduate within time", min_value=float(
        df['grad_100_value'].min()), max_value=float(df['grad_100_value'].max()))
    counted_pct = st.slider("Counted percent", min_value=float(
        df['counted_pct'].min()), max_value=float(df['counted_pct'].max()))
    ft_pct = st.slider("Percent of fulltime students", min_value=float(
        df['ft_pct'].min()), max_value=float(df['ft_pct'].max()))
    pell_value = st.slider("Pell grant amount", min_value=float(
        df['pell_value'].min()), max_value=float(df['pell_value'].max()))
    ft_fac_value = st.slider("Fulltime faculty contributions", min_value=float(
        df['ft_fac_value'].min()), max_value=float(df['ft_fac_value'].max()))
    grad_150_value = st.slider("Graduate within 1.5 time", min_value=float(
        df['grad_150_value'].min()), max_value=float(df['grad_150_value'].max()))
    cohort_size = st.slider("Cohort size", min_value=float(
        df['cohort_size'].min()), max_value=float(df['cohort_size'].max()))
    aid_value = st.slider("Aid value", min_value=float(
        df['aid_value'].min()), max_value=float(df['aid_value'].max()))

    st.write("After selecting the above features using the slider, press on the 'Classify' button below to determine whether it is a high- or low-award institution.")
    
    # Make a prediction
    if st.button("Classify"):
        prediction = predict_model(model, data=df)
        st.write(f"Prediction: {prediction['Label'][0]}")

    st.subheader("Rate this App")
    st.feedback("stars")

    st.subheader("Message us:")
    prompt = st.text_input("Your message")
    if prompt:
        st.write(f"The user has sent: {prompt}")


if __name__ == "__main__":
    main()
