import win32gui

def stringFinder():
    songTitle = "No song is being played!"
    vlcStorage = []
    def enumWindowsProc(hwnd,lParam):
        g = win32gui.GetWindowText(hwnd)
        vlcStorage.append(g)
    win32gui.EnumWindows(enumWindowsProc,0)
    for title in vlcStorage:
        if "VLC media player" in title:
            songTitle = title
            songTitle = songTitle.replace("- VLC media player","")
            songTitle = songTitle.replace("VLC media player","")
            songTitle = songTitle.replace(".mp3","")
            songTitle = songTitle.replace(".flac","")
            if not songTitle.strip():
                songTitle = "No song is being played!"
            return songTitle
    return songTitle


def txtStorage(songName):
    file = open("Music.txt","w")
    file.write(songName)
    file.truncate()

    
def main():
    print("test")
    input("Press any key to begin searching for songs being played by VLC media player\n")
    initialTitle = stringFinder()
    txtStorage(initialTitle)
    try:
        while True:
            newTitle = stringFinder()
            if initialTitle == newTitle:
                pass
            else:
                print("The song being shown to the stream is : ",newTitle)
                txtStorage(newTitle)
                initialTitle = newTitle
                
        
    except KeyboardInterrupt:
            pass
            
            
if __name__ == '__main__':
    main()