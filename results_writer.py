"""
This module saves analysis results to CSV files.
"""
def save_results(age_group_analysis, approval_summary):
    """
    Save analysis results into separate CSV files.
    """

    age_group_analysis.to_csv("age_group_loan_analysis.csv")

    approval_summary.to_csv(
        "approved_vs_denied_summary.csv",
        index=False
    )

    print("\n" + "=" * 60)
    print("FILES SAVED")
    print("=" * 60)

    print("Saved: age_group_loan_analysis.csv")
    print("Saved: approved_vs_denied_summary.csv")
