import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# ---------- 实验设计表 ----------
# 定义因素水平（保持原变量名X1-X4）
factor_levels = {
    'X1': [12.0, 14.5, 17.0, 19.5, 22.0, 24.5, 27.0, 29.5, 32.0],
    'X2': [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1],
    'X3': [48.0, 53.5, 59.0, 64.5, 70.0, 75.5, 81.0, 86.5, 92.0],
    'X4': [0.20, 0.35, 0.50, 0.65, 0.80, 0.95, 1.10, 1.25, 1.40]
}

# 均匀设计表
uniform_design = np.array([
    [1, 3, 7, 9],
    [2, 6, 4, 8],
    [3, 9, 1, 7],
    [4, 2, 8, 6],
    [5, 5, 5, 5],
    [6, 8, 2, 4],
    [7, 1, 9, 6],
    [8, 4, 6, 2],
    [9, 7, 3, 1]
])

# 生成实验设计表
experiments = []
for row in uniform_design:
    experiment = {
        'Acrylic Acid (X1)': factor_levels['X1'][row[0]-1],
        'Initiator (X2)': factor_levels['X2'][row[1]-1],
        'Neutralization (X3)': factor_levels['X3'][row[2]-1],
        'Formaldehyde (X4)': factor_levels['X4'][row[3]-1]
    }
    experiments.append(experiment)

df_design = pd.DataFrame(experiments)

# 模拟响应变量
np.random.seed(42)
noise = np.random.normal(0, 5, 9)
df_design['Response (Y)'] = (
    50 + 2*df_design['Acrylic Acid (X1)'] - 5*df_design['Initiator (X2)'] +
    0.5*df_design['Neutralization (X3)'] + 10*df_design['Formaldehyde (X4)'] + noise
)

# 保存为PNG
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(
    cellText=df_design.round(2).values,
    colLabels=df_design.columns,
    cellLoc='center',
    loc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.savefig('experimental_design_en.png', dpi=300, bbox_inches='tight')

# ---------- 线性回归结果表 ----------
# 执行回归
X = sm.add_constant(df_design[['Acrylic Acid (X1)', 'Initiator (X2)', 'Neutralization (X3)', 'Formaldehyde (X4)']])
y = df_design['Response (Y)']
model = sm.OLS(y, X).fit()

# 生成回归结果表
results_df = pd.DataFrame({
    'Coefficient': model.params,
    'Std Error': model.bse,
    'P-value': model.pvalues
}).round(4)

# 保存为PNG
fig, ax = plt.subplots(figsize=(8, 3))
ax.axis('tight')
ax.axis('off')
table = ax.table(
    cellText=results_df.values,
    colLabels=results_df.columns,
    rowLabels=results_df.index,
    cellLoc='center',
    loc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(10)
plt.savefig('regression_results_en.png', dpi=300, bbox_inches='tight')

print("tables saved as experimental_design_en.png and regression_results_en.png")