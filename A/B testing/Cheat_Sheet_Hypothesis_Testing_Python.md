# Cheat_Sheet_Hypothesis_Testing_Python.md

# Cheat Sheet: Hypothesis Testing in Python

A quick-reference guide for hypothesis testing, parametric vs. non-parametric decision paths, decision rules, and Python code implementations (`pingouin`, `statsmodels`, `scipy.stats`, `pandas`).

---

## 1. Core Decision Rules

Compare the calculated **$p$-value** against the significance level **$\alpha$** (commonly $\alpha = 0.05$):

| Condition | Decision | Conclusion |
| :--- | :--- | :--- |
| **$p$-value $< \alpha$** | **Reject $H_0$** | Accept $H_A$. Strong evidence of a statistically significant difference/effect. |
| **$p$-value $\ge \alpha$** | **Fail to reject $H_0$** | Retain $H_0$. Insufficient evidence to claim a significant difference/effect. |

---

## 2. Testing Overview & Selection Flowchart

                        Data Type & Question
                                 │
     ┌───────────────────────────┴───────────────────────────┐
Proportions                                             Numerical
     │                                                       │
┌──────┴──────┐                                         ┌──────┴──────┐
2 Groups     >2 Groups or                            2 Groups         >2 Groups
(z-test)   Independence                          (t-test/MWU)        (Kruskal)
(Chi-Square)                                  │
┌──────┴──────┐
Independent    Paired
(MWU)      (Wilcoxon)


---

## 3. Python Code Implementations

### A. Proportions & Categorical Tests

#### 1. Two-Sample $z$-test for Proportions
* **When to use:** Comparing the proportions of success between two independent categorical groups.
* **Hypotheses:** $H_0: p_1 = p_2$ vs. $H_A: p_1 > p_2$ (or $\neq, <$)

```python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# Success counts and total sample sizes for [Group 1, Group 2]
success_counts = np.array([count_group1, count_group2])
n_obs = np.array([total_group1, total_group2])

# Perform z-test
stat, p_value = proportions_ztest(
    count=success_counts, nobs=n_obs, alternative="larger"
)
print(f"z-stat: {stat:.4f}, p-val: {p_value:.4f}")
2. Chi-Square (χ 
2
 ) Test of Independence
When to use: Testing if two categorical variables (≥2 levels each) are statistically independent.

Hypotheses: H 
0
​
 : Variables are independent vs. H 
A
​
 : Variables are dependent.

Python
import pingouin

expected, observed, stats = pingouin.chi2_independence(
    data=df, x="cat_var_1", y="cat_var_2"
)
print(stats[stats["test"] == "pearson"])
3. Chi-Square (χ 
2
 ) Goodness-of-Fit Test
When to use: Testing if an observed frequency distribution matches an expected/hypothesized distribution.

Hypotheses: H 
0
​
 : Observed fits Expected vs. H 
A
​
 : Observed does not fit Expected.

Python
from scipy.stats import chisquare

# Both arguments must be arrays/series of raw counts
gof_test = chisquare(f_obs=observed_counts["n"], f_exp=hypothesized_counts["n"])
print(f"Chi2: {gof_test.statistic:.4f}, p-val: {gof_test.pvalue:.4f}")
B. Paired / Dependent Numeric Tests
1. Paired t-test (Parametric)
When to use: Comparing means of two dependent measurements taken on the same subjects (e.g., 2012 vs. 2016 values per county).

Assumptions: Differences are normally distributed.

Python
import pingouin

results = pingouin.ttest(
    x=df["metric_time1"],
    y=df["metric_time2"],
    paired=True,
    alternative="two-sided",
)
print(results)
2. Wilcoxon Signed-Rank Test (Non-Parametric)
When to use: Non-parametric alternative to paired t-test when paired differences are not normally distributed or heavily skewed.

Python
import pingouin

wilcoxon_test_results = pingouin.wilcoxon(
    x=df["metric_time1"], y=df["metric_time2"], alternative="two-sided"
)
print(wilcoxon_test_results)
C. Independent Numeric Tests
1. Wilcoxon-Mann-Whitney (Mann-Whitney U) Test
When to use: Non-parametric test comparing two independent numerical groups (no normal distribution assumption required).

Data Prep: Reshape long data to wide data first via .pivot().

Python
import pingouin

# 1. Reshape long to wide format
wide_df = df[["numeric_col", "group_col"]].pivot(
    columns="group_col", values="numeric_col"
)

# 2. Run Mann-Whitney U test
wmw_test = pingouin.mwu(
    x=wide_df["Group_A"], y=wide_df["Group_B"], alternative="two-sided"
)
print(wmw_test)
2. Kruskal-Wallis Test
When to use: Non-parametric alternative to one-way ANOVA when comparing a numerical outcome across 3 or more independent groups.

Python
import pingouin

kw_test = pingouin.kruskal(
    data=df, dv="numeric_outcome", between="categorical_group"
)
print(kw_test)
4. Key Data Transformation Patterns
Proportional Stacked Bar Chart Prep
Python
import matplotlib.pyplot as plt
import pandas as pd

# Normalize values to get proportions per group
props = (
    df.groupby("group_var")["category_var"]
    .value_counts(normalize=True)
    .unstack()
)

# Plot stacked bar graph
props.plot(kind="bar", stacked=True)
plt.ylabel("Proportion")
plt.show()
Computing Hypothesized Expected Counts
Python
# Compute total sample size
n_total = len(df)

# Expected counts = Expected Proportion * Total Sample Size
hypothesized["n"] = hypothesized["prop"] * n_total