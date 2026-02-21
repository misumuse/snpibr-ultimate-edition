# snpibr // system terminal dashboard

![python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![linux](https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![license](https://img.shields.io/badge/license-GPLV3-blue?style=for-the-badge)
![status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)

### what is this
snpibr is your personal command center for crostini. it pulls your hardware specs, checks the weather without using mid emojis, and lets you control your music without leaving the terminal. it’s built to look like a system breach but actually gives you useful data.

### how to boot it up
if you aren't already in the sandbox (this one a cringe example), get back in:
1. `cd ~/projects/hacker_weather`
2. `source .venv/bin/activate`
3. `python3 sys_scan.py`

### the pages
* **(h)ome**: the main dashboard. shows cpu/ram bars, the local time, and the weather.
* **(m)usic**: the audio deck. shows what’s playing, the artist, and a volume bar. 
* **(proc)esses**: the snitch page. shows the top 8 apps eating your ram so you can see what’s slowing you down.

### controls (type these and hit enter)
* `p` -> play or pause your music/video.
* `s` -> skip to the next track.
* `b` -> go back to the previous track.
* `u` -> volume up (crank it 5%).
* `d` -> volume down (drop it 5%).
* `q` -> kill the connection and exit snpibr.

### the tech inside
* **weather**: uses open-meteo + geocoder. it finds your ip, gets your lat/long, and pulls raw data. no api keys needed, no rate-limit blocks.
* **specs**: uses `psutil` to scrape your linux container’s brain.
* **music**: uses `playerctl`. it talks to the chromeos media bridge to see what your browser is playing.
* **license**: gnu gplv3. copyleft protected.

### fixing stuff
* **weather says offline?** check your internet. if it still says offline, open-meteo might be down or your geocoder didn't find your ip yet.
* **music says inactive?** make sure you have a tab open with spotify or youtube and that you've hit play at least once so the system sees the media stream.
