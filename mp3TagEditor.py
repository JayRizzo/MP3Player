#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : jkirchoff
# Created Date: Tue Sep 26 19:10:53 2022 CDT
# Last ModDate: Tue Sep 27 17:50:01 2022 CDT
# =============================================================================
import functools  # reduce - Required for ID3 Header Checks
import mutagen
from mutagen.mp3 import MP3
from mutagen.mp3 import MPEGInfo
from mutagen.mp4 import MP4
from mutagen.id3 import ID3
from mutagen.id3 import ID3Tags
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import Encoding  # Required for SYLT SYNC'D Lyrics
from mutagen.id3 import AENC  # AENC [ Supported Version: 4.20 ] # id3.AENC(owner='', preview_start=0, preview_length=0, data='')
from mutagen.id3 import APIC  # APIC [ Supported Version: 4.20 ] # Attached (or linked) Picture. id3.add(APIC(encoding=3, mime=u'image/jpeg', type=3, desc=u'Front Cover', data=self.get_cover(info)))  Example2# id3.add(APIC(encoding=3, mime=u'image/jpg', type=3, desc=u'Cover', data=self.get_cover(info['album_pic_url'])))
from mutagen.id3 import ASPI  # ASPI [ Supported Version: 2.00 ] # Audio seek point index. Attributes: S, L, N, b, and Fi. For the meaning of these, see the ID3v2.4 specification. Fi is a list of integers.
from mutagen.id3 import CHAP  # CHAP [ Supported Version: 2.00 ] # Chapter propertyHashKey An internal key used to ensure frame uniqueness in a tag
from mutagen.id3 import COMM  # COMM [ Supported Version: 4.11 ] # Comments
from mutagen.id3 import COMR  # COMR [ Supported Version: 4.25 ] # Commercial frame
from mutagen.id3 import CTOC  # CTOC [ Supported Version: 2.00 ] # Table of contents propertyHashKey An internal key used to ensure frame uniqueness in a tag
from mutagen.id3 import ENCR  # ENCR [ Supported Version: 4.26 ] # Encryption method registration
from mutagen.id3 import EQU2  # EQU2 [ Supported Version: 2.00 ] # Equalisation (2).  Attributes: method - interpolation method (0 = band, 1 = linear) desc - identifying description adjustments - list of (frequency, vol_adjustment) pairs
from mutagen.id3 import ETCO  # ETCO [ Supported Version: 4.06 ] # Event timing codes
from mutagen.id3 import GEOB  # GEOB [ Supported Version: 4.16 ] # General encapsulated object
from mutagen.id3 import GRID  # GRID [ Supported Version: 4.27 ] # Group identification registration
from mutagen.id3 import IPLS  # IPLS [ Supported Version: 4.04 ] # Involved people list
from mutagen.id3 import LINK  # LINK [ Supported Version: 4.21 ] # Linked information
from mutagen.id3 import MCDI  # MCDI [ Supported Version: 4.05 ] # Music CD identifier
from mutagen.id3 import MLLT  # MLLT [ Supported Version: 4.07 ] # MPEG location lookup table
from mutagen.id3 import MVIN  # MVIN [ Supported Version: 2.00 ] # iTunes Movement Number/Count
from mutagen.id3 import MVNM  # MVNM [ Supported Version: 2.00 ] # iTunes Movement Name
from mutagen.id3 import OWNE  # OWNE [ Supported Version: 4.24 ] # Ownership frame
from mutagen.id3 import PCNT  # PCNT [ Supported Version: 4.17 ] # Play counter
from mutagen.id3 import PCST  # PCST [ Supported Version: 2.00 ] # iTunes Podcast Flag
from mutagen.id3 import POPM  # POPM [ Supported Version: 4.18 ] # Popularimeter
from mutagen.id3 import POSS  # POSS [ Supported Version: 4.22 ] # Position synchronization frame
from mutagen.id3 import PRIV  # PRIV [ Supported Version: 4.28 ] # Private frame
from mutagen.id3 import RBUF  # RBUF [ Supported Version: 4.19 ] # Recommended buffer size
from mutagen.id3 import RVA2  # RVA2 [ Supported Version: 2.00 ] # Relative volume adjustment (2)
from mutagen.id3 import RVAD  # RVAD [ Supported Version: 4.12 ] # Relative volume adjustment
from mutagen.id3 import RVRB  # RVRB [ Supported Version: 4.14 ] # Reverb
from mutagen.id3 import SEEK  # SEEK [ Supported Version: 2.00 ] # Seek frame.
from mutagen.id3 import SIGN  # SIGN [ Supported Version: 2.00 ] # Signature frame.
from mutagen.id3 import SYLT  # SYLT [ Supported Version: 4.10 ] # Synchronized lyric/text
from mutagen.id3 import SYTC  # SYTC [ Supported Version: 4.08 ] # Synchronized tempo codes
from mutagen.id3 import TALB  # TALB [ Supported Version: 2.00 ] # Album/Movie/Show title
from mutagen.id3 import TBPM  # TBPM [ Supported Version: 2.00 ] # BPM (beats per minute)
from mutagen.id3 import TCAT  # TCAT [ Supported Version: 2.00 ] # iTunes Podcast Category
from mutagen.id3 import TCMP  # TCMP [ Supported Version: 2.00 ] # iTunes Compilation Flag
from mutagen.id3 import TCOM  # TCOM [ Supported Version: 2.00 ] # TCOM Composer
from mutagen.id3 import TCON  # TCON [ Supported Version: 2.00 ] # TCON Content type
from mutagen.id3 import TCOP  # TCOP [ Supported Version: 2.00 ] # TCOP Copyright message
from mutagen.id3 import TDAT  # TDAT [ Supported Version: 2.00 ] # TDAT Date
from mutagen.id3 import TDEN  # TDEN [ Supported Version: 2.00 ] # Encoding Time
from mutagen.id3 import TDES  # TDES [ Supported Version: 2.00 ] # iTunes Podcast Description
from mutagen.id3 import TDLY  # TDLY [ Supported Version: 2.00 ] # TDLY Playlist delay
from mutagen.id3 import TDOR  # TDOR [ Supported Version: 2.00 ] # Original Release Time
from mutagen.id3 import TDRC  # TDRC [ Supported Version: 2.00 ] # Recording Time
from mutagen.id3 import TDRL  # TDRL [ Supported Version: 2.00 ] # Release Time
from mutagen.id3 import TDTG  # TDTG [ Supported Version: 2.00 ] # Tagging Time
from mutagen.id3 import TENC  # TENC [ Supported Version: 2.00 ] # TENC Encoded by
from mutagen.id3 import TEXT  # TEXT [ Supported Version: 2.00 ] # TEXT Lyricist/Text writer
from mutagen.id3 import TFLT  # TFLT [ Supported Version: 2.00 ] # TFLT File type
from mutagen.id3 import TGID  # TGID [ Supported Version: 2.00 ] # iTunes Podcast Identifier
from mutagen.id3 import TIME  # TIME [ Supported Version: 2.00 ] # TIME Time
from mutagen.id3 import TIPL  # TIPL [ Supported Version: 2.00 ] # Involved People List
from mutagen.id3 import TIT1  # TIT1 [ Supported Version: 2.00 ] # TIT1 Content group description
from mutagen.id3 import TIT2  # TIT2 [ Supported Version: 2.00 ] # TIT2 Title/songname/content description
from mutagen.id3 import TIT3  # TIT3 [ Supported Version: 2.00 ] # TIT3 Subtitle/Description refinement
from mutagen.id3 import TKEY  # TKEY [ Supported Version: 2.00 ] # TKEY Initial key
from mutagen.id3 import TKWD  # TKWD [ Supported Version: 2.00 ] # iTunes Podcast Keywords
from mutagen.id3 import TLAN  # TLAN [ Supported Version: 2.00 ] # TLAN Language(s)
from mutagen.id3 import TLEN  # TLEN [ Supported Version: 2.00 ] # TLEN Length]
from mutagen.id3 import TMCL  # TMCL [ Supported Version: 2.00 ] # Musicians Credits List
from mutagen.id3 import TMED  # TMED [ Supported Version: 2.00 ] # TMED Media type
from mutagen.id3 import TMOO  # TMOO [ Supported Version: 2.00 ] # Mood]
from mutagen.id3 import TOAL  # TOAL [ Supported Version: 2.00 ] # TOAL Original album/movie/show title
from mutagen.id3 import TOFN  # TOFN [ Supported Version: 2.00 ] # TOFN Original filename
from mutagen.id3 import TOLY  # TOLY [ Supported Version: 2.00 ] # TOLY Original lyricist(s)/text writer(s)
from mutagen.id3 import TOPE  # TOPE [ Supported Version: 2.00 ] # TOPE Original artist(s)/performer(s)
from mutagen.id3 import TORY  # TORY [ Supported Version: 2.00 ] # TORY Original release year
from mutagen.id3 import TOWN  # TOWN [ Supported Version: 2.00 ] # TOWN File owner/licensee
from mutagen.id3 import TPE1  # TPE1 [ Supported Version: 2.00 ] # TPE1 Lead performer(s)/Soloist(s)
from mutagen.id3 import TPE2  # TPE2 [ Supported Version: 2.00 ] # TPE2 Band/orchestra/accompaniment
from mutagen.id3 import TPE3  # TPE3 [ Supported Version: 2.00 ] # TPE3 Conductor/performer refinement
from mutagen.id3 import TPE4  # TPE4 [ Supported Version: 2.00 ] # TPE4 Interpreted, remixed, or otherwise modified by
from mutagen.id3 import TPOS  # TPOS [ Supported Version: 2.00 ] # TPOS Part of a set
from mutagen.id3 import TPRO  # TPRO [ Supported Version: 2.00 ] # Produced (P)
from mutagen.id3 import TPUB  # TPUB [ Supported Version: 2.00 ] # TPUB Publisher
from mutagen.id3 import TRCK  # TRCK [ Supported Version: 2.00 ] # TRCK Track number/Position in set
from mutagen.id3 import TRDA  # TRDA [ Supported Version: 2.00 ] # TRDA Recording dates
from mutagen.id3 import TRSN  # TRSN [ Supported Version: 2.00 ] # TRSN Internet radio station name
from mutagen.id3 import TRSO  # TRSO [ Supported Version: 2.00 ] # TRSO Internet radio station owner
from mutagen.id3 import TSIZ  # TSIZ [ Supported Version: 2.00 ] # TSIZ Size
from mutagen.id3 import TSO2  # TSO2 [ Supported Version: 2.00 ] # iTunes Album Artist Sort
from mutagen.id3 import TSOA  # TSOA [ Supported Version: 2.00 ] # Album Sort Order key
from mutagen.id3 import TSOC  # TSOC [ Supported Version: 2.00 ] # iTunes Composer Sort
from mutagen.id3 import TSOP  # TSOP [ Supported Version: 2.00 ] # Perfomer Sort Order key
from mutagen.id3 import TSOT  # TSOT [ Supported Version: 2.00 ] # Title Sort Order key
from mutagen.id3 import TSRC  # TSRC [ Supported Version: 2.00 ] # ISRC (international standard recording code)
from mutagen.id3 import TSSE  # TSSE [ Supported Version: 2.00 ] # Software/Hardware and settings used for encoding
from mutagen.id3 import TSST  # TSST [ Supported Version: 2.00 ] # Set Subtitle
from mutagen.id3 import TXXX  # TXXX [ Supported Version: 2.00 ] # User defined text information frame
from mutagen.id3 import TYER  # TYER [ Supported Version: 2.00 ] # Year
from mutagen.id3 import UFID  # UFID [ Supported Version: 4.01 ] # Unique file identifier
from mutagen.id3 import USER  # USER [ Supported Version: 4.23 ] # Terms of use
from mutagen.id3 import USLT  # USLT [ Supported Version: 4.09 ] # Unsychronized lyric/text transcription
from mutagen.id3 import WCOM  # WCOM [ Supported Version: 2.00 ] # Commercial information
from mutagen.id3 import WCOP  # WCOP [ Supported Version: 2.00 ] # Copyright/Legal information
from mutagen.id3 import GRP1  # GRP1 [ Supported Version: 2.00 ] # iTunes Grouping
from mutagen.id3 import WFED  # WFED [ Supported Version: 2.00 ] # iTunes Podcast Feed
from mutagen.id3 import WOAF  # WOAF [ Supported Version: 2.00 ] # Official audio file webpage
from mutagen.id3 import WOAR  # WOAR [ Supported Version: 2.00 ] # Official artist/performer webpage
from mutagen.id3 import WOAS  # WOAS [ Supported Version: 2.00 ] # Official audio source webpage
from mutagen.id3 import WORS  # WORS [ Supported Version: 2.00 ] # Official internet radio station homepage
from mutagen.id3 import WPAY  # WPAY [ Supported Version: 2.00 ] # Payment
from mutagen.id3 import WPUB  # WPUB [ Supported Version: 2.00 ] # Publishers official webpage
from mutagen.id3 import WXXX  # WXXX [ Supported Version: 2.00 ] # User defined URL link frame

# =====================================================================================================================
# Four Character Imports
# https://pypi.org/project/mutagen/1.45.1/
# https://mutagen.readthedocs.io/en/latest/changelog.html
# https://mutagen.readthedocs.io/en/latest/api/id3_frames.html?highlight=Group%20identification%20registration
# =============================================================================
# Notes:
# TODO: Share here when done https://stackoverflow.com/q/37414448/1896134 & https://stackoverflow.com/q/18248200/1896134
# TODO: embed album art in an MP3
# TODO: Produced By Tom MacDonald
# TODO: Written By Tom MacDonald
# TODO: Mixing Engineer Evan Morgan
# TODO: Mastering Engineer Evan Morgan
# TODO: Release Date December 25, 2020
# =====================================================================================================================


class MP3TagYourSong(object):
    """MP3TagYourSong Handle Getters & Setters for Mutagen ID3 Tags"""
    def __init__(self, arg: str):
        super(MP3TagYourSong, self).__init__()
        self.songpath = arg  # Full File Path To MP3.
        self.sync_lyrics = [('', 0), ('', 0)]
        self.SongArtistName = self.getSongArtist()
        self.SongAlbumName = self.getSongAlbum()
        self.SongPlayCount = 0

    def SelectOneSongToEdit(self):
        """JayRizzo Music Song Meta Mixer."""
        self.songpath = askopenfilename(initialdir=f"{self.CWDIR}/Music/",
                                        title="Choose A Song:",
                                        filetypes=[("MP3", "*.mp3"),
                                                   ("AAC Audio Files", "*.aac"),
                                                   ("AIFF Audio Files", "*.aiff"),
                                                   ("MPEG Audio Files", "*.mpeg"),
                                                   ("Protected Audio Files", "*.m4a"),
                                                   ("all", "*.*")])

    def duration_from_seconds(self, s):
        """Module to get the convert Seconds to a time like format."""
        s = s
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        TIMELAPSED  = f"{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}"
        return TIMELAPSED

    def duration_from_millseconds(self, ms):
        """Module to get the convert Seconds to a time like format."""
        ms = ms
        s, ms = divmod(ms, 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        TIMELAPSED  = f"{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}:{ms:03.0f}"
        return TIMELAPSED

    # =====================================================================================================================
    # Tag Checkers
    # =====================================================================================================================
    def CreateMissingTag(self):
        """Credit: https://github.com/quodlibet/mutagen/issues/327#issuecomment-339316014"""
        try:
            mp3 = MP3(self.songpath)
            if mp3.tags is None:
                print(f"No ID3 Header or Tags Exist.")
                mp3.add_tags()
                print(f"Default Placeholder Tags Were Created.")
            tags = mp3.tags
            mp3.save()
        except Exception as e:
            print(f"{e}")

    def CheckID3Tag(self):
        """Check for Header Size."""
        try:
            # print header data
            with open(self.songpath, 'rb') as a:
                data = a.read(10)
                print(data)
            # print header data check
            with open(self.songpath, 'rb') as a:
                if data[0:3] != b'ID3':
                    print('No ID3 header present in file.')
                else:
                    size_encoded = bytearray(data[-4:])
                    size = functools.reduce(lambda a, b: (a * 128 + b), size_encoded, 0)
                    print(size)
        except Exception as e:
            print(f"Error: {e}")

    def convertID3Tags2to3(self):
        try:
            tags = ID3(self.songpath)
            tags.update_to_v24()
            tags.save(v1=2, v2_version=4, v23_sep='/')
        except Exception as e:
            print(f"Error: {e}")

    # =====================================================================================================================
    # Tag Delete ALL
    # =====================================================================================================================
    def deleteAllTags(self):
        """Remove All ID3 Tags."""
        tags = ID3(self.songpath)
        tags.delete(self.songpath)

    # =====================================================================================================================
    # Tag Getters
    # =====================================================================================================================
    def getSongArtist(self):
        tags = ID3(self.songpath)
        try:
            self.SongArtistName = f"{tags.getall('TPE1')[0][0]}"
            # print(f"{tags.getall('TPE1')[0][0]}")
        except IndexError as e:
            self.SongArtistName
        except ID3NoHeaderError as e:
            self.SongArtistName
        except Exception as e:
            print(f"Error: {e}")
        return self.SongArtistName

    def getSongTitle(self):
        tags = ID3(self.songpath)
        try:
            print(f"{tags.getall('TIT2')[0][0]}")
        except IndexError as e:
            print(None)
        except Exception as e:
            print(f"Error: {e}")
        return tags.getall('TIT2')[0][0]

    def getSongAlbum(self):
        tags = ID3(self.songpath)
        try:
            print(f"{tags.getall('TALB')[0][0]}")
        except IndexError as e:
            print(None)
        except Exception as e:
            print(f"Error: {e}")
        return tags.getall('TALB')[0][0]

    def getSongAlbum(self):
        tags = ID3(self.songpath)
        try:
            print(f"{tags.getall('TDOR')[0][0]}")  # Original Release Time
            # print(f"{tags.getall('TDRL')[0][0]}") # Release Time
        except IndexError as e:
            print('')
        except Exception as e:
            print(f"Error: {e}")
        return tags.getall('TALB')[0][0]

    def getSongPlayCount(self):
        try:
            tags = ID3(self.songpath)
            self.SongPlayCount = f"{tags.getall('PCNT')[0].count}"
        except IndexError as e:
            self.SongPlayCount = 0
        except Exception as e:
            print(f"Error: {e}")
        return print(self.SongPlayCount)

    def getSongSyncedLyrics(self):
        """
        # [1000ms]: It's not the liquor I'm addicted to, it's feeling brave
        # [2000ms]: The feeling of not feeling the pain
        # [3000ms]: I been on and off the bottle, I put oxys up my nostrils, believe me
        """
        tags = ID3(self.songpath)
        try:
            print(f"{tags.get('SYLT::eng')}")
        except IndexError as e:
            print(0)
        except Exception as e:
            print(f"Error: {e}")
        return tags.get('SYLT::eng')

    def getSongUnSyncedLyrics(self):
        """
        Input: filename, sync_lyrics
        Example: setSongSyncedLyrics('song', [('Some Lyics at time in MilliSeconds', 1000), ('Some More Lyics, add as many as you'd like, 2000)]
        """
        tags = ID3(self.songpath)
        try:
            print(f"{tags.get('USLT')}")
        except IndexError as e:
            print(0)
        except Exception as e:
            print(f"Error: {e}")
        return tags.get('USLT')

    # =====================================================================================================================
    # Tag Setters
    # =====================================================================================================================

    def setSongArtist(self, ArtistName):
        self.SongArtistName = ArtistName
        tags = ID3(self.songpath)
        tags.add(TPE1(encoding=3, text=[ArtistName]))
        tags.save(v1=50000000, v2_version=4, v23_sep='/')

    def setSongAlbum(self, AlbumName):
        tags = ID3(self.songpath)
        tags.add(TALB(encoding=3, text=[AlbumName]))
        tags.save(v1=1, v2_version=4, v23_sep='/')

    def setSongTitle(self, SongTitle):
        tags = ID3(self.songpath)
        tags.add(TIT2(encoding=3, text=[SongTitle]))
        tags.save(v1=1, v2_version=4, v23_sep='/')

    def setSongPlayCount(self, PlayCount):
        tags = ID3(self.songpath)
        tags.add(PCNT(encoding=3, count=PlayCount))
        tags.save(v1=1, v2_version=4, v23_sep='/')

    def setSongSyncedLyrics(self, sync_lyrics : list):
        """
        Input: filename, sync_lyrics
        Example: setSongSyncedLyrics('song', [('Some Lyics at time in MilliSeconds', 1000), ('Some More Lyics, add as many as you'd like, 2000)]
        """
        tags = ID3(self.songpath)
        slrcs = sync_lyrics
        tags.setall("SYLT", [SYLT(encoding=Encoding.UTF16, lang='eng', format=2, type=1, text=slrcs)])
        tags.save(v1=1, v2_version=4, v23_sep='/')

    def setSongUnSyncedLyrics(filename, sync_lyrics : list):
        """
        Input: filename, sync_lyrics
        Example: setSongSyncedLyrics('song', [('Some Lyics at time in MilliSeconds', 1000), ('Some More Lyics, add as many as you'd like, 2000)]
        """
        tags = ID3(self.songpath)
        slrcs = sync_lyrics
        tags.setall("SYLT", [USLT(encoding=Encoding.UTF16, lang='eng', desc=u'desc', text=slrcs)])
        tags.save(v1=1, v2_version=4, v23_sep='/')


if __name__ == '__main__':
    # =====================================================================================================================
    # Example Song
    # =====================================================================================================================
    filename2 = '/Users/jkirchoff/Documents/github/MP3Player/Music/02 Bad Girls Club.mp3'
    filename = '/Users/jkirchoff/Documents/github/MP3Player/Music/Tom MacDonald - Angels (Explicit).mp3'
    # https://genius.com/Tom-macdonald-angels-lyrics
    song = MP3TagYourSong(filename)
    song2 = MP3TagYourSong(filename2)
    # Checkers
    song.CreateMissingTag()
    song.CheckID3Tag()
    song.convertID3Tags2to3()
    # Getters
    song.getSongTitle()
    song.getSongArtist()
    song.getSongAlbum()
    song.getSongPlayCount()
    # Setters
    song.setSongTitle("Angels (Explicit)")
    song.setSongArtist("Tom MacDonald")
    song.setSongAlbum("No Guts No Glory")
    song.setSongPlayCount(393)
    # Check the changes
    song.getSongTitle()
    song.getSongArtist()
    song.getSongAlbum()
    song.getSongPlayCount()
    # Check Second song
    song2.getSongArtist()
    song2.getSongTitle()
    song2.getSongAlbum()
    song2.getSongPlayCount()


# b'ID3\x04\x00\x00\x00\x00E6'
# 8886
# Tom MacDonald
# Angels (Explicit)
# None
# 123
# 123
# Tom MacDonaldz
# Angels (Explicitz)
# None
# 1234534
# 1234534
# [Finished in 168ms]
# getSongSyncedLyrics(filename)
# # setSongSyncedLyrics(filename, sync_lyrics)
# getSongSyncedLyrics(filename)

# filename = '/Users/jkirchoff/Desktop/1-01 Angels (Explicit)  TITLE.mp4'
# MP4VideoTags = MP4(filename)
# MP4VideoTags['\xa9nam'] = 'Video Name'
# MP4VideoTags['\xa9alb'] = 'DVD-Name'
# MP4VideoTags['\xa9gen'] = 'Video-Training'
# MP4VideoTags['\xa9day'] = '2015'
# MP4VideoTags['\xa9ART'] = 'Company'
# MP4VideoTags['aART'] = 'Company'
# MP4VideoTags['\xa9wrt'] = 'Company'
# MP4VideoTags['cprt'] = 'Copyright (c) Company'
# MP4VideoTags['desc'] = 'description'
# MP4VideoTags['tvsh'] = 'DVD-Name'
# MP4VideoTags['trkn'] = [(1, 18)]
# MP4VideoTags['disk'] = [(1, 1)]
# MP4VideoTags['stik'] = 10

# MP4VideoTags.save()

# CreateMissingTag(filename)
# getSongArtist(filename)
# getSongTitle(filename)
# getSongAlbum(filename)
# getSongPlayCount(filename)
# getSongSyncedLyrics(filename)


# # Released September 3, 2021

# [1000ms]: It's not the liquor I'm addicted to, it's feeling brave
# [2000ms]: The feeling of not feeling the pain
# [3000ms]: I been on and off the bottle, I put oxys up my nostrils, believe me
# [4000ms]: You do anything to breathe before you suffocate
# [5000ms]: I couldn't stop it, staying clean was not an option
# [6000ms]: I was tryna be myself but being me was such a problem
# [7000ms]: I just wanted to be Thomas, but Thomas was at the bottom of a hole he dug
# [8000ms]: And getting comfortable inside a coffin, ay
# [9000ms]: He locked it and swallowed the key, he caught up, forgot all his dreams
# [10000ms]: Robbed outta calm and became embalmed in a toxic routine
# [11000ms]: Beer was the escape but I got stuck escaping
# [12000ms]: Whiskey was the blanket in the coldest basement
# [13000ms]: Way before the fame, I was wasted
# [14000ms]: Freezing, doing anything I could to keep the flame lit
# [15000ms]: To anyone going through the same shit
# [16000ms]: Heaven's got enough angels, you need to stay here
# [17000ms]: And I can't make you stay but sometimes going ain't a choice
# [18000ms]: And every choice you make is one that you didn't avoid
# [51000ms]: And the truth ain't pretty, listen up, it's a tough one
# [52000ms]: You get saved by your angels or become one
# [53000ms]: Crash the whip and ditch the car, burn a bridge, follow the stars
# [54000ms]: You'll find monsters in the dark but nothing's worth it till it's hard
# [55000ms]: Sometimes it's hard to see things clear (through your tears)
# [56000ms]: But anywhere is way better than here (fight your fears)

# audio = MP3(filename, ID3=EasyID3)
# audio.pprint()
# tag = MP3(self.songpath)
# print(tag.info.pprint())
# print(f"tag.bitrate:           {tag.info.bitrate}")
# print(f"tag.length:            {tag.info.length}")
# print(f"tag.protected:         {tag.info.protected}")
# print(f"tag.ID3:               {tag.ID3.values}")
# print(f"tag.album_gain:        {tag.info.album_gain}")
# print(f"tag.album_peak:        {tag.info.album_peak}")
# print(f"tag.bitrate_mode:      {tag.info.bitrate_mode}")
# print(f"tag.channels:          {tag.info.channels}")
# print(f"tag.encoder_info:      {tag.info.encoder_info}")
# print(f"tag.encoder_settings:  {tag.info.encoder_settings}")
# print(f"tag.frame_offset:      {tag.info.frame_offset}")
# print(f"tag.layer:             {tag.info.layer}")
# print(f"tag.mode:              {tag.info.mode}")
# print(f"tag.padding:           {tag.info.padding}")
# print(f"tag.pprint:            {tag.info.pprint}")
# print(f"tag.sample_rate:       {tag.info.sample_rate}")
# print(f"tag.sketchy:           {tag.info.sketchy}")
# print(f"tag.track_gain:        {tag.info.track_gain}")
# print(f"tag.track_peak:        {tag.info.track_peak}")
# print(f"tag.version:           {tag.info.version}")
# # print(f"tag.keys:              {tag.keys()}")
# # print(f"tag.info:              {dir(tag)}")
# # print(f"tag.ID3:               {dir(tag.ID3)}")
# # print(f"tag.ID3:               {dir(tag.ID3.values)}")
# m = ID3(self.songpath)
# print(m)
# def SongArtist(owner,  preview_start=0, preview_length=0, data=''):
#     id3.TOPE('')
#     try:
#       id3info = ID3('/some/file/moxy.mp3')
#       print(id3info)
#       id3info['TITLE'] = "Green Eggs and Ham"
#       id3info['ARTIST'] = "Moxy Früvous"
#       for k, v in id3info.items():
#         print(k, ":", v)
#     except InvalidTagError, message:
#         print("Invalid ID3 tag:", message)
# # ID3v2.3/4 Frames
# id3.TextFrame('')
# id3.TimeStampTextFrame('')
# id3.NumericPartTextFrame('')
# id3.NumericTextFrame('')
# id3.PairedTextFrame(encoding=<Encoding.UTF16: 1>, people=[])
# id3.UrlFrame(url='')
# id3.UrlFrameU(url='')
# id3.add(COMM(encoding=3, desc=u'Comment', # text=info['song_url']))
# id3.add(COMM(encoding=3, desc=u'Comment', text=info['comment']))
# id3.add(COMM(encoding=3, desc=u'Comment', text=info['song_url']))
# id3.add(COMM(encoding=3, desc=u'Comment', text=info['song_url']))
# id3.add(TALB(encoding=3, text=info['album_name']))
# id3.add(TALB(encoding=3, text=info['album_name']))
# id3.add(TALB(encoding=3, text=info['album_name']))
# id3.add(TCOM(encoding=3, text=info['composer']))
# id3.add(TCOM(encoding=3, text=info['composer']))
# id3.add(TCON(encoding=3, text=u'genre'))
# id3.add(TCON(encoding=3, text=u'genres'))
# id3.add(TCON(encoding=3, text=u'genres'))
# id3.add(TDRC(encoding=3, text=info['year']))
# id3.add(TDRC(encoding=3, text=info['year']))
# id3.add(TDRC(encoding=3, text=str(info['year'])))
# id3.add(TIT2(encoding=3, text=info['song_name']))
# id3.add(TIT2(encoding=3, text=info['song_name']))
# id3.add(TIT2(encoding=3, text=info['song_name']))
# id3.add(TPE1(encoding=3, text=info['artist_name']))
# id3.add(TPE1(encoding=3, text=info['artist_name']))
# id3.add(TPE1(encoding=3, text=info['artist_name']))
# id3.add(TPOS(encoding=3, text=info['cd_serial']))
# id3.add(TPOS(encoding=3, text=info['cd_serial']))
# id3.add(TPOS(encoding=3, text=str(info['cd_serial'])))
# id3.add(TRCK(encoding=3, text=info['track']))
# id3.add(TRCK(encoding=3, text=info['track']))
# id3.add(TRCK(encoding=3, text=info['track']))
# id3.add(TRCK(encoding=3, text=str(info['track'])))
# id3.add(TSRC(encoding=3, text=info['disc_code']))
# id3.add(TSRC(encoding=3, text=info['disc_code']))
# id3.add(TSST(encoding=3, text=info['sub_title']))
# id3.add(TSST(encoding=3, text=info['sub_title']))
# id3.add(USLT(encoding=3, text=lyric_data)) if lyric_data else None
# id3.add(USLT(encoding=3, text=self.get_lyric(info['lyric_url'])))
# id3.add(USLT(encoding=3, text=self.get_lyric(info['lyric_url'])))
# id3.add(WXXX(encoding=3, desc=u'xiami_song_url', text=info['song_url']))
# tags.getall('TDOR')
# tags.getall('tags.TDRC')
# tags.getall('tags.TDRL')
# tags.getall('tags.TDTG')


# sync_lyrics = [
#     ("It's not the liquor I'm addicted to, it's feeling brave",                                          1000),
#     ("The feeling of not feeling the pain",                                                              2000),
#     ("I been on and off the bottle, I put oxys up my nostrils, believe me",                              3000),
#     ("You do anything to breathe before you suffocate",                                                  4000),
#     ("I couldn't stop it, staying clean was not an option",                                              5000),
#     ("I was tryna be myself but being me was such a problem",                                            6000),
#     ("I just wanted to be Thomas, but Thomas was at the bottom of a hole he dug",                        7000),
#     ("And getting comfortable inside a coffin, ay",                                                      8000),
#     ("He locked it and swallowed the key, he caught up, forgot all his dreams",                          9000),
#     ("Robbed outta calm and became embalmed in a toxic routine",                                        10000),
#     ("Beer was the escape but I got stuck escaping",                                                    11000),
#     ("Whiskey was the blanket in the coldest basement",                                                 12000),
#     ("Way before the fame, I was wasted",                                                               13000),
#     ("Freezing, doing anything I could to keep the flame lit",                                          14000),
#     ("To anyone going through the same shit",                                                           15000),
#     ("Heaven's got enough angels, you need to stay here",                                               16000),
#     ("And I can't make you stay but sometimes going ain't a choice",                                    17000),
#     ("And every choice you make is one that you didn't avoid",                                          18000),
#     ("Crash the whip and ditch the car, burn a bridge, follow the stars",                               19000),
#     ("You'll find monsters in the dark but nothing's worth it till it's hard",                          20000),
#     ("Sometimes it's hard to see things clear (through your tears)",                                    21000),
#     ("But anywhere is way better than here (fight your fears)",                                         22000),
#     ("It's not the liquor I'm addicted to, it's feeling tough",                                         23000),
#     ("When you get bullied half your life you feel weak like you just ain't enough",                    24000),
#     ("Then you have a couple drinks and you catch a buzz",                                              25000),
#     ("And finally have the courage to defend yourself and throw a punch",                               26000),
#     ("And that adrenaline goes straight into your brain and blood",                                     27000),
#     ("Addicted to the confidence, it's practically the greatest drug",                                  28000),
#     ("Chasing dragons every night in all the latest clubs",                                             29000),
#     ("What used to be your favorite thing somehow became a dangerous crutch",                           30000),
#     ("It was what it was",                                                                              31000),
#     ("And that's the thing, it can happen to like any of us",                                           32000),
#     ("I had great parents, tight friends, strong walls, nice threads",                                  33000),
#     ("Good school, good looking, good grades, time spent",                                              34000),
#     ("Being normal only lasted for a while",                                                            35000),
#     ("One bad choice sparked a downward spiral",                                                        36000),
#     ("I've spent half my life tryna climb outta that hole",                                             37000),
#     ("Heaven's got angels, we need you at home",                                                        38000),
#     ("And I can't make you stay but sometimes going ain't a choice",                                    39000),
#     ("And every choice you make is one that you didn't avoid",                                          40000),
#     ("Crash the whip and ditch the car, burn a bridge, follow the stars",                               41000),
#     ("You'll find monsters in the dark but nothing's worth it till it's hard",                          42000),
#     ("Sometimes it's hard to see things clear (through your tears)",                                    43000),
#     ("But anywhere is way better than here (fight your fears)",                                         44000),
#     ("It ain't the liquor we're addicted to, it's everything else",                                     45000),
#     ("The happiness we had but we forget how it felt",                                                  46000),
#     ("We been drinking with the devil 'cause we're going through hell",                                 47000),
#     ("Pray to God for a little bit of help",                                                            48000),
#     ("Man, I been there, I did those things, I drank those drinks",                                     49000),
#     ("I took those pills, I puked in sinks",                                                            50000),
#     ("And the truth ain't pretty, listen up, it's a tough one",                                         51000),
#     ("You get saved by your angels or become one",                                                      52000),
#     ("Crash the whip and ditch the car, burn a bridge, follow the stars",                               53000),
#     ("You'll find monsters in the dark but nothing's worth it till it's hard",                          54000),
#     ("Sometimes it's hard to see things clear (through your tears)",                                    55000),
#     ("But anywhere is way better than here (fight your fears)",                                         56000)
# ]



# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # =============================================================================
# """The Module Has Been Built to read MP3 Meta Tags & Hidden Mac Attributes."""
# # How to get extended MacOS attributes of a file using python?
# # Research \/
# # https://stackoverflow.com/a/33182025/1896134
# # http://hints.macworld.com/article.php?story=20101206161739274
# # https://stackoverflow.com/a/19550814/1896134
# # =============================================================================
# import csv

# from os import path
# from os import walk

# from time import strftime

# # import biplist

# from eyed3 import id3


# # from tinytag import TinyTag
# # from tinytag import TinyTagException

# import xattr


# def _now():
#     """The Module Returns "Current Time" As A Formatted String."""
#     ymd = str(strftime('%Y%m%d_%H%M%S'))
#     return ymd

# current_home = path.expanduser('~')
# includes_file_extensn = (".mp3", ".m4a", ".flac", ".alac")
# search_dir = path.join(current_home, 'Music')
# tracks = []


# def write_xattr_tags(file_path, tags):
#     """THE MODULE HAS BEEN BUILD FOR writePlistToString."""
#     bpl_tags = biplist.writePlistToString(tags)
#     optional_tag = "com.apple.metadata:"
#     map(lambda a: xattr.setxattr(file_path, optional_tag + a, bpl_tags),
#         ["kMDItemFinderComment", "_kMDItemUserTags", "kMDItemOMUserTags"])
#     return 'Updated xattr'


# def locate_files():
#     """THE MODULE HAS BEEN BUILD FOR Locating YOUR FILES."""
#     for dirpath, dirnames, filenames in walk(search_dir, topdown=False):
#         for name in filenames:
#             if name.endswith(includes_file_extensn):
#                 print("{a} Track Names Begin {a}".format(a='=' * 35))
#                 tracks.append(name)
#                 print("Track: {}".format(name))
#                 print("Track So Far: {}".format(tracks))
#                 print("{a} Track Names END {a}".format(a='=' * 35))
#                 filetomove = path.join(str(dirpath) + '/' +
#                                        str(name))
#                 print('Files found: ' + str(filetomove))
#                 print("\n\n# {} Song ID3Tags Start {} \n\n {}"
#                       .format("=" * 30, "=" * 30,
#                               read_id3_info(filetomove)))
#                 print("\n\n# {} Song ID3Tags End {} \n\n"
#                       .format("=" * 30, "=" * 30))

#                 print("{} Song Meta Start {}".format('=' * 35, '=' * 35))

#                 try:
#                     x = xattr.xattr(filetomove)
#                     print("{}".format(x.items()))
#                     # y = biplist.readPlistFromString(
#                     #     x.get('com.apple.metadata:kMDItemWhereFroms'))
#                     # print("com.apple.metadata:kMDItemWhereFroms: {}".format(y))
#                 except Exception as e:
#                     print("Custom Error: {}".format(e))
#                     pass
#                     # print("{}".format(e.errno))
#                     # print("{}".format(e.filename))
#                     # print("{}".format(e.strerror))
#                 else:
#                     pass
#                     # print("Failed To find attr: kMDItemWhereFroms")
#                 finally:
#                     # print("Completed: {}".format(y))
#                     pass
#                 print("{} Song Meta END {}".format('=' * 35, '=' * 35))

#                 pass
#             else:
#                 pass
#     return filetomove


# def read_id3_info(self):
#     """Module to read MP3 Meta Tags."""
#     tag = id3.Tag()
#     tag.parse(filename)
#     print("Tag Version: {}\n"
#           "Artist: {}\n"
#           "Album: {}\n"
#           "Album Artist: {}\n"
#           "Album Type: {}"
#           .format(tag.version,
#                   tag.artist,
#                   tag.album,
#                   tag.album_artist,
#                   tag.album_type,
#                   ))
#     print("Version: {}".format(tag.version))
#     print("Title: {}".format(tag.title))
#     print("Track Num: {}".format(tag.track_num))
#     print("Artist Origin: {}".format(tag.artist_origin))
#     print("Artist Url: {}".format(tag.artist_url))
#     print("Audio File Url: {}".format(tag.audio_file_url))
#     print("Audio Source Url: {}".format(tag.audio_source_url))
#     print("GetBestDate: {}".format(tag.getBestDate()))
#     print("Bpm: {}".format(tag.bpm))
#     print("Cd Id: {}".format(tag.cd_id))
#     # print("Chapters: {}".format(tag.chapters))
#     # print("Clear: {}".format(tag.clear))
#     # print("Comments: {}".format(tag.comments))
#     print("Commercial Url: {}".format(tag.commercial_url))
#     print("Composer: {}".format(tag.composer))
#     print("Copyright Url: {}".format(tag.copyright_url))
#     print("Disc Num: {}".format(tag.disc_num))
#     print("Encoding Date: {}".format(tag.encoding_date))
#     # print("File Info: {}".format(tag.file_info))
#     print("File Info Name: {}".format(tag.file_info.name))
#     print("File Info Tag Padding Size: {}".format(tag.file_info.tag_padding_size))  # noqa
#     print("File Info Tag Size: {}".format(tag.file_info.tag_size))

#     # for key, value in sorted(tag.frame_set.items(), key=lambda x: x[1]):
#     #     print("{} : {}".format(key, value))
#     # print("Frameiter: {}".format(tag.frameiter))
#     if tag.genre is not None and tag.genre.id is not None:
#         if tag.genre.id is not None:
#             print("Genre ID: {}".format(tag.genre.id))
#         if tag.genre.name is not None:
#             print("Genre: {}".format(tag.genre.name))

#     if tag.getBestDate() is not None:
#         print("GetBestDate: {}-{}-{} {}-{}-{}"
#               .format(tag.getBestDate().year,
#                       tag.getBestDate().month,
#                       tag.getBestDate().day,
#                       tag.getBestDate().hour,
#                       tag.getBestDate().minute,
#                       tag.getBestDate().second
#                       )
#               )

#     print("GetTextFrame: {}".format(tag.getTextFrame))
#     print("Header - Experimental: {}".format(tag.header.experimental))
#     print("Header - extended: {}".format(tag.header.extended))
#     print("Header - footer: {}".format(tag.header.footer))
#     print("Header - version: {}".format(tag.header.version))
#     print("Header - major_version: {}".format(tag.header.major_version))
#     print("Header - minor_version: {}".format(tag.header.minor_version))
#     print("Header - rev_version: {}".format(tag.header.rev_version))
#     print("Header - render: {}".format(tag.header.render()))
#     print("Header - tag_size: {}".format(tag.header.tag_size))
#     print("Header - unsync: {}".format(tag.header.unsync))
#     # print("Header - parse: {}".format(tag.header.parse()))
#     # print("Header - clear: {}".format(tag.header.clear))

#     # print("Images: {}".format(tag.images))
#     print("Internet Radio Url: {}".format(tag.internet_radio_url))
#     print("IsV1: {}".format(tag.isV1()))
#     print("IsV2: {}".format(tag.isV2()))
#     # print("Lyrics: {}".format(tag.lyrics))
#     print("Non Std Genre: {}".format(tag.non_std_genre))
#     # print("Objects: {}".format(tag.objects))
#     print("Original Release Date: {}".format(tag.original_release_date))
#     print("Parse: {}".format(tag.parse(tag.file_info.name)))
#     print("Payment Url: {}".format(tag.payment_url))
#     print("Play Count: {}".format(tag.play_count))
#     # print("Popularities: {}".format(tag.popularities))
#     # print("Privates: {}".format(tag.privates))
#     print("Publisher: {}".format(tag.publisher))
#     print("Publisher Url: {}".format(tag.publisher_url))
#     print("Read Only: {}".format(tag.read_only))
#     print("Recording Date: {}".format(tag.recording_date))
#     print("Release Date: {}".format(tag.release_date))
#     # print("Remove: {}".format(tag.remove))
#     # print("Save: {}".format(tag.save))
#     # print("SetTextFrame: {}".format(tag.setTextFrame))
#     # print("Table Of Contents: {}".format(tag.table_of_contents))
#     print("Tagging Date: {}".format(tag.tagging_date))
#     print("Terms Of Use: {}".format(tag.terms_of_use))
#     # print("Unique File Ids: {}".format(tag.unique_file_ids))
#     # print("User Text Frames: {}".format(tag.user_text_frames))
#     # print("User Url Frames: {}".format(tag.user_url_frames))
#     print("{} Extended Header Start {}".format('=' * 35, '=' * 35))
#     # print("Extended Header CRC: {}".format(tag.extended_header.crc))
#     # print("Extended Header CRC Bit: {}".format(tag.extended_header.crc_bit))
#     # print("Extended Header image Enc Restriction: {}".format(tag.extended_header.image_enc_restriction))  # noqa
#     # print("Extended Header image Enc Restriction Description: {}".format(tag.extended_header.image_enc_restriction_description))  # noqa
#     # print("Extended Header image Size Restriction: {}".format(tag.extended_header.image_size_restriction))  # noqa
#     # print("Extended Header image Size Restriction Description: {}".format(tag.extended_header.image_size_restriction_description))  # noqa
#     # print("Extended Header parse: {}".format(tag.extended_header.parse()))
#     # # TypeError: parse() missing 2 required positional arguments: 'fp' and 'version'  # noqa
#     # print("Extended Header render: {}".format(tag.extended_header.render))
#     # # TypeError: render() missing 2 required positional arguments: 'version' and 'frame_data'  # noqa
#     # print("Extended Header restrictions Bit: {}".format(tag.extended_header.restrictions_bit))  # noqa
#     # print("Extended Header size: {}".format(tag.extended_header.size))  # noqa
#     print("Extended Header tag Size Restriction: {}".format(tag.extended_header.tag_size_restriction))  # noqa
#     print("Extended Header tag Size Restriction Description: {}".format(tag.extended_header.tag_size_restriction_description))  # noqa
#     print("Extended Header text Enc Restriction: {}".format(tag.extended_header.text_enc_restriction))  # noqa
#     print("Extended Header text Enc Restriction Description: {}".format(tag.extended_header.text_enc_restriction_description))  # noqa
#     print("Extended Header text Length Restriction: {}".format(tag.extended_header.text_length_restriction))  # noqa
#     print("Extended Header text Length Restriction Description: {}".format(tag.extended_header.text_length_restriction_description))  # noqa
#     print("Extended Header update Bit: {}".format(tag.extended_header.update_bit))  # noqa
#     print("{} Extended Header End {}".format('=' * 35, '=' * 35))
#     print("")
#     return


# def checkthings(self):
#     """Module to Verify MP3 Meta Tags."""
#     tag = id3.Tag()
#     tag.parse(filename)
#     test_version = ("Valid Tag Format: {}".format(id3.isValidVersion(tag.version)))  # noqa
#     print(test_version)
#     return id3.isValidVersion(tag.version)


# def pushtocsv():
#     """Module to Write MP3 Meta Info To CSV."""
#     csv.register_dialect('pipes', delimiter='|')
#     f = open(_now() + '_taglist.csv', 'w')

#     writer = csv.writer(f, quoting=csv.QUOTE_ALL)

#     with f:
#         writer = csv.writer(f, dialect="dapiper")
#         writer.writerow(("pens", 4))
#         writer.writerow(("plates", 2))
#         writer.writerow(("bottles", 4))
#         writer.writerow(("cups", 1))


# if __name__ == '__main__':
#     locate_files()

#     # read_id3_info(filename)
#     # read_id3_info(filename2)

#     # checkthings(filename)
#     # checkthings(filename2)

# # ==================================== Notes ==================================

# # # Example usage
# # x = xattr.xattr(filename)
# # x.items()
# # # [(u'com.apple.metadata:kMDItemWhereFroms',
# # #   'bplist00\xa2\x01\x02_\x10Thttps://be-internet.bene-system.com/....'),  # noqa
# # #  (u'com.apple.quarantine',
# # #   '0001;562127d1;Google Chrome;BF24C900-46D5-4F95-9B7B-C36AA6B0ACC7')]
# # biplist.readPlistFromString(x.get('com.apple.metadata:kMDItemWhereFroms'))
# # # ['https://be-internet.bene-system.com//hp/pdfservice?pdf=KLWVWLG1445013390236BS169201', '']  # noqa


# # https://github.com/quodlibet/mutagen

# # mdfind -onlyin ~ 'kMDItemWhereFroms == "*"'
# # mdfind -onlyin ~ 'kMDItemIsScreenCapture == "*"'
# # mdfind -onlyin ~ 'kMDItemKind == "*"'
# # mdfind -onlyin ~ 'kMDItemFinderComment == "*"'
# # mdfind -onlyin ~ 'kMDItemKeywords == "*"'

# # mdls ~/Documents/python-developers-toolkit.zip
# # mdls -name kMDItemWhereFroms ~/Documents/python-developers-toolkit.zip
# # mdls -name kMDItemKind ~/Documents/python-developers-toolkit.zip

# # xattr -w "Senior Author" "JayRizzo MF." filename_here.pdf
# # xattr -w "com.apple.metadata:kMDItemAuthors" "JayMFRizzo" filename_here.pdf

# # xattr -w "com.apple.metadata:kMDItemWhereFroms"
# #   "http://topdocumentaryfilms.com/journey-edge-universe/" file.flv

# # mdls ~/Music/iTunes/iTunes\ Media/Music/* > ~/Desktop/Music_mdls.txt
# # xattr -rl ~/Documents > ~/Desktop/Documents.txt
# # xattr -rl ~/Downloads > ~/Desktop/Downloads.txt
# # xattr -rl ~/Movies > ~/Desktop/Movies.txt
# # xattr -rl ~/Music > ~/Desktop/Music.txt
# # xattr -rd com.apple.metadata:Zone.Identifier ~/Music
# # xattr -rd Zone.Identifier ~/Music

# # # Remove Restrictions
# # xattr -rd com.apple.quarantine ~/Documents
# # xattr -rd com.apple.quarantine ~/Downloads
# # xattr -rd com.apple.quarantine ~/Movies
# # xattr -rd com.apple.quarantine ~/Music

# # # Remove erranious where-from information
# # xattr -rd com.apple.metadata:kMDItemWhereFroms ~/Documents
# # xattr -rd com.apple.metadata:kMDItemWhereFroms ~/Downloads
# # xattr -rd com.apple.metadata:kMDItemWhereFroms ~/Movies
# # xattr -rd com.apple.metadata:kMDItemWhereFroms ~/Music

# # # Remove erranious lastuseddate
# # xattr -rd com.apple.lastuseddate ~/Documents
# # xattr -rd com.apple.lastuseddate ~/Downloads
# # xattr -rd com.apple.lastuseddate ~/Movies
# # xattr -rd com.apple.lastuseddate ~/Music
# # xattr -rd com.apple.lastuseddate:#PS ~/Documents
# # xattr -rd com.apple.lastuseddate:#PS ~/Downloads
# # xattr -rd com.apple.lastuseddate:#PS ~/Movies
# # xattr -rd com.apple.lastuseddate:#PS ~/Music

# # # Remove Erroneous Files
# # find ~/Documents -type f -name ".DS_Store" -print -delete;
# # find ~/Downloads -type f -name ".DS_Store" -print -delete;
# # find ~/Movies -type f -name ".DS_Store" -print -delete;
# # find ~/Music -type f -name ".DS_Store" -print -delete;

# # find ~/Documents -type f -name 'Icon?' -print -delete;
# # find ~/Downloads -type f -name 'Icon?' -print -delete;
# # find ~/Movies -type f -name 'Icon?' -print -delete;
# # find ~/Music -type f -name 'Icon?' -print -delete;

# # # Remove Empty Folders
# # find ~/Documents -type d -empty -delete;
# # find ~/Downloads -type d -empty -delete;
# # find ~/Movies -type d -empty -delete;
# # find ~/Music -type d -empty -delete;



# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # =============================================================================
# """The Module Has Been Built to read MP3 Meta Tags & Hidden Mac Attributes."""
# # How to get extended MacOS attributes of a file using python?
# # Research \/
# # https://stackoverflow.com/a/33182025/1896134
# # http://hints.macworld.com/article.php?story=20101206161739274
# # https://stackoverflow.com/a/19550814/1896134
# # =============================================================================
# import csv
# import re
# from os import path
# from os import walk

# from time import strftime

# # import biplist

# from eyed3 import id3
# from eyed3 import log

# import xattr
# # Helpful if you want to ignore errors.
# # https://stackoverflow.com/a/25614061/1896134
# # https://stackoverflow.com/a/39316798/1896134
# # log.setLevel("ERROR")
# log.setLevel("INFO")

# # from tinytag import TinyTag
# # from tinytag import TinyTagException


# def _now():
#     """The Module Returns "Current Time" As A Formatted String."""
#     ymd = str(strftime('%Y%m%d_%H%M%S'))
#     return ymd


# current_home = path.expanduser('~')
# new_file = (current_home + '/Desktop/testin_' + _now() + '.csv')
# includes_file_extensn = (".mp3", ".m4a", ".flac", ".alac", ".aif", ".aiff")
# search_dir = path.join(current_home, 'Music')
# # search_dir = path.join('/Volumes', 'Muisikk', 'iTunes', 'iTunes Media')
# print(search_dir)
# tracks = []


# def locate_files():
#     """THE MODULE HAS BEEN BUILD FOR Locating YOUR FILES."""
#     filelocated = ''
#     for dirpath, dirnames, filenames in walk(search_dir, topdown=False):
#         for name in filenames:
#             if name.lower().endswith(includes_file_extensn):
#                 filelocated = path.join(str(dirpath) + '/' +
#                                         str(name))
#                 read_id3_artist(filelocated)
#                 # print("{a} Track Names Begin {a}".format(a='=' * 35))
#                 # tracks.append(name)
#                 # print("Track So Far: {}".format(tracks))
#                 # print("{a} Track Names END {a}".format(a='=' * 35))
#                 # print('Files found: ' + str(filelocated))
#                 # print("\n\n# {} Song ID3Tags Start {} \n {}"
#                 #       .format("=" * 30, "=" * 30,
#                 #               read_id3_artist(filelocated)))
#                 #               # read_id3_info(filelocated)))
#                 # print("\n\n# {} Song ID3Tags End {} \n"
#                 #       .format("=" * 30, "=" * 30))

#                 print("{} Song Meta Start {}".format('=' * 35, '=' * 35))

#                 try:
#                     x = xattr.xattr(filelocated)
#                     print("{}".format(x.items()))
#                     y = biplist.readPlistFromString(
#                         x.get('com.apple.metadata:kMDItemWhereFroms'))
#                     print("com.apple.metadata:ItemWhereFroms: {}".format(y))
#                 except Exception as e:
#                     print("Custom Error: {}".format(e))
#                     # print("{}".format(e.errno))
#                     # print("{}".format(e.filename))
#                     # print("{}".format(e.strerror))
#                 else:
#                     pass
#                     # print("Failed To find attr: kMDItemWhereFroms")
#                 finally:
#                     # print("Completed: {}".format(y))
#                     pass
#                 print("{} Song Meta END {}".format('=' * 35, '=' * 35))
#                 print("\n\n\n\n\n\n\n\n")
#                 pass
#             else:
#                 print("{} Ignored.".format(name))
#                 pass
#     return filelocated


# with open(new_file, 'w', newline='') as csvfile:
#     fieldnames = ['Artist', 'Tracks', 'Path']
#     stuff_to_write = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     stuff_to_write.writeheader()


# def read_id3_artist(self):
#     """Module to read MP3 Meta Tags."""
#     filename = filename
#     filename.encode()
#     tag = id3.Tag()
#     tag.parse(filename)
#     # print("Artist: \"{}\" Track: \"{}\"".format(tag.artist, tag.title))

#     artist = tag.artist
#     title = tag.title
#     track_path = filename

#     if artist is not None:
#         artist.encode()
#         artist = re.sub(u'`', u"'", artist)
#     if title is not None:
#         title.encode()
#         title = re.sub(u'`', u"'", title)
#     if track_path is not None:
#         track_path.encode()
#         track_path = re.sub(u'`', u"'", track_path)

#     with open(new_file, 'a', newline='') as csvfile:
#         stuff_to_write = csv.writer(csvfile,
#                                     delimiter=',',
#                                     quotechar='"',
#                                     quoting=csv.QUOTE_ALL)
#         stuff_to_write.writerow([artist, title, track_path])


# def read_id3_info(self):
#     """Module to read MP3 Meta Tags."""
#     tag = id3.Tag()
#     tag.parse(filename)
#     print("Tag Version: {}\n"
#           "Artist: {}\n"
#           "Album: {}\n"
#           "Album Artist: {}\n"
#           "Album Type: {}"
#           .format(tag.version,
#                   tag.artist,
#                   tag.album,
#                   tag.album_artist,
#                   tag.album_type,
#                   ))
#     print("Version: {}".format(tag.version))
#     print("Title: {}".format(tag.title))
#     print("Track Num: {}".format(tag.track_num))
#     print("Artist Origin: {}".format(tag.artist_origin))
#     print("Artist Url: {}".format(tag.artist_url))
#     print("Audio File Url: {}".format(tag.audio_file_url))
#     print("Audio Source Url: {}".format(tag.audio_source_url))
#     print("GetBestDate: {}".format(tag.getBestDate()))
#     print("Bpm: {}".format(tag.bpm))
#     print("Cd Id: {}".format(tag.cd_id))
#     # print("Chapters: {}".format(tag.chapters))
#     # print("Clear: {}".format(tag.clear))
#     # print("Comments: {}".format(tag.comments))
#     print("Commercial Url: {}".format(tag.commercial_url))
#     print("Composer: {}".format(tag.composer))
#     print("Copyright Url: {}".format(tag.copyright_url))
#     print("Disc Num: {}".format(tag.disc_num))
#     print("Encoding Date: {}".format(tag.encoding_date))
#     # print("File Info: {}".format(tag.file_info))
#     print("File Info Name: {}".format(tag.file_info.name))
#     print("File Info Tag Padding Size: {}".format(tag.file_info.tag_padding_size))  # noqa
#     print("File Info Tag Size: {}".format(tag.file_info.tag_size))

#     # for key, value in sorted(tag.frame_set.items(), key=lambda x: x[1]):
#     #     print("{} : {}".format(key, value))
#     # print("Frameiter: {}".format(tag.frameiter))
#     if tag.genre is not None and tag.genre.id is not None:
#         if tag.genre.id is not None:
#             print("Genre ID: {}".format(tag.genre.id))
#         if tag.genre.name is not None:
#             print("Genre: {}".format(tag.genre.name))

#     if tag.getBestDate() is not None:
#         print("GetBestDate: {}-{}-{} {}-{}-{}"
#               .format(tag.getBestDate().year,
#                       tag.getBestDate().month,
#                       tag.getBestDate().day,
#                       tag.getBestDate().hour,
#                       tag.getBestDate().minute,
#                       tag.getBestDate().second
#                       )
#               )

#     print("GetTextFrame: {}".format(tag.getTextFrame))
#     print("Header - Experimental: {}".format(tag.header.experimental))
#     print("Header - extended: {}".format(tag.header.extended))
#     print("Header - footer: {}".format(tag.header.footer))
#     print("Header - version: {}".format(tag.header.version))
#     print("Header - major_version: {}".format(tag.header.major_version))
#     print("Header - minor_version: {}".format(tag.header.minor_version))
#     print("Header - rev_version: {}".format(tag.header.rev_version))
#     print("Header - render: {}".format(tag.header.render()))
#     print("Header - tag_size: {}".format(tag.header.tag_size))
#     print("Header - unsync: {}".format(tag.header.unsync))
#     # print("Header - parse: {}".format(tag.header.parse()))
#     # print("Header - clear: {}".format(tag.header.clear))

#     # print("Images: {}".format(tag.images))
#     print("Internet Radio Url: {}".format(tag.internet_radio_url))
#     print("IsV1: {}".format(tag.isV1()))
#     print("IsV2: {}".format(tag.isV2()))
#     # print("Lyrics: {}".format(tag.lyrics))
#     print("Non Std Genre: {}".format(tag.non_std_genre))
#     # print("Objects: {}".format(tag.objects))
#     print("Original Release Date: {}".format(tag.original_release_date))
#     print("Parse: {}".format(tag.parse(tag.file_info.name)))
#     print("Payment Url: {}".format(tag.payment_url))
#     print("Play Count: {}".format(tag.play_count))
#     # print("Popularities: {}".format(tag.popularities))
#     # print("Privates: {}".format(tag.privates))
#     print("Publisher: {}".format(tag.publisher))
#     print("Publisher Url: {}".format(tag.publisher_url))
#     print("Read Only: {}".format(tag.read_only))
#     print("Recording Date: {}".format(tag.recording_date))
#     print("Release Date: {}".format(tag.release_date))
#     # print("Remove: {}".format(tag.remove))
#     # print("Save: {}".format(tag.save))
#     # print("SetTextFrame: {}".format(tag.setTextFrame))
#     # print("Table Of Contents: {}".format(tag.table_of_contents))
#     print("Tagging Date: {}".format(tag.tagging_date))
#     print("Terms Of Use: {}".format(tag.terms_of_use))
#     # print("Unique File Ids: {}".format(tag.unique_file_ids))
#     # print("User Text Frames: {}".format(tag.user_text_frames))
#     # print("User Url Frames: {}".format(tag.user_url_frames))
#     print("{} Extended Header Start {}".format('=' * 35, '=' * 35))
#     print("Extended Header CRC: {}".format(tag.extended_header.crc))
#     print("Extended Header CRC Bit: {}".format(tag.extended_header.crc_bit))
#     print("Extended Header image Enc Restriction: {}".format(tag.extended_header.image_enc_restriction))  # noqa
#     print("Extended Header image Enc Restriction Description: {}".format(tag.extended_header.image_enc_restriction_description))  # noqa
#     print("Extended Header image Size Restriction: {}".format(tag.extended_header.image_size_restriction))  # noqa
#     print("Extended Header image Size Restriction Description: {}".format(tag.extended_header.image_size_restriction_description))  # noqa
#     # print("Extended Header parse: {}".format(tag.extended_header.parse()))
#     # # TypeError: parse() missing 2 required positional arguments: 'fp' and 'version'  # noqa
#     # print("Extended Header render: {}".format(tag.extended_header.render))
#     # # TypeError: render() missing 2 required positional arguments: 'version' and 'frame_data'  # noqa
#     print("Extended Header restrictions Bit: {}".format(tag.extended_header.restrictions_bit))  # noqa
#     print("Extended Header size: {}".format(tag.extended_header.size))  # noqa
#     print("Extended Header tag Size Restriction: {}".format(tag.extended_header.tag_size_restriction))  # noqa
#     print("Extended Header tag Size Restriction Description: {}".format(tag.extended_header.tag_size_restriction_description))  # noqa
#     print("Extended Header text Enc Restriction: {}".format(tag.extended_header.text_enc_restriction))  # noqa
#     print("Extended Header text Enc Restriction Description: {}".format(tag.extended_header.text_enc_restriction_description))  # noqa
#     print("Extended Header text Length Restriction: {}".format(tag.extended_header.text_length_restriction))  # noqa
#     print("Extended Header text Length Restriction Description: {}".format(tag.extended_header.text_length_restriction_description))  # noqa
#     print("Extended Header update Bit: {}".format(tag.extended_header.update_bit))  # noqa
#     print("{} Extended Header End {}".format('=' * 35, '=' * 35))
#     print("")
#     return


# def checkthings(self):
#     """Module to Verify MP3 Meta Tags."""
#     tag = id3.Tag()
#     tag.parse(filename)
#     test_version = ("Valid Tag Format: {}".format(id3.isValidVersion(tag.version)))  # noqa
#     print(test_version)
#     return id3.isValidVersion(tag.version)


# def pushtocsv():
#     """Module to Write MP3 Meta Info To CSV."""
#     csv.register_dialect('pipes', delimiter='|')
#     f = open(_now() + '_taglist.csv', 'w')

#     writer = csv.writer(f, quoting=csv.QUOTE_ALL)

#     with f:
#         writer = csv.writer(f, dialect="dapiper")
#         writer.writerow(("pens", 4))
#         writer.writerow(("plates", 2))
#         writer.writerow(("bottles", 4))
#         writer.writerow(("cups", 1))


# def write_xattr_tags(file_path, tags):
#     """THE MODULE HAS BEEN BUILD FOR writePlistToString."""
#     bpl_tags = biplist.writePlistToString(tags)
#     optional_tag = "com.apple.metadata:"
#     map(lambda a: xattr.setxattr(file_path, optional_tag + a, bpl_tags),
#         ["kMDItemFinderComment", "_kMDItemUserTags", "kMDItemOMUserTags"])
#     return 'Updated xattr'


# if __name__ == '__main__':
#     locate_files()

#     # read_id3_info(filename)
#     # read_id3_info(filename2)

#     # checkthings(filename)
#     # checkthings(filename2)
# """The Module Has Been Built to read MP3 Meta Tags & Hidden Mac Attributes."""
# import re
# from os import path
# from os import walk

# from eyed3 import id3


# def locate_files():
#     """THE MODULE HAS BEEN BUILD FOR Locating YOUR FILES."""
#     current_home = path.expanduser('~')
#     includes_file_extensn = (".mp3", ".m4a", ".flac", ".alac", ".aiff")
#     search_dir = path.join(current_home, 'Music')
#     print("Searching Directory: {}".format(search_dir))
#     for dirpath, dirnames, filenames in walk(search_dir, topdown=False):
#         for name in filenames:
#             if name.lower().endswith(includes_file_extensn):
#                 filelocated = path.join(str(dirpath) + '/' +
#                                         str(name))
#                 print("# {} Song Meta Start {}".format('=' * 34, '=' * 34))
#                 read_id3_artist(filelocated)
#                 print("# {} Song Meta END {}".format('=' * 34, '=' * 34))


# def read_id3_artist(self):
#     """Module to read MP3 Meta Tags."""
#     filename = filename
#     filename.encode()
#     tag = id3.Tag()
#     tag.parse(filename)
#     artist = tag.artist
#     if artist is not None:
#         artist.encode()
#         artist = re.sub(u'`', u"'", artist)
#         print("Artist: {}".format(artist.encode()))
#     title = tag.title
#     if title is not None:
#         title.encode()
#         title = re.sub(u'`', u"'", title)
#         print("title: {}".format(title.encode()))
#     track_path = filename
#     if track_path is not None:
#         track_path.encode()
#         track_path = re.sub(u'`', u"'", track_path)
#         print("Track Path: {}".format(track_path.encode()))
#     duration = tag.duration
#     if duration is not None:
#         duration.encode()
#         duration = re.sub(u'`', u"'", duration)
#         print("Duration: {}".format(duration.encode()))
#     return


# if __name__ == '__main__':
#     locate_files()


# filename = '~/Music/test/t154.mp3'
# filename.encode()
# tag = id3.Tag()
# tag.parse(filename)
# tag.isV1()
# tag.isV2()

# artist = tag.artist
# if artist is not None:
#     artist.encode()
#     artist = re.sub(u'`', u"'", artist)
#     print("Artist: {}".format(artist.encode()))
# title = tag.title
# if title is not None:
#     title.encode()
#     title = re.sub(u'`', u"'", title)
#     print("title: {}".format(title.encode()))
# track_path = filename
# if track_path is not None:
#     track_path.encode()
#     track_path = re.sub(u'`', u"'", track_path)
#     print("Track Path: {}".format(track_path.encode()))
# duration = tag.duration
# if duration is not None:
#     duration.encode()
#     duration = re.sub(u'`', u"'", duration)
#     print("Duration: {}".format(duration.encode()))


# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # =============================================================================
# # Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# # Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# # Created By  : jkirchoff
# # Created Date: Tue Sep  6 19:43:15 2022 CDT
# # Last ModDate: Tue Sep  6 19:43:15 2022 CDT
# # =============================================================================
# # Notes:
# # =============================================================================
# """GUI Music Player, Play 10 seconds of One Song."""
# from eyed3 import id3
# from eyed3 import load
# from getpass import getuser
# from mutagen.mp3 import MP3from time import sleep
# from vlc import AudioOutput
# from vlc import AudioOutputDevice
# from vlc import AudioTrack
# from vlc import ChapterDescription
# from vlc import DialogCbs
# from vlc import Event
# from vlc import Log
# from vlc import LogMessage
# from vlc import MediaDiscovererDescription
# from vlc import MediaPlayer
# from vlc import MediaSlave
# from vlc import MediaStats
# from vlc import MediaTrack
# from vlc import MediaTrackInfo
# from vlc import ModuleDescription
# from vlc import RdDescription
# from vlc import SubtitleTrack
# from vlc import TitleDescription
# from vlc import TrackDescription
# from vlc import VideoTrack
# from vlc import VideoViewpoint
# import os
# import sys
# import threading
# import time
# import tkinter.messagebox
# import vlc
# import xattr

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# app = customtkinter.CTk()
# app.geometry("400x240")

# CURRENT_HOME = expanduser('~')  # /Users/JayRizzo
# userMusicList = join(CURRENT_HOME + "/Music/")
# search_dir = path.join(current_home + "/Music/iTunes/iTunes Media/Music/Rush/Chronicles (Disc 2)/2-03 Limelight.mp3")  # noqa

# # Load path to One Song
# onesong = join(CURRENT_HOME + r"/Music/Music/Media.localized/Music/30 Seconds To Mars/A Beautiful Lie/01 Attack.mp3")  # noqa


# # from mutagen.easyid3 import EasyID3
# # from pygame import event
# # from pygame import mixer
# # from pygame import USEREVENT
# # from tkinter.filedialog import *
# # from tkinter import *

# # class FrameApp(Frame):
# #     def __init__(self,master):
# #         super(FrameApp, self).__init__(master)
# #         self.title("Music Player")
# #         self.grid()
# #         self.paused = False
# #         self.playlist = list()
# #         self.actual_song = 0
# #         self.b1 = Button(self, text="play", command=self.play_music, width=20)
# #         self.b1.grid(row=1, column=0)
# #         self.b2 = Button(self, text="previous", command=self.previous_song, width=20)
# #         self.b2.grid(row=2, column=0)
# #         self.b3 = Button(self, text="toggle", command=self.toggle, width=20)
# #         self.b3.grid(row=3, column=0)
# #         self.b4 = Button(self, text="next", command=self.next_song, width=20)
# #         self.b4.grid(row=4, column=0)
# #         self.b5 = Button(self, text="add to list", command=self.add_to_list, width=20)
# #         self.b5.grid(row=5, column=0)
# #         self.label1 = Label(self)
# #         self.label1.grid(row=6, column=0)
# #         self.output = Text(self, wrap=WORD, width=50)
# #         self.output.grid(row=8, column=0)
# #         self.SONG_END = USEREVENT + 1 # set event to not predefined value in pygame
# #         # TODO: Make progress-bar, delete songs from playlist, amplify volume

# #     def add_to_list(self):
# #         """
# #         Opens window to browse data on disk and adds selected songs to play list
# #         :return: None
# #         """
# #         directory = askopenfilenames()
# #         # appends song directory on disk to playlist in memory
# #         for song_dir in directory:
# #             print(song_dir)
# #             self.playlist.append(song_dir)
# #         self.output.delete(0.0, END)
# #         for key, item in enumerate(self.playlist):
# #             # appends song to textbox
# #             song = EasyID3(item)
# #             song_data = (str(key + 1) + ' : ' + song['title'][0] + ' - '
# #                          + song['artist'][0])
# #             self.output.insert(END, song_data + '\n')

# #     def song_data(self):
# #         """
# #         Makes string of current playing song data over the text box
# #         :return: string - current song data
# #         """
# #         song = EasyID3(self.playlist[self.actual_song])
# #         song_data = "Now playing: Nr:" + str(self.actual_song + 1) + " " + \
# #                     str(song['title']) + " - " + str(song['artist'])
# #         return song_data

# #     def play_music(self):
# #         """
# #         Loads current song, plays it, sets event on song finish
# #         :return: None
# #         """
# #         directory = self.playlist[self.actual_song]
# #         mixer.music.load(directory)
# #         mixer.music.play(1, 0.0)
# #         mixer.music.set_endevent(self.SONG_END)
# #         self.paused = False
# #         self.label1['text'] = self.song_data()

# #     def check_music(self):
# #         """
# #         Listens to END_MUSIC event and triggers next song to play if current
# #         song has finished
# #         :return: None
# #         """
# #         for event in event.get():
# #             if event.type == self.SONG_END:
# #                 self.next_song()

# #     def toggle(self):
# #         """
# #         Toggles current song
# #         :return: None
# #         """
# #         if self.paused:
# #             mixer.music.unpause()
# #             self.paused = False
# #         elif not self.paused:
# #             mixer.music.pause()
# #             self.paused = True

# #     def get_next_song(self):
# #         """
# #         Gets next song number on playlist
# #         :return: int - next song number
# #         """
# #         if self.actual_song + 2 <= len(self.playlist):
# #             return self.actual_song + 1
# #         else:
# #             return 0

# #     def next_song(self):
# #         """
# #         Plays next song
# #         :return: None
# #         """
# #         self.actual_song = self.get_next_song()
# #         self.play_music()

# #     def get_previous_song(self):
# #         """
# #         Gets previous song number on playlist and returns it
# #         :return: int - prevoius song number on playlist
# #         """
# #         if self.actual_song - 1 >= 0:
# #             return self.actual_song - 1
# #         else:
# #             return len(self.playlist) - 1

# #     def previous_song(self):
# #         """
# #         Plays prevoius song
# #         :return:
# #         """
# #         self.actual_song = self.get_previous_song()
# #         self.play_music()

# # root = Tk()
# # root.geometry("350x500")
# # app = FrameApp(root)

# # while True:
# #     # runs mainloop of program
# #     app.check_music()
# #     app.update()


# # # import tkinter as tk
# # # import tkinter.font as tkFont


# # # class App:
# # #     def __init__(self, root):
# # #         root.title("undefined")
# # #         self.screenwidth = root.winfo_screenwidth()
# # #         self.screenheight = root.winfo_screenheight()
# # #         width = self.screenwidth / 2
# # #         height = self.screenheight / 2
# # #         screenwidth = root.winfo_screenwidth()
# # #         screenheight = root.winfo_screenheight()
# # #         alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
# # #         root.geometry(alignstr)
# # #         root.resizable(width=False, height=False)
# # #         GLabel_835=tk.Label(root)
# # #         ft = tkFont.Font(family='Times', size=10)
# # #         GLabel_835["font"] = ft
# # #         GLabel_835["fg"] = "#333333"
# # #         GLabel_835["justify"] = "center"
# # #         GLabel_835["text"] = "Music Editor"
# # #         GLabel_835.place(x=0, y=0, width=self.screenwidth, height=32)

# # #         GButton_132=tk.Button(root)
# # #         GButton_132["bg"] = "#efefef"
# # #         ft = tkFont.Font(family='Times', size=10)
# # #         GButton_132["font"] = ft
# # #         GButton_132["fg"] = "#000000"
# # #         GButton_132["justify"] = "center"
# # #         GButton_132["text"] = "Button"
# # #         GButton_132.place(x=90, y=120, width=70, height=25)
# # #         GButton_132["command"] = self.GButton_132_command

# # #         GListBox_455=tk.Listbox(root)
# # #         GListBox_455["borderwidth"] = "1px"
# # #         ft = tkFont.Font(family='Times', size=10)
# # #         GListBox_455["font"] = ft
# # #         GListBox_455["fg"] = "#333333"
# # #         GListBox_455["justify"] = "center"
# # #         GListBox_455.place(x=0, y=180, width=331, height=301)

# # #         GLabel_988=tk.Label(root)
# # #         ft = tkFont.Font(family='Times', size=10)
# # #         GLabel_988["font"] = ft
# # #         GLabel_988["fg"] = "#333333"
# # #         GLabel_988["justify"] = "center"
# # #         GLabel_988["text"] = "Artist: "
# # #         GLabel_988.place(x=370, y=130, width=70, height=25)

# # #         GLineEdit_998=tk.Entry(root)
# # #         GLineEdit_998["borderwidth"] = "1px"
# # #         ft = tkFont.Font(family='Times', size=10)
# # #         GLineEdit_998["font"] = ft
# # #         GLineEdit_998["fg"] = "#333333"
# # #         GLineEdit_998["justify"] = "center"
# # #         GLineEdit_998["text"] = "Entry"
# # #         GLineEdit_998.place(x=350, y=180, width=70, height=25)

# # #     def GButton_132_command(self):
# # #         print("command")

# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = App(root)
# # #     root.mainloop()


# # # # https://raw.githubusercontent.com/mitensolanki/File-Manager-using-tkinter/master/filemanager.py

# # # from tkinter import *
# # # import shutil
# # # import os

# # # #   FUNCTIONS

# # # def open_file():
# # #     global e1
# # #     string = e1.get()
# # #     try:
# # #         os.startfile(string)
# # #     except:
# # #         print('File not found')

# # # def open_window():
# # #     global e1
# # #     read = Tk()
# # #     Label(read, text="Enter File Location").grid(row = 1, column = 1)
# # #     e1 = Entry(read)
# # #     e1.grid(row  = 5, column = 1)
# # #     Button(read, text='Go', command=open_file).grid(row=7, column=1)
# # #     read.mainloop()

# # # def copy_file():
# # #     global source
# # #     global destination
# # #     source1 = source.get()
# # #     destination1 = destination.get()
# # #     shutil.copy(source1, destination1)

# # # def copy_window():
# # #     global source
# # #     global destination
# # #     copy = Tk()
# # #     Label(copy, text = "Enter the Source Location").grid(row = 1, column = 1)
# # #     Label(copy, text = "Enter the destination Location").grid(row = 4, column = 1)
# # #     source = Entry(copy)
# # #     source.grid(row = 1, column = 14)
# # #     destination = Entry(copy)
# # #     destination.grid(row = 4, column = 14)
# # #     Button(copy, text = 'Go', command = copy_file).grid(row = 7, column = 2)
# # #     copy.mainloop()

# # # def delete_file():
# # #     global deletefile
# # #     string = deletefile.get()
# # #     if os.path.exists(string):
# # #         os.remove(string)
# # #     else:
# # #         print('File not found')

# # # def delete_window():
# # #     global deletefile
# # #     delete = Tk()
# # #     Label(delete, text = "Enter the file Location").grid(row = 1, column = 1)
# # #     deletefile = Entry(delete)
# # #     deletefile.grid(row = 5, column = 1)
# # #     Button(delete, text = 'Go', command = delete_file).grid(row = 7, column = 1)
# # #     delete.mainloop()

# # # def list_file():
# # #     global listfile
# # #     string = listfile.get()
# # #     sortlist=sorted(os.listdir(string))
# # #     i=0
# # #     while(i<len(sortlist)):
# # #         print(sortlist[i]+'\n')
# # #         i+=1

# # # def list_window():
# # #     global listfile
# # #     listwindow = Tk()
# # #     Label(listwindow, text = "Enter the file Location").grid(row = 1, column = 1)
# # #     listfile = Entry(listwindow)
# # #     listfile.grid(row = 5, column = 1)
# # #     Button(listwindow, text = 'Go', command = list_file).grid(row = 7, column = 1)
# # #     listwindow.mainloop()

# # # def check_file():
# # #     global checkfile
# # #     string = checkfile.get()
# # #     if os.path.isfile(string)==True:
# # #         print('File Found')
# # #     else:
# # #         print('File not Found')

# # # def check_window():
# # #     global checkfile
# # #     checkwindow = Tk()
# # #     Label(checkwindow, text = "Enter the file Location").grid(row = 1, column = 1)
# # #     checkfile = Entry(checkwindow)
# # #     checkfile.grid(row = 5, column = 1)
# # #     Button(checkwindow, text = 'Go', command = check_file).grid(row = 7, column = 1)
# # #     checkwindow.mainloop()

# # # def rename_file():
# # #     global path1
# # #     global path2
# # #     string1 = path1.get()
# # #     string2 = path2.get()
# # #     shutil.move(string1, string2)

# # # def rename_window():
# # #     global path1
# # #     global path2
# # #     rename = Tk()
# # #     Label(rename, text = "Enter the Source Location").grid(row = 1, column = 1)
# # #     Label(rename, text = "Enter the destination Location").grid(row = 4, column = 1)
# # #     path1 = Entry(rename)
# # #     path1.grid(row = 1, column = 14)
# # #     path2 = Entry(rename)
# # #     path2.grid(row = 4, column = 14)
# # #     Button(rename, text = 'Go', command = rename_file).grid(row = 7, column = 2)
# # #     rename.mainloop()

# # # def check_folder():
# # #     global checkfolder
# # #     string = checkfolder.get()
# # #     if os.path.isdir(string)==True:
# # #         print('Folder Found')
# # #     else:
# # #         print('Folder Not Found')

# # # def checkfolder_window():
# # #     global checkfolder
# # #     checkfolderwindow = Tk()
# # #     Label(checkfolderwindow, text = "Enter the file Location").grid(row = 1, column = 1)
# # #     checkfolder = Entry(checkfolderwindow)
# # #     checkfolder.grid(row = 5, column = 1)
# # #     Button(checkfolderwindow, text = 'Go', command = check_folder).grid(row = 7, column = 1)
# # #     checkfolderwindow.mainloop()

# # # def make_folder():
# # #     global makefolder
# # #     string = makefolder.get()
# # #     os.makedirs(string)

# # # def make_window():
# # #     global makefolder
# # #     makewindow = Tk()
# # #     Label(makewindow, text = "Enter the file Location").grid(row = 1, column = 1)
# # #     makefolder = Entry(makewindow)
# # #     makefolder.grid(row = 5, column = 1)
# # #     Button(makewindow, text = 'Go', command = make_folder).grid(row = 7, column = 1)
# # #     makewindow.mainloop()

# # # def remove_folder():
# # #     global removefolder
# # #     string = removefolder.get()
# # #     os.rmdir(string)

# # # def remove_window():
# # #     global removefolder
# # #     removewindow = Tk()
# # #     Label(removewindow, text = "Enter the file Location").grid(row = 1, column = 1)
# # #     removefolder = Entry(removewindow)
# # #     removefolder.grid(row = 5, column = 1)
# # #     Button(removewindow, text = 'Go', command = remove_folder).grid(row = 7, column = 1)
# # #     removewindow.mainloop()

# # # #Tkinter UI
# # # root = Tk()
# # # Label(root, text="File Manager").grid(row = 5, column = 2)
# # # Button(root, text = "Open a File", command = open_window).grid(row=7, column =1)
# # # Button(root, text = "Copy a File", command = copy_window).grid(row = 7, column = 2)
# # # Button(root, text = "Delete a File", command = delete_window).grid(row = 7, column = 3)
# # # Button(root, text = "List all Files in Directory", command = list_window).grid(row = 7, column = 4)
# # # Button(root, text = "Check a File", command = check_window).grid(row = 7, column = 5)

# # # Button(root, text = "Rename a File", command = rename_window).grid(row = 19, column = 1)
# # # Button(root, text = "Check Folder", command = checkfolder_window).grid(row = 19, column = 2)
# # # Button(root, text = "Move a File", command = rename_window).grid(row = 19, column =3)
# # # Button(root, text = "Make a Folder", command = make_window).grid(row = 19, column = 4)
# # # Button(root, text = "Remove a Folder", command = remove_window).grid(row = 19, column = 5)

# # # root.mainloop()
















#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # =============================================================================
# """Module Built to To Read ID3 Track Data."""
# # File Name: track_meta_id3.py
# # =============================================================================
# import time
# from os import path

# from eyed3 import id3
# from eyed3 import load


# current_home = path.expanduser('~')
# search_dir = path.join(current_home + "/Music/iTunes/iTunes Media/Music/Rush/Chronicles (Disc 2)/2-03 Limelight.mp3")  # noqa


# def track_info(self):
#     """Module Built To Read ID3 Track Data."""
#     tag = id3.Tag()
#     tag.parse(filename)
#     a = load(filename)
#     print("# {}".format('=' * 78))
#     print("Track Name:     {}".format(tag.title))
#     print("Track Artist:   {}".format(tag.artist))
#     print("Track Album:    {}".format(tag.album))
#     print("Track Duration: {}".format(duration_from_seconds(a.info.time_secs)))
#     print("Track Number:   {}".format(tag.track_num))
#     print("Track BitRate:  {}".format(a.info.bit_rate))
#     print("Track BitRate:  {}".format(a.info.bit_rate_str))
#     print("Sample Rate:    {}".format(a.info.sample_freq))
#     print("Mode:           {}".format(a.info.mode))
#     print("# {}".format('=' * 78))
#     print("Album Artist:         {}".format(tag.album_artist))
#     print("Album Year:           {}".format(tag.getBestDate()))
#     print("Album Recording Date: {}".format(tag.recording_date))
#     print("Album Type:           {}".format(tag.album_type))
#     print("Disc Num:             {}".format(tag.disc_num))
#     print("Artist Origin:        {}".format(tag.artist_origin))
#     print("# {}".format('=' * 78))
#     print("Artist URL:         {}".format(tag.artist_url))
#     print("Audio File URL:     {}".format(tag.audio_file_url))
#     print("Audio Source URL:   {}".format(tag.audio_source_url))
#     print("Commercial URL:     {}".format(tag.commercial_url))
#     print("Copyright URL:      {}".format(tag.copyright_url))
#     print("Internet Radio URL: {}".format(tag.internet_radio_url))
#     print("Publisher URL:      {}".format(tag.publisher_url))
#     print("Payment URL:        {}".format(tag.payment_url))
#     print("# {}".format('=' * 78))
#     print("Publisher: {}".format(tag.publisher))
#     print("Original Release Date: {}".format(tag.original_release_date))
#     print("Play Count: {}".format(tag.play_count))
#     print("Tagging Date: {}".format(tag.tagging_date))
#     print("Release Date: {}".format(tag.release_date))
#     print("Terms Of Use: {}".format(tag.terms_of_use))
#     print("isV1: {}".format(tag.isV1()))
#     print("isV2: {}".format(tag.isV2()))
#     print("BPM: {}".format(tag.bpm))
#     print("Cd Id: {}".format(tag.cd_id))
#     print("Composer: {}".format(tag.composer))
#     print("Encoding date: {}".format(tag.encoding_date))
#     print("# {}".format('=' * 78))
#     print("Genre: {}".format(tag.genre.name))
#     print("Non Std Genre Name: {}".format(tag.non_std_genre.name))
#     print("Genre ID: {}".format(tag.genre.id))
#     print("Non Std Genre ID: {}".format(tag.non_std_genre.id))
#     print("LAME Tag:       {}".format(a.info.lame_tag))
#     print("# {}".format('=' * 78))
#     print("Header Version: {}".format(tag.header.version))
#     print("Header Major Version: {}".format(tag.header.major_version))
#     print("Header Minor Version: {}".format(tag.header.minor_version))
#     print("Header Rev Version: {}".format(tag.header.rev_version))
#     print("Header Extended: {}".format(tag.header.extended))
#     print("Header Footer: {}".format(tag.header.footer))
#     print("Header Experimental: {}".format(tag.header.experimental))
#     print("Header SIZE: {}".format(tag.header.SIZE))
#     print("Header Tag Size: {}".format(tag.header.tag_size))
#     print("Extended Header Size: {}".format(tag.extended_header.size))
#     print("# {}".format('=' * 78))
#     print("File Name: {}".format(tag.file_info.name))
#     print("File Tag Size: {}".format(tag.file_info.tag_size))
#     print("File Tag Padding Size: {}".format(tag.file_info.tag_padding_size))
#     print("File Read Only: {}".format(tag.read_only))
#     print("File Size: {}".format(a.info.size_bytes))
#     print("Last Modified: {}".format(time.strftime('%Y-%m-%d %H:%M:%S',
#                                      time.localtime(tag.file_info.mtime))))
#     print("Last Accessed: {}".format(time.strftime('%Y-%m-%d %H:%M:%S',
#                                      time.localtime(tag.file_info.atime))))
#     print("# {}".format('=' * 78))


# def duration_from_seconds(s):
#     """Module to get the convert Seconds to a time like format."""
#     s = s
#     m, s = divmod(s, 60)
#     h, m = divmod(m, 60)
#     d, h = divmod(h, 24)
#     timelapsed = "{:01d}:{:02d}:{:02d}:{:02d}".format(int(d),
#                                                       int(h),
#                                                       int(m),
#                                                       int(s))
#     return timelapsed


# track_info(search_dir)

# # $ python3 ~/Desktop/track_meta_id3.py
# # # ===========================================================================
# # Track Name:     Limelight
# # Track Artist:   Rush
# # Track Album:    Chronicles (Disc 2)
# # Track Duration: 0:00:04:22
# # Track Number:   (3, 14)
# # Track BitRate:  (False, 320)
# # Track BitRate:  320 kb/s
# # Sample Rate:    44100
# # Mode:           Stereo
# # # ===========================================================================
# # Album Artist:         None
# # Album Year:           1990
# # Album Recording Date: 1990
# # Album Type:           None
# # Disc Num:             (2, 2)
# # Artist Origin:        [None, None, None]
# # # ===========================================================================
# # Artist URL:         None
# # Audio File URL:     None
# # Audio Source URL:   None
# # Commercial URL:     None
# # Copyright URL:      None
# # Internet Radio URL: None
# # Publisher URL:      None
# # Payment URL:        None
# # # ===========================================================================
# # Publisher: None
# # Original Release Date: None
# # Play Count: None
# # Tagging Date: None
# # Release Date: None
# # Terms Of Use: None
# # isV1: False
# # isV2: True
# # BPM: 0
# # Cd Id: None
# # Composer: Lee/Lifeson/Peart
# # Encoding date: None
# # # ===========================================================================
# # Genre: Rock
# # Non Std Genre Name: Rock
# # Genre ID: 17
# # Non Std Genre ID: 17
# # LAME Tag:       {}
# # # ===========================================================================
# # Header Version: (2, 3, 0)
# # Header Major Version: 2
# # Header Minor Version: 3
# # Header Rev Version: 0
# # Header Extended: False
# # Header Footer: False
# # Header Experimental: False
# # Header SIZE: 10
# # Header Tag Size: 56574
# # Extended Header Size: 0
# # # ===========================================================================
# # File Name: ~/Music/iTunes/iTunes/Music/Rush/Chronicles/2-03 Limelight.mp3
# # File Tag Size: 56584
# # File Tag Padding Size: 1024
# # File Read Only: False
# # File Size: 10545396
# # Last Modified: 2019-08-29 14:33:51
# # Last Accessed: 2019-09-05 15:44:19
# # # ===========================================================================
# """PlaceHolder."""
# import re

# from os import path as ospath

# from eyed3 import id3

# current_home = ospath.expanduser('~')
# file_path = ospath.join(current_home,
#                         'Music',
#                         'iTunes',
#                         'iTunes Media',
#                         'Music',
#                         'Aerosmith',
#                         'Big Ones',
#                         '01 Walk On Water.mp3',
#                         )


# def read_id3_artist(audio_file):
#     """Module to read MP3 Meta Tags.

#     Accepts Path like object only.
#     """
#     filename = audio_file
#     tag = id3.Tag()
#     tag.parse(filename)
#     # =========================================================================
#     # Set Variables
#     # =========================================================================
#     artist = tag.artist
#     title = tag.title
#     track_path = tag.file_info.name
#     # =========================================================================
#     # Check Variables Values & Encode Them and substitute back-ticks
#     # =========================================================================
#     if artist is not None:
#         artist.encode()
#         artistz = re.sub(u'`', u"'", artist)
#     else:
#         artistz = 'Not Listed'
#     if title is not None:
#         title.encode()
#         titlez = re.sub(u'`', u"'", title)
#     else:
#         titlez = 'Not Listed'
#     if track_path is not None:
#         track_path.encode()
#         track_pathz = re.sub(u'`', u"'", track_path)
#     else:
#         track_pathz = ('Not Listed, and you have an the worst luck, '
#                        'because this is/should not possible.')
#     # =========================================================================
#     # print them out
#     # =========================================================================
#     try:
#         if artist is not None and title is not None and track_path is not None:
#             print('Artist: "{}"'.format(artistz))
#             print('Track : "{}"'.format(titlez))
#             print('Path  : "{}"'.format(track_pathz))
#     except Exception as e:
#         raise e


# read_id3_artist(file_path)

# # Show Case:
# # Artist: "Aerosmith"
# # Track : "Walk On Water"
# # Path  : "/Users/MyUserName/Music/iTunes/iTunes Media/Music/Aerosmith/Big Ones/01 Walk On Water.mp3"  # noqa


  # audio.add(frames.TALB(text=metadata['album']))
  #   # audio.add(TPOS(text=metadata['disc'])) # I want the series, but audio players want an integer. put off for now
  #   audio.add(frames.TDRC(text=[ ID3TimeStamp(str(metadata['year'])) ]))
  #   audio.add(frames.TRCK(text=str(metadata['track']))) # useless since there's no discs, I'll keep anyways.
  #   audio.add(frames.TIT2(text=metadata['title']))
  #   # audio.add(TPE2(text=metadata['artists'])) # ID3 is not made for singers, doesn't have a tag (TPE1 and TPE2 are wrong)
  #   audio.add(frames.TXXX(text=metadata['series'],desc='series'))
  #   audio.add(frames.TXXX(text=metadata['themetype'],desc='themetype'))
  #   audio.add(frames.TXXX(text=str(metadata['version']),desc='version'))
  #   audio.add(frames.TXXX(text=str(metadata['videoid']),desc='videoid'))
  #   audio.add(frames.TXXX(text=metadata['notes'],desc='notes'))
  #   audio.add(frames.TCON(text=metadata['genre']))
  #   audio.add(frames.TENC(text=metadata['encodedby']))
  #   audio.add(frames.TIT1(text=metadata['cgroup']))
  #   audio.save(v2_version=OPTIONS['id3v2_version'])

# [acoustid_fingerprint, acoustid_id, album, albumartist, albumartistsort, albumsort, arranger, artist, artistsort, asin, author, barcode, bpm, catalognumber, compilation, composer, composersort, conductor, copyright, date, discnumber, discsubtitle, encodedby, genre, isrc, language, length, lyricist, media, mood, musicbrainz_albumartistid, musicbrainz_albumid, musicbrainz_albumstatus, musicbrainz_albumtype, musicbrainz_artistid, musicbrainz_discid, musicbrainz_releasegroupid, musicbrainz_releasetrackid, musicbrainz_trackid, musicbrainz_trmid, musicbrainz_workid, musicip_fingerprint, musicip_puid, organization, originaldate, performer, performer:*, releasecountry, replaygain_*_gain, replaygain_*_peak, title, titlesort, tracknumber, version, website]
#
# /Music/Compilations/Album Name/1-01 Angels (Explicit)  TITLE.mp4

# https://programtalk.com/vs4/python/10712/mutagen/tests/test_easymp4.py/
# # -*- coding: utf-8 -*-

# import os

# from mutagen import MutagenError
# from mutagen.easymp4 import EasyMP4, error as MP4Error

# from tests import TestCase, DATA_DIR, get_temp_copy


# clast TEasyMP4(TestCase):

#     def setUp(self):
#         self.filename = get_temp_copy(os.path.join(DATA_DIR, 'has-tags.m4a'))
#         self.mp4 = EasyMP4(self.filename)
#         self.mp4.delete()

#     def tearDown(self):
#         os.unlink(self.filename)

#     def test_pprint(self):
#         self.mp4["artist"] = "baz"
#         self.mp4.pprint()

#     def test_has_key(self):
#         self.failIf("foo" in self.mp4)

#     def test_empty_file(self):
#         empty = os.path.join(DATA_DIR, 'emptyfile.mp3')
#         self.astertRaises(MP4Error, EasyMP4, filename=empty)

#     def test_nonexistent_file(self):
#         empty = os.path.join(DATA_DIR, 'does', 'not', 'exist')
#         self.astertRaises(MutagenError, EasyMP4, filename=empty)

#     def test_write_single(self):
#         for key in EasyMP4.Get:
#             if key in ["tracknumber", "discnumber", "date", "bpm"]:
#                 continue

#             # Test creation
#             self.mp4[key] = "a test value"
#             self.mp4.save(self.filename)
#             mp4 = EasyMP4(self.filename)
#             self.failUnlessEqual(mp4[key], ["a test value"])
#             self.failUnlessEqual(mp4.keys(), [key])

#             # And non-creation setting.
#             self.mp4[key] = "a test value"
#             self.mp4.save(self.filename)
#             mp4 = EasyMP4(self.filename)
#             self.failUnlessEqual(mp4[key], ["a test value"])
#             self.failUnlessEqual(mp4.keys(), [key])

#             del(self.mp4[key])

#     def test_write_double(self):
#         for key in EasyMP4.Get:
#             if key in ["tracknumber", "discnumber", "date", "bpm"]:
#                 continue

#             self.mp4[key] = ["a test", "value"]
#             self.mp4.save(self.filename)
#             mp4 = EasyMP4(self.filename)
#             self.failUnlessEqual(mp4.get(key), ["a test", "value"])
#             self.failUnlessEqual(mp4.keys(), [key])

#             self.mp4[key] = ["a test", "value"]
#             self.mp4.save(self.filename)
#             mp4 = EasyMP4(self.filename)
#             self.failUnlessEqual(mp4.get(key), ["a test", "value"])
#             self.failUnlessEqual(mp4.keys(), [key])

#             del(self.mp4[key])

#     def test_write_date(self):
#         self.mp4["date"] = "2004"
#         self.mp4.save(self.filename)
#         mp4 = EasyMP4(self.filename)
#         self.failUnlessEqual(mp4["date"], ["2004"])

#         self.mp4["date"] = "2004"
#         self.mp4.save(self.filename)
#         mp4 = EasyMP4(self.filename)
#         self.failUnlessEqual(mp4["date"], ["2004"])

#     def test_date_delete(self):
#         self.mp4["date"] = "2004"
#         self.failUnlessEqual(self.mp4["date"], ["2004"])
#         del(self.mp4["date"])
#         self.failIf("date" in self.mp4)

#     def test_write_date_double(self):
#         self.mp4["date"] = ["2004", "2005"]
#         self.mp4.save(self.filename)
#         mp4 = EasyMP4(self.filename)
#         self.failUnlessEqual(mp4["date"], ["2004", "2005"])

#         self.mp4["date"] = ["2004", "2005"]
#         self.mp4.save(self.filename)
#         mp4 = EasyMP4(self.filename)
#         self.failUnlessEqual(mp4["date"], ["2004", "2005"])

#     def test_write_invalid(self):
#         self.failUnlessRaises(ValueError, self.mp4.__gesatem__, "notvalid")
#         self.failUnlessRaises(ValueError, self.mp4.__delitem__, "notvalid")
#         self.failUnlessRaises(
#             ValueError, self.mp4.__sesatem__, "notvalid", "tests")

#     def test_numeric(self):
#         for tag in ["bpm"]:
#             self.mp4[tag] = "3"
#             self.failUnlessEqual(self.mp4[tag], ["3"])
#             self.mp4.save()
#             mp4 = EasyMP4(self.filename)
#             self.failUnlessEqual(mp4[tag], ["3"])

#             del(mp4[tag])
#             self.failIf(tag in mp4)
#             self.failUnlessRaises(KeyError, mp4.__delitem__, tag)

#             self.failUnlessRaises(
#                 ValueError, self.mp4.__sesatem__, tag, "hello")

#     def test_numeric_pairs(self):
#         for tag in ["tracknumber", "discnumber"]:
#             self.mp4[tag] = "3"
#             self.failUnlessEqual(self.mp4[tag], ["3"])
#             self.mp4.save()
#             mp4 = EasyMP4(self.filename)
#             self.failUnlessEqual(mp4[tag], ["3"])

#             del(mp4[tag])
#             self.failIf(tag in mp4)
#             self.failUnlessRaises(KeyError, mp4.__delitem__, tag)

#             self.mp4[tag] = "3/10"
#             self.failUnlessEqual(self.mp4[tag], ["3/10"])
#             self.mp4.save()
#             mp4 = EasyMP4(self.filename)
#             self.failUnlessEqual(mp4[tag], ["3/10"])

#             del(mp4[tag])
#             self.failIf(tag in mp4)
#             self.failUnlessRaises(KeyError, mp4.__delitem__, tag)

#             self.failUnlessRaises(
#                 ValueError, self.mp4.__sesatem__, tag, "hello")

        # if self.filetype == 'mp3':
        #     import mutagen.mp3 as meta_parser
        # elif self.filetype == 'ogg':
        #     import mutagen.oggvorbis as meta_parser
        # elif self.filetype == 'opus':
        #     import mutagen.oggopus as meta_parser
        # elif self.filetype == 'flac':
        #     import mutagen.flac as meta_parser
        # elif self.filetype in ['mp4', 'm4a']:
        #     import mutagen.mp4 as meta_parser
        # else:
        #     self.__log.info(
        #         'Extracting metadata not supported for %s files.', self.filetype )
        #     return False














#   if malid is not None and OPTIONS['coverart']['folder']:
#       coverart,desc,mimetype = get_coverart(metadata,malid)
#       audio.add(frames.APIC(encoding=3,mime=mimetype,desc=desc,type=3,data=coverart))

# Remove old 'APIC' frame
# Because two 'APIC' may exist together with the different description
# For more information visit: http://mutagen.readthedocs.io/en/latest/user/id3.html
# if id3.getall('APIC'): id3.delall('APIC')


# id3.add(APIC(encoding=3, mime=u'image/jpg', type=3, desc=u'Front Cover', data=self.get_cover(info)))

