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
        "image": "https://unsplash.com/s/photos/manali"
    },
    {
        "id": 3,
        "place": "Dubai",
        "price": 40000,
        "duration": "6 Days",
        "type": "International",
        "image": "https://unsplash.com/s/photos/dubai"
    },
    {
        "id": 4,
        "place": "Kerala",
        "price": 18000,
        "duration": "6 Days",
        "type": "Backwaters",
        "image": "https://unsplash.com/s/photos/kerala"
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
