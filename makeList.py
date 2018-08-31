from bs4 import BeautifulSoup
import urllib2
import re
import requests
yt_url="www.youtube.com"
import httplib2
import os
import sys



# Sample Python code for user authorization

import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
  results = service.channels().list(
    **kwargs
  ).execute()
  
  print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
       (results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']['viewCount']))

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  channels_list_by_username(service,
      part='snippet,contentDetails,statistics',
      forUsername='GoogleDevelopers')

#channelName=raw_input("Enter Channel URL: ")
#type(channelName)
#print("You Entered ", channelName)
#print("Passing channel URL...")
#print("Please wait...")
        
#url=(channelName)
#url='https://www.youtube.com/user/fireflies2781996'
print("done...")

print("Opening URL...")
#html=urllib2.urlopen(url)
#print("done...")

#print("Parsing URL")
#response=html.read()
#newSoup=BeautifulSoup(response,"html.parser")
#print("done...")

#print("Collecting links...")
#yt_links=newSoup.find_all("a", class_="yt-uix-tile-link")
#print("done...")

#print("Writing to file...please wait")



#with open('link.txt','a') as file:
#    for link in yt_links:
#        yt_href=link.get("href")
#        yt_title=link.get("title")
#        file.write(yt_url+str(yt_href)+"\n")      
        #file.write(yt_url+str(yt_href)+"||Title:"+yt_title.encode('utf-8')+"\n")      
#file.close()


#for link in yt_links:
#    yt_href=link.get("href")
#    complete_link = yt_url+yt_href
#    print(complete_link)
    #add_video=urllib2.urlopen(complete_link)
    #elment=add_video.find_next_siblings(id="checkbox")
    #print(element)
    

#raw_link_array = []
#with open('link.txt') as link_file:
#    raw_link_array = link_file.readlines()
#link_file.close()

#print(link_array)


#new_link_array = []
#new_link_array.append(raw_link_array[0])
#new_link_array.append(raw_link_array[1])
#new_link_array.append(raw_link_array[2])
#print(new_link_array)


html2=urllib2.urlopen("https://www.youtube.com/watch?v=sxkuPgirNOs")
response2=html2.read()
newSoup2=BeautifulSoup(response2,"html.parser")

#first_link=newSoup2.find(string="Add to")
#second_link=first_link.find_parent("div")
#third_link=second_link.find_next_siblings("div")
#print(first_link)
#print(second_link)
#print(third_link)


parent=newSoup2.find("body")
#print(parent)
child=parent.find_next()
child2=child.find_next()
child3=child2.find_next()
child4=child3.find_next()
child5=child4.find_next()
print(child5)

with open("parse.txt",'a') as file:
    for link in response2:
        file.write(str(response2)+('\n'))



print("done...")
print("exiting...")

                              
                              
                              
                              
                              
                              
                              
                              
                              
