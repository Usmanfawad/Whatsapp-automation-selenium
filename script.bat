@ECHO OFF
ECHO ------------Opening google chrome-------------
cd /d "C:\Program Files\Google\Chrome\Application"
START chrome.exe --remote-debugging-port=8989 --user-data-dir="D:\Professional data\Professional\Fiverr\Clients\doni283\ChromeProfileData"
TIMEOUT 5
EXIT 0
