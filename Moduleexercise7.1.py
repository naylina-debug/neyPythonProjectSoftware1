# Tuple of seasons
seasons = ("winter", "spring", "summer", "autumn")

# Ask the user for the month number
month = int(input("Enter the month number (1–12): "))

# Adjust month so that December is treated as the first month of winter
# Month mapping:
# Dec(12) → 0, Jan(1) → 1, Feb(2) → 2, ..., Nov(11) → 11
adjusted_month = month % 12

# Determine the season
season_index = adjusted_month // 3
season = seasons[season_index]

print("The season is:", season)
