#main
import streamlit as st

def main():
    st.title("Schedule Management App")
    st.sidebar.title("Navigation")
    
    # Sidebar navigation
    page = st.sidebar.selectbox("Select a page", ["Academic Schedule", "Leisure Schedule"])
    
    if page == "Academic Schedule":
        import sheet.sheet01 as academic
        academic.academic_schedule()
    elif page == "Leisure Schedule":
        import sheet.sheet02 as leisure
        leisure.leisure_schedule()

if __name__ == "__main__":
    main()

#sheet 01
import streamlit as st
import plotly.express as px
import pandas as pd

def academic_schedule():
    st.title("Academic Schedule")
    
    # Placeholder for academic schedule data
    academic_events = st.session_state.get('academic_events', [])
    
    # Add new academic event
    with st.form(key='academic_form'):
        subject = st.text_input("Subject")
        date = st.date_input("Date")
        time = st.time_input("Time")
        submit_button = st.form_submit_button(label='Add Schedule')
        
        if submit_button and subject:
            academic_events.append({
                'subject': subject,
                'date': date,
                'time': time
            })
            st.session_state.academic_events = academic_events
            st.success("Schedule added successfully!")
    
    # Display academic events
    if academic_events:
        st.subheader("Your Academic Schedules")
        for event in academic_events:
            st.write(f"{event['subject']} on {event['date']} at {event['time']}")
        
        # Convert events to DataFrame for visualization
        df = pd.DataFrame(academic_events)
        df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
        
        # Plot calendar view
        st.subheader("Academic Schedule Calendar")
        fig = px.timeline(
            df,
            x_start="datetime",
            x_end="datetime",
            y="subject",
            title="Academic Schedule",
            labels={"datetime": "Date & Time", "subject": "Subject"}
        )
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No academic schedules added yet.")

if __name__ == "__main__":
    academic_schedule()

#sheet02
import streamlit as st
import plotly.express as px
import pandas as pd

def leisure_schedule():
    st.title("Leisure Schedule")
    
    # Placeholder for leisure schedule data
    leisure_events = st.session_state.get('leisure_events', [])
    
    # Add new leisure event
    with st.form(key='leisure_form'):
        event_name = st.text_input("Event Name")
        event_date = st.date_input("Event Date")
        event_time = st.time_input("Event Time")
        submit_button = st.form_submit_button(label='Add Event')
        
        if submit_button and event_name:
            leisure_events.append({
                'name': event_name,
                'date': event_date,
                'time': event_time
            })
            st.session_state.leisure_events = leisure_events
            st.success("Event added successfully!")
    
    # Display leisure events
    if leisure_events:
        st.subheader("Your Leisure Events")
        for event in leisure_events:
            st.write(f"{event['name']} on {event['date']} at {event['time']}")
        
        # Convert events to DataFrame for visualization
        df = pd.DataFrame(leisure_events)
        df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
        
        # Plot calendar view
        st.subheader("Leisure Schedule Calendar")
        fig = px.timeline(
            df,
            x_start="datetime",
            x_end="datetime",
            y="name",
            title="Leisure Schedule",
            labels={"datetime": "Date & Time", "name": "Event Name"}
        )
        fig.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No leisure events scheduled yet.")

if __name__ == "__main__":
    leisure_schedule()
