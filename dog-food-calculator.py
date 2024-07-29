import streamlit as st
import streamlit.components.v1 as components
import math

# Initialize session state
if 'result' not in st.session_state:
    st.session_state.result = False

# Title
st.title('🐶 사료 급여량 계산기 💻')


# Weight input
weight = st.text_input("🐶 무게 (kg):")

# Calories per gram input
calories_per_gram = st.text_input("🍫 사료 무게 당 칼로리 (kcal/g):")

# Condition buttons
conditions = [
    {'label': '4개월 이하', 'value': '4개월이하'},
    {'label': '5~12개월', 'value': '5~12개월'},
    {'label': '중성', 'value': '중성'},
    {'label': '비중성화', 'value': '비중성화'},
    {'label': '비만', 'value': '비만'},
    {'label': '체중감량', 'value': '체중감량'}
]

condition_labels = [cond['label'] for cond in conditions]
condition_values = [cond['value'] for cond in conditions]

condition_selected = st.selectbox(
    "🩺 강아지 나이",
    condition_labels,
    index=None,
    key='condition_radio'
)
try:
  condition = condition_values[condition_labels.index(condition_selected)]
except ValueError:
  condition = None
    
# Check if inputs are valid
def is_valid_input():
    try:
        weight_f = float(weight)
        calories_per_gram_f = float(calories_per_gram)
        return weight_f > 0 and calories_per_gram_f > 0 and condition in condition_values
    except ValueError:
        return False

# Update query parameters      
def update_query_param():
  st.query_params['weight'] = weight
  st.query_params['condition'] = condition
  st.query_params['caloriesPerGram'] = calories_per_gram      
      
# Calculate result      
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
    }.get(condition, None)
    
    DER = RER * factor
    daily_calories = DER
    food_amount = daily_calories / calories_per_gram_f
    
    st.session_state.result = True
    st.session_state.food_amount = round(food_amount, 2)
    st.session_state.daily_calories = round(daily_calories, 2)
    
    # Scroll to the result
    components.html(
        """
        <script>
            window.parent.document.getElementById('result').scrollIntoView();
        </script>
        """,
        height=0
    )
      
if not is_valid_input():
    st.write("`✅ 강아지 정보를 입력해주세요`")
else:
    calculate_result()
    
    # Display result
    st.markdown('<div id="result"></div>', unsafe_allow_html=True)
    if st.session_state.result is True:
      st.write(f"#### 🍚 하루 권장 사료 양(g) 👉 `{st.session_state.food_amount} g`")
      st.write(f"#### 🔥 하루 급여 칼로리(kcal) 👉 `{st.session_state.daily_calories} kcal`")
      

# Run the app with: streamlit run <filename>.py
