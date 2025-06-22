import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('chatbot_pattern_frequency_table.csv')

# Filter for top patterns (e.g., Total > 30 to avoid clutter)
top_patterns = df[df['Total'] > 30].sort_values(by='Total', ascending=False)

# Plot stacked bar chart
plt.figure(figsize=(12, 8))
top_patterns.set_index('Pattern Name')[['Customer Support', 'Government', 'Darkpattern']].plot(
    kind='bar', 
    stacked=True,
    colormap='viridis',
    edgecolor='black'
)

plt.title('Chatbot UI Pattern Adoption by Sector (Top Patterns)', fontsize=14)
plt.xlabel('Pattern Name', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(title='Sector')
plt.tight_layout()
plt.show()