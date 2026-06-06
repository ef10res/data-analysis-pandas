import pandas as pd

def analyze_average_loan_by_age_group(df):
    """
    Question 1:
    Which applicant age groups have the highest average loan amounts?
    """

    print("\n" + "=" * 60)
    print("QUESTION 1")
    print("=" * 60)

    age_group_analysis = (
        df.groupby("applicant_age")
          .agg(
              average_loan_amount=("loan_amount", "mean"),
              median_loan_amount=("loan_amount", "median"),
              number_of_applications=("loan_amount", "count")
          )
          .sort_values("average_loan_amount", ascending=False)
    )

    print(age_group_analysis)

    top_age_group = age_group_analysis.index[0]
    top_average = age_group_analysis.iloc[0]["average_loan_amount"]

    print(
        f"\nThe applicant age group with the highest average loan amount is "
        f"{top_age_group}, with an average loan amount of ${top_average:,.2f}."
    )

    return age_group_analysis


def analyze_approved_vs_denied(df):
    """
    Question 2:
    How do approved and denied mortgage applications compare?
    """

    print("\n" + "=" * 60)
    print("QUESTION 2")
    print("=" * 60)

    approved_applications = df[df["action_taken"] == 1]

    denied_applications = df[df["action_taken"] == 3]

    approved_average_loan = approved_applications["loan_amount"].mean()
    denied_average_loan = denied_applications["loan_amount"].mean()

    approved_average_income = approved_applications["income"].mean()
    denied_average_income = denied_applications["income"].mean()

    summary = pd.DataFrame({
        "Application Status": ["Approved / Originated", "Denied"],
        "Average Loan Amount": [approved_average_loan, denied_average_loan],
        "Average Applicant Income": [approved_average_income, denied_average_income],
        "Number of Applications": [
            len(approved_applications),
            len(denied_applications)
        ]
    })

    print(summary)

    return summary


def show_top_loan_records(df):
    """
    Show the 10 largest loan amounts.
    """

    print("\n" + "=" * 60)
    print("TOP 10 LARGEST LOANS")
    print("=" * 60)

    largest_loans = (
        df[
            [
                "loan_amount",
                "income",
                "applicant_age",
                "action_taken"
            ]
        ]
        .sort_values("loan_amount", ascending=False)
        .head(10)
    )

    print(largest_loans)

    return largest_loans
