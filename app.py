import streamlit as st
from datetime import date

def main():
    st.title("Enhanced Due Diligence (EDD) Form - Version 1.3")

    # 1. Customer Details
    st.header("1. Customer Details")
    customer_name = st.text_input("Customer Name")
    id_number = st.text_input("Identification Number (CPR, Passport, etc.)")


    # 2. General Enhanced Due Diligence Measures
    # if selected_risks:
    st.header("2. General Enhanced Due Diligence Measures")
    st.subheader("Evidence of Address")
    st.checkbox("Through Credit Reference Agency")
    st.checkbox("Verification by visit")
    st.date_input("Date of Visit", value=date.today())
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
    
    
    # 3. High Risk Classification
    st.header("3. High Risk Classification")
    st.markdown("Please select all applicable classifications")

    risk_classifications = {
        "High risk business/activity":                          ["4.1", "4.7", "4.8", "4.9", "4.10", "5"],
        "Non-resident individual or entity":                    ["4.2", "4.7", "4.8", "4.9", "4.10", "5"],
        "Dealing with or resident of High risk jurisdiction":   ["4.3", "4.7", "4.8", "4.9", "4.10", "5"],
        "Politically Exposed Person (PEP)":                     ["4.4", "4.7", "4.8", "4.9", "5"],
        "Related to PEP (PEP-R)":                               ["4.5", "4.7", "4.8", "4.9", "5"],
        "Associates of PEP (PEP-A)":                            ["4.6", "4.7", "4.8", "4.9", "4.10", "5"],
        "Club, Charity, or Other Society":                      ["4.8", "4.9", "4.11", "5"],
        "Pooled Fund":                                          ["4.7", "4.8", "4.9", "4.10", "4.12", "5"],
        "Correspondent Banking Relationship":                   ["4.10", "4.13", "5"],
        "Introduced Business from Professional Intermediaries": ["4.7", "4.8", "4.9", "4.10", "4.13", "5"]
    }

    selected_risks = []
    for key in risk_classifications.keys():
        if st.checkbox(key):
            selected_risks.append(key)

    # Section 4.1 - High Risk Business/Activity
    if "High risk business/activity" in selected_risks:
        st.subheader("4.1 High Risk Business/Activity")
        st.text_input("Occupation / Nature of Business")
        st.text_input("ISIC Code")
        st.text_area("Business Activity Description")

    # Section 4.2 - Non-Resident Individual or Entity
    if "Non-resident individual or entity" in selected_risks:
        st.subheader("4.2 Non-Resident Individual or Entity")
        st.radio("Customer Type", ["Face-to-face", "Non face-to-face"])
        st.text_input("Country of Residency")
        st.radio("6 Month Bank Statement attached?", ["Yes", "No"])
        st.text_input("If not attached, provide reason")
        st.radio("Contact with Applicant", ["Yes", "No"])
        st.radio("Employment Verification", ["Yes", "No"])
        st.radio("Income Details Verified on Statement", ["Yes", "No"])
        st.text_area("Purpose of Opening Account in Bahrain")

    # Section 4.3 - High Risk Jurisdiction
    if "Dealing with or resident of High risk jurisdiction" in selected_risks:
        st.subheader("4.3 High Risk Jurisdiction")
        st.radio("Customer Type", [
            "Individual/Entity dealing with High Risk Jurisdiction",
            "Resident of High Risk Jurisdiction",
            "Entity incorporated in High Risk Jurisdiction"
        ])
        st.text_input("Country of Dealing / Residence / Incorporation")

    # Section 4.4 - Politically Exposed Person (PEP)
    if "Politically Exposed Person (PEP)" in selected_risks:
        st.subheader("4.4 Politically Exposed Person (PEP)")
        st.radio("Classification", ["Domestic PEP", "Foreign PEP"])
        st.radio("Status", ["Current PEP", "Former PEP"])
        st.text_input("Public Position Held")

    # Section 4.5 - Related to PEP (PEP-R)
    if "Related to PEP (PEP-R)" in selected_risks:
        st.subheader("4.5 Related to PEP (PEP-R)")
        st.text_input("Name of PEP-R")
        st.text_input("Name of PEP")
        st.radio("Relation", ["Spouse", "Parent", "Child", "Sibling"])
        st.radio("Classification", ["Domestic PEP", "Foreign PEP"])
        st.radio("Status", ["Current PEP", "Former PEP"])
        st.text_input("Public Position Held by PEP")

    # Section 4.6 - Associates of PEP (PEP-A)
    if "Associates of PEP (PEP-A)" in selected_risks:
        st.subheader("4.6 Associates of PEP (PEP-A)")
        for i in range(2):
            st.markdown(f"**Entry {i+1}**")
            st.text_input("Name of PEP or PEP-R", key=f"pep_name_{i}")
            st.multiselect("Association to PEP", [
                "Employed by PEP",
                "Close relative of a PEP (up to third degree)",
                "Senior Manager is PEP or PEP-R",
                "Authorized Signatory is PEP or PEP-R",
                "Director is PEP or PEP-R",
                "Shareholder is PEP or PEP-R"
            ], key=f"assoc_type_{i}")
            st.radio("Classification", ["Domestic PEP", "Foreign PEP"], key=f"class_{i}")
            st.radio("Status", ["Current PEP", "Former PEP"], key=f"status_{i}")
            st.text_input("Public Position Held", key=f"position_{i}")

    # Section 4.7 - Entities Owned by Customer
    if any(r in selected_risks for r in [
        "High risk business/activity", "Non-resident individual or entity", "Dealing with or resident of High risk jurisdiction",
        "Politically Exposed Person (PEP)", "Related to PEP (PEP-R)", "Associates of PEP (PEP-A)", "Pooled Fund", "Introduced Business from Professional Intermediaries"
    ]):
        st.subheader("4.7 Entities Owned by the Customer")
        for i in range(3):
            st.text_input("Name of Entity", key=f"entity_{i}")
            st.text_input("Nature of Ownership", key=f"ownership_{i}")
            st.number_input("Holding (%)", 0, 100, key=f"holding_{i}")
            st.text_input("Registration Number", key=f"reg_num_{i}")
            st.text_input("Country of Incorporation", key=f"country_inc_{i}")
            st.date_input("Date of Incorporation", key=f"inc_date_{i}")
            st.text_input("Nature of Business", key=f"biz_type_{i}")

    # Section 4.8 - Account with Other Financial Institutions
    if any(r in selected_risks for r in [
        "High risk business/activity", "Non-resident individual or entity", "Dealing with or resident of High risk jurisdiction",
        "Politically Exposed Person (PEP)", "Related to PEP (PEP-R)", "Associates of PEP (PEP-A)", "Club, Charity, or Other Society", "Pooled Fund", "Introduced Business from Professional Intermediaries"
    ]):
        st.subheader("4.8 Accounts with Other Financial Institutions")
        for i in range(3):
            st.text_input("Name of Financial Institution", key=f"fi_name_{i}")
            st.text_input("Jurisdiction", key=f"fi_jurisdiction_{i}")
            st.text_input("Account Type", key=f"fi_type_{i}")
            st.date_input("Account Opening Date", key=f"fi_date_{i}")

    # Section 4.9 - Anticipated Activity
    if any(r in selected_risks for r in [
        "High risk business/activity", "Non-resident individual or entity", "Dealing with or resident of High risk jurisdiction", "Politically Exposed Person (PEP)", "Related to PEP (PEP-R)",
        "Associates of PEP (PEP-A)", "Club, Charity, or Other Society", "Pooled Fund", "Introduced Business from Professional Intermediaries"
    ]):
        st.subheader("4.9 Anticipated Activity")
        for i in range(3):
            st.markdown(f"**Transaction {i+1}**")
            st.radio("Direction", ["Debit", "Credit"], key=f"flow_dir_{i}")
            st.radio("Channel", ["Cash", "Cheque", "Wire"], key=f"channel_{i}")
            st.text_input("Purpose", key=f"purpose_{i}")
            st.selectbox("Frequency", ["Monthly", "Quarterly", "Annually"], key=f"freq_{i}")
            st.text_input("Originator/Beneficiary", key=f"party_{i}")
            st.number_input("Amount", min_value=0.0, key=f"amt_{i}")

    # Section 4.10 - Shareholders/UBOs
    if any(r in selected_risks for r in [
        "High risk business/activity", "Non-resident individual or entity", "Dealing with or resident of High risk jurisdiction",
        "Associates of PEP (PEP-A)", "Pooled Fund", "Introduced Business from Professional Intermediaries", "Correspondent Banking Relationship"
    ]):
        st.subheader("4.10 Shareholders / UBOs (>20%)")
        for i in range(3):
            st.text_input("Name", key=f"ubo_name_{i}")
            st.text_input("Nationality", key=f"ubo_nat_{i}")
            st.date_input("Date of Birth", key=f"ubo_dob_{i}")
            st.text_input("Place of Birth", key=f"ubo_pob_{i}")
            st.text_input("Country of Residence", key=f"ubo_res_{i}")
            st.radio("PEP Status", ["Yes", "No"], key=f"ubo_pep_{i}")
            st.text_input("Nature of Ownership", key=f"ubo_own_{i}")
            st.text_input("Indirect Through/By", key=f"ubo_indirect_{i}")
            st.number_input("Holding (%)", 0, 100, key=f"ubo_holding_{i}")

    # Section 4.11 - Club/Charity
    if "Club, Charity, or Other Society" in selected_risks:
        st.subheader("4.11 Club, Charity or Other Society")
        st.radio("Authorization Certificate Attached?", ["Yes", "No"])
        st.text_area("Details (if not attached)")
        st.radio("Charity Declaration Attached?", ["Yes", "No"])
        st.text_area("Details (if not attached)")

    # Section 4.12 - Pooled Fund
    if "Pooled Fund" in selected_risks:
        st.subheader("4.12 Pooled Fund")
        st.radio("AML Questionnaire Attached?", ["Yes", "No"])
        st.text_area("Details (if not attached)")

    # Section 4.13 - Correspondent Banking
    if "Correspondent Banking Relationship" in selected_risks or "Introduced Business from Professional Intermediaries" in selected_risks:
        st.subheader("4.13 Correspondent Banking Relationship")
        for doc in ["Banking License", "Group Structure", "Corporate Governance", "AML Policies", "AML Questionnaire"]:
            st.radio(f"{doc} Attached?", ["Yes", "No"])
            st.text_area(f"Details for {doc} (if not attached)")
    



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
    st.date_input("Verification Date (Officer)", value=date.today())

    st.text_input("Compliance Name")
    st.text_input("Compliance Designation")
    st.date_input("Verification Date (Compliance)", value=date.today())

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