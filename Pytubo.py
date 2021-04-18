from tqdm import  tqdm
from time import sleep

from pytube import *





#Video unico

previoprogress = 0
#Mostra o progresso do download
def progress(stream,chunk,bytes_remainig):
    global  previoprogress
    total_size  = stream.filesize
    bytes_download = total_size - bytes_remainig

    liveprogress =  (int)(bytes_download/ total_size * 100)
    if liveprogress > previoprogress:
        previoprogress = liveprogress
        print(liveprogress)

url = input("Digite seu Url")
p1 = (YouTube(url))
p1.register_on_progress_callback(progress)
p1.streams.first().download("c:/Users/User/Desktop\study\Teste")




#Apenas Audio
#p1.streams.get_audio_only().download("c:/Users/User/Desktop/Music_2/Guns_n_Roses")

# Playlist
#p2 = Playlist("https://www.youtube.com/watch?fbclid=IwAR1jLStRwdzHUfLo5Jb_H3WWD-YGPVVmSCr71oisfamYaxKOBugDlbfo4SI&v=-4pXPDO9PTU&feature=youtu.be")

#for video in p2.videos:
    #video.streams.get_audio_only().download("c:/Users/User/Desktop/study")


