import BBReferenceStats as bbstats

lebron_james = "jamesle01"  # LeBron James' BKRef Identifier - https://www.basketball-reference.com/players/j/jamesle01.html
season = 2017               # 2016-2017 Season
option = 0                  # get regular season data (or != 0 for playoffs data, only for getGameStats)

# Example - get regular season per game data for a player for a season
reg_season_gamelog = bbstats.getGameStats(lebron_james,season,option)   # get data
print(reg_season_gamelog)

# Example - get playoffs season per game data for a player for a season
playoffs_gamelog = bbstats.getGameStats(lebron_james,season,option)   # get data
print(playoffs_gamelog)

# Example - get shooting data for a player for a season
shot_data = bbstats.getShootingStats(lebron_james,season)   # get data
print(shot_data)

# you can even save dataframes to a CSV file - thank god for pandas
shot_data.to_csv(r"LBJ_2016-2017_shotdata.csv",index=False)



