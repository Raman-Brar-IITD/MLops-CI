import streamlit as st

def square(n):
    return n ** 2

# Function to test cube
def cube(n) :
    return n ** 3

# Function to test fifth power
def fifth_power(n):
    return n ** 3
# Streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")

# Get user input
n = st.number_input("Enter an Number", value=1, step=1)

# Calculate results
squar = square(n)
cub = cube(n)
fifth_powe = fifth_power(n)

# Display results
st.write(f"The square of {n} is: {squar}")
st.write(f"The cube of {n} is: {cub}")
st.write(f"The fifth power of {n} is: {fifth_powe}")

