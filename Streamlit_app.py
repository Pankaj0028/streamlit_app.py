import streamlit as st
import pandas as pd
import datetime

# --------------------------
# Sample Destination Data
# --------------------------
import streamlit as st
import pandas as pd
import datetime

# --------------------------
# Sample Destination Data with Valid Image URLs
# --------------------------
destinations = [
    {
        "id": 1,
        "place": "Goa",
        "price": 15000,
        "duration": "5 Days",
        "type": "Beach",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    },
    {
        "id": 2,
        "place": "Manali",
        "price": 12000,
        "duration": "6 Days",
        "type": "Hill Station",
        "image": "https://surl.li/duqeuy"
    },
    {
        "id": 3,
        "place": "Dubai",
        "price": 55000,
        "duration": "7 Days",
        "type": "International",
        "image": "https://images.unsplash.com/photo-1504274066651-8d31a536b11a"
    },
    {
        "id": 4,
        "place": "Kerala",
        "price": 18000,
        "duration": "5 Days",
        "type": "Backwaters",
        "image": "https://images.unsplash.com/photo-1507525428034-7b724efc8f32"
    },
    {
        "id": 5,
        "place": "Jaipur",
        "price": 14000,
        "duration": "4 Days",
        "type": "Heritage",
        "image": "https://images.unsplash.com/photo-1603262110263-fb0e401e0d9d"
    },
    {
        "id": 6,
        "place": "Shimla",
        "price": 13000,
        "duration": "5 Days",
        "type": "Hill Station",
        "image": "https://images.unsplash.com/photo-1548013146-72479768bada"
    },
    {
        "id": 7,
        "place": "Singapore",
        "price": 60000,
        "duration": "6 Days",
        "type": "International",
        "image": "https://images.unsplash.com/photo-1505761671935-60b3a7427bad"
    },
    {
        "id": 8,
        "place": "Andaman",
        "price": 35000,
        "duration": "7 Days",
        "type": "Island",
        "image": "https://images.unsplash.com/photo-1587620962725-abab7fe55159"
    },
    {
        "id": 9,
        "place": "Paris",
        "price": 85000,
        "duration": "8 Days",
        "type": "International",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34"
    },
    {
        "id": 10,
        "place": "Kashmir",
        "price": 20000,
        "duration": "6 Days",
        "type": "Hill Station",
        "image": "https://images.unsplash.com/photo-1603782921746-7f0a798c2e6b"
    },
    {
        "id": 11,
        "place": "Bali",
        "price": 45000,
        "duration": "6 Days",
        "type": "International",
        "image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"
    },
    {
        "id": 12,
        "place": "Rajasthan",
        "price": 25000,
        "duration": "7 Days",
        "type": "Desert",
        "image": "https://images.unsplash.com/photo-1589977997772-4f49a67c8cf8"
    },
    {
        "id": 13,
        "place": "Thailand",
        "price": 40000,
        "duration": "6 Days",
        "type": "International",
        "image": "https://images.unsplash.com/photo-1526481280698-8fccd6a8cf98"
    },
    {
        "id": 14,
        "place": "Ladakh",
        "price": 28000,
        "duration": "8 Days",
        "type": "Adventure",
        "image": "https://images.unsplash.com/photo-1610534508540-9f7baf5120a9"
    },
    {
        "id": 15,
        "place": "Maldives",
        "price": 75000,
        "duration": "6 Days",
        "type": "Island",
        "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"
    }
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
