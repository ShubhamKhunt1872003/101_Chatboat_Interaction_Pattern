import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
import numpy as np

# Load your frequency data
frequency_df = pd.read_csv("chatbot_pattern_frequency_table.csv")

# Set the pattern names as index
analysis_df = frequency_df.set_index("Pattern Name")

# Step 1: Data Validation
print("\nData Validation:")
print("1. Checking for null values:")
print(analysis_df.isnull().sum())

print("\n2. Checking for zero-frequency rows:")
zero_rows = analysis_df[(analysis_df.sum(axis=1) == 0)]
print(f"Found {len(zero_rows)} rows with all zeros:")
print(zero_rows.index.tolist())

# Step 2: Filter Data (remove zero rows)
analysis_df = analysis_df[analysis_df.sum(axis=1) > 0]
print(f"\nAfter filtering, {len(analysis_df)} patterns remain")

# Step 3: Create Heatmap (unchanged)
plt.figure(figsize=(12, 20))
normalized_df = analysis_df.div(analysis_df.sum(axis=1), axis=0)

heatmap = sns.heatmap(
    normalized_df[["Customer Support", "Government", "Darkpattern"]],
    annot=analysis_df[["Customer Support", "Government", "Darkpattern"]],
    fmt="d",
    cmap="YlOrRd",
    linewidths=0.5,
    cbar_kws={'label': 'Normalized Frequency'}
)

plt.title("Pattern Usage Across Chatbot Categories", pad=20)
plt.ylabel("Pattern")
plt.xlabel("Chatbot Category")
plt.xticks(rotation=45)
plt.tight_layout()

heatmap_output_path = "chatbot_pattern_distribution_heatmap.png"
plt.savefig(heatmap_output_path, dpi=300, bbox_inches='tight')
plt.close()
print(f"\n✅ Heatmap saved to: {heatmap_output_path}")

# Step 4: Chi-Square Test with Additional Checks
contingency_table = analysis_df[["Customer Support", "Government", "Darkpattern"]]

# Additional check for expected frequencies
try:
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    # Check expected frequencies
    if (expected < 1).any():
        print("\nWarning: Some expected frequencies < 1. Results may be unreliable.")
    
    # Save results
    chi2_results = pd.DataFrame({
        "Chi-Square Statistic": [chi2],
        "p-value": [p],
        "Degrees of Freedom": [dof],
        "Significant at α=0.05": [p < 0.05]
    })
    
    chi2_output_path = "chi2_test_results.csv"
    chi2_results.to_csv(chi2_output_path, index=False)
    print(f"✅ Chi-square test results saved to: {chi2_output_path}")

    # Interpretation
    print("\nChi-Square Test Results Interpretation:")
    print(f"Chi-Square Statistic: {chi2:.2f}")
    print(f"p-value: {p:.4f}")

    if p < 0.05:
        print("Result: Significant - Pattern usage differs between chatbot categories")
    else:
        print("Result: Not Significant - Pattern usage is similar across categories")

    # Effect size
    n = contingency_table.sum().sum()
    cramers_v = np.sqrt(chi2 / (n * (min(contingency_table.shape) - 1)))
    print(f"\nEffect Size (Cramer's V): {cramers_v:.3f}")

except ValueError as e:
    print(f"\n❌ Error in chi-square test: {e}")
    print("This usually means:")
    print("- Some patterns have zero counts in all categories (already filtered out)")
    print("- Some categories have zero counts for all patterns")
    print("\nPlease check your contingency table:")
    print(contingency_table)