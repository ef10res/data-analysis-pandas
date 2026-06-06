from data_loader import load_dataset, clean_dataset, show_dataset_overview

from analysis import (
    analyze_average_loan_by_age_group,
    analyze_approved_vs_denied,
    show_top_loan_records
)

from charts import (
    create_age_group_bar_chart,
    create_approval_status_pie_chart
)

from results_writer import save_results


FILE_NAME = "utah_hmda_data_2022.csv"


def main():
    """
    Main function that controls the full program flow.
    """
    # load data set
    df = load_dataset(FILE_NAME)

    if df is None:
        return

    # run functions
    df = clean_dataset(df)

    show_dataset_overview(df)

    age_group_analysis = analyze_average_loan_by_age_group(df)

    approval_summary = analyze_approved_vs_denied(df)

    show_top_loan_records(df)

    create_age_group_bar_chart(age_group_analysis)

    create_approval_status_pie_chart(df)

    save_results(age_group_analysis, approval_summary)

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
