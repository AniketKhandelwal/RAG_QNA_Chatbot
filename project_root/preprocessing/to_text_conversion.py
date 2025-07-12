def row_to_text(row):
    return (
        f"Loan ID: {row['Loan_ID']}. "
        f"{row['Gender']} {row['Education']} applicant, "
        f"{row['Married']}, "
        f"{'self-employed' if row['Self_Employed'] == 'Yes' else 'not self-employed'}, "
        f"income: {row['ApplicantIncome']}, "
        f"loan amount: {row['LoanAmount']} for {row['Loan_Amount_Term']} months, "
        f"credit history: {row['Credit_History']}, "
        f"property area: {row['Property_Area']}. "
        f"Loan status: {'approved' if row['Loan_Status'] == 'Y' else 'denied'}."
    )
