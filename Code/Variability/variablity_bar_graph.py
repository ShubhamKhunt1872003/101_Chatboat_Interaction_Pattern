import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'Segoe UI Emoji'

# Updated data
data = [
    ["Conversational Recovery", 7.2, 0.004, "Gov: 1.0 | Dark: 0.18", ""],
    ["Message Reaction", 5.6, 0.009, "Gov: 0.78 | Cust: 0.20", ""],
    ["Typing Indicator", 2.8, 0.07, "Cust: 0.80 | Gov: 0.78", ""],
    ["Access Icon (bottom right)", 4.3, 0.02, "Cust: 0.86 | Gov: 0.38", ""]
]

# Create figure
plt.figure(figsize=(12, 6), dpi=100)
ax = plt.gca()

# Custom styling
colors = ['#4C72B0', '#55A868', '#C44E52', '#8172B2']  # Blue, Green, Red, Purple
bar_width = 0.6

# Plot F-values
patterns = [x[0] for x in data]
f_values = [x[1] for x in data]
bars = plt.bar(patterns, f_values, color=colors, width=bar_width, alpha=0.85)

# Add interpretation text (above bars)
for i, row in enumerate(data):
    y_pos = f_values[i] + 0.4
    plt.text(i, y_pos, row[3], ha='center', va='bottom', fontsize=14,
             bbox=dict(facecolor='white', edgecolor='none', pad=1))

# Placeholder for bottom annotation if needed
for i, row in enumerate(data):
    plt.text(i, -0.5, row[4], ha='center', va='top', fontsize=12,
             bbox=dict(facecolor='whitesmoke', edgecolor='none', pad=4))

# Threshold line
plt.axhline(y=3.5, color='black', linestyle='--', linewidth=1, alpha=0.7)
plt.text(3.3, 3.75, 'Significance Threshold (F = 3.5)', fontsize=10, color='black')

# Customize axes
plt.ylabel('F-value (Variability Strength)', fontsize=16)
plt.xticks(range(len(patterns)), [x.replace(" ", "\n") for x in patterns], fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(0, max(f_values) * 1.25)

# Remove spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.savefig('pattern_variability_chart.png', dpi=120, bbox_inches='tight')
plt.show()
