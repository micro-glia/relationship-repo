import pandas as pd  # for handling data
import datetime      # for timestamps

# Function to calculate relationship health metrics
def calculate_metrics(data):
    """
    Calculate key metrics like contact frequency and engagement levels.
    :param data: List of dictionaries containing contact info
    :return: Dataframe with calculated metrics
    """
    df = pd.DataFrame(data)
    today = datetime.date.today()

    # Calculate the number of days since the last contact
    df['Days Since Last Contact'] = df['Last Contact Date'].apply(lambda x: (today - x).days)

    # Example scoring (you can enhance this logic)
    df['Engagement Score'] = 100 - df['Days Since Last Contact']

    # Sort by engagement score (higher is better)
    df_sorted = df.sort_values(by='Engagement Score', ascending=False)

    return df_sorted

# Example Data
contacts = [
    {'Name': 'Alice', 'Last Contact Date': datetime.date(2024, 12, 25)},
    {'Name': 'Bob', 'Last Contact Date': datetime.date(2024, 12, 20)},
    {'Name': 'Charlie', 'Last Contact Date': datetime.date(2024, 11, 30)},
]

# Run the function
if __name__ == "__main__":
    result = calculate_metrics(contacts)
    print(result)

