import json
from datetime import timedelta

from googleapiclient.discovery import build
import time


# Replace with your API key

youtube = build('youtube', 'v3', developerKey=api_key)


# Function to get 500 items (Timing is different each time, depending on connection and other factors.)
# I average a ~ 30 second parse
def parse(query):
    items = []
    next_page_token = None

    while len(items) < 500:
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        # Get view counts for each video in the current batch
        for item in response['items']:
            video_id = item['id']['videoId']
            video_request = youtube.videos().list(
                part="statistics",
                id=video_id
            )
            video_response = video_request.execute()
            view_count = video_response['items'][0]['statistics']['viewCount']
            item['viewCount'] = view_count
            items.append(item)

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    # Limit to 500 items
    return items[:500]

start = time.time()
jsoned = parse("tf2 gambling")

with open('youtube_items.json', 'w') as json_file:
    json.dump(jsoned, json_file, indent=4)

end = time.time()
time_lapsed = end - start
timer = str(time_lapsed)
print("Exported 500 items to youtube_items.json in " + timer)
