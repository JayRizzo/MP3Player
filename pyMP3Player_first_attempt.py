#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : jkirchoff
# Created Date: Tue Sep  6 19:43:15 2022 CDT
# Last ModDate: Wed Sep  7 23:13:07 2022 CDT
# =============================================================================
# Notes:
# =============================================================================
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from mutagen.mp3 import MP3
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
    def __init__(self):
        # ============ Initialize the Tkinter ============
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

        # ============ Initialize the Mixer ============
        self.mixer_init = mixer.init()
        self.paused = FALSE
        self.playlist = []
        self.muted = FALSE
        self.filename = ''
        # ============ Create Menu Bar & Items ============
        self.menubar = Menu(master=self)
        self.config(menu=self.menubar)
        self.fileMenu = Menu(self.menubar)

        # ============ Create SubMenu Items ============
        # Create the SubMenu
        self.fileMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.editMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.editMenu)

        self.songMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label=f"Song {MUSICNOTE}", menu=self.songMenu)

        self.helpMenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpMenu)

        # ============ Create Commands for Menu & Sub-Menu Items ============
        self.fileMenu.add_command(label="Open File", command=self.browse_file)
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
        self.helpMenu.add_command(label="About Us", command=self.about_us)

        # ============ Create All Four Column Frames ============
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.frame_left = customtkinter.CTkFrame(master=self, width=self.x/.75, corner_radius=15)
        self.frame_left.grid(row=0, column=0, columnspan=1, sticky="nswe")
        self.frame_center = customtkinter.CTkFrame(master=self, width=self.x/.5, corner_radius=15)
        self.frame_center.grid(row=0, column=1, columnspan=1, sticky="nswe")
        self.frame_right = customtkinter.CTkFrame(master=self, width=self.x/.75, corner_radius=15)
        self.frame_right.grid(row=0, column=2, columnspan=1, sticky="nswe")
        self.frame_fileList = customtkinter.CTkFrame(master=self, width=self.x/.5, corner_radius=15)
        self.frame_fileList.grid(row=0, column=3, columnspan=1, sticky="nswe")

        # # ============ Initialize the Canvas ============
        # self.canvas=Canvas(self,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
        # self.hbar=Scrollbar(self.canvas,orient=HORIZONTAL)
        # self.hbar.pack(side=BOTTOM,fill=X)
        # self.hbar.config(command=self.canvas.xview)
        # self.vbar=Scrollbar(self.canvas,orient=VERTICAL)
        # self.vbar.pack(side=RIGHT,fill=Y)
        # self.vbar.config(command=self.canvas.yview)
        # self.canvas.config(width=300,height=300)
        # self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        # self.canvas.pack(side=LEFT,expand=True,fill=BOTH)

        # ============ Populate First Frame (LEFT) ============
        self.label_1  = customtkinter.CTkLabel(master=self.frame_left, text=f"{MUSICNOTE} RizzoBox {MUSICNOTE}", font=("Roboto Medium", -16))  # font name and size in px.grid(row=1, column=0, padx=10, pady=10)
        self.button_1 = customtkinter.CTkButton(master=self.frame_left, text="Add Music To Playlist", command=self.browse_file).grid(row=2, column=0, padx=10, pady=10)
        self.button_2 = customtkinter.CTkButton(master=self.frame_left, text="Load Playlist", command=self.button_event).grid(row=3, column=0, padx=10, pady=10)
        self.button_3 = customtkinter.CTkButton(master=self.frame_left, text="Save Playlist", command=self.button_event).grid(row=4, column=0, padx=10, pady=10)
        self.button_4 = customtkinter.CTkButton(master=self.frame_left, text="Create Playlist", command=self.button_event).grid(row=5, column=0, padx=10, pady=10)
        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:").grid(row=9, column=0, padx=10, pady=10, sticky="w")
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.frame_left, values=["75%", "80%", "85%", "90%", "95%", "100%", "105%", "110%", "115%", "120%", "125%"], command=self.change_scaling)
        self.scaling_optionemenu.grid(row=10, column=0, padx=10, pady=10, sticky="w")
        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left, values=["Light", "Dark", "System"], command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=11, column=0, padx=10, pady=10, sticky="w")
        self.optionmenu_2 = customtkinter.CTkOptionMenu(master=self.frame_left, values=["blue", "dark-blue", "green"], command=self.change_theme)
        self.optionmenu_2.grid(row=12, column=0, padx=10, pady=10, sticky="w")

        # ============ Populate Second Frame (CENTER) ============
        self.frame_center.rowconfigure(1)
        self.frame_center.columnconfigure(0)
        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_center, text="Lyrics:", height=self.screen_y_half, corner_radius=6, fg_color=("white", "gray38"), justify=tkinter.LEFT)
        self.label_info_1.grid(row=0, column=0, rowspan=1, columnspan=10, sticky="nwe", padx=10, pady=(10, 0))
        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_center)
        self.progressbar.grid(row=1, column=0, rowspan=1, columnspan=10, sticky="new", padx=10, pady=10)

        # ============ Bottom Center Buttons ============
        self.button_0 = customtkinter.CTkButton(master=self.frame_center, font=("Consolas", 45), text=f"{PAUSEBUTN}", command=self.pause_music).grid(  row=2, column=0, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_1 = customtkinter.CTkButton(master=self.frame_center, font=("Consolas", 45), text=f"{BACKARROW}", command=self.button_event).grid( row=2, column=1, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_2 = customtkinter.CTkButton(master=self.frame_center, font=("Consolas", 45), text=f"{PLAYBUTTN}", command=self.play_music).grid(   row=2, column=2, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_3 = customtkinter.CTkButton(master=self.frame_center, font=("Consolas", 45), text=f"{FORWARROW}", command=self.skip_music).grid( row=2, column=3, rowspan=1, columnspan=1, padx=5, pady=5)
        self.button_4 = customtkinter.CTkButton(master=self.frame_center, font=("Consolas", 45), text=f"{STOPBUTTN}", command=self.stop_music).grid( row=2, column=4, rowspan=1, columnspan=1, padx=5, pady=5)
        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_center, font=("Consolas", 25), text=f"{SHFLLBUTN} Shuffle", command=self.button_event).grid(row=3, column=1, pady=1, padx=20, sticky="nw")
        self.button_6 = customtkinter.CTkButton(master=self.frame_center, font=("Consolas", 45), text=f"{MUTEBUTTN}", command=self.mute_music).grid(   row=3, column=2, rowspan=1, columnspan=1, padx=5, pady=5)
        # self.switch_2 = customtkinter.CTkSwitch(master=self.frame_center, font=("Consolas", 25), text=f"{MUTEBUTTN} Mute", command=self.mute_music).grid(row=3, column=2, pady=1, padx=20, sticky="nw")
        self.switch_3 = customtkinter.CTkSwitch(master=self.frame_center, font=("Consolas", 25), text="Repeat", command=self.repeat_music).grid(row=3, column=3, pady=1, padx=20, sticky="nw")
        self.slider_1 = customtkinter.CTkSlider(master=self.frame_center).grid(row=1, column=5, rowspan=4, columnspan=2, padx=(10, 10), pady=(40, 10), sticky="ns")
        # self.button_5 = customtkinter.CTkButton(master=self.frame_center, font=("Consolas", 45), text=f"{SHFLLBUTN}", command=self.button_event).grid( row=3, column=1, rowspan=1, columnspan=1, padx=5, pady=5)
        # self.button_7 = customtkinter.CTkButton(master=self.frame_center, font=("Consolas", 25), text=f"{REPEATBTN}", command=self.repeat_music).grid( row=3, column=3, rowspan=1, columnspan=1, padx=5, pady=5)


        # ============ Populate Third Frame (RIGHT) ============
        # self.frame_right.rowconfigure((0, 1, 2, 3), weight=0)
        # self.frame_right.rowconfigure(7, weight=0)
        # self.frame_right.columnconfigure((0, 2), weight=2)
        # self.frame_right.columnconfigure(2, weight=2)
        self.frame_right = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_right.grid(row=0, column=1, rowspan=1, columnspan=2, padx=10, pady=10, sticky="wnse")
        self.label_artist_00 = customtkinter.CTkLabel(master=self.frame_right, text=f" {MUSICNOTE} Song Info: {MUSICNOTE} ", width=120, height=25, corner_radius=8).grid(row=0, rowspan=1, column=1, sticky="w")
        self.label_artist_01 = customtkinter.CTkLabel(master=self.frame_right, text=f"Name: ", width=120, height=20, corner_radius=8).grid(row=1, rowspan=1, column=1, sticky="w")
        self.label_artist_02 = customtkinter.CTkLabel(master=self.frame_right, text=f"Artist: ", width=120, height=20, corner_radius=8).grid(row=2, rowspan=1, column=1, sticky="w")
        self.label_artist_03 = customtkinter.CTkLabel(master=self.frame_right, text=f"Composer: ", width=120, height=20, corner_radius=8).grid(row=3, rowspan=1, column=1, sticky="w")
        self.label_artist_04 = customtkinter.CTkLabel(master=self.frame_right, text=f"Album: ", width=120, height=20, corner_radius=8).grid(row=4, rowspan=1, column=1, sticky="w")
        self.label_artist_05 = customtkinter.CTkLabel(master=self.frame_right, text=f"Grouping: ", width=120, height=20, corner_radius=8).grid(row=5, rowspan=1, column=1, sticky="w")
        self.label_artist_06 = customtkinter.CTkLabel(master=self.frame_right, text=f"Work: ", width=120, height=20, corner_radius=8).grid(row=6, rowspan=1, column=1, sticky="w")
        self.label_artist_07 = customtkinter.CTkLabel(master=self.frame_right, text=f"Movement Number: ", width=120, height=20, corner_radius=8).grid(row=7, rowspan=1, column=1, sticky="w")
        self.label_artist_08 = customtkinter.CTkLabel(master=self.frame_right, text=f"Movement Count: ", width=120, height=20, corner_radius=8).grid(row=8, rowspan=1, column=1, sticky="w")
        self.label_artist_09 = customtkinter.CTkLabel(master=self.frame_right, text=f"Movement Name: ", width=120, height=20, corner_radius=8).grid(row=9, rowspan=1, column=1, sticky="w")
        self.label_artist_10 = customtkinter.CTkLabel(master=self.frame_right, text=f"Genre: ", width=120, height=20, corner_radius=8).grid(row=10, rowspan=1, column=1, sticky="w")
        self.label_artist_11 = customtkinter.CTkLabel(master=self.frame_right, text=f"Size: ", width=120, height=20, corner_radius=8).grid(row=11, rowspan=1, column=1, sticky="w")
        self.label_artist_12 = customtkinter.CTkLabel(master=self.frame_right, text=f"Time: ", width=120, height=20, corner_radius=8).grid(row=12, rowspan=1, column=1, sticky="w")
        self.label_artist_13 = customtkinter.CTkLabel(master=self.frame_right, text=f"Disc Number: ", width=120, height=20, corner_radius=8).grid(row=13, rowspan=1, column=1, sticky="w")
        self.label_artist_14 = customtkinter.CTkLabel(master=self.frame_right, text=f"Disc Count: ", width=120, height=20, corner_radius=8).grid(row=14, rowspan=1, column=1, sticky="w")
        self.label_artist_15 = customtkinter.CTkLabel(master=self.frame_right, text=f"Track Number: ", width=120, height=20, corner_radius=8).grid(row=15, rowspan=1, column=1, sticky="w")
        self.label_artist_16 = customtkinter.CTkLabel(master=self.frame_right, text=f"Track Count: ", width=120, height=20, corner_radius=8).grid(row=16, rowspan=1, column=1, sticky="w")
        self.label_artist_17 = customtkinter.CTkLabel(master=self.frame_right, text=f"Year: ", width=120, height=20, corner_radius=8).grid(row=17, rowspan=1, column=1, sticky="w")
        self.label_artist_18 = customtkinter.CTkLabel(master=self.frame_right, text=f"Date Modified: ", width=120, height=20, corner_radius=8).grid(row=18, rowspan=1, column=1, sticky="w")
        self.label_artist_19 = customtkinter.CTkLabel(master=self.frame_right, text=f"Date Added: ", width=120, height=20, corner_radius=8).grid(row=19, rowspan=1, column=1, sticky="w")
        self.label_artist_20 = customtkinter.CTkLabel(master=self.frame_right, text=f"Bit Rate: ", width=120, height=20, corner_radius=8).grid(row=20, rowspan=1, column=1, sticky="w")
        self.label_artist_21 = customtkinter.CTkLabel(master=self.frame_right, text=f"Sample Rate: ", width=120, height=20, corner_radius=8).grid(row=21, rowspan=1, column=1, sticky="w")
        self.label_artist_22 = customtkinter.CTkLabel(master=self.frame_right, text=f"Volume Adjustment: ", width=120, height=20, corner_radius=8).grid(row=22, rowspan=1, column=1, sticky="w")
        self.label_artist_23 = customtkinter.CTkLabel(master=self.frame_right, text=f"Kind: ", width=120, height=20, corner_radius=8).grid(row=23, rowspan=1, column=1, sticky="w")
        self.label_artist_24 = customtkinter.CTkLabel(master=self.frame_right, text=f"Equalizer: ", width=120, height=20, corner_radius=8).grid(row=24, rowspan=1, column=1, sticky="w")
        self.label_artist_25 = customtkinter.CTkLabel(master=self.frame_right, text=f"Comments: ", width=120, height=20, corner_radius=8).grid(row=25, rowspan=1, column=1, sticky="w")
        self.label_artist_26 = customtkinter.CTkLabel(master=self.frame_right, text=f"Plays: ", width=120, height=20, corner_radius=8).grid(row=26, rowspan=1, column=1, sticky="w")
        self.label_artist_27 = customtkinter.CTkLabel(master=self.frame_right, text=f"Last Played: ", width=120, height=20, corner_radius=8).grid(row=27, rowspan=1, column=1, sticky="w")
        self.label_artist_28 = customtkinter.CTkLabel(master=self.frame_right, text=f"Skips: ", width=120, height=20, corner_radius=8).grid(row=28, rowspan=1, column=1, sticky="w")
        self.label_artist_29 = customtkinter.CTkLabel(master=self.frame_right, text=f"Last Skipped: ", width=120, height=20, corner_radius=8).grid(row=29, rowspan=1, column=1, sticky="w")
        self.label_artist_30 = customtkinter.CTkLabel(master=self.frame_right, text=f"My Rating: ", width=120, height=20, corner_radius=8).grid(row=30, rowspan=1, column=1, sticky="w")
        self.label_artist_31 = customtkinter.CTkLabel(master=self.frame_right, text=f"Location: ", width=120, height=20, corner_radius=8).grid(row=31, rowspan=1, column=1, sticky="w")

        # ============ Populate Fourth Frame (RIGHT) ============
        self.frame_fileList.columnconfigure(1, weight=0)
        self.listbox_tk = Listbox(master=self.frame_fileList)
        self.label_tk = Label(text="A list of colors:")
        self.playlistbox = Listbox()
        self.label_tk.grid(row=0, column=3, rowspan=1, columnspan=1, padx=10, pady=10, sticky="nsew")
        self.playlistbox.grid(row=0, column=3, rowspan=1, columnspan=1, padx=10, pady=10, sticky="nsew")

        # ============ Set Default Values ============
        self.scaling_optionemenu.set("100%")
        self.optionmenu_1.set("Dark")
        self.optionmenu_2.set("dark-blue")
        self.progressbar.set(0)

    # ============ BEGIN Define Funcitons BEGIN ============

    def button_event(self):
        print("Button pressed")

    def window_info(self):
        screen_dimensions = f"{self.winfo_height()}x{self.winfo_width()}"
        print(f"Screen Dimensions: {screen_dimensions}")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_theme(self, new_theme):
        customtkinter.set_default_color_theme(new_theme)

    def change_scaling(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_spacing_scaling(new_scaling_float)
        customtkinter.set_widget_scaling(new_scaling_float)

    def on_closing(self, event=0):
        self.destroy()

    def browse_file(self):
        self.filename_path = askopenfilename(filetypes=[("MP3", "*.mp3"),
                                                        ("AAC Audio Files", "*.aac"),
                                                        ("AIFF Audio Files", "*.aiff"),
                                                        ("MPEG Audio Files", "*.mpeg"),
                                                        ("Protected Audio Files", "*.m4a"),
                                                        ("all", "*.*")])
        print(f"Selected Path Added to Queue: {self.filename_path}")
        self.add_to_playlist(self.filename_path)
        mixer.music.queue(self.filename_path)
        # print(f"File Path Added to Queue: {self.filename_path}")

    def add_to_playlist(self, filename):
        self.filename = basename(filename)
        self.index = 0
        playlist = []
        try:
            self.playlistbox.delete(0, END)
            playlist.delete(0, END)
        except AttributeError as e:
            print(f"")
        self.playlistbox.insert(self.index, self.filename)
        playlist.insert(self.index, self.filename_path)
        self.index += 1
        # print(self.playlistbox)
        # print(self.playlist)

    def get_filenames():
        path = "/Users/jkirchoff/Desktop/"
        return os.listdir(path)

    def start_count(self, t):
        # mixer.music.get_busy(): - Returns FALSE when we press the stop button (music stop playing)
        # Continue - Ignores all of the statements below it. We check if music is paused or not.
        self.current_time = 0
        while self.current_time <= self.t and mixer.music.get_busy():
            if self.paused:
                continue
            else:
                self.mins, self.secs = divmod(current_time, 60)
                self.mins = round(self.mins)
                self.secs = round(self.secs)
                self.timeformat = '{:02d}:{:02d}'.format(self.mins, self.secs)
                self.currenttimelabel['text'] = "Current Time" + ' - ' + self.timeformat
                self.time.sleep(1)
                self.current_time += 1

    def show_details(self, play_song):
        self.file_data = splitext(play_song)
        if self.file_data[1] == '.mp3':
            self.audio = MP3(self.play_song)
            self.total_length = self.audio.info.length
        else:
            self.a = mixer.Sound(self.play_song)
            self.total_length = a.get_length()
        # div - total_length/60, mod - total_length % 60
        self.mins, secs = divmod(self.total_length, 60)
        self.mins = round(self.mins)
        self.secs = round(self.secs)
        self.timeformat = '{:02d}:{:02d}'.format(self.mins, self.secs)
        self.lengthlabel['text'] = "Total Length" + ' - ' + self.timeformat
        self.t1 = threading.Thread(target=self.start_count, args=(self.total_length,))
        self.t1.start()

    def onSelect(self, val):
        self.sender = self.val.widget
        self.idx = sender.curselection()
        self.value = sender.get(self.idx)
        self.var.set(self.value)

    def play_music(self):
        print(self.playlistbox.curselection())
        if self.paused:
            mixer.music.unpause()
            # self.statusbar['text'] = "Music Resumed"
            self.paused = FALSE
        else:
            self.stop_music()
            sleep(2)
            selected_song = self.playlistbox.curselection()
            print(f"selected_song: {selected_song}")
            selected_song = int(selected_song[0])
            print(f"selected_song: {selected_song}")
            play_it = playlist[selected_song]
            print(f"play_it: {play_it}")
            mixer.music.load(play_it)
            mixer.music.play()
            # self.statusbar['text'] = f"Playing music - {play_it}"
            show_details(play_it)
            # except IndexError as e:
            #     print(f"Error: Nothing was Loaded. \nSys: {e}")
            # except Exception as e:
            #     tkinter.messagebox.showerror('File not found!', f'Could not find the file. Please check again.\n\n{e}')

    def stop_music(self):
        mixer.music.stop()
        # self  .statusbar['text'] = "Music Stopped"

    def pause_music(self):
        global paused
        self.paused = TRUE
        mixer.music.pause()
        # self.statusbar['text'] = "Music Paused"

    def rewind_music(self):
        self.play_music()
        # self.statusbar['text'] = "Music Rewinded"

    def skip_music(self):
        self.play_music()
        # self.statusbar['text'] = "Music Skipped Ahead"

    def repeat_music(self):
        self.play_music()
        # self.statusbar['text'] = "Music On Repeat"

    def set_vol(self, val):
        self.volume = float(val) / 100
        mixer.music.set_volume(self.volume)

    def mute_music(self):
        global muted
        if self.muted:  # Unmute the music
            mixer.music.set_volume(0.7)
            self.muted = FALSE
            self.button_4 = customtkinter.CTkButton(master=self.frame_center, font=("", 66), text=f"{SPKRBUTTN}", command=self.mute_music).grid(   row=3, column=2, rowspan=1, columnspan=1, padx=5, pady=5)
        else:  # mute the music
            mixer.music.set_volume(0)
            self.muted = TRUE
            self.button_4 = customtkinter.CTkButton(master=self.frame_center, font=("", 66), text=f"{MUTEBUTTN}", command=self.mute_music).grid(   row=3, column=2, rowspan=1, columnspan=1, padx=5, pady=5)

    def del_song(self):
        selected_song = self.playlistbox.curselection()
        selected_song = int(selected_song[0])
        self.playlistbox.delete(selected_song)
        playlist.pop(selected_song)

    def showMenu(self, e):
        self.menu.post(e.x_root, e.y_root)

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

    def about_us(self):
        self.messagebox.showinfo('About Player', 'This is a music player build using Python Tkinter by @JayRizzo')

    def on_closing(self):
        """https://stackoverflow.com/a/65657779/1896134 ."""
        self.stop_music()
        close = messagebox.askokcancel("Close", "Are You Sure You Want To Close The Program?")
        self.saveConfig()
        self.destroy()

    def saveConfig(self):
        global config
        with open("config.ini", "w") as conf:
            conf.write(f"{self.geometry()}\n")


    # ============ END Define Funcitons END ============

if __name__ == "__main__":
    app = App()
    app.attributes('-fullscreen', False)
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.wm_attributes("-transparent", True)
    app.wm_attributes("-topmost", False)
    app.minsize(1120, 470)
    # app.state("zoomed")
    app.mainloop()

# TODO: Find Use-able Scroll Bar For Tkinter FRAMES ============
# self.scrollbar = customtkinter.CTkScrollbar(master=self.frame_right)
# self.scrollbar.grid(row=0, column=4, rowspan=1, columnspan=1, sticky="ew")
# https://gist.github.com/mp035/9f2027c3ef9172264532fcd6262f3b01
