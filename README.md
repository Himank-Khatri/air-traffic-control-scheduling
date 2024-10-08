# Air Traffic Control - Flight Scheduling Simulation

This web application simulates flight scheduling and landing using a combination of Priority Scheduling and First Come First Serve (FCFS) algorithms. It allows you to manage multiple flights with different priorities and landing times, visualizing the order of landings and flight queue in real time.

## Application Link

[Air Traffic Control Simulation Web App](https://air-traffic-control-simulation.streamlit.app/)

## Features

- **Flight Scheduling**: Add flights with a specific type (Emergency, Medical, Military, Commercial, Cargo), each having different landing priorities.
- **Landing Simulation**: Schedule and land all flights based on a combination of priority and their arrival time.
- **Gantt Chart Visualization**: View the order in which flights were landed through a Gantt chart.
- **Flight Queue Management**: Manage the current flight queue and view details of flights awaiting landing.
- **Real-Time Updates**: Get real-time updates on the landing process and the queue.

## Priority System

- **Emergency (Priority 1)**: Highest priority
- **Medical (Priority 2)**
- **Military (Priority 3)**
- **Commercial (Priority 4)**
- **Cargo (Priority 5)**: Lowest priority

## How to Use

1. **Add Flight**:
   - In the sidebar, input the landing time for the flight.
   - Select the flight type, which automatically assigns the corresponding priority.
   - Click "Add Flight" to add it to the queue.
   
2. **Schedule and Land Flights**:
   - Once all the flights are added, click "Schedule and Land All Flights" to begin the landing simulation.
   
3. **View Results**:
   - After landing, the order of landed flights is displayed along with a Gantt chart.
   - View the current queue of flights that are yet to land.

## Technical Details

- **Language**: Python
- **Framework**: Streamlit
- **Data Visualization**: Plotly (Gantt chart)
- **Backend**: Priority queue using Python’s `heapq` module
- **Time Handling**: Python’s `datetime` and `timedelta` modules for scheduling flights.

## Author

Himank Khatri,
Farhan Gandhi,
Parthiv Bhandary.
