import pandas as pd

def summary_stats_by_starting_yards(starting_yardline):
    return iowa_only_filtered_result_df[iowa_only_filtered_result_df['start_yards_to_goal'] <= starting_yardline]


def print_divider():
    print('---------------------------------------------------------------')


# swap file ref to view other years
df = pd.read_csv('data/iowa_2022_drives.csv')

valid_drive_types = ['PUNT', 'TD', 'FG', 'DOWNS', 'FUMBLE', 'INT', 'MISSED FG', 'INT TD']
invalid_drive_types = ['END OF HALF', 'END OF GAME', 'Uncategorized']

filtered_result_df = df[~df['drive_result'].isin(invalid_drive_types)]
iowa_only_filtered_result_df = filtered_result_df[filtered_result_df['offense'] == 'Iowa']

print_divider()
print('Total Drive Summary')
print(iowa_only_filtered_result_df
      .groupby('drive_result')
      .drive_result.agg('count')
      .to_frame('count')
      .reset_index()
      .sort_values('count', ascending=False))
print_divider()
forty_plus = summary_stats_by_starting_yards(60)
print('Drive Summary when starting at 40+')
print(forty_plus.groupby('drive_result')
      .drive_result.agg('count')
      .to_frame('count')
      .reset_index()
      .sort_values('count', ascending=False))
print_divider()
fifty_plus = summary_stats_by_starting_yards(50)
print('Drive Summary when starting at 50+')
print(fifty_plus.groupby('drive_result')
      .drive_result.agg('count')
      .to_frame('count')
      .reset_index()
      .sort_values('count', ascending=False))
print_divider()
sixty_plus = summary_stats_by_starting_yards(40)
print('Drive Summary when starting at 60+')
print(sixty_plus.groupby('drive_result')
      .drive_result.agg('count')
      .to_frame('count')
      .reset_index()
      .sort_values('count', ascending=False))
print_divider()
seventy_plus = summary_stats_by_starting_yards(30)
print('Drive Summary when starting at 60+')
print(seventy_plus.groupby('drive_result')
      .drive_result.agg('count')
      .to_frame('count')
      .reset_index()
      .sort_values('count', ascending=False))
print_divider()
