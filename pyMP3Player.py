#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Tue Sep  6 19:43:15 2022 CDT
# Last ModDate: Thu Sep 22 00:32:05 2022 CDT
# =============================================================================
# Notes: [acoustid_fingerprint, acoustid_id, album, albumartist, albumartistsort, albumsort, arranger, artist, artistsort, asin, author, barcode, bpm, catalognumber, compilation, composer, composersort, conductor, copyright, date, discnumber, discsubtitle, encodedby, genre, isrc, language, length, lyricist, media, mood, musicbrainz_albumartistid, musicbrainz_albumid, musicbrainz_albumstatus, musicbrainz_albumtype, musicbrainz_artistid, musicbrainz_discid, musicbrainz_releasegroupid, musicbrainz_releasetrackid, musicbrainz_trackid, musicbrainz_trmid, musicbrainz_workid, musicip_fingerprint, musicip_puid, organization, originaldate, performer, performer:*, releasecountry, replaygain_*_gain, replaygain_*_peak, title, titlesort, tracknumber, version, website]
# =============================================================================
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'  # noqa This is used to hide the default pygame import print statement.
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen import id3
from time import sleep
from os import path
from os.path import basename
from os.path import exists as filepathexist
from os.path import expanduser
from os.path import join
from os.path import splitext
from os.path import isfile
from pygame import mixer
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from ttkthemes import themed_tk as tk
import customtkinter
import tkinter
from tkinter import Tk, BOTH, Listbox, StringVar, END
from tkinter.ttk import Frame, Label
from random import shuffle
import threading
import time
from os import getcwd

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

MUSICNOTE = '\U0001F3B5'
BACKARROW = '\U000023EA'
FORWARROW = '\U000023E9'
PLAYBUTTN = '\U000025B6\U0000FE0F'
STOPBUTTN = '\U000023F9'
REPEATBTN = '\U0001F501'
PAUSEBUTN = '\U000023F8'
SHFLLBUTN = '\U0001F500'
MUTEBUTTN = '\U0001F507'
SPKRBUTTN = '\U0001F50A'
INFOBUTTN = '\U00002139'


class App(customtkinter.CTk):
    """JayRizzo Music Player."""
    def __init__(self):
        """JayRizzo Music Player Initial Launch Setup."""
        # ========================================================================
        # ======================== Initialize the Tkinter ========================
        # ========================================================================
        super().__init__()
        self.read_window(self)
        self.x = self.winfo_width()
        self.y = self.winfo_height()
        self.screen_x = self.winfo_screenwidth()
        self.screen_y = self.winfo_screenheight()
        self.screen_x_half = int(self.winfo_screenwidth()/2 - self.x/2)
        self.screen_y_half = int(self.winfo_screenheight()/2 - self.y/2)
        self.title(f"{MUSICNOTE} JayRizzo MP3 Player {MUSICNOTE}")
        self.iconbitmap(r'mp_images/JayRizzo.ico')
        self.CWDIR = getcwd()

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
        self.SONGLENGTH                 = 0                     # Current Song Length Slider
        self.TOTALSONGL                 = 0                     # Total Time For All Songs
        self.volume                     = 100.0                 # Set Initial Volume For PyGame Player
        self.FILENAME                   = ''
        self.FULLFILEPATH               = ''
        self.SONGINFO                   = []
        # ========================================================================
        # =================== Initialize the Current Song Meta ===================
        # ========================================================================
        self.CURSONGARTIST              = None
        # ========================================================================
        # ======================== Create Menu Bar & Items =======================
        # ========================================================================
        self.menubar        = Menu(master=self)
        self.config(menu=self.menubar)
        self.fileMenu       = Menu(self.menubar)

        # ========================================================================
        # ========================= Create SubMenu Items =========================
        # ========================================================================
        # Create the SubMenu
        self.fileMenu       = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=f"File", menu=self.fileMenu)

        self.editMenu       = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=f"Edit", menu=self.editMenu)

        self.songMenu       = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=f"{MUSICNOTE} Song", menu=self.songMenu)

        self.helpMenu       = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=f"{INFOBUTTN} Help", menu=self.helpMenu)

        # ========================================================================
        # =============== Create Commands for Menu & Sub-Menu Items ==============
        # ========================================================================
        self.fileMenu.add_command(label="Add Songs To Playlist File", command=self.AddManySongToPlaylist)
        self.fileMenu.add_command(label="Exit", command=self.destroy)
        self.editMenu.add_command(label="Edit Test", command=self.about_us)
        self.songMenu.add_command(label=f"{PLAYBUTTN} Play", command=self.play_music)
        self.songMenu.add_command(label=f"{PAUSEBUTN} Pause", command=self.pause_music)
        self.songMenu.add_command(label=f"{BACKARROW} Rewind", command=self.rewind_music)
        self.songMenu.add_command(label=f"{FORWARROW} Rewind", command=self.skip_music)
        self.songMenu.add_command(label=f"{STOPBUTTN} Stop", command=self.stop_music)
        self.songMenu.add_command(label=f"{MUTEBUTTN} Mute", command=self.mute_music)
        self.songMenu.add_command(label=f"{INFOBUTTN} Song Details", command=self.show_details)
        self.songMenu.add_command(label=f"{REPEATBTN} Repeat", command=self.about_us)
        self.songMenu.add_command(label=f"{SHFLLBUTN} Shuffle", command=self.about_us)
        self.helpMenu.add_command(label=f"{INFOBUTTN} About Us", command=self.about_us)
        self.helpMenu.add_command(label=f"{INFOBUTTN} Window Info", command=self.window_info)

        # ========================================================================
        # ===================== Create One Main Canvas ===========================
        # ========================================================================
        self.MainCanvas=customtkinter.CTkCanvas(self, bg="black", height=self.y, width=self.x)
        self.MainCanvas.grid(rowspan=2, columnspan=4, sticky="nswe")

        # ========================================================================
        # ===================== Create All Four Column Frames ====================
        # ========================================================================
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.FrameLeft = customtkinter.CTkFrame(master=self.MainCanvas,  corner_radius=15)
        self.FrameLeft.grid(row=0, column=0, rowspan=1, columnspan=1, sticky="nswe")
        self.FrameCenterLeft = customtkinter.CTkFrame(master=self.MainCanvas,  corner_radius=15)
        self.FrameCenterLeft.grid(row=0, column=1, rowspan=1, columnspan=1, sticky="nswe")
        self.FrameCenterRight = customtkinter.CTkFrame(master=self.MainCanvas, corner_radius=15)
        self.FrameCenterRight.grid(row=0, column=2, rowspan=1, columnspan=1, sticky="nswe")
        self.FrameRight = customtkinter.CTkFrame(master=self.MainCanvas, corner_radius=15)
        self.FrameRight.grid(row=0, column=3, rowspan=1, columnspan=1, sticky="nswe")

        # ========================================================================
        # ========================= Initialize the Status Bar ====================
        # ========================================================================
        self.FrameBottomBar = customtkinter.CTkLabel(master=self.MainCanvas, relief=SUNKEN, anchor=customtkinter.E)
        self.FrameBottomBar.grid(row=1, column=0, columnspan=4, sticky="nswe")
          # pack(side=customtkinter.BOTTOM, fill=customtkinter.X)
        # ========================================================================
        # ====================== Populate First Frame (LEFT) =====================
        # ========================================================================
        self.Label1  = customtkinter.CTkLabel(master=self.FrameLeft, text=f"{MUSICNOTE} RizzoBox {MUSICNOTE}", text_font=("Roboto Medium", -16))  # font name and size in px.grid(row=1, column=0, padx=10, pady=10)
        self.button_1 = customtkinter.CTkButton(master=self.FrameLeft, text="Add Song To Playlist", command=self.AddManySongToPlaylist).grid(row=2, column=0, padx=10, pady=10)
        self.button_2 = customtkinter.CTkButton(master=self.FrameLeft, text="Load Playlist", command=self.button_event).grid(row=3, column=0, padx=10, pady=10)
        self.button_3 = customtkinter.CTkButton(master=self.FrameLeft, text="Save Playlist", command=self.button_event).grid(row=4, column=0, padx=10, pady=10)
        self.button_4 = customtkinter.CTkButton(master=self.FrameLeft, text="Create Playlist", command=self.button_event).grid(row=5, column=0, padx=10, pady=10)
        self.Labelmode = customtkinter.CTkLabel(master=self.FrameLeft, text="Appearance Mode:").grid(row=9, column=0, padx=10, pady=10, sticky="w")
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.FrameLeft, values=["75%", "80%", "85%", "90%", "95%", "100%", "105%", "110%", "115%", "120%", "125%"], command=self.change_scaling)
        self.scaling_optionemenu.grid(row=10, column=0, padx=10, pady=10, sticky="w")
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.FrameLeft, values=["Light", "Dark", "System"], command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=11, column=0, padx=10, pady=10, sticky="w")
        # self.optionmenu_2 = customtkinter.CTkOptionMenu(master=self.FrameLeft, values=["blue", "dark-blue", "green"], command=self.change_theme)
        # self.optionmenu_2.grid(row=12, column=0, padx=10, pady=10, sticky="w")

        # ========================================================================
        # ==================== Populate Second Frame (CENTER) ====================
        # ========================================================================
        self.FrameCenterLeft.rowconfigure(1)
        self.FrameCenterLeft.columnconfigure(0)

        self.Labelinfo_1 = customtkinter.CTkLabel(master=self.FrameCenterLeft, text=f"Time: {self.SONGLENGTH}", height=self.screen_y_half, corner_radius=6, fg_color=("white", "gray38"), justify=tkinter.LEFT)
        self.Labelinfo_1.grid(row=0, column=0, rowspan=1, columnspan=6, sticky="new", padx=10, pady=(10, 0))

        self.progressbar = customtkinter.CTkProgressBar(master=self.FrameCenterLeft, orient="horizontal", width=100)
        self.progressbar.grid(row=1, column=0, rowspan=1, columnspan=6, sticky="new", padx=10, pady=10)
        self.progressbar_label = customtkinter.CTkLabel(master=self.FrameCenterLeft, text=50, width=30, height=25)
        self.progressbar_label.grid(row=1, column=1, rowspan=1, columnspan=1, padx=( 0,  0 ), pady=( 0, 0 ), sticky="e")

        # ========================================================================
        # ======================== Center-Bottom Buttons =========================
        # ========================================================================
        self.button_0 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{PAUSEBUTN}", corner_radius=60, command=self.pause_music)
        self.button_0.grid( sticky='n', row=2, column=0, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_1 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{BACKARROW}", corner_radius=60, command=self.button_event).grid( sticky='n', row=2, column=1, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_2 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{PLAYBUTTN}", corner_radius=60, command=self.play_music).grid(   sticky='n', row=2, column=2, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_3 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{FORWARROW}", corner_radius=60, command=self.skip_music).grid( sticky='n', row=2, column=3, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_4 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{STOPBUTTN}", corner_radius=60, command=self.stop_music).grid( sticky='n', row=2, column=4, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_5 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{SHFLLBUTN}", corner_radius=60, command=self.button_event).grid( sticky='n', row=3, column=1, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_6 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{MUTEBUTTN}", corner_radius=60, command=self.mute_music,bg='systemTransparent').grid( sticky='n', row=3, column=2, rowspan=1, columnspan=1, padx=5, pady=5)
        # self.switch_3 = customtkinter.CTkSwitch(master=self.FrameCenterLeft, text_font=("Consolas", 25), text=f"{REPEATBTN} Repeat", corner_radius=60, command=self.repeat_music).grid(sticky='ns', row=3, column=3, pady=15, padx=20)
        self.button_7 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{REPEATBTN}", corner_radius=60, command=self.repeat_music).grid( row=3, column=3, rowspan=1, columnspan=1, padx=5, pady=5)

        # ========================================================================
        # ====================== Center-Right Volume Scroll ======================
        # ========================================================================
        self.volume_slider = customtkinter.CTkSlider(master=self.FrameCenterLeft, orient="vertical", command=self.set_vol, from_=0, to=1, number_of_steps=1000)
        self.volume_slider.grid(          row=1, column=5, rowspan=2, columnspan=1, padx=(10, 10), pady=(40, 10), sticky="n")
        self.volume_label = customtkinter.CTkLabel(master=self.FrameCenterLeft, text=50, width=30, height=25)
        self.volume_label.grid(row=3, column=5, rowspan=1, columnspan=1, padx=( 0,  0), pady=( 0, 0), sticky="n")

        # ========================================================================
        # ===================== Populate Third Frame (RIGHT) =====================
        # ========================================================================
        self.FrameCenterRight.rowconfigure((0, 1, 2, 3), weight=1)
        self.FrameCenterRight.columnconfigure((0, 2), weight=2)
        self.FrameCenterRight = customtkinter.CTkFrame(master=self.FrameCenterRight)
        self.FrameCenterRight.grid(row=0, column=1, rowspan=1, columnspan=2, padx=10, pady=10, sticky="wnse")
        self.LabelArtist_header = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f" {MUSICNOTE} Current Song Info: {MUSICNOTE} ", width=300, height=25, corner_radius=8).grid(row=0, rowspan=1, column=1, sticky="w")
        self.LabelSongName = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Name: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=1, rowspan=1, column=1, sticky="w")
        self.LabelSongArtist = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Artist: {self.CURSONGARTIST}", width=120, height=20, corner_radius=8, anchor="w").grid(row=2, rowspan=1, column=1, sticky="w")
        self.LabelSongComposer = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Composer: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=3, rowspan=1, column=1, sticky="w")
        self.LabelArtist04 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Album: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=4, rowspan=1, column=1, sticky="w")
        self.LabelArtist05 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Grouping: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=5, rowspan=1, column=1, sticky="w")
        self.LabelArtist06 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Work: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=6, rowspan=1, column=1, sticky="w")
        self.LabelArtist07 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Movement Number: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=7, rowspan=1, column=1, sticky="w")
        self.LabelArtist08 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Movement Count: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=8, rowspan=1, column=1, sticky="w")
        self.LabelArtist09 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Movement Name: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=9, rowspan=1, column=1, sticky="w")
        self.LabelArtist10 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Genre: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=10, rowspan=1, column=1, sticky="w")
        self.LabelArtist11 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Size: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=11, rowspan=1, column=1, sticky="w")
        self.LabelArtist12 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Time: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=12, rowspan=1, column=1, sticky="w")
        self.LabelArtist13 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Disc Number: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=13, rowspan=1, column=1, sticky="w")
        self.LabelArtist14 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Disc Count: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=14, rowspan=1, column=1, sticky="w")
        self.LabelArtist15 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Track Number: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=15, rowspan=1, column=1, sticky="w")
        self.LabelArtist16 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Track Count: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=16, rowspan=1, column=1, sticky="w")
        self.LabelArtist17 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Year: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=17, rowspan=1, column=1, sticky="w")
        self.LabelArtist18 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Date Modified: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=18, rowspan=1, column=1, sticky="w")
        self.LabelArtist19 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Date Added: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=19, rowspan=1, column=1, sticky="w")
        self.LabelArtist20 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Bit Rate: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=20, rowspan=1, column=1, sticky="w")
        self.LabelArtist21 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Sample Rate: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=21, rowspan=1, column=1, sticky="w")
        self.LabelArtist22 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Volume Adjustment: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=22, rowspan=1, column=1, sticky="w")
        self.LabelArtist23 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Kind: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=23, rowspan=1, column=1, sticky="w")
        self.LabelArtist24 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Equalizer: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=24, rowspan=1, column=1, sticky="w")
        self.LabelArtist25 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Comments: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=25, rowspan=1, column=1, sticky="w")
        self.LabelArtist26 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Plays: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=26, rowspan=1, column=1, sticky="w")
        self.LabelArtist27 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Last Played: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=27, rowspan=1, column=1, sticky="w")
        self.LabelArtist28 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Skips: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=28, rowspan=1, column=1, sticky="w")
        self.LabelArtist29 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Last Skipped: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=29, rowspan=1, column=1, sticky="w")
        self.LabelArtist30 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"My Rating: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=30, rowspan=1, column=1, sticky="w")
        self.LabelArtist31 = customtkinter.CTkLabel(master=self.FrameCenterRight, text=f"Location: ", width=120, height=20, corner_radius=8, anchor="w").grid(row=31, rowspan=1, column=1, sticky="w")

        # ========================================================================
        # ===================== Populate Fourth Frame (RIGHT) ====================
        # ========================================================================
        self.FrameRight.columnconfigure(1, weight=0)
        self.PLAYLSTBOX = Listbox(master=self.FrameRight, yscrollcommand=True)
        self.PLAYLSTBOX.grid(row=0, column=3, rowspan=1, columnspan=1, padx=10, pady=10, sticky="nsew")

        # ========================================================================
        # ===================== Set Default Values ===============================
        # ========================================================================
        self.scaling_optionemenu.set("75%")
        self.optionmenu_1.set("Dark")
        # self.optionmenu_2.set("dark-blue")
        self.progressbar.set(0)

    # ========================================================================
    # ===================== BEGIN Define Functions BEGIN =====================
    # ========================================================================

    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)

    def about_us(self):
        messagebox.showinfo('About Player', 'This is a music player build using Python Tkinter by @JayRizzo')

    def on_closing(self, event=0):
        """JayRizzo Music Player Exit Behavior. https://stackoverflow.com/a/65657779/1896134 ."""
        close = messagebox.askokcancel("Close", "Are You Sure You Want To Close The Program?")
        if close:
            print(f"Closed: {close}")
            self.stop_music()
            self.saveConfig()
            self.destroy()
        else:
            print(f"Closed: {close}")
        return

    def update_clock(self):
        """JayRizzo Music Player Update Song Clock."""
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)
        return

    def setCurrentSongPath(self, songpath):
        """JayRizzo Music Player Get Current Selected Song Length."""
        self.FULLFILEPATH = songpath
        self.FILENAME = basename(self.FULLFILEPATH)
        self.SONGINFO = MP3(self.FULLFILEPATH)
        print(f"setCurrentSongPath(): songpath: {songpath}")
        print(f"setCurrentSongPath(): self.FULLFILEPATH: {self.FULLFILEPATH}")
        print(f"setCurrentSongPath(): self.FILENAME: {self.FILENAME}")
        print(f"setCurrentSongPath(): self.PLAYLSTPTH: {self.PLAYLSTPTH}")
        return

    # def addOneSongToPlaylist(self):
    #     """JayRizzo Music Player Add Song To Playlist."""
    #     songpath = askopenfilename(initialdir=f"{self.CWDIR}/Music/",
    #                                title="Choose A Song:",
    #                                filetypes=[("MP3", "*.mp3"),
    #                                           ("AAC Audio Files", "*.aac"),
    #                                           ("AIFF Audio Files", "*.aiff"),
    #                                           ("MPEG Audio Files", "*.mpeg"),
    #                                           ("Protected Audio Files", "*.m4a"),
    #                                           ("all", "*.*")])
    #     self.setCurrentSongPath(songpath)
    #     self.PLAYLSTPTH.insert(len(self.PLAYLSTPTH), self.FULLFILEPATH)
    #     self.PLAYLSTBOX.insert(self.PLAYLSTBOX.size(), self.FILENAME)
    #     print(f"self.FULLFILEPATH: {self.FULLFILEPATH}")
    #     mixer.music.queue(self.FULLFILEPATH)
    #     self.PLAYLSTBOX.select_set(0)  #  This only sets focus on the first item.
    #     return

    def AddManySongToPlaylist(self):
        songs = filedialog.askopenfilenames(initialdir=f"{self.CWDIR}/Music/", title="Choose A Selection Of Songs", filetypes=(("mp3 files", "*.mp3"), ))
        for song in songs:
            index = 1
            self.FULLFILEPATH = song
            song = song.replace(f"{self.CWDIR}/Music/","")
            song = song.replace(f".mp3","")
            song = song.replace(f"_"," ")
            self.PLAYLSTPTH.insert(index, self.FULLFILEPATH)
            mixer.music.queue(self.FULLFILEPATH)
            # self.PLAYLSTBOX.insert(index, song)
            self.PLAYLSTBOX.insert(self.PLAYLSTBOX.size(), song)
            index += 1
            print(song)
            print(self.FULLFILEPATH)
            print(self.PLAYLSTPTH)
            print(self.PLAYLSTBOX)
        # self.setCurrentSongPath(songs[0])
        self.PLAYLSTBOX.select_set(0)  #  This only sets focus on the first item.

    def getSongLength(self, songpath):
        """JayRizzo Music Player Get Current Selected Song Length."""
        self.SONGINFO = MP3(songpath)
        self.CURSONGTIME = self.SONGINFO.info.length
        return self.CURSONGTIME

    def showSongInfo(self, songpath):
        """JayRizzo Music Player Get Current Selected Song Info."""
        self.SONGINFO                                       = EasyID3(songpath)
        self.LabelSongName.set_text(f"SongName:             {self.SONGINFO.title}")
        self.LabelSongArtist.set_text(f"Artist:             {self.SONGINFO.albumartist}")
        self.LabelSongArtist.set_text(f"Album Artist:       {self.SONGINFO.albumartist}")
        self.LabelSongComposer.set_text(f"Composer:         {self.SONGINFO.composer}")
        self.LabelSongComposer.set_text(f"Album:            {self.SONGINFO.album}")
        self.LabelSongComposer.set_text(f"Album No:         {self.SONGINFO.discnumber}")
        self.LabelSongComposer.set_text(f"Organization:     {self.SONGINFO.organization}")
        print(f"{self.SONGINFO}")
        print(f"{self.CURSONGARTIST}")
        print(f"{self.SONGINFO.keys()}")
        print(f"{self.SONGINFO.values()}")
        print(f"Song Info: {dir(self.SONGINFO)}")

    def start_count(self, t):
        """The mixer.music.get_busy():
        Returns FALSE when we press the stop button (music stop playing),
        the 'Continue' statement allows us to check if music is paused or not."""
        self.CURSONGTIME = 0
        self.CURRSONG = mixer.music.get_pos() / 1000
        self.getSongLength(self.PLAYLSTBOX.curselection())
        while self.CURRSONG <= self.CURSONGTIME and mixer.music.get_busy():
            if self.PAUSED:
                continue
            else:
                converted_time = time.strftime('%H:%M:%S', time.gmtime(self.CURRSONG))
                print(f"Current Time: {converted_time}")
                self.progressbar.set(mixer.music.get_pos() / 1000)
                # self.progressbar.config(text=f'Time: {self.CURRSONG}/{converted_time}')
                self.timeformat = duration_from_seconds(secs)
                time.sleep(1)
                self.CURRSONG += 1
                self.progressbar.after(1000)
        return

    def show_details(self, play_song):
        self.file_data = splitext(play_song)
        if self.file_data[1] == '.mp3':
            self.audio = MP3(play_song)
            self.SONGLENGTH = self.audio.info.length
        else:
            self.a = mixer.Sound(self.play_song)
            self.SONGLENGTH = a.get_length()
            self.timeformat = duration_from_seconds(secs)
        self.t1 = threading.Thread(target=self.start_count, args=(self.SONGLENGTH,))
        self.t1.start()
        return

    def onSelect(self, val):
        self.sender = self.val.widget
        self.idx = sender.curselection()
        self.value = sender.get(self.idx)
        self.var.set(self.value)


    # ========================================================================
    # ================== BEGIN Music Buttons BEGIN ===========================
    # ========================================================================
    def play_music(self):
        try:
            if self.PAUSED:
                self.pause_music()
                self.PAUSED = False
                self.STOPPED = False
            elif self.PLAYLSTBOX.curselection() is None:
                warn("No Song Loaded or Selected.")
            else:
                self.stop_music()
                self.CURSELECTDSONG = self.PLAYLSTBOX.curselection()
                self.CURSELECTDSONG = int(self.CURSELECTDSONG[0])
                play_it = self.PLAYLSTPTH[self.CURSELECTDSONG]
                mixer.music.load(play_it)
                mixer.music.play()
                self.STOPPED = False
                # print(f"self.FULLFILEPATH: {self.FULLFILEPATH}")
                # print(f"self.PLAYLSTBOX.curselection(): {self.PLAYLSTBOX.curselection()}")
                # print(f"self.CURSELECTDSONG: {self.CURSELECTDSONG}")
                # print(f"play_it: {play_it}")
                self.show_details(play_it)
                self.showSongInfo(play_it)
        except IndexError as e:
            print("No Song Selected to play.")

    def stop_music(self):
        mixer.music.stop()
        self.stopped = True

    def pause_music(self):
        if self.PAUSED is False:
            mixer.music.pause()
            self.PAUSED = True
            self.FrameBottomBar.set_text("Music Paused")
        else:
            mixer.music.unpause()
            self.PAUSED = False
            self.FrameBottomBar.set_text("Music UnPaused")

    def rewind_music(self):
        self.play_music()
        self.FrameBottomBar.set_text("Music Started Over")

    def skip_music(self):
        "Play Next Song."
        self.FrameBottomBar.set_text("Skipped To Next Song Ahead")

    def repeat_music(self):
        mixer.music.play(-1)
        self.FrameBottomBar.set_text("Song On Infinite Repeat")

    def set_vol(self, val):
        self.volume = float(val)
        mixer.music.set_volume(self.volume)
        self.volume_label.set_text(str(round(round(self.volume, 3) * 100, 1)))
        self.get_vol()
        return self.volume

    def get_vol(self):
        a = self.volume * 100
        print(f"volume: {round(a, 2)}")
        return round(a, 2)

    def mute_music(self):
        previousVolume = self.volume
        if self.MUTED:  # Unmute the music
            mixer.music.set_volume(previousVolume)
            self.MUTED = False
            self.button_4 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("", 45), text=f"{SPKRBUTTN}", corner_radius=60, command=self.mute_music).grid(   row=3, column=2, rowspan=1, columnspan=1, padx=5, pady=0)
        else:  # mute the music
            mixer.music.set_volume(0)
            self.MUTED = True
            self.button_4 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("", 45), text=f"{MUTEBUTTN}", corner_radius=60, command=self.mute_music).grid(   row=3, column=2, rowspan=1, columnspan=1, padx=5, pady=0)

    def shuffle_music(self):
        self.PLAYLSTBOX = shuffle(self.PLAYLSTBOX)
        self.button_5 = customtkinter.CTkButton(master=self.FrameCenterLeft, text_font=("Consolas", 45), text=f"{SHFLLBUTN}", corner_radius=60, command=self.button_event).grid( row=3, column=1, rowspan=1, columnspan=1, padx=5, pady=5)

    # ========================================================================
    # ========================= END Music Buttons END ========================
    # ========================================================================

    # ========================================================================
    # ===================== BEGIN Playlist Behavior BEGIN ====================
    # ========================================================================

    def del_song(self):
        self.CURSELECTDSONG = self.PLAYLSTBOX.curselection()
        self.CURSELECTDSONG = int(self.CURSELECTDSONG[0])
        self.PLAYLSTBOX.delete(self.CURSELECTDSONG)
        self.PLAYLSTPTH.pop(self.CURSELECTDSONG)

    # ========================================================================
    # ================== Settings & Configuration ============================
    # ========================================================================
    def read_window(self, event):
        if isfile("config.ini"):
            #Here I read the X and Y positon of the window from when I last closed it.
            with open("config.ini", "r") as conf:
                self.geometry(conf.read().strip())
        else:
            self.x = self.winfo_width()
            self.y = self.winfo_height()
            self.screen_x = self.winfo_screenwidth()
            self.screen_y = self.winfo_screenheight()
            self.screen_x_half = int(self.winfo_screenwidth()/2 - self.x/2)
            self.screen_y_half = int(self.winfo_screenheight()/2 - self.y/2)
            self.geometry(f"{self.screen_x_half}x{self.screen_y_half}-0-557")

    def button_event(self):
        """JayRizzo Music Player Placeholder Setup."""
        print("Button pressed")
        return

    def change_appearance_mode(self, new_appearance_mode):
        """JayRizzo Music Player Change Appearance Mode."""
        customtkinter.set_appearance_mode(new_appearance_mode)
        return

    def change_theme(self, new_theme):
        """JayRizzo Music Player Change Theme."""
        customtkinter.set_default_color_theme(new_theme)
        return

    def change_scaling(self, new_scaling: str):
        """JayRizzo Music Player Change Zoom Scaling."""
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_spacing_scaling(new_scaling_float)
        customtkinter.set_widget_scaling(new_scaling_float)
        return

    def saveConfig(self):
        global config
        with open("config.ini", "w") as conf:
            conf.write(f"{self.geometry()}\n")

    def window_info(self):
        """JayRizzo Music Player Window Info."""
        screen_dimensions = f"{self.winfo_height()}x{self.winfo_width()}"
        print(f"Screen Dimensions: {screen_dimensions}")
        return

    # ========================================================================
    # ================= Time Duration & Measurement ==========================
    # ========================================================================
    def duration_from_seconds(self, s):
        """Module to get the convert Seconds to a time like format."""
        s = s
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        TIMELAPSED = f"{int(d):01d}:{int(h),:02d}:{int(m),:02d}:{int(s),:02d}"
        return TIMELAPSED

    def duration_from_milliseconds(self, ms):
        """Module to convert milliseconds to Seconds in a time like format."""
        ms = ms
        s, ms = divmod(ms, 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        TIMELAPSED = f"{int(d):01d}:{int(h),:02d}:{int(m),:02d}:{int(s),:02d}:{int(ms):02d}"
        return TIMELAPSED
    # ========================================================================
    # ========================== Database Functions ==========================
    # ========================================================================
    def clicked_add_songs(self, playlist):
        list_size = self.PLAYLSTBOX.size()
        for i in range(list_size):
            song = self.PLAYLSTBOX.get(i)
            path = song_dir_list[i]
            # Add Song to playlist on database

    # ========================================================================
    # ======================= END Define Functions END =======================
    # ========================================================================

if __name__ == "__main__":
    app = App()
    app.attributes('-fullscreen', False)
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.wm_attributes("-transparent", True)
    app.wm_attributes("-topmost", False)
    app.minsize(1120, 470)
    # app.state("zoomed")
    app.mainloop()


