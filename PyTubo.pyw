from pytube import YouTube
import PySimpleGUI as py


py.theme('Dark green 3')
def main():

    layout = [
              [ py.Text("Digite o link para Download:",font='Arial 12')],
              [py.Input(size=(34,2),key='link')],
              [py.Text("Escolha onde salvar o arquivo", font='Arial 12')],
              [py.Input(size=(28, 2), key='savelink'),py.FolderBrowse()],
              [py.Button("Baixar",font='Arial 12')]
    ]
    janela = py.Window("Video_Download",layout,size=(300,200))

    while True:
       event,values = janela.read()
       linkv = values['link']
       savelink = values['savelink']
       pv = YouTube(linkv)
       if event == 'Baixar':
         pv. streams.get_by_resolution(resolution='720p').download(savelink)


if __name__ == "__main__":
    main()
