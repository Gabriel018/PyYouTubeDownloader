from pytube import YouTube
import PySimpleGUI as py



def main():

    layout = [
              [ py.Text("digite o link")],
              [py.Input(size=(20,2),key='link')],
               [py.Button("Baixar")]
    ]

    janela = py.Window("Video_Download",layout)

    while True:
       event,values = janela.read()

       linkv = values['link']


       pv = YouTube(linkv)
       if event == 'Baixar':
         pv. streams.get_by_resolution(resolution='720p').download('C:\PysimpleGui')



if __name__ == "__main__":
    main()