#!/usr/bin/env

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# Settings
# YouTube Data API
YOUTUBE_API_KEY = ''
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
YOUTUBE_SEARCH_CHANNELID = 'UCN-bFIdJM0gQlgX7h6LKcZA'
YOUTUBE_SEARCH_QUERY = 'しゅわりんTV'
YOUTUBE_SEARCH_PART = 'id'
YOUTUBE_SEARCH_MAX_RESULTS = 50
YOUTUBE_SEARCH_ORDER = 'date'

def youtube_search(part, query, maxResults, order, channelId):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=YOUTUBE_API_KEY
    )

    search_response = youtube.search().list(
            part=part,
            q=query,
            maxResults=maxResults,
            order=order,
            channelId=channelId
    ).execute()

    return search_response


tmp = youtube_search(YOUTUBE_SEARCH_PART,YOUTUBE_SEARCH_QUERY,YOUTUBE_SEARCH_MAX_RESULTS,YOUTUBE_SEARCH_ORDER,YOUTUBE_SEARCH_CHANNELID)

for result in tmp.get("items", []):
    print(result)