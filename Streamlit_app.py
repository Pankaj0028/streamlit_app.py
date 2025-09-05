import streamlit as st
import pandas as pd
import datetime

# --------------------------
# Sample Destination Data
# --------------------------
destinations = [
    {
        "id": 1,
        "place": "Goa",
        "price": 12000,
        "duration": "5 Days",
        "type": "Beach",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    },
    {
        "id": 2,
        "place": "Manali",
        "price": 15000,
        "duration": "7 Days",
        "type": "Hill Station",
        "image": "https://images.unsplash.com/photo-1606925797300-3a5c9d8c2a63"
    },
    {
        "id": 3,
        "place": "Dubai",
        "price": 40000,
        "duration": "6 Days",
        "type": "International",
        "image": "data:image/jpeg;base64,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"
    },
    {
        "id": 4,
        "place": "Kerala",
        "price": 18000,
        "duration": "6 Days",
        "type": "Backwaters",
        "image": "https://images.unsplash.com/photo-1518684079-3c830dcef090"
    },
]

df = pd.DataFrame(destinations)

# --------------------------
# App Config
# --------------------------
st.set_page_config(page_title="Travel SaaS", page_icon="🧳", layout="wide")
st.title("🧳 Tours & Travels SaaS Platform")
st.caption("Your one-stop SaaS tool for booking dream vacations ✈️")

# Initialize session
if "cart" not in st.session_state:
    st.session_state.cart = []

# --------------------------
# Sidebar Navigation
# --------------------------
menu = st.sidebar.radio("📌 Navigate", ["Home", "Browse Packages", "My Cart", "Checkout"])

# --------------------------
# Home Page
# --------------------------
if menu == "Home":
    st.header("🌍 Welcome Traveler!")
    st.write("Explore destinations, add packages to your cart, and book easily.")

# --------------------------
# Browse Packages
# --------------------------
elif menu == "Browse Packages":
    st.header("🏝️ Available Packages")

    filter_type = st.selectbox("Filter by Type", ["All"] + df["type"].unique().tolist())

    if filter_type != "All":
        filtered = df[df["type"] == filter_type]
    else:
        filtered = df

    for _, row in filtered.iterrows():
        with st.container():
            st.image(row["image"], width=400)
            st.subheader(f"{row['place']} ({row['duration']})")
            st.write(f"🌐 Type: {row['type']}")
            st.write(f"💰 Price per traveler: ₹{row['price']}")
            qty = st.number_input(f"Number of travelers for {row['place']}", min_value=1, max_value=20, step=1, key=row["id"])
            if st.button(f"Add {row['place']} to Cart", key=f"btn_{row['id']}"):
                st.session_state.cart.append({
                    "Destination": row["place"],
                    "Travelers": qty,
                    "Price": row["price"],
                    "Total": qty * row["price"]
                })
                st.success(f"Added {row['place']} for {qty} traveler(s) ✅")

# --------------------------
# My Cart
# --------------------------
elif menu == "My Cart":
    st.header("🛒 Your Cart")
    if st.session_state.cart:
        cart_df = pd.DataFrame(st.session_state.cart)
        st.dataframe(cart_df, use_container_width=True)
        st.info(f"Total Amount: ₹{cart_df['Total'].sum()}")
    else:
        st.warning("Your cart is empty. Browse packages to add.")

# --------------------------
# Checkout
# --------------------------
elif menu == "Checkout":
    st.header("💳 Checkout")
    if not st.session_state.cart:
        st.warning("Your cart is empty! Add some packages first.")
    else:
        with st.form("checkout_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            start_date = st.date_input("Start Date", min_value=datetime.date.today())
            confirm = st.form_submit_button("Confirm Booking ✅")

        if confirm:
            total = sum(item["Total"] for item in st.session_state.cart)
            st.success(f"🎉 Thank you {name}! Your booking is confirmed. Total = ₹{total}")
            st.session_state.cart.clear()
