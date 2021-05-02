import pandas as pd
import numpy as np

df = pd.read_csv("./lesson_1/lection1_materials/WA_Fn-UseC_-Telco-Customer-Churn.csv")

a = df.loc[~(df['TotalCharges'].str.isdigit()) | ~(df['TotalCharges'].str == ''), 'TotalCharges'].sort_values()
a.to_csv("file_name", sep='\t', encoding='utf-8')

a.head(3)