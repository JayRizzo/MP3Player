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
        self.SONGLENGTH                 = 0                     # Default Song Length Slider
        self.TOTALSONGL                 = 0                     # Total Time For All Songs
        self.VOLUME                     = 100.00                # Set Initial Volume For PyGame Player
        self.PLAYER                     = ''
        self.FILENAME                   = ''
        self.B4PAUSEDVOLUME             = 0.00
        self.FULLFILEPATH               = ''
        self.MP3SONGARTIST              = ''
        self.MP3SONGALBUM               = ''
        self.MP3SONGPLAYCOUNT           = ''
        self.right_click_menu           = ['Unused', ['&FPS', '—', 'Menu A', 'Menu B', 'Menu C', ['Menu C1', 'Menu C2'], '—', 'Exit']]

        # ========================================================================
        # ==================== Initialize the SimpleGUI Layout ===================
        # ========================================================================
        self.theme = sg.ChangeLookAndFeel('Dark')

        self.menu_def = [
                          ['File', ['Open', 'Save', 'Exit',]]
                        , ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],]
                        , ['Help', 'About...']
                        ]
        self.option = sg.SetOptions (
                                      background_color = 'black'
                                    , element_background_color = 'skyBlue'
                                    , text_element_background_color = 'black'
                                    , font = ('Arial', 10, 'bold')
                                    , text_color = 'lightgrey'
                                    , input_text_color = 'White'
                                    , button_color = ('Blue', 'black')
                                    )


        self.column1 = [
                          [sg.Listbox(self.PLAYLSTBOX,   size = (70, 10), key = "-PLAYLISTBOX-", enable_events = True)]
                        , [sg.Slider(range = (0, 100), size = (60, 15), orientation = 'h', key = '-SONGSLIDERPOS-',    default_value = 0, disabled = True,  disable_number_display = True, enable_events = True, tick_interval = 0, pad = (20, 5))]
                        , [
                            sg.Button(f"{BACKARROW}", key = '-BACKSONG-',    image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = True)
                          , sg.Button(f"{PLAYBUTTN}", key = '-PLAYSONG-',    image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = True)
                          , sg.Button(f"{PAUSEBUTN}", key = '-PAUSESONG-',   image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = True)
                          , sg.Button(f"{STOPBUTTN}", key = '-STOPSONG-',    image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = True)
                          , sg.Button(f"{FORWARROW}", key = '-FORWARDSONG-', image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = True)
                          , sg.Button(f"{REPEATBTN}", key = '-REPEATSONG-',  image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = True)
                          , sg.Button(f"{SHFLLBUTN}", key = '-SHUFFLESONG-', image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = True)
                          , sg.Button(f"{MUTEBUTTN}", key = '-MUTESONG-',    image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = True)
                          , sg.Button(f"{INFOBUTTN}", key = '-INFOSONG-',    image_subsample = 2, border_width = 0, disabled = True, font = ("Helvetica", 60), enable_events = True, button_color = (sg.theme_background_color(), sg.theme_background_color()), visible = False)
                          ]
                       ]
        self.column2 = [
                            [sg.FilesBrowse(size = (17, 1), enable_events = True, file_types = (("MP3 files", "*.mp3"),),                                                  key = '-MP3SONG-'  )]
                          , [sg.Text(f'Time:    {self.CURSONGTIME} of {self.SONGLENGTH}', font = ("Consolas", 20), enable_events = True, justification = 'CENTER', key = '-SONGLENGTHDURATIONTEXT-', )]
                          , [sg.Text(f'Song:    {self.FILENAME}',                         font = ("Consolas", 20), enable_events = True, justification = 'CENTER', key = '-SONGNAME-')]
                          , [sg.Text(f'Artist:  {self.MP3SONGARTIST}',                    font = ("Consolas", 20), enable_events = True, justification = 'LEFT',   key = '-SONGARTIST-')]
                          , [sg.Text(f'Album:   {self.MP3SONGALBUM}',                     font = ("Consolas", 20), enable_events = True, justification = 'LEFT',   key = '-SONGALBUM-')]
                          , [sg.Text(f'Plays:   {self.MP3SONGPLAYCOUNT}',                 font = ("Consolas", 20), enable_events = True, justification = 'LEFT',   key = '-SONGPLAYCOUNT-')]
                       ]
        self.column3 = [
                            [sg.Slider(range = (0, 100), size = (15, 15), orientation = 'v',      font = ("Helvetica", 15), enable_events = True, key = '-VOLUMESLIDERPOS-',  default_value = 100, disabled = False, disable_number_display = True, tick_interval = 0.1)]
                       ]
        self.Layout = [
                        [
                              sg.Column(self.column1, element_justification = 'LEFT', vertical_alignment = 'LEFT',   justification = 'CENTER', pad = (10, 10), key = 'LCOL')
                            , sg.Column(self.column2, element_justification = 'LEFT', vertical_alignment = 'LEFT', justification = 'CENTER', pad = (10, 10), key = 'CCOL')
                            , sg.Column(self.column3, element_justification = 'LEFT', vertical_alignment = 'RIGHT',  justification = 'RIGHT',  pad = (10, 10), key = 'RCOL')
                        ]
                      ]
        self.window = sg.Window(F"{MUSICNOTE} JayRizzo's MP3 Player {MUSICNOTE}"
                                , [[sg.Menu(self.menu_def)], self.Layout]
                                , font = 'Arial 18', resizable = True, grab_anywhere = False)

    def DurationFromSeconds(self, s = 0):
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
        return sg.Button(title, button_color = ('#F0F0F0', '#F0F0F0'), border_width = 0, key = key)

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

    def LoadSongs(self):
        self.PLAYLSTPTH = self.values['-MP3SONG-'].split(';')
        for i in self.values['-MP3SONG-'].split(';'):
            print(self.PLAYLSTPTH)
            print(self.window['-PLAYLISTBOX-'])
            self.FILENAME = ''.join([i])
            self.PLAYLSTBOX += self.PLAYLSTPTH
            self.window['-PLAYLISTBOX-'].update([self.PLAYLSTBOX])

        print(f"PLAYLISTBOX: {self.PLAYLSTBOX}")
        self.setSongLength(self.FILENAME)
        self.getSongMetaData(self.FILENAME)
        # Enable Buttons After Song Loaded Event
        print(f"02 self.event: {self.event}  self.values: {self.values} self.FILENAME: {self.FILENAME} {self.FILENAME}")
        self.window['-PLAYLISTBOX-'].update(set_to_index=1, scroll_to_index=1)
        mixer.music.stop()
        mixer.music.load(self.FILENAME)
        self.window['-BACKSONG-'].update(   disabled = False, visible = True)
        self.window['-PLAYSONG-'].update(   disabled = False, visible = True)
        self.window['-FORWARDSONG-'].update(disabled = False, visible = True)
        self.window['-REPEATSONG-'].update( disabled = False, visible = True)
        self.window['-SHUFFLESONG-'].update(disabled = False, visible = True)
        self.window['-PAUSESONG-'].update(  disabled = False, visible = True)
        self.window['-STOPSONG-'].update(   disabled = False, visible = True)
        self.window['-MUTESONG-'].update(   disabled = False, visible = True)
        self.window['-INFOSONG-'].update(   disabled = False, visible = True)
        self.window['-SONGSLIDERPOS-'].update(disabled = False, visible = True, range = (0,self.SONGLENGTH))


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
        self.window['-PAUSESONG-'].update(visible=True)

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
        mixer.music.play(start = t)

    def pauseSong(self):
        mixer.music.pause()
        self.getSongPos()
        # self.window['-PAUSESONG-'].update(visible=False)

    def unPauseSong(self):
        mixer.music.unPause()
        self.getSongPos()
        # self.window['-PAUSESONG-'].update(visible=True)

    def stopSong(self):
        mixer.music.stop()

    def muteSong(self):
        if not self.MUTED:
            self.window['-MUTESONG-'].update(f'{MUTEBUTTN}')
            self.MUTED = True
            self.B4PAUSEDVOLUME = self.values['-VOLUMESLIDERPOS-']
            self.window['-VOLUMESLIDERPOS-'].update(0)
            self.set_vol(0)
            print(f"B4PAUSEDVOLUME: {self.B4PAUSEDVOLUME}, MUTED: {self.MUTED}, VOLUME: {self.VOLUME}, window['-MUTESONG-']: {self.window['-MUTESONG-']}, window['-VOLUMESLIDERPOS-']: {self.window['-VOLUMESLIDERPOS-']}")
        elif self.MUTED:
            self.window['-MUTESONG-'].update(f'{SPKRBUTTN}')
            self.MUTED = False
            self.B4PAUSEDVOLUME = f"{self.values['-VOLUMESLIDERPOS-']}"
            self.window['-VOLUMESLIDERPOS-'].update(self.B4PAUSEDVOLUME)
            self.set_vol(self.B4PAUSEDVOLUME)
            print(f"B4PAUSEDVOLUME: {self.B4PAUSEDVOLUME}, MUTED: {self.MUTED}, VOLUME: {self.VOLUME}, window['-MUTESONG-']: {self.window['-MUTESONG-']}, window['-VOLUMESLIDERPOS-']: {self.window['-VOLUMESLIDERPOS-']}")
        else:
            pass

    def stopSong(self):
        mixer.music.stop()

    def set_vol(self, val):
        self.VOLUME = self.values['-VOLUMESLIDERPOS-'] / 100 # mixer volume only accepts values between 0.00 and 1.00
        mixer.music.set_volume(self.VOLUME)
        self.get_vol()
        return self.VOLUME

    def get_vol(self):
        a = self.VOLUME * 100
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
                self.LoadSongs()

            if self.event == "-MUTESONG-":
                # Update Song Mixer Events
                self.muteSong()

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
                # print(f"00 self.event: {self.event} self.values: {self.values} song position: {self.getSongPos()} {self.FILENAME}")
                self.window.Element('-PLAYLISTBOX-').Widget.curselection()

if __name__ == "__main__":
    app = App()
    app.main()
