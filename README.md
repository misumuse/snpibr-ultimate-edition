# snpibr // system terminal dashboard

![python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![linux](https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![license](https://img.shields.io/badge/license-GPLV3-blue?style=for-the-badge)
![status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)

### what is this
snpibr is your personal command center for crostini. it pulls your hardware specs, checks the weather without using as much ram, and lets you control your music without leaving the terminal. it’s built to look like a system breach but actually gives you useful data. oh and yeah you don't have to use crostini to use this, any distro will work. 

### how to boot it up
if you aren't already in the sandbox (this one a cringe example), get back in:
1. `cd ~/projects/hacker_weather`
2. `source .venv/bin/activate`
3. `python3 sys_scan.py`

<img width="1364" height="718" alt="Screenshot 2026-02-20 11 25 47 PM" src="https://github.com/user-attachments/assets/563a74e4-871f-4c84-aeae-4389c8811a6c" />

### the pages
* **(h)ome**: the main dashboard. shows cpu/ram bars, the local time, and the weather.
* **(m)usic**: the audio deck. shows what’s playing, the artist, and a volume bar. 
* **(proc)esses**: the snitch page. shows the top 8 apps eating your ram so you can see what’s slowing you down.

<img width="1365" height="718" alt="Screenshot 2026-02-20 11 26 12 PM" src="https://github.com/user-attachments/assets/a1ba6c89-c4ad-476e-a11b-950179b2d59b" />

### controls (type these and hit enter)
* `p` -> play or pause your music/video.
* `s` -> skip to the next track.
* `b` -> go back to the previous track.
* `u` -> volume up (crank it 5%).
* `d` -> volume down (drop it 5%).
* `q` -> kill the connection and exit snpibr.

<img width="1365" height="718" alt="Screenshot 2026-02-20 11 26 02 PM" src="https://github.com/user-attachments/assets/cf87d2d3-d6da-4d27-9545-b1ad5c4ade1b" />

### the tech inside
* **weather**: uses open-meteo + geocoder. it finds your ip, gets your lat/long, and pulls raw data. no api keys needed, no rate-limit blocks.
* **specs**: uses `psutil` to scrape your linux container’s brain.
* **music**: uses `playerctl`. it talks to the chromeos media bridge to see what your browser is playing.
* **license**: gnu gplv3. copyleft protected.

### fixing stuff
* **weather says offline?** check your internet. if it still says offline, open-meteo might be down or your geocoder didn't find your ip yet.
* **music says inactive?** make sure you have a tab open with spotify or youtube and that you've hit play at least once so the system sees the media stream.
  here is how to fix the music tab so it actually talks to your spotify or youtube tabs again.

step 1: the chrome "handshake" fix
open a new tab in your chrome browser and go to these two flags. make sure they are set to enabled:

chrome://flags/#global-media-controls

chrome://flags/#hardware-media-key-handling

pro-tip: after you change these, you have to click the relaunch button at the bottom of the screen for the fix to kick in.

step 2: refresh the audio bridge
if playerctl still says "no players found," run these commands in your terminal to kick the audio service back to life:

Bash
# reset the pulse audio config
rm -rf ~/.config/pulse
# restart the user-level audio service (this works where systemctl fails)
systemctl --user restart cros-pulse-config
step 3: testing the link
to verify the fix before you open snpibr, run this:

Bash
playerctl --list-all
if it shows chromium or spotify, you're golden. if it’s empty, play a video in a chrome tab first, then check again.


* **don't know what snpibr means?** I don't either, your guess is as good as mine
