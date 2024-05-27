# Jupyter Notebook cheatsheet

## Installing Jupyter Notebook

1. **Install Python:**
   - Ensure you have Python installed. If not, download and install it from [Python's official website](https://www.python.org/downloads/).

2. **Install Jupyter:**
   - Open your terminal and run `pip install jupyter`.

3. **Start Jupyter Notebook:**
   - Open your terminal and run `jupyter notebook`.

## Getting Started with Jupyter Notebook

4. **Creating a New Notebook:**
   - Click on the "New" button and select your preferred kernel (e.g., Python 3) to create a new notebook.

5. **Cell Types:**
   - Jupyter supports different cell types: Code, Markdown, and Raw NBConvert. Choose the cell type from the toolbar.

6. **Running Code:**
   - To execute a cell, select it and press `Shift + Enter`.
   - Use `Ctrl + Enter` to run the cell and remain in the same cell.

## Working with Python Code

7. **Importing Libraries:**
   - Import Python libraries using the `import` statement (e.g., `import numpy as np`).

```python
import pandas as pd
```

8. **Markdown Cells:**
   - Create Markdown cells for documentation and text explanations.
   - Use `#` for headers, `*` or `_` for emphasis, and other Markdown formatting.

```markdown
# This is a Markdown cell
```

9. **Magic Commands:**
   - Magic commands start with `%` or `%%`. For example:

```python
%matplotlib inline
```

```python
# To time the execution of a cell
%%time
```

10. **Displaying Output:**
    - Print output using the `print` function or simply typing the variable name at the end of a code cell.

```python
x = 10
x
```

## Managing Code Execution

11. **Commenting:**
    - Add comments to code cells using `#`.

```python
# This is a comment
```

12. **Interrupting/Restarting the Kernel:**
    - Use the "Kernel" menu to interrupt or restart the Python kernel.

13. **Clearing Output:**
    - Clear cell outputs with "Cell" > "All Output" > "Clear".

## Data Import, Manipulation, and Cleaning

14. **Pandas:**
    - Import Pandas: `import pandas as pd`.
    - Read data from various formats: `pd.read_csv()`, `pd.read_excel()`.

```python
import pandas as pd
data = pd.read_csv('your_data.csv')
```

15. **Data Exploration:**
    - Use Pandas to explore and summarize data.

```python
data.head()
data.info()
data.describe()
```

16. **Data Cleaning:**
    - Clean data by handling missing values and duplicates.

```python
data.dropna()
data.drop_duplicates()
```

17. **Removing Blank Spaces in a Column:**
    - Use the `str.strip()` method to remove leading and trailing white spaces in a column.

```python
data['column_name'] = data['column_name'].str.strip()
```

18. **Handling missing values:**
    - Fill missing values with a specific value.

```python
data.fillna(0, inplace=True)  # Replace NaN with 0
data.fillna('unknown', inplace=True)  # Replace NaN with 'unknown'
```

19. **Removing unwanted columns:**

```python
data.drop(columns=['unwanted_column1', 'unwanted_column2'], inplace=True)
```

20. **Renaming columns for clarity:**

```python
data.rename(columns={'old_name1': 'new_name1', 'old_name2': 'new_name2'}, inplace=True)
```

21. **Changing the data type of columns:**

```python
data['column_name'] = data['column_name'].astype('int')  # Convert to integer
data['column_name'] = data['column_name'].astype('float')  # Convert to float
data['column_name'] = data['column_name'].astype('str')  # Convert to string
```

22. **Data Selection:**
    - Select specific columns or rows using Pandas indexing.

```python
data['column_name']
data.loc[]
data.iloc[]
```

23. **Data Grouping:**
    - Group data using the `groupby` function.

```python
grouped = data.groupby('column_name')
```

24. **Handling outliers:**
    - Remove outliers based on z-score.

```python
from scipy import stats

data = data[(np.abs(stats.zscore(data['numeric_column'])) < 3)]
```

## Data Analysis and Visualization

24. **Matplotlib and Seaborn:**
    - Import libraries: `import matplotlib.pyplot as plt`, `import seaborn as sns`.

```python
import matplotlib.pyplot as plt
import seaborn as sns
```

25. **NumPy:**
    - Import NumPy: `import numpy as np`.
    - Perform mathematical operations on arrays.

```python
import numpy as np
```

## Keyboard Shortcuts

26. **Keyboard Shortcuts:**
    - Press `H` in command mode to view keyboard shortcuts.
    - Learn and use common shortcuts to increase productivity.

## Saving and Exporting

27. **Saving the cleaned data to a new Excel file:**
```python
data.to_excel('cleaned_file.xlsx', index=False)
```

28. **Saving a Notebook:**
    - Use "File" > "Save and Checkpoint" to save your notebook.

29. **Exporting Notebooks:**
    - Export notebooks to various formats like HTML, PDF, and more using "File" > "Download as".
