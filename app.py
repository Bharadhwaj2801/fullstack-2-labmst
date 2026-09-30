import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="NERCHUKO",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
    color: #2563eb;
}

.subtitle {
    font-size: 18px;
    color: #555;
}

.card {
    background-color: #f8fafc;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
    margin-bottom: 15px;
}

.course-title {
    font-size: 24px;
    font-weight: bold;
    color: #1e293b;
}

.skill {
    background-color: #dbeafe;
    padding: 8px 14px;
    border-radius: 20px;
    display: inline-block;
    margin: 5px;
    color: #1e40af;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🎓 NERCHUKO</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Online Learning Dashboard</div>',
    unsafe_allow_html=True
)

st.divider()

st.sidebar.title("NERCHUKO")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "User Details", "Courses"]
)


if page == "Dashboard":

    st.header("📊 Learning Dashboard")

    # User information
    st.subheader("👤 User Details")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Name", "Bharadhwaj")

    with col2:
        st.metric("Mail", "student@example.com")

    with col3:
        st.metric("Contact", "+91 9876543210")

    with col4:
        st.metric("Ongoing Course", "Python")


    st.divider()

    st.subheader("📚 Ongoing Course")

    course_name = "Python Programming"

    completion = 72

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown(
            f'<div class="card">'
            f'<div class="course-title">{course_name}</div>'
            f'<p>Learn Python programming from basics to advanced concepts.</p>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.write("Course Completion")

        st.progress(completion / 100)

        st.write(f"**{completion}% completed**")

    with col2:

        st.metric(
            "Completion",
            f"{completion}%"
        )

        st.metric(
            "Lessons Completed",
            "18 / 25"
        )


    st.divider()

    st.subheader("🧠 Skills Learnt")

    skills = [
        "Python Basics",
        "Variables",
        "Loops",
        "Functions",
        "Lists",
        "Dictionaries",
        "Data Analysis",
        "Pandas"
    ]

    for skill in skills:

        st.markdown(
            f'<span class="skill">{skill}</span>',
            unsafe_allow_html=True
        )


    st.divider()

    st.subheader("📈 Course Progress")

    progress_data = pd.DataFrame({
        "Course": [
            "Python",
            "Data Analysis",
            "SQL",
            "Machine Learning"
        ],

        "Completion": [
            72,
            45,
            30,
            10
        ]
    })

    fig = px.bar(
        progress_data,
        x="Course",
        y="Completion",
        text="Completion",
        title="Learning Progress"
    )

    fig.update_traces(
        texttemplate="%{text}%",
        textposition="outside"
    )

    fig.update_yaxes(
        range=[0, 100],
        title="Completion (%)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


elif page == "User Details":

    st.header("👤 User Details")

    st.text_input(
        "Name",
        value="Bharadhwaj"
    )

    st.text_input(
        "Mail",
        value="student@example.com"
    )

    st.text_input(
        "Contact",
        value="+91 9876543210"
    )

    st.text_input(
        "Ongoing Course",
        value="Python Programming"
    )

    if st.button("Save Details"):

        st.success(
            "User details saved successfully!"
        )


elif page == "Courses":

    st.header("📚 My Courses")

    courses = {
        "Python Programming": 72,
        "Data Analysis": 45,
        "SQL": 30,
        "Machine Learning": 10
    }

    for course, progress in courses.items():

        st.markdown(
            f"### {course}"
        )

        st.progress(
            progress / 100
        )

        st.write(
            f"{progress}% completed"
        )

        st.divider()
