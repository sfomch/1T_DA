import pandas as pd
data = pd.read_csv('data\germany_cars.csv', sep=',')
print(data.head())

print(len(data))
data_drop = data.drop_duplicates().reset_index()
print(len(data_drop))
# for i in range(0, 46404):
#     print(i)
#     if data.duplicated().iloc[i]:
#         d += 1
#         print(d)
# print(d)
#
#
