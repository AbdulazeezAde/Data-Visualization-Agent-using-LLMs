from data_loader import load_data
from data_explorer import explore_data
from question_generator import generate_questions
from utils import print_exploration_results

if __name__ == "__main__":
    # Replace this with your dataset's path
    file_path = "sales.csv"

    # Step 1: Load the data
    data = load_data(file_path)

    # Step 2: Explore the data
    exploration_results, data_summary = explore_data(data)

    # Step 3: Print exploration results
    print_exploration_results(exploration_results)

    # Step 4: Print the dataset summary
    print("\nDataset Summary:")
    print(data_summary)

    # Step 5: Generate questions based on the data summary
    questions = generate_questions(data_summary)
    print("\nGenerated Questions:")
    print(questions)
