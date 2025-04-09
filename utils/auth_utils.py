import streamlit as st

def login_required(func):
    """
    Decorator to ensure user is logged in before accessing certain pages
    """
    def wrapper(*args, **kwargs):
        if not st.experimental_user.is_logged_in:
            st.error("Please log in to access this page.")
            st.button("Go to Login Page", on_click=lambda: st.switch_page("app.py"))
            return
        return func(*args, **kwargs)
    return wrapper

def login_screen():
    """
    Display the login screen with Google authentication button
    """
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://via.placeholder.com/150", width=150)
        st.title("Daily Activity Tracker")
        st.subheader("Your AI-powered personal assistant")
        
        st.markdown("---")
        st.subheader("Please log in to continue")
        st.button("🔑 Log in with Google", 
                 key="login_button", 
                 on_click=st.login,
                 use_container_width=True)
        
        st.markdown("---")
        st.caption("Your data stays local - we respect your privacy")

def get_user_info():
    """
    Get user information from the authentication token
    """
    if not st.experimental_user.is_logged_in:
        return None
    
    return {
        "name": st.experimental_user.name,
        "email": st.experimental_user.email,
        "id": st.experimental_user.id
    }