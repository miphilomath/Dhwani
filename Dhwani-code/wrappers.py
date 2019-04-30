#!/usr/bin/env python3

import os, subprocess
from multiprocessing import Queue, Process
from random import randint

def volumeInc(percentage):
    if os.system("amixer -D pulse sset Master %s\%+" %(percentage)):
        return True
    return False

def volumeDec(percentage):
    if os.system("amixer -D pulse sset Master %s\%-" %(percentage)):
        return True
    return False

def volumeSet(percentage):
    if os.system("amixer -D pulse sset Master %s\%" %(percentage)):
        return True
    return False

def backlightInc(percentage):
    if os.system("xbacklight -inc %s" %(percentage)):
        return True
    return False

def backlightDec(percentage):
    if os.system("xbacklight -dec %s" %(percentage)):
        return True
    return False

def backlightSet(percentage):
    if os.system("xbacklight -set %s" %(percentage)):
        return True
    return False

def launch(exec_name):
    os.system(exec_name)

def openMusicPlayer(name=False):
    application_desktop = subprocess.Popen(["xdg-mime", "query", "default", "audio/wav"], stdout=subprocess.PIPE).stdout.read()
    possible_execs = []
    print(application_desktop)
    if application_desktop and not name:
        with open("/usr/share/applications/%s" %(application_desktop.decode('utf-8')[:-1]), "r") as f:
            for line in f.readlines():
                if line[:4] in "Exec":
                    possible_execs.append(line.split()[0].split("=")[1])

        browser = subprocess.Popen(possible_execs[0])    
    else:
        print("[WARNING] Could not find xdg default audio player! Trying to use manually set \
        player")
        try:
            browser = subprocess.Popen(name.split())
            print("[INFO   ] Opened default music player")
        except (TypeError, FileNotFoundError) as e:
            raise Exception('Could not open default music player. Have you set it? Does it exist on the system?')
        
        return False

def openWebBrowser(name=False):
    application_desktop = subprocess.Popen(["xdg-mime", "query", "default", "audio/html"], stdout=subprocess.PIPE).stdout.read()
    possible_execs = []
    print(application_desktop)
    if application_desktop and not name:
        with open("/usr/share/applications/%s" %(application_desktop.decode('utf-8')[:-1]), "r") as f:
            for line in f.readlines():
                if line[:4] in "Exec":
                    possible_execs.append(line.split()[0].split("=")[1])

        browser = subprocess.Popen(possible_execs[0])    
    else:
        print("[WARNING] Could not find xdg default web browser! Trying to use manually set \
        player")
        try:
            browser = subprocess.Popen(name.split())
            print("[INFO   ] Opened default web browser")
        except (TypeError, FileNotFoundError) as e:
            raise Exception('Could not open default web browser. Have you set it? Does it exist on the system?')
        
        return False


