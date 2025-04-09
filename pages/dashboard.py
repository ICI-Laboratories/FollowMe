import streamlit as st
import pandas as pd
from utils.auth_utils import login_required, get_user_info

# Configure page settings
st.set_page_config(
    page_title="Dashboard - Daily Activity Tracker",
    page_icon="📊",
    layout="wide"
)

# Apply the login_required decorator to ensure authentication
@login_required
def dashboard_page():
    user_info = get_user_info()
    
    # Page header
    st.title("Activity Dashboard")
    st.subheader(f"Hello, {user_info['name']}! Here's your activity overview.")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["Daily Overview", "Weekly Stats", "Monthly Trends"])
    
    # Sample data - in a real app, this would come from a database
    with tab1:
        st.subheader("Today's Activities")
        
        # Sample data for demonstration
        if 'activities' not in st.session_state:
            # Create empty dataframe for demo purposes
            st.session_state.activities = pd.DataFrame({
                'Activity': [],
                'Duration': [],
                'Priority': [],
                'Status': []
            })
        
        # Display activities table
        if len(st.session_state.activities) == 0:
            st.info("No activities scheduled for today. Add your first activity to get started!")
        else:
            st.dataframe(st.session_state.activities, use_container_width=True)
        
        # Quick add form in this tab as well
        with st.expander("Add New Activity"):
            with st.form("add_activity_form"):
                activity_name = st.text_input("Activity Name")
                col1, col2 = st.columns(2)
                with col1:
                    duration = st.number_input("Duration (minutes)", min_value=5, step=5, value=30)
                with col2:
                    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
                
                submitted = st.form_submit_button("Add Activity")
                if submitted and activity_name:
                    # Add to the dataframe
                    new_activity = pd.DataFrame({
                        'Activity': [activity_name],
                        'Duration': [duration],
                        'Priority': [priority],
                        'Status': ['Pending']
                    })
                    st.session_state.activities = pd.concat([st.session_state.activities, new_activity], 
                                                         ignore_index=True)
                    st.success(f"Added '{activity_name}' to your activities!")
                    st.experimental_rerun()
    
    with tab2:
        st.subheader("Weekly Activity Summary")
        
        # Placeholder for weekly stats visualization
        st.markdown("### Activity Distribution")
        
        # Sample data for the chart
        chart_data = pd.DataFrame({
            'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            'Completed': [4, 2, 5, 3, 0, 0, 0],
            'Pending': [0, 1, 0, 2, 5, 4, 3]
        })
        
        # Display a simple bar chart
        st.bar_chart(
            chart_data.melt('Day', var_name='Status', value_name='Count').set_index('Day'),
            color=['#4CAF50', '#FFC107']
        )
    
    with tab3:
        st.subheader("Monthly Trends")
        st.info("Monthly analytics will be available after using the app for at least 30 days.")
        
        # Placeholder for future implementation
        st.markdown("### Coming Soon")
        st.markdown("""
        - Activity heatmap
        - Productivity score
        - AI-powered insights and suggestions
        - Customizable reports
        """)
    
    # Footer with logout option
    st.markdown("---")
    st.button("🚪 Log out", on_click=st.logout, key="logout_dashboard")

# Run the main function
if __name__ == "__main__":
    dashboard_page()