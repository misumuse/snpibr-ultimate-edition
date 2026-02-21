import os
import platform
import socket
import requests
import psutil
import subprocess
import geocoder
from datetime import datetime, timezone
import time

# Styling
GREEN, RED, CYAN, YELLOW, RESET, BOLD = "\033[38;5;46m", "\033[38;5;196m", "\033[38;5;51m", "\033[38;5;226m", "\033[0m", "\033[1m"

def get_weather():
    """Stable weather using Open-Meteo (No API key required)"""
    try:
        g = geocoder.ip('me')
        if not g.latlng: return "LOC_ERROR"
        lat, lon = g.latlng
        
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()['current_weather']
            temp = data['temperature']
            code = data['weathercode']
            # Simple text mapping for codes
            status = "CLEAR" if code <= 3 else "CLOUDY" if code <= 67 else "STORM"
            return f"{temp}C | {status}"
        return "API_ERR"
    except:
        return "OFFLINE"

def get_player_data(query):
    try:
        return subprocess.check_output(["playerctl", "metadata", query], stderr=subprocess.DEVNULL).decode().strip()
    except: return "N/A"

def draw_header():
    print(f"{GREEN}{BOLD}  _____ _   _ _____ _____ ____  _____  ")
    print(r" / ____| \ | |  __ \_   _|  _ \|  __ \ ")
    print(r"| (___ |  \| | |__) || | | |_) | |__) |")
    print(r" \___ \| . ` |  ___/ | | |  _ <|  _  / ")
    print(r" ____) | |\  | |    _| |_| |_) | | \ \ ")
    print(r"|_____/|_| \_|_|   |_____|____/|_|  \_\ " + f"{RESET}")

def main():
    page = "HOME"
    weather_cache = get_weather()
    last_weather_update = time.time()

    while True:
        os.system('clear')
        draw_header()
        
        # Refresh weather every 10 mins
        if time.time() - last_weather_update > 600:
            weather_cache = get_weather()
            last_weather_update = time.time()

        print(f"{CYAN}[+]{RESET} MODE: {page} | UTC: {datetime.now(timezone.utc).strftime('%H:%M')}")
        print(f"{GREEN}{'='*60}{RESET}")

        if page == "HOME":
            cpu = psutil.cpu_percent()
            cpu_bar = "█" * int(cpu/10) + "░" * (10 - int(cpu/10))
            mem = psutil.virtual_memory().percent
            mem_bar = "█" * int(mem/10) + "░" * (10 - int(mem/10))
            
            print(f"{YELLOW}[SYSTEM]{RESET} CPU: [{cpu_bar}] {cpu}%")
            print(f"{YELLOW}[MEMORY]{RESET} RAM: [{mem_bar}] {mem}%")
            print(f"{YELLOW}[ENVIR.]{RESET} {weather_cache}")
            print(f"{YELLOW}[LOCAL ]{RESET} {datetime.now().strftime('%H:%M:%S')}")

        elif page == "MUSIC":
            try:
                status = subprocess.check_output(["playerctl", "status"], stderr=subprocess.DEVNULL).decode().strip()
            except: status = "STOPPED"
            
            # Simulated volume bar
            try:
                vol = float(subprocess.check_output(["playerctl", "volume"], stderr=subprocess.DEVNULL).decode().strip())
                vol_pc = int(vol * 100)
                vol_bar = "█" * int(vol_pc/10) + "░" * (10 - int(vol_pc/10))
            except: vol_bar, vol_pc = "░░░░░░░░░░", "0"

            print(f"{CYAN}--- SNPIBR AUDIO CONTROL ---{RESET}")
            print(f"STATUS:   {BOLD}{status}{RESET}")
            print(f"TRACK:    {get_player_data('title')[:40]}")
            print(f"ARTIST:   {get_player_data('artist')[:40]}")
            print(f"VOLUME:   [{vol_bar}] {vol_pc}%")
            print(f"\n{YELLOW}KEYS: (p)ause, (s)kip, (b)ack, (u)p, (d)own{RESET}")

        elif page == "PROC":
            print(f"{CYAN}--- TOP PROCESSES ---{RESET}")
            processes = sorted(psutil.process_iter(['pid', 'name', 'memory_percent']), 
                             key=lambda x: x.info['memory_percent'], reverse=True)[:8]
            for p in processes:
                print(f"{p.info['pid']:<8}{p.info['name'][:18]:<20}{round(p.info['memory_percent'], 2):<10}%")

        print(f"{GREEN}{'='*60}{RESET}")
        print(f"{BOLD}NAV: (h)ome, (m)usic, (proc)esses | (q)uit{RESET}")
        
        cmd = input(f"{CYAN}SNPIBR >> {RESET}").lower().strip()

        if cmd == 'q': break
        elif cmd == 'h': page = "HOME"
        elif cmd == 'm': page = "MUSIC"
        elif cmd in ['proc', 'processes']: page = "PROC"
        
        # Audio Logic
        if cmd == 'p': os.system("playerctl play-pause")
        elif cmd == 's': os.system("playerctl next")
        elif cmd == 'b': os.system("playerctl previous")
        elif cmd == 'u': os.system("playerctl volume 0.05+")
        elif cmd == 'd': os.system("playerctl volume 0.05-")

if __name__ == "__main__":
    main()