import streamlit as st

def square(n:float) -> float:
    return n ** 2

# Function to test cube
def cube(n:float) -> float:
    return n ** 3

# Function to test fifth power
def fifth_power(n:float) -> float:
    return n ** 4
# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")

# Get user input
n = st.number_input("Enter an Number", value=1, step=1)

# Calculate results
square = square(n)
cube = cube(n)
fifth_power = fifth_power(n)

# Display results
st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")

