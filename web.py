import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("placement_model.pkl", "rb"))

# Page Configuration
st.set_page_config(
    page_title="Job Placement Prediction System",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Job Placement Prediction System")
st.write("Predict whether a student is likely to get placed based on academic and skill-related factors.")

# User Inputs

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

internships = st.number_input(
    "Number of Internships",
    min_value=0,
    max_value=20,
    value=1
)

projects = st.number_input(
    "Number of Projects",
    min_value=0,
    max_value=20,
    value=2
)

workshops = st.number_input(
    "Workshops / Certifications",
    min_value=0,
    max_value=20,
    value=1
)

aptitude = st.slider(
    "Aptitude Test Score",
    min_value=0,
    max_value=100,
    value=70
)

softskills = st.slider(
    "Soft Skills Rating",
    min_value=1,
    max_value=10,
    value=5
)

extra = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

training = st.selectbox(
    "Placement Training",
    ["No", "Yes"]
)

ssc = st.number_input(
    "SSC Marks (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

hsc = st.number_input(
    "HSC Marks (%)",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

# Convert Yes/No to Encoded Values
extra = 1 if extra == "Yes" else 0
training = 1 if training == "Yes" else 0

# Predict Button
if st.button("Predict Placement"):

    input_data = pd.DataFrame({
        "CGPA": [cgpa],
        "Internships": [internships],
        "Projects": [projects],
        "Workshops/Certifications": [workshops],
        "AptitudeTestScore": [aptitude],
        "SoftSkillsRating": [softskills],
        "ExtracurricularActivities": [extra],
        "PlacementTraining": [training],
        "SSC_Marks": [ssc],
        "HSC_Marks": [hsc]
    })

    #prediction = model.predict(input_data)[0]

    #probability = model.predict_proba(input_data)[0][1]
    prediction = model.predict(input_data)[0]

    probs = model.predict_proba(input_data)[0]    
    st.subheader("Prediction Result")

    #if prediction == 1:
    #    st.success("✅ Student is likely to be Placed")
    #else:
    #    st.error("❌ Student is likely to be Not Placed")
    if prediction == "Placed":
        st.success("✅ Student is likely to be Placed")
    else:
        st.error("❌ Student is likely to be Not Placed")
    st.metric(
        "Placement Probability",
        f"{probs[1] * 100:.2f}%"
    )

    st.subheader("Career Recommendations")

    if cgpa < 7:
        st.warning("Improve CGPA to increase placement chances.")

    if internships == 0:
        st.warning("Complete at least one internship.")

    if projects < 2:
        st.warning("Build more academic or industry projects.")

    if aptitude < 60:
        st.warning("Improve aptitude and problem-solving skills.")

    if softskills < 5:
        st.warning("Work on communication and soft skills.")

    if training == 0:
        st.warning("Attend placement training sessions.")

    if (
        cgpa >= 7 and
        internships >= 1 and
        projects >= 2 and
        aptitude >= 60 and
        softskills >= 5
    ):
        st.success("🎉 Strong profile for campus placements!")