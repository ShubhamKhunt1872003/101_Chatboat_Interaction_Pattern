import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load ANOVA results
df = pd.read_csv('anova_results.csv')

# 2. Create the visualization figure with more space
plt.figure(figsize=(16, 12))  # Increased figure size


# 4. Plot p-values with more space
ax2 = plt.subplot(2, 1, 2)
scatter = sns.scatterplot(x='Pattern', y='p-value', data=df, 
                         size='F-statistic', hue='F-statistic',
                         sizes=(50, 250), palette='viridis', ax=ax2)
ax2.axhline(0.05, color='red', linestyle='--', alpha=0.5)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90, fontsize=8)  # Smaller font
ax2.set_title('ANOVA Results: p-values by Pattern (Red Line = 0.05 Significance Threshold)', pad=20)
ax2.set_ylabel('p-value', labelpad=10)
ax2.grid(True, alpha=0.3)

# Adjust legend position
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Add more space between subplots
plt.subplots_adjust(hspace=0.5)  # Increased vertical space

plt.tight_layout()
plt.savefig('anova_visualization.png', dpi=300, bbox_inches='tight')
plt.show()

# 5. Create a summary table visualization with better spacing
plt.figure(figsize=(14, 6))  # Wider figure for table
plt.axis('off')

# Create table with cell padding
table = plt.table(cellText=df[['Pattern', 'F-statistic', 'p-value', 'Significant']].values,
                colLabels=['Pattern', 'F-statistic', 'p-value', 'Significant'],
                loc='center',
                cellLoc='center',
                colColours=['#f7f7f7']*4,
                colWidths=[0.4, 0.2, 0.2, 0.2])

# Adjust cell properties
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)  # Increase cell sizes

plt.savefig('anova_summary_table.png', dpi=200, bbox_inches='tight')

print("Visualizations created: anova_visualization.png and anova_summary_table.png")