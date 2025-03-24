import matplotlib
# 强制使用通用agg后端
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统黑体
plt.rcParams['axes.unicode_minus'] = False

# 试验方案表格
design_data = {
    "因素": ["A", "B", "A×B", "C", "•", "•", "D"],
    "列号": [1, 2, 3, 4, 5, 6, 7]
}
design_df = pd.DataFrame(design_data)

# 试验结果表格
result_data = {
    "试验号": [1, 2, 3, 4, 5, 6, 7, 8],
    "A": [1, 1, 1, 2, 1, 2, 2, 2],
    "B": [1, 1, 2, 2, 1, 2, 1, 2],
    "A×B": [1, 2, 1, 2, 2, 1, 2, 1],
    "C": [1, 2, 2, 1, 2, 1, 1, 2],
    "D": [1, 2, 1, 2, 1, 2, 1, 2],
    "收率-70": [-5, 4, 1, 3, 0, 3, -8, -3]
}
result_df = pd.DataFrame(result_data)

# 方差分析计算表格
anova_data = {
    "列号": ["A", "B", "A×B", "C", "5", "6", "D"],
    "I": [3, -12, -12, -4, -5, -7, ""],
    "II": [-8, -7, 7, 7, -1, 0, ""],
    "I-II": [11, 9, -19, -19, -3, -5, ""],
    "(I-II)^2": [121, 81, 361, 361, 9, 25, "T = -5"]
}
anova_df = pd.DataFrame(anova_data)

# 创建可视化图表
plt.figure(figsize=(15, 10))

# 试验方案表格
plt.subplot(2, 2, 1)
plt.title("试验方案设计表")
plt.table(cellText=design_df.values,
          colLabels=design_df.columns,
          loc="center",
          cellLoc="center")
plt.axis("off")

# 试验结果表格
plt.subplot(2, 2, 2)
plt.title("试验结果数据表")
plt.table(cellText=result_df.values,
          colLabels=result_df.columns,
          loc="center",
          cellLoc="center")
plt.axis("off")

# 方差分析表格
plt.subplot(2, 2, 3)
plt.title("方差分析计算表")
plt.table(cellText=anova_df.values,
          colLabels=anova_df.columns,
          loc="center",
          cellLoc="center")
plt.axis("off")

# 收率可视化
plt.subplot(2, 2, 4)
plt.title("各试验收率对比")
plt.plot(result_df["试验号"], result_df["收率-70"], marker="o")
plt.xlabel("试验号")
plt.ylabel("收率-70")
plt.grid(True)

plt.tight_layout()
plt.savefig("orthogonal_experiment.png", dpi=300, bbox_inches='tight')
print("图片已保存为 orthogonal_experiment.png")