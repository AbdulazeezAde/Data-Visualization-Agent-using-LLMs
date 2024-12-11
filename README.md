# Data-Visualization-Agent-using-LLMs

This project is an Autonomous Data Exploration Agent that:

1. Loads a dataset from a CSV file.
2. Analyzes the dataset to provide insights, including columns, missing values, data types, and summary statistics.
3. Automatically generates a human-readable summary of the dataset.
4. Uses an LLM (OpenAI's GPT-3.5) to generate insightful questions about the data for further analysis.


**Features**
1. Load and Explore Data: Automatically identifies columns, missing values, and key statistics.
2. Get Dataset Summary: Produces a concise summary of the dataset in plain English.
3. Generate Questions: Uses OpenAI's GPT-3.5 to generate meaningful exploratory questions based on the dataset.
4. Modular Design:Functions are broken into reusable modules, making it easy to extend or integrate into other projects.

**PROJECT STRUCTURE**

project/

│

├── main.py                     # Main script to run the application

├── data_loader.py              # Contains the `load_data` function

├── data_explorer.py            # Contains `explore_data` and `generate_dataset_summary`

├── question_generator.py       # Contains `generate_questions`

├── utils.py                    # Contains helper functions like `print_exploration_results`

└── __init__.py                 # Optional, for making it a package

**Getting Started
Prerequisites**
Python 3.8 or higher
OpenAI API key (to use GPT-3.5)

**Installation**
```bash
git clone https://github.com/AbdulazeezAde/Data-Visualization-Agent-using-LLMs.git
```

```
cd Data-Visualization-Agent-using-LLMs
```
**Install Dependencies**
```
pip install -r requirements.txt
```

Set up your OpenAI API key: Add your API key as an environment variable.
```
export OPENAI_API_KEY=your_openai_api_key
```
```
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
```

