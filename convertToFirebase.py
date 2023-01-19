#use pip install pyrebase and gspread
import gspread
import pyrebase
import pandas as pd
import pyrebase
import json

import logic_troubleshoot as lt

api_key_gcloud = "AIzaSyAoTjCexw1lJyz712BRIuIx-VnuIaqaeDo"

# Connect to the Google Sheets API using your credentials
gc = gspread.authorize(api_key_gcloud)

# Open the specified sheet by its title
sh = gc.open_by_url(lt.url_team_stats)

# Select the first worksheet in the sheet
worksheet = sh.get_worksheet(0)

# Read the data in the worksheet into a dataframe
df = pd.DataFrame(worksheet.get_all_values())

# Convert dataframe to JSON
data = json.loads(df.to_json(orient='records'))

# Connect to Firebase using your Firebase configuration
config = {
  "apiKey": "AIzaSyB2WrC6Nm6tQzovMpJvfeThT74udePUaIk", # Replace with your API key
  "authDomain": "saic-ipl.firebaseapp.com",            # Replace with your project's domain
  "databaseURL": "https://saic-ipl-default-rtdb.asia-southeast1.firebasedatabase.app/", # Replace with your database URL
  "storageBucket": "saic-ipl.appspot.com"              # Replace with your storage bucket
}

firebase = pyrebase.initialize_app(config)

# Write the dictionary to Firebase
db = firebase.database()
db.child("data").set(data)
