from prettytable import PrettyTable

def print_exploration_results(results):
    """
    Prints dataset exploration results in a tabular format.

    Args:
        results (dict): Dictionary containing exploration results.
    """
    columns_table = PrettyTable()
    columns_table.field_names = ["Column Name", "Missing Values", "Data Type"]
    for col in results["columns"]:
        columns_table.add_row([col, results["missing_values"][col], results["data_types"][col]])
    print("\nTable: Dataset Overview")
    print(columns_table)
