import streamlit as st
import os
from utils.auth_utils import login_screen, get_user_info

# Print available attributes for debugging
# Uncomment this to see what attributes are available
# if st.experimental_user.is_logged_in:
#     for attr in dir(st.experimental_user):
#         if not attr.startswith('_'):
#             print(f"Attribute: {attr}, Value: {getattr(st.experimental_user, attr)}")

# Configure page settings
st.set_page_config(
    page_title="Daily Activity Tracker",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS for better styling
st.markdown("""
<style>
    .stButton > button {
        background-color: #4285F4;
        color: white;
        font-weight: bold;
        border-radius: 4px;
        border: none;
        padding: 10px 15px;
    }
    .stButton > button:hover {
        background-color: #3367D6;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: normal;
        margin-bottom: 2rem;
        color: #666;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px;
        background-color: #f5f5f5;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# Check if user is logged in
if not st.experimental_user.is_logged_in:
    login_screen()
else:
    # Get user info
    user_info = get_user_info()
    
    # Main content for logged-in users
    col1, col2, col3 = st.columns([1, 3, 1])
    
    with col2:
        st.markdown(f"<h1 class='main-header'>Welcome, {user_info['name']}!</h1>", unsafe_allow_html=True)
        st.markdown("<p class='sub-header'>Your personal AI activity tracking assistant</p>", unsafe_allow_html=True)
        
        # Quick overview stats
        stat1, stat2, stat3 = st.columns(3)
        with stat1:
            st.metric(label="Activities Today", value="0")
        with stat2:
            st.metric(label="Streak", value="1 day")
        with stat3:
            st.metric(label="Completed", value="0%")
        
        # Main action buttons
        st.markdown("### What would you like to do today?")
        col_a, col_b = st.columns(2)
        with col_a:
            st.button("➕ Add New Activity", use_container_width=True)
        with col_b:
            st.button("📊 View Analytics", use_container_width=True)
        
        # Quick add section
        st.markdown("### Quick Add")
        activity = st.text_input("Activity name")
        col_c, col_d = st.columns(2)
        with col_c:
            duration = st.number_input("Duration (minutes)", min_value=5, max_value=240, step=5, value=30)
        with col_d:
            priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        
        st.button("Save Activity", use_container_width=True)
        
        # Reminders section
        st.markdown("### Upcoming Reminders")
        st.info("No reminders set for today. Add your first activity to get started!")
        
        # Logout option
        st.markdown("---")
        st.button("🚪 Log out", on_click=st.logout, key="logout_button")
    
    # Footer
    st.markdown(
        "<div class='footer'>Daily Activity Tracker © 2025 | Your data stays local</div>",
        unsafe_allow_html=True
    )