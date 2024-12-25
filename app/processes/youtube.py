import json
import os
import datetime
from collections import Counter
from googleapiclient.discovery import build
import app.processes.color_analysis as ca
from app.DataClasses import videoItem

# Set the path to your service account key file
cred = os.getenv("ServiceAcct")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "path/to/service_account_key.json"

# Build the YouTube service using the credentials
youtube = build('youtube', 'v3')

from datetime import datetime

def parse_and_process(query, title_counter, description_counter, color_list):
    items = []
    next_page_token = None

    while len(items) < 500:
        try:
            # Fetch search results
            request = youtube.search().list(
                part="snippet",
                q=query,
                type="video",
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()

            for item in response['items']:
                try:
                    # Get video statistics
                    video_id = item['id']['videoId']
                    video_request = youtube.videos().list(
                        part="statistics",
                        id=video_id
                    )
                    video_response = video_request.execute()

                    # Attach statistics to the item
                    statistics = video_response['items'][0].get('statistics', {})
                    view_count = statistics.get('viewCount', '0')
                    item['viewCount'] = view_count

                    # Process video data
                    snippet = item.get('snippet', {})
                    required_keys = ['title', 'description', 'thumbnails']
                    if not all(key in snippet for key in required_keys):
                        continue  # Skip invalid items

                    title = snippet['title']
                    description = snippet['description']
                    thumbnails = snippet['thumbnails']
                    publish_time_str = snippet.get('publishedAt')

                    # Parse the publish time string to a datetime object
                    try:
                        publish_time = datetime.fromisoformat(publish_time_str.replace('Z', '+00:00'))

                    except ValueError as e:
                        print(f"Error parsing publish time: {e}")
                        publish_time = None

                    # Update counters
                    title_counter.update(title.split())
                    description_counter.update(description.split())

                    # Compute view weight
                    if publish_time:
                        view_weight = processViewWeight(view_count, publish_time)
                    else:
                        view_weight = 0  # Set to 0 if publish_time is not valid

                    # Process thumbnail colors
                    if 'high' in thumbnails and 'url' in thumbnails['high']:
                        high_res_thumbnail = thumbnails['high']['url']
                        list_of_colors = ca.getColors(high_res_thumbnail)
                        for color in list_of_colors:
                            color_list.update([color['color']])

                    # Construct video item
                    video_item = videoItem(view_weight, color_list, title_counter, description_counter)
                    items.append(video_item)

                except Exception as inner_e:
                    print(f"Error processing video {item.get('id', {}).get('videoId')}: {inner_e}")

            # Handle pagination
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        except Exception as outer_e:
            print(f"Error fetching data: {outer_e}")
            break

    print("Successfully parsed and processed data")
    return items


def processViewWeight(views,uploaded):
    currentTime = datetime.datetime.now()
    timeDifference = currentTime - uploaded
    total_seconds = timeDifference.total_seconds()
    weight = views / total_seconds
    return weight
