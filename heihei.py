import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. 实验数据
data = {
    'Temp10C': [14.10, 9.7, 5.11],
    'Temp24C': [11.11, 10.8, 13.14],
    'Temp38C': [13.19, 7.11, 12.13],
    'Temp52C': [10.12, 6.10, 14.10]
}
df = pd.DataFrame(data, index=['Conc2%', 'Conc4%', 'Conc6%'])

# 2. 计算关键统计量
T = df.values.flatten().sum()
n = df.size
C = T ** 2 / n
St = np.sum(df.values ** 2) - C
Sa = np.sum([row.sum() ** 2 for row in df.values]) / 4 - C
Sb = np.sum([col.sum() ** 2 for col in df.T.values]) / 3 - C
Se = St - Sa - Sb

# 3. 自由度与均方
df_a, df_b, df_e = 2, 3, 6
MSa, MSb, MSe = Sa/df_a, Sb/df_b, Se/df_e

# 4. 计算F统计量
F_concentration = MSa / MSe
F_temperature = MSb / MSe

# 5. 整理结果
result_df = pd.DataFrame({
    'Factor': ['Concentration', 'Temperature'],
    'df': [df_a, df_b],
    'MS': [round(MSa, 4), round(MSb, 4)],
    'F-value': [round(F_concentration, 4), round(F_temperature, 4)],
    'Critical Value': [5.14, 4.76],
    'Conclusion': [
        'No Significant' if F_concentration < 5.14 else 'Significant',
        'No Significant' if F_temperature < 4.76 else 'Significant'
    ]
})

# 6. 绘制结果表格并保存为图片
plt.figure(figsize=(12, 5))

# 调整列宽以适应英文标签
table = plt.table(
    cellText=result_df.values,
    colLabels=result_df.columns,
    cellLoc='center',
    loc='center',
    colWidths=[0.2, 0.08, 0.12, 0.12, 0.15, 0.25]
)

# 表格样式设置
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.1, 1.1)
plt.title('ANOVA Results Visualization', fontsize=14, pad=20)
plt.axis('off')

plt.savefig('anova_results.png', dpi=300, bbox_inches='tight')
plt.close()

print("详细计算结果：")
print(result_df)