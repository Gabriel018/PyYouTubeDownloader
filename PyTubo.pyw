import sys

from pytube import YouTube
import PySimpleGUI as py
from pytube import Playlist
from pytube.cli import on_progress
from self import self

py.theme('Dark green 3')



def main():

            layout = [
                      [ py.Text("Digite o link para Download:",font='Arial 12')],
                      [py.Input(size=(34,2),key='link')],
                      [py.Text("Escolha onde salvar o arquivo", font='Arial 12')],
                      [py.Input(size=(28, 2), key='savelink'),py.FolderBrowse()],
                      [py.Text("")],
                      [py.Button("Video",font='Arial 12'),py.Button("Audio",font='Arial 12'),
                       py.Button("Sair",font='Arial 12',button_color='red')]
            ]
            janela = py.Window("Video_Download",layout,size=(300,300))

            while True:

               event ,values = janela.read()
               linkv = values['link']
               savelink = values['savelink']
               video = YouTube(linkv)

               if event == 'Video':
                 py.popup(" titulo do video:  ", video.title, font="arial 13")
                 py.popup_notify("Aguarde o Donwload ser concluido.. ", fade_in_duration=8)
                 video.streams.get_by_resolution(resolution='720p').download(savelink)
                 janela.find_element('link').update('')
                 janela.find_element('savelink').update('')
                 py.popup("Download concluido",font="arial 13")

               if event == 'Audio':
                py.popup(" titulo do video:  ", video.title, font="arial 13")
                py.popup("Download concluido...", font="arial 13", text_color="blue")
                video. streams.get_audio_only().download(savelink)
                janela.find_element('link').update('')
                janela.find_element('savelink').update('')
                py.popup("Download concluido", font="arial 13")

               if event == 'Sair':
                sys.exit()

if __name__ == '__main__':
    main()