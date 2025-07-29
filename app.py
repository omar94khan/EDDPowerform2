import streamlit as st
from datetime import date

def main():
    st.title("Enhanced Due Diligence (EDD) Form - Version 1.3")

    # 1. Customer Details
    st.header("1. Customer Details")
    customer_name = st.text_input("Customer Name")
    id_number = st.text_input("Identification Number (CPR, Passport, etc.)")

    # 2. High Risk Classification
    st.header("2. High Risk Classification")
    st.markdown("Please select all applicable classifications")

    risk_classifications = {
        "High risk business/activity": ["3", "4.1", "4.7", "4.8", "4.9", "4.10", "5"],
        "Non-resident individual or entity": ["3", "4.2", "4.7", "4.8", "4.9", "4.10", "5"],
        "Dealing with or resident of High risk jurisdiction": ["3", "4.3", "4.7", "4.8", "4.9", "4.10", "5"],
        "Politically Exposed Person (PEP)": ["3", "4.4", "4.7", "4.8", "4.9", "5"],
        "Related to PEP (PEP-R)": ["3", "4.5", "4.7", "4.8", "4.9", "5"],
        "Associates of PEP (PEP-A)": ["3", "4.6", "4.7", "4.8", "4.9", "4.10", "5"],
        "Club, Charity, or Other Society": ["3", "4.8", "4.9", "4.11", "5"],
        "Pooled Fund": ["3", "4.7", "4.8", "4.9", "4.10", "4.12", "5"],
        "Correspondent Banking Relationship": ["3", "4.10", "4.13", "5"],
        "Introduced Business from Professional Intermediaries": ["3", "4.7", "4.8", "4.9", "4.10", "4.13", "5"]
    }

    selected_risks = []
    for key in risk_classifications.keys():
        if st.checkbox(key):
            selected_risks.append(key)

    # 3. General Enhanced Due Diligence Measures
    if selected_risks:
        st.header("3. General Enhanced Due Diligence Measures")
        st.subheader("Evidence of Address")
        st.checkbox("Through Credit Reference Agency")
        st.checkbox("Verification by visit")
        st.date_input("Date of Visit", value=datetime.today())
        st.text_input("Staff Name")
        st.text_input("Other (please specify)")

        st.subheader("Source of Wealth")
        st.text_area("Describe the source of wealth")

        st.subheader("Source of Funds")
        st.text_area("Describe the origin of funds")

        st.subheader("Purpose & Utility of the Account")
        st.checkbox("Depository Relation")
        st.checkbox("Facility Settlement")
        st.text_input("Other Purpose")

    # Dynamic Sections
    def show_section(title, required):
        st.header(title)
        for item in required:
            st.markdown(f"Fill **Section {item}** based on classification requirements.")

    if selected_risks:
        st.header("4. Specific Enhanced Due Diligence Sections Required")
        for risk in selected_risks:
            show_section(risk, risk_classifications[risk])

    # 5. Screening
    st.header("5. Screening (Mandatory)")
    st.radio("World Check Screening", ["Positive Match", "False Match"])
    st.text_area("Findings")
    st.radio("Public Domain Info", ["Adverse media", "Neutral media", "No Match"])
    st.text_area("Findings (Media)")

    # 6. Verification
    st.header("6. Verification")
    st.text_input("Account Officer Name")
    st.text_input("Account Officer Designation")
    st.date_input("Verification Date (Officer)", value=datetime.today())

    st.text_input("Compliance Name")
    st.text_input("Compliance Designation")
    st.date_input("Verification Date (Compliance)", value=datetime.today())

    # 7. Executive Management Approval
    st.header("7. Executive Management Approval")
    st.selectbox("New Customer Recommendation", ["Approved", "Reject"])
    st.selectbox("Existing Customer Recommendation", ["Continue", "Discontinue"])

    # 8. Post Account Opening
    st.header("8. Post Account Opening")
    st.text_input("CIF")
    st.text_input("Account Number")
    st.date_input("Date Account Opened")
    st.date_input("Date of Next Review")

    # Submit
    if st.button("Submit Form"):
        st.success("EDD Form submitted successfully!")



main()