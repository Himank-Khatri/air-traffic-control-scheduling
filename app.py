import streamlit as st
import heapq
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px

# Define a Flight class to represent each flight
class Flight:
    def __init__(self, flight_id, priority, landing_time, plane_type):
        self.flight_id = flight_id
        self.priority = priority  # Lower number = Higher priority
        self.landing_time = landing_time  # Time to land in minutes
        self.plane_type = plane_type
        self.arrival_time = datetime.now()
        self.start_time = None
        self.end_time = None

    def __lt__(self, other):
        # Priority scheduling: Compare based on priority first, then FCFS based on arrival_time
        return (self.priority, self.arrival_time) < (other.priority, other.arrival_time)

    def __repr__(self):
        return f"Flight(ID: {self.flight_id}, Type: {self.plane_type}, Priority: {self.priority}, Landing Time: {self.landing_time} minutes)"

# Function to create a new flight object
def create_new_flight(flight_id, priority, landing_time, plane_type):
    return Flight(flight_id, priority, landing_time, plane_type)

# Streamlit app
def main():
    st.title("Air Traffic Control - Flight Scheduling with Priority and FCFS")

    # Initialize the flight queue and execution history
    if 'flight_queue' not in st.session_state:
        st.session_state.flight_queue = []

    if 'execution_history' not in st.session_state:
        st.session_state.execution_history = []

    if 'last_end_time' not in st.session_state:
        st.session_state.last_end_time = datetime.now()  # Initialize last end time

    # Sidebar input form for flight details
    st.sidebar.header("Enter Flight Details")
    
    # Automatic increment of Flight ID
    flight_id = len(st.session_state.execution_history) + len(st.session_state.flight_queue) + 1

    # Select the type of plane to set priority
    plane_type = st.sidebar.selectbox("Type of Plane (with Priority)", 
                                       options=["Emergency (Priority 1)", "Medical (Priority 2)", "Military (Priority 3)", "Commercial (Priority 4)", "Cargo (Priority 5)"],
                                       help="Emergency has highest priority and Cargo has the lowest.")

    # Map plane type to priority
    plane_priority_map = {
        "Emergency (Priority 1)": 1,
        "Medical (Priority 2)": 2,
        "Military (Priority 3)": 3,
        "Commercial (Priority 4)": 4,
        "Cargo (Priority 5)": 5
    }
    priority = plane_priority_map[plane_type]

    # Input landing time (in minutes)
    landing_time = st.sidebar.number_input("Landing Time (in minutes)", min_value=1, value=10)

    # Button to add flight
    if st.sidebar.button("Add Flight"):
        if flight_id:
            # Create a new flight object and add to the queue
            new_flight = create_new_flight(flight_id, priority, landing_time, plane_type)
            heapq.heappush(st.session_state.flight_queue, new_flight)
            st.sidebar.success(f"Flight {flight_id} (Type: {plane_type}) added to the queue with priority {priority}")

    # Button to schedule and land all flights
    if st.sidebar.button("Schedule and Land All Flights"):
        if st.session_state.flight_queue:
            while st.session_state.flight_queue:
                # Get the next flight to land (Priority + FCFS)
                next_flight = heapq.heappop(st.session_state.flight_queue)

                # Simulate the landing process
                landing_duration = timedelta(minutes=next_flight.landing_time)

                # Set the start time based on the last end time
                next_flight.start_time = st.session_state.last_end_time
                next_flight.end_time = next_flight.start_time + landing_duration
                
                # Update the last end time for the next flight
                st.session_state.last_end_time = next_flight.end_time

                # Store flight execution in history
                st.session_state.execution_history.append({
                    'Flight': next_flight.flight_id,
                    'Priority': next_flight.priority,  # Add priority to execution history
                    'Start': next_flight.start_time,
                    'End': next_flight.end_time
                })

            st.sidebar.success("All flights have been successfully landed!")

        else:
            st.sidebar.warning("No flights to schedule.")

    # Display the order in which flights were landed
    st.subheader("Order of Flights Landed")
    if st.session_state.execution_history:
        history_df = pd.DataFrame(st.session_state.execution_history)

        # Create the Gantt chart using Plotly without gradient color
        fig = px.timeline(history_df, x_start="Start", x_end="End", y="Flight", title="Flight Landing Gantt Chart")
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig)

        # Format start and end time to show only hours and minutes in a separate DataFrame for display
        history_df['Start'] = history_df['Start'].dt.strftime('%H:%M')
        history_df['End'] = history_df['End'].dt.strftime('%H:%M')

        st.dataframe(history_df[['Flight', 'Priority', 'Start', 'End']])  # Show priority in the DataFrame

    # Display the current flight queue in DataFrame
    st.subheader("Current Flight Queue")
    if st.session_state.flight_queue:
        queue_data = {
            'Flight ID': [],
            'Type': [],
            'Priority': [],
            'Landing Time (min)': []
        }
        for flight in st.session_state.flight_queue:
            queue_data['Flight ID'].append(flight.flight_id)
            queue_data['Type'].append(flight.plane_type)
            queue_data['Priority'].append(flight.priority)
            queue_data['Landing Time (min)'].append(flight.landing_time)

        queue_df = pd.DataFrame(queue_data)
        st.dataframe(queue_df)
    else:
        st.write("No flights in the queue.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
