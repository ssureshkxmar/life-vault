import streamlit as st
import datetime

def main():
    st.markdown('<h2 style="color: #00f3ff;">📅 Professional Attendance Tracker</h2>', unsafe_allow_html=True)
    st.write("Maintain your academic consistency with our professional tracking system.")

    # Student Details
    st.markdown("### Profile Verification")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Student Name", placeholder="Enter full name")
        student_id = st.text_input("Student ID", placeholder="ID-XXXX")
    with col2:
        course = st.selectbox("Select Course", ["Computer Science", "Engineering", "Medicine", "Arts", "Commerce", "Law"])
        section = st.text_input("Section", placeholder="e.g. A2")

    st.markdown("---")
    
    # Attendance Entry
    st.markdown("### Attendance Logging")
    col3, col4 = st.columns(2)
    with col3:
        date = st.date_input("Select Date", datetime.date.today())
        status = st.radio("Attendance Status", ["Present ✅", "Absent ❌", "Late ⏳"], horizontal=True)
    
    with col4:
        reason = st.text_area("Remarks/Notes", placeholder="Optional: E.g. Medical leave, technical issues...")

    if st.button("💾 Submit Attendance Log", use_container_width=True):
        if not name or not student_id:
            st.error("Please provide both Name and Student ID for professional logging.")
        else:
            # Here we would typically save to a database. For now, we simulate success.
            st.success(f"Successfully logged attendance for {name} ({student_id}) on {date}.")
            st.info(f"Status: {status}")
            
            # Show summary stats
            st.markdown("#### Weekly Summary")
            cols = st.columns(3)
            cols[0].metric("Attendance Rate", "94%", "+2%")
            cols[1].metric("Classes Attended", "28/30", "+1")
            cols[2].metric("Consistency Score", "A+", "Elite")

    # Historical Logs (Placeholder)
    st.markdown("---")
    st.markdown("### Recent Log History")
    history_data = [
        {"Date": "2026-03-25", "Status": "Present", "Remarks": "Regular Class"},
        {"Date": "2026-03-24", "Status": "Present", "Remarks": "Lab Session"},
        {"Date": "2026-03-23", "Status": "Late", "Remarks": "Traffic delay"}
    ]
    st.table(history_data)
