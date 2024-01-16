import streamlit as st

st.title("BMI Calculator")


def bmi_calc(weight, height):
    bmi = weight / (height ** 2)
    return bmi

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("Enter your weight (in kgs)")
with col2:
    height = st.number_input("Enter your height (in meters)")

but =  st.button("Calculate BMI")
if but:
    bmi = bmi_calc(weight, height)
    st.write("Your BMI is: ", bmi)
    if bmi < 18.5:
        st.warning("You are Underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.success("You are Healthy")
    elif bmi >= 25 and bmi < 30:
        st.warning("You are Overweight")
    elif bmi >= 30:
        st.error("You are Obese")
    else:
        st.error("Please enter valid details")
    