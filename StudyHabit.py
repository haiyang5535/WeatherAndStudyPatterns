import pandas as pd
import random
from datetime import date, timedelta

# Function to generate random study habits data within the last week
def generate_random_samples_week(num_samples=20):
    locations = ["Indoors (Library)", "Indoors (Dorm)", "Outdoors (Park)", "Other"]
    times_of_day = ["Morning (6 AM–12 PM)", "Afternoon (12 PM–6 PM)", "Evening (6 PM–12 AM)", "Night (12 AM–6 AM)"]
    
    samples = []
    base_date = date.today()
    for i in range(num_samples):
        random_day = random.randint(0, 6)  # Random date within the past 7 days
        entry = {
            "Date": (base_date - timedelta(days=random_day)).strftime("%m/%d/%Y"),  # Random date within a week
            "Study Duration (hours)": round(random.uniform(0.5, 8), 1),  # Random hours between 0.5 and 8
            "Study Location": random.choice(locations),
            "Time of Study": random.choice(times_of_day),
            "Productivity Level": random.randint(1, 10)  # Random productivity level between 1 and 10
        }
        samples.append(entry)
    return pd.DataFrame(samples)

# Generate 20 samples
study_habits_samples_week = generate_random_samples_week(20)

# Save the dataset to a CSV file
study_habits_samples_week.to_csv("study_habits_samples_week.csv", index=False)

print("The dataset has been saved as 'study_habits_samples_week.csv'.")
