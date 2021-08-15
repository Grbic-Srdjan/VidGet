from pytube import YouTube

YouTubeLink = input("Enter the URL to the video, that you want to download: ");
YouTubeVideo = YouTube(YouTubeLink); 
Videos = YouTubeVideo.streams.all();
Video = list(enumerate(Videos))
for i in Video:
    print(i)

FormatOption = int(input("Enter one of the number above to get the video in format, that you want. ")); 
VideoToDownload = Videos[FormatOption];
VideoToDownload.download();

print("Your Awesome Video has been Downloaded! ");
print("You are Welcome :) . "); 
