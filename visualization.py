# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read your data file into a DataFrame
data = pd.read_csv('your_data.csv')

# Visualization Cheat Sheet

# 1. Line Plot
plt.figure(figsize=(10, 6))
plt.plot(data['x'], data['y'])
plt.title('Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['x'], data['y'])
plt.title('Scatter Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()

# 3. Histogram
plt.figure(figsize=(10, 6))
plt.hist(data['values'], bins=20, color='skyblue')
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

# 4. Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='categories', y='values', data=data, palette='viridis')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# 5. Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='category', y='values', data=data, palette='Set2')
plt.title('Box Plot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()

# 6. Heatmap
plt.figure(figsize=(10, 6))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 7. Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(data['values'], labels=data['categories'], autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Pie Chart')
plt.show()

# 8. Area Plot
plt.figure(figsize=(10, 6))
plt.fill_between(data['x'], data['y'], color='skyblue', alpha=0.5)
plt.title('Area Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.show()

# 9. Violin Plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='category', y='values', data=data, palette='muted')
plt.title('Violin Plot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()

# 10. Pair Plot (for exploring multiple variables)
sns.pairplot(data)
plt.show()
