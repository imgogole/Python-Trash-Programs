# YT Video Downloader
# Function that downloads your favorite Youtube video !

import pytube

Choice = input("Enter the link : ")
Result = pytube.Youtube(Choice)
Result.streams.first().download()
print("Downloaded !")
