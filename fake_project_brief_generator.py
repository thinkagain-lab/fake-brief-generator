import streamlit as st
from faker import Faker

# Initialize Faker
fake = Faker()

def generate_fake_brief(project_type, industry):
    objectives = fake.paragraph(nb_sentences=3)
    audience = fake.sentence(nb_words=8)
    requirements = fake.paragraph(nb_sentences=4)
    outcomes = fake.paragraph(nb_sentences=3)
    
    brief = f"""
    **Project Type**: {project_type}
    **Industry**: {industry}
    
    **Project Objectives**:
    {objectives}
    
    **Target Audience**:
    {audience}
    
    **Key Requirements**:
    {requirements}
    
    **Expected Outcomes**:
    {outcomes}
    """
    
    return brief

def main():
    st.title("Fake Project Brief Generator")

    # Input fields
    project_type = st.selectbox("Select Project Type", ["Logo", "Branding", "Illustration", "Web Design", "App Design", "Marketing Campaign", "Packaging Design"])
    industry = st.selectbox("Select Industry", ["Food", "Retail", "Education", "Healthcare", "Technology", "Finance", "Entertainment", "Travel", "Real Estate"])

    # Generate button
    if st.button("Generate"):
        with st.spinner("Generating brief..."):
            brief = generate_fake_brief(project_type, industry)
            st.success("Fake Project Brief Generated!")
            st.markdown(brief)

if __name__ == "__main__":
    main()
