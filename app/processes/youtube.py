import json
import os
import datetime
from collections import Counter
from googleapiclient.discovery import build
import app.processes.color_analysis as ca
import app.DataClasses as dc
from app.DataClasses import videoItem

# Set the path to your service account key file
cred = os.getenv("ServiceAcct")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "C:/Users/aaron/Downloads/gen-lang-client-0645691485-55f5e55d5b80.json"

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

    return json.dumps(items[:500], indent=2)


def videoProcess(jsonContent, titlecounter, descriptioncounter, colorlist):
    for item in jsonContent['title']:
        titlecounter.update(item)
    for item in jsonContent['description']:
        descriptioncounter.update(item)

    viewWeight = processViewWeight(jsonContent['viewCount'], jsonContent['publishTime'])

    high_res_thumbnail = jsonContent['thumbnails']['high']['url']
    listofcolor = ca.getColors(high_res_thumbnail)

    for color in listofcolor:
        c = color['color']
        colorlist.update(c)

    return videoItem(viewWeight, colorlist, titlecounter, descriptioncounter)


def processViewWeight(views,uploaded):
    currentTime = datetime.datetime.now()
    timeDifference = currentTime - uploaded
    total_seconds = timeDifference.total_seconds()
    weight = views / total_seconds
    return weight
