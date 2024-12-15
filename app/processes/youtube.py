import os
from googleapiclient.discovery import build

# Set the path to your service account key file
cred = os.getenv("ServiceAcct")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "Path/To/Json"

# Build the YouTube service using the credentials
youtube = build('youtube', 'v3')

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

    return items[:500]

# Example usage
query = "your_search_query"
items = parse(query)
for item in items:
    print(f"Title: {item['snippet']['title']}, Views: {item['viewCount']}")
