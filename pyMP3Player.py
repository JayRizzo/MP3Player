#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Tue Sep  6 19:43:15 2022 CDT
# Last ModDate: Tue Sep 27 21:12:59 2022 CDT
# =============================================================================
# Notes:
# =============================================================================
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # noqa This is used to hide the default pygame import print statement.
from mp3TagEditor import MP3TagYourSong
from mutagen import id3
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from os import getcwd
from os import path
from os.path import basename
from os.path import exists as filepathexist
from os.path import expanduser
from os.path import isfile
from os.path import join
from os.path import splitext
from pygame import mixer
from random import shuffle
from time import sleep
import glob
from mp3TagEditor import MP3TagYourSong
import PySimpleGUI as sg
import random
import threading
import time
import tkinter

# ========================================================================
# Load Emoji Characters In Place Of Buttons ==============================
# ========================================================================
BACKARROW = '\U000023EA'
PLAYBUTTN = '\U000025B6\U0000FE0F'
FORWARROW = '\U000023E9'
PAUSEBUTN = '\U000023F8'
STOPBUTTN = '\U000023F9'
MUSICNOTE = '\U0001F3B5'
REPEATBTN = '\U0001F501'
SHFLLBUTN = '\U0001F500'
MUTEBUTTN = '\U0001F507'
SPKRBUTTN = '\U0001F50A'
INFOBUTTN = '\U00002139'

class App(object):
    """JayRizzo Music Player."""
    def __init__(self):
        """JayRizzo Music Player Initial Launch Setup."""
        super().__init__()
        # ========================================================================
        # ========================= Initialize the Mixer =========================
        # ========================================================================
        self.mixer_init                 = mixer.init()          # PyGame Initializer
        self.STOPPED                    = True                  # Player Stopped Status
        self.PAUSED                     = False                 # Player Paused Status
        self.MUTED                      = False                 # Player Mute Status
        self.PLAYLSTPTH                 = []                    # Current Playlist Path
        self.PLAYLSTBOX                 = []                    # Current Playlist Box
        self.CURSELECTDSONG             = ''                    # Current Selected Song Time
        self.CURSONGTIME                = 0                     # Current Song Time Song
        self.SLIDERTIME                 = 0                     # Current Song Time Slider
        self.SETPOSITION                = 0                     # Current Song Time Slider
        self.SONGLENGTH                 = 0                   # Default Song Length Slider
        self.TOTALSONGL                 = 0                     # Total Time For All Songs
        self.VOLUME                     = 100.0                 # Set Initial Volume For PyGame Player
        self.PLAYER                     = ''
        self.FILENAME                   = ''
        self.SONGNAME                   = ''
        self.FULLFILEPATH               = ''
        self.MP3SONGARTIST              = ''
        self.MP3SONGALBUM               = ''
        self.MP3SONGPLAYCOUNT           = ''

        # ========================================================================
        # ==================== Initialize the SimpleGUI Layout ===================
        # ========================================================================
        self.theme = sg.ChangeLookAndFeel('Dark')

        self.menu_def = [['File', ['Open', 'Save', 'Exit',]],
                         ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                         ['Help', 'About...'],
                        ]

        self.option = sg.SetOptions (background_color = 'black',
            element_background_color = 'skyBlue',
            text_element_background_color = 'black',
               font = ('Arial', 10, 'bold'),
               text_color = 'lightgrey',
               input_text_color ='White',
               button_color = ('Blue', 'black')
               )


        self.column1 = [[sg.Listbox(self.PLAYLSTBOX,   size=(70, 10), key="-PLAYLISTBOX-", enable_events=True)]]
        self.column2 = [
                        [sg.FileBrowse(size=(17, 1), key="-MP3SONG-", enable_events=True, file_types=(("MP3 files", "*.mp3"),))],
                        [sg.Text(f'Song Time: {self.CURSONGTIME} of {self.SONGLENGTH}', key = "-SONGLENGTHDURATIONTEXT-", justification = 'CENTER')],
                        [sg.Text(f'Song  : {self.SONGNAME}', font=("Helvetica", 25), key = "-SONGNAME-", enable_events=True, justification='center')],
                        [sg.Text(f'Artist: {self.MP3SONGARTIST}',   key = "-SONGARTIST-",   justification = 'left')],
                        [sg.Text(f'Album : {self.MP3SONGALBUM}',    key = "-SONGALBUM-",    justification = 'left')],
                        [sg.Text(f'Plays : {self.MP3SONGPLAYCOUNT}',    key = "-SONGPLAYCOUNT-",    justification = 'left')],
                      ]
        self.column3 = [[sg.Slider(range=(0, 100), size=(10, 15), orientation='v', key='-VOLUMESLIDERPOS-',  default_value=100, disabled=False, disable_number_display=True, enable_events=True, tick_interval=0.1)]]
        self.row2    = [[sg.Slider(range=(0, 100), size=(60, 15), orientation='h', key='-SONGSLIDERPOS-',    default_value=0, disabled=True,  disable_number_display=True, enable_events=True, tick_interval=0)]]
        self.row3 = [
                       sg.Button(f"{BACKARROW}", key="-BACKSONG-" ,     disabled=True, font=("Helvetica", 60), enable_events=True),
                       sg.Button(f"{PLAYBUTTN}", key="-PLAYSONG-" ,     disabled=True, font=("Helvetica", 60), enable_events=True),
                       sg.Button(f"{PAUSEBUTN}", key="-PAUSESONG-",     disabled=True, font=("Helvetica", 60), enable_events=True),
                       sg.Button(f"{STOPBUTTN}", key="-STOPSONG-" ,     disabled=True, font=("Helvetica", 60), enable_events=True),
                       sg.Button(f"{FORWARROW}", key="-FORWARDSONG-" ,  disabled=True, font=("Helvetica", 60), enable_events=True),
                    ]
        self.row4 = [
                        sg.Button(f"{REPEATBTN}", key="-REPEATSONG-" ,   disabled=True, font=("Helvetica", 60), enable_events=True),
                        sg.Button(f"{SHFLLBUTN}", key="-SHUFFLESONG-" ,  disabled=True, font=("Helvetica", 60), enable_events=True),
                        sg.Button(f"{MUTEBUTTN}", key="-MUTESONG-",      disabled=True, font=("Helvetica", 60), enable_events=True),
                        sg.Button(f"{SPKRBUTTN}", key="-UNMUTESONG-" ,   disabled=True, font=("Helvetica", 60), enable_events=True),
                        sg.Button(f"{INFOBUTTN}", key="-INFOSONG-" ,     disabled=True, font=("Helvetica", 60), enable_events=True),
                    ]

        self.Layout = [[
                                  sg.Column(self.column1, element_justification='left', vertical_alignment='left',   justification='center', pad=(10, 10), key='LCOL')
                                , sg.Column(self.column2, element_justification='left', vertical_alignment='center', justification='center', pad=(10, 10), key='CCOL')
                                , sg.Column(self.column3, element_justification='left', vertical_alignment='left',   justification='center', pad=(10, 10), key='RCOL2')
                                ],
                               self.row2,
                               self.row3,
                               self.row4]

        self.window = sg.Window(F"{MUSICNOTE} JayRizzo's MP3 Player {MUSICNOTE}",
                                [[sg.Menu(self.menu_def)], self.Layout],
                                font='Arial 18', resizable=True, grab_anywhere=False)

    def DurationFromSeconds(self, s=0):
        """
            Convert Seconds to Human Readable Time Format.
            INPUT : s (AKA: Seconds)
            OUTPUT: 00:00:00
        """
        m, s        = divmod(s, 60)
        h, m        = divmod(m, 60)
        d, h        = divmod(h, 24)
        y, d        = divmod(d, 365)
        PRINTZTIME  = f"{h:02.0f}:{m:02.0f}:{s:02.0f}"
        return PRINTZTIME

    def ImageButton(self, title, key):
        return sg.Button(title, button_color=('#F0F0F0', '#F0F0F0'),
                    border_width=0, key=key)

    def loadSong(self, filename):
        mixer.music.stop()
        mixer.music.load(filename)
        self.PLAYLSTBOX = basename(filename).split('/')[0].split('.')[0]
        print(f"PLAYLISTBOX: {self.PLAYLSTBOX}")
        self.window['-PLAYLISTBOX-'].update([self.PLAYLSTBOX])
        self.setSongLength(filename)

    def getSongName(self):
        return self.SONGNAME

    def getSongMetaData(self, filename):
        self.MP3SONGARTIST = MP3TagYourSong(self.FILENAME).getSongArtist()
        self.MP3SONGALBUM = MP3TagYourSong(self.FILENAME).getSongAlbum()
        self.MP3SONGNAME = MP3TagYourSong(self.FILENAME).getSongName()
        self.MP3SONGPLAYCOUNT = MP3TagYourSong(self.FILENAME).getSongPlayCount()
        self.window['-SONGNAME-'].update(f"Song: {self.MP3SONGNAME}")
        self.window['-SONGARTIST-'].update(f"Artist: {self.MP3SONGARTIST}")
        self.window['-SONGALBUM-'].update(f"Album: {self.MP3SONGALBUM}")
        self.window['-SONGPLAYCOUNT-'].update(f"Plays: {self.MP3SONGPLAYCOUNT}")
        return self.MP3SONGARTIST

    def LoadSong(self):
        self.FILENAME = self.values['-MP3SONG-']
        self.loadSong(self.FILENAME)
        self.setSongName(self.FILENAME)
        self.getSongMetaData(self.FILENAME)
        # Enable Buttons After Song Loaded Event
        self.window['-PLAYSONG-'].update(disabled=False)
        self.window['-PAUSESONG-'].update(disabled=False)
        self.window['-STOPSONG-'].update(disabled=False)
        self.window['-SONGSLIDERPOS-'].update(disabled=False)
        self.window['-SONGSLIDERPOS-'].update(range=(0,self.SONGLENGTH))
        print(f"02 self.event: {self.event}  self.values: {self.values} self.FILENAME: {self.FILENAME} {self.SONGNAME}")


    def setSongName(self, filename):
        self.SONGNAME = basename(filename).split('/')[0].split('.')[0]
        self.window['-SONGNAME-'].update(self.SONGNAME)
        return self.SONGNAME

    def getSongLength(self, filename):
        song = MP3(filename)
        print(song.info.length)
        return song.info.length

    def setSongLength(self, filename):
        song = MP3(filename)
        self.SONGLENGTH = song.info.length
        return self.SONGLENGTH

    def playSong(self):
        self.SETPOSITION = 0
        self.window['-SONGSLIDERPOS-'].update(0)
        mixer.music.play()

    def getSongPos(self):
        x = self.SETPOSITION + round(int(mixer.music.get_pos()/1000), 2)
        self.window['-SONGSLIDERPOS-'].update(x)
        self.window['-SONGLENGTHDURATIONTEXT-'].update(f'Song Time: {self.DurationFromSeconds(x)} of {self.DurationFromSeconds(self.SONGLENGTH)}')
        return self.CURSONGTIME

    def setSongPos(self, t):
        """When you skip ahead, save the position in int(x)."""
        self.SETPOSITION = t
        self.CURSONGTIME = round(int(mixer.music.get_pos()/1000), 2) + self.SETPOSITION
        x = self.values['-SONGSLIDERPOS-']
        self.window['-SONGLENGTHDURATIONTEXT-'].update(f'Song Time: {self.DurationFromSeconds(x)} of {self.DurationFromSeconds(self.SONGLENGTH)}')
        mixer.music.play(start=t)

    def pauseSong(self):
        mixer.music.pause()
        self.getSongPos()

    def unPauseSong(self):
        mixer.music.unPause()
        self.getSongPos()

    def stopSong(self):
        mixer.music.stop()

    def set_vol(self, val):
        self.volume = self.values['-VOLUMESLIDERPOS-'] / 100 # mixer volume only accepts values between 0.00 and 1.00
        mixer.music.set_volume(self.volume)
        self.get_vol()
        return self.volume

    def get_vol(self):
        a = self.volume * 100
        return round(a, 2)

    def main(self):
        # Create an self.event loop
        while True:
            self.event, self.values = self.window.read(500)

            if self.event == "OK" or self.event == sg.WIN_CLOSED:
                # END PROGRAM IF USER CLOSES WINDOW
                break

            if self.event == "-MP3SONG-":
                # Update Song Mixer Events
                self.LoadSong()

            if self.event == "-PLAYSONG-" and self.PLAYER is not None:
                # Update Song Mixer
                self.playSong()

            if self.event == "-PLAYLISTBOX-" and self.PLAYER is not None:
                # Update Song Mixer
                print(f"03 PLAYLISTBOX.event: {self.event}  self.values: {self.values}")

            if self.event == "-PAUSESONG-" and self.PLAYER is not None:
                # Update Song Mixer
                print(f"06 self.values: {self.values}")
                self.pauseSong()

            if self.event == "-STOPSONG-" and self.PLAYER is not None:
                # Update Song Mixer
                print(f"08 self.values: {self.values}")
                self.stopSong()

            if self.event == "-VOLUMESLIDERPOS-":
                self.set_vol(self.values['-VOLUMESLIDERPOS-'])
                print(f"09 self.SET VOLUMEN: {self.values}")

            if self.event == "-SONGSLIDERPOS-" and self.PLAYER is not None:
                # Update Slider After Manual Update
                print(f"08 self.values: {self.values}")
                self.setSongPos(self.values['-SONGSLIDERPOS-'])

            else:
                # Update Slider
                self.CURSONGTIME = round(int(mixer.music.get_pos()/1000), 2)
                self.getSongPos()
                # print(f"09 Song Time: {self.CURSONGTIME}")
                print(f"00 self.event: {self.event} self.values: {self.values}")
                # print(f"00 self.event: {self.event} self.values: {self.values} song position: {self.getSongPos()} {self.SONGNAME}")

if __name__ == "__main__":
    app = App()
    app.main()
