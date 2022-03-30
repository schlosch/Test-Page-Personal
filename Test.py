
import streamlit as st
import pandas as pd

st.write("Ballert Bruder")

df = pd.DataFrame({
    'first column': ['Jens', 'Richard', 'Oliver', 'Janosch', 'Paul', 'Florian', 'Philipp'],
    'second column': [10, 20, 30, 40,  30, 40, 30]
    })

option = st.selectbox(
    'Which member do you like best?',
     df['first column'])

'You selected: ', option

from PIL import Image
image = Image.open('bb.jpeg')

st.image(image, caption='Ehrenvolles Gemälde - Künstler unbekannt')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Bestimme dein Level',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:

if left_column.button('Nicht drücken'):
     st.write('Warum drückst du, wenn es ausdrücklich heißt "nicht drücken"')
else:
     st.write('Alles ist ruhig')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Bestimme deine Rolle',
        ("Jünger", "Gut riechend", "First Kill Philipp"))
    st.write(f"Du bist {chosen}!")