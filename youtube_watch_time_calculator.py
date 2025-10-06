print("Welcome to the youtube watch time calculator.")
videos_watched = int(input("Enter the number of videos you have watched "))
average_length = int(input("What was the average length of each video in minutes? "))
total_time = videos_watched*average_length
days_equivalent = total_time/24
print(f"Your watch time is {total_time} and this has an equivalent of {days_equivalent:.0f} days.")
