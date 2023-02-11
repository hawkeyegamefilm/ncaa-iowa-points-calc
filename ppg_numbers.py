import pandas as pd

df = pd.read_csv('data/iowa_ppg_history.csv')

# print(df['offense_ppg_rank'].describe())
print("Average Defensive PPG rank since 2001")
print(round(df['defense_ppg_rank'].mean(),2))
print("Median Defensive PPG rank since 2001")
print(df['defense_ppg_rank'].median())

# print(df['offense_ppg_rank'].describe())
print("Average Offensive PPG rank since 2001")
print(round(df['offense_ppg_rank'].mean(), 2))
print("Median Offensive PPG rank since 2001")
print(df['offense_ppg_rank'].median())

non_o_points = df['non_o_points'].sum()
games = df['games'].sum()
d_st_ppg = non_o_points/games
print("Average points scored by Defense + KR, PR & Punt Blocks")
print(str(round(d_st_ppg, 2)))

print("Average Defensive PPG rank over the last 5 years")
print(df.tail(5)['defense_ppg_rank'].mean())
print("Average Offensive PPG rank over the last 5 years")
print(df.tail(5)['offense_ppg_rank'].mean())
