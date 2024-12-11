def explore_data(df):
    """
    Generates a dictionary of dataset details including columns, missing values,
    data types, and summary statistics.

    Args:
        df (pd.DataFrame): DataFrame to explore.

    Returns:
        tuple: A dictionary of exploration results and a textual summary of the dataset.
    """
    exploration = {
        "columns": df.columns.tolist(),
        "missing_values": df.isnull().sum().to_dict(),
        "data_types": df.dtypes.to_dict(),
        "summary": df.describe(include="all").to_dict()
    }
    
    # Automatically generate a summary of the dataset
    summary_text = generate_dataset_summary(exploration)
    return exploration, summary_text

def generate_dataset_summary(exploration):
    """
    Generates a human-readable summary of the dataset based on exploration results.

    Args:
        exploration (dict): Dictionary containing exploration details.

    Returns:
        str: Textual summary of the dataset.
    """
    columns = exploration["columns"]
    missing_values = exploration["missing_values"]
    summary_stats = exploration["summary"]

    # Start summarizing
    summary = f"The dataset contains {len(columns)} columns: {', '.join(columns)}.\n"

    # Include ranges and key stats for numerical columns
    numeric_columns = [col for col in summary_stats if "mean" in summary_stats[col]]
    for col in numeric_columns:
        col_mean = summary_stats[col].get("mean", "N/A")
        col_min = summary_stats[col].get("min", "N/A")
        col_max = summary_stats[col].get("max", "N/A")
        summary += f"Column '{col}' has a mean of {col_mean:.2f}, with values ranging from {col_min} to {col_max}.\n"

    # Add information about missing values
    missing_info = [f"'{col}': {count} missing values" for col, count in missing_values.items() if count > 0]
    if missing_info:
        summary += f"Missing values: {', '.join(missing_info)}.\n"
    else:
        summary += "No missing values were found.\n"

    return summary.strip()
