import streamlit as st

st.title("🛒 Smart Grocer Calculator")

# Prices
RICE_PRICE = 60      # ₹ per kg
SUGAR_PRICE = 45     # ₹ per kg
OIL_PRICE = 120      # ₹ per litre

st.subheader("Enter Quantities")

# User inputs
rice_qty = st.number_input("Rice (kg)", min_value=0.0, step=0.5)
sugar_qty = st.number_input("Sugar (kg)", min_value=0.0, step=0.5)
oil_qty = st.number_input("Oil (litres)", min_value=0.0, step=0.5)

# Calculate button
if st.button("Calculate Bill"):
    # Billing logic
    total_before_discount = (rice_qty * RICE_PRICE) + (sugar_qty * SUGAR_PRICE) + (oil_qty * OIL_PRICE)

    discount = 0
    if total_before_discount > 500:
        discount = total_before_discount * 0.10

    final_amount = total_before_discount - discount

    # Results
    st.subheader("📘 Bill Summary")
    st.write(f"**Total before discount:** ₹{total_before_discount:.2f}")
    st.write(f"**Discount applied:** ₹{discount:.2f}")
    st.write(f"**Final amount to pay:** ₹{final_amount:.2f}")
