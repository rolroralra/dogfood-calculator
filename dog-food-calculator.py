import streamlit as st
import math

# Weight input
st.title('Dog Food Calculator')
weight = st.text_input("Dog's Weight (kg):")

# Condition buttons
conditions = [
    {'label': '4개월 이하', 'value': '4개월이하'},
    {'label': '5~12개월', 'value': '5~12개월'},
    {'label': '중성', 'value': '중성'},
    {'label': '비중성화', 'value': '비중성화'},
    {'label': '비만', 'value': '비만'},
    {'label': '체중감량', 'value': '체중감량'}
]

st.write("Dog's Condition:")
condition_labels = [cond['label'] for cond in conditions]
condition_values = [cond['value'] for cond in conditions]
condition = st.radio(
    "",
    condition_labels,
    index=None
)

# Calories per gram input
calories_per_gram = st.text_input("Calories per Gram (kcal/g):")

# Check if inputs are valid
def is_valid_input(weight, calories_per_gram, condition):
    try:
        weight = float(weight)
        calories_per_gram = float(calories_per_gram)
        return weight > 0 and calories_per_gram > 0 and condition in condition_values
    except ValueError:
        return False
      
def calculate_result():
    weight_f = float(weight)
    calories_per_gram_f = float(calories_per_gram)
    
    RER = math.pow(weight_f, 0.75) * 70
    factor = {
        '4개월이하': 3,
        '5~12개월': 2,
        '중성': 1.6,
        '비중성화': 1.8,
        '비만': 1.4,
        '체중감량': 1
    }.get(condition, 1)
    
    DER = RER * factor
    daily_calories = DER
    food_amount = daily_calories / calories_per_gram_f
    
    st.session_state.result = round(food_amount, 2)
      
if st.button("Calculate"):
    if not is_valid_input(weight, calories_per_gram, condition):
        st.write("Please enter valid inputs.")
    else:
        calculate_result()

# # Calculate result if inputs are valid
if is_valid_input(weight, calories_per_gram, condition):
    calculate_result()
else:
    st.session_state.result = None

# Display result
if st.session_state.result is not None:
    st.write("### Result")
    st.write(f"하루 권장 사료 양: **{st.session_state.result} g**")
    
# Run the app with: streamlit run <filename>.py
