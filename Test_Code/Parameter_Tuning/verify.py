import pandas as pd

df1 = pd.read_csv('../Resources/k-folds/partitioned_data/1_en_cat.txt')
df2 = pd.read_csv('../Resources/k-folds/partitioned_data/2_en_cat.txt')
df3 = pd.read_csv('../Resources/k-folds/partitioned_data/3_en_cat.txt')
df4 = pd.read_csv('../Resources/k-folds/partitioned_data/4_en_cat.txt')
df5 = pd.read_csv('../Resources/k-folds/partitioned_data/5_en_cat.txt')

ef1 = pd.read_csv('../Resources/k-folds/partitioned_data/raw_partition/1_en.txt')
ef2 = pd.read_csv('../Resources/k-folds/partitioned_data/raw_partition/2_en.txt')
ef3 = pd.read_csv('../Resources/k-folds/partitioned_data/raw_partition/3_en.txt')
ef4 = pd.read_csv('../Resources/k-folds/partitioned_data/raw_partition/4_en.txt')
ef5 = pd.read_csv('../Resources/k-folds/partitioned_data/raw_partition/5_en.txt')

print(len(df1.index)+len(ef1.index))
print(len(ef1.index)+len(ef2.index)+len(ef3.index)+len(ef4.index)+len(ef5.index))