import pywinauto,time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

app = Application().start(cmd_line=u"C:\\Users\\HP\\AppData\\Roaming\\Spotify\\Spotify.exe")
time.sleep(2)
app.Name.Topplaylistofyour.connect.click()