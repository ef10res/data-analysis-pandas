"""
charts.py
The charts are saved as PNG image files.
"""
import matplotlib.pyplot as plt
import pandas as pd


def create_age_group_bar_chart(age_group_analysis):
    """
    Create a bar chart showing average loan amount by applicant age group.
    """

    chart_data = age_group_analysis["average_loan_amount"].sort_values(
        ascending=False
    )

    plt.figure(figsize=(12, 6))

    chart_data.plot(kind="bar")

    plt.title("Average Loan Amount by Applicant Age Group")
    plt.xlabel("Applicant Age Group")
    plt.ylabel("Average Loan Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("average_loan_by_age_group.png")

    plt.close()

    print("Saved chart: average_loan_by_age_group.png")


def create_approval_status_pie_chart(df):
    """
    Create a pie chart comparing approved and denied applications.
    """

    approved_count = len(df[df["action_taken"] == 1])

    denied_count = len(df[df["action_taken"] == 3])

    status_counts = pd.Series({
        "Approved / Originated": approved_count,
        "Denied": denied_count
    })

    plt.figure(figsize=(7, 7))

    status_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Approved vs Denied Mortgage Applications")
    plt.ylabel("")
    plt.tight_layout()

    plt.savefig("approved_vs_denied_pie_chart.png")

    plt.close()

    print("Saved chart: approved_vs_denied_pie_chart.png")
