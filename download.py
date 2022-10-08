from pytube import YouTube 

#tempat save
SAVE_PATH = "C:/Users/User/Videos/download" 

#video yang mau di download
url = 'https://youtube.com/shorts/YjjcbPQP2Cw?feature=share'
my_video = YouTube(url)
print(my_video.title)
my_video = my_video.streams.get_highest_resolution()

#download video
try:
    my_video.download(SAVE_PATH)
    print("Download Success")
except:
    print("Some Error!")
