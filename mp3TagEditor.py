#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : jkirchoff
# Created Date: Tue Sep 26 19:10:53 2022 CDT
# Last ModDate: Tue Sep 27 17:50:01 2022 CDT
# =============================================================================
import functools  # Reduce - Required for ID3 Header Checks
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError  # Required for catching errors when no ID3 tag exists on the file.
from mutagen.id3 import Encoding  # Required for SYLT SYNC'D Lyrics
from mutagen.id3 import AENC as _AENC # AENC [ Supported Version: 4.20 ] # id3.AENC(owner='', preview_start=0, preview_length=0, data='')
from mutagen.id3 import APIC as _APIC  # APIC [ Supported Version: 4.20 ] # Attached (or linked) Picture. id3.add(_APIC(encoding=3, mime=u'image/jpeg', type=3, desc=u'Front Cover', data=self.get_cover(info)))  Example2# id3.add(_APIC(encoding=3, mime=u'image/jpg', type=3, desc=u'Cover', data=self.get_cover(info['album_pic_url'])))
from mutagen.id3 import ASPI as _ASPI  # ASPI [ Supported Version: 2.00 ] # Audio seek point index. Attributes: S, L, N, b, and Fi. For the meaning of these, see the ID3v2.4 specification. Fi is a list of integers.
from mutagen.id3 import CHAP as _CHAP  # CHAP [ Supported Version: 2.00 ] # Chapter propertyHashKey An internal key used to ensure frame uniqueness in a tag
from mutagen.id3 import COMM as _COMM  # COMM [ Supported Version: 4.11 ] # Comments
from mutagen.id3 import COMR as _COMR  # COMR [ Supported Version: 4.25 ] # Commercial frame
from mutagen.id3 import CTOC as _CTOC  # CTOC [ Supported Version: 2.00 ] # Table of contents propertyHashKey An internal key used to ensure frame uniqueness in a tag
from mutagen.id3 import ENCR as _ENCR  # ENCR [ Supported Version: 4.26 ] # Encryption method registration
from mutagen.id3 import EQU2 as _EQU2  # EQU2 [ Supported Version: 2.00 ] # Equalisation (2).  Attributes: method - interpolation method (0 = band, 1 = linear) desc - identifying description adjustments - list of (frequency, vol_adjustment) pairs
from mutagen.id3 import ETCO as _ETCO  # ETCO [ Supported Version: 4.06 ] # Event timing codes
from mutagen.id3 import GEOB as _GEOB  # GEOB [ Supported Version: 4.16 ] # General encapsulated object
from mutagen.id3 import GRID as _GRID  # GRID [ Supported Version: 4.27 ] # Group identification registration
from mutagen.id3 import IPLS as _IPLS  # IPLS [ Supported Version: 4.04 ] # Involved people list
from mutagen.id3 import LINK as _LINK  # LINK [ Supported Version: 4.21 ] # Linked information
from mutagen.id3 import MCDI as _MCDI  # MCDI [ Supported Version: 4.05 ] # Music CD identifier
from mutagen.id3 import MLLT as _MLLT  # MLLT [ Supported Version: 4.07 ] # MPEG location lookup table
from mutagen.id3 import MVIN as _MVIN  # MVIN [ Supported Version: 2.00 ] # iTunes Movement Number/Count
from mutagen.id3 import MVNM as _MVNM  # MVNM [ Supported Version: 2.00 ] # iTunes Movement Name
from mutagen.id3 import OWNE as _OWNE  # OWNE [ Supported Version: 4.24 ] # Ownership frame
from mutagen.id3 import PCNT as _PCNT  # PCNT [ Supported Version: 4.17 ] # Play counter
from mutagen.id3 import PCST as _PCST  # PCST [ Supported Version: 2.00 ] # iTunes Podcast Flag
from mutagen.id3 import POPM as _POPM  # POPM [ Supported Version: 4.18 ] # Popularimeter
from mutagen.id3 import POSS as _POSS  # POSS [ Supported Version: 4.22 ] # Position synchronization frame
from mutagen.id3 import PRIV as _PRIV  # PRIV [ Supported Version: 4.28 ] # Private frame
from mutagen.id3 import RBUF as _RBUF  # RBUF [ Supported Version: 4.19 ] # Recommended buffer size
from mutagen.id3 import RVA2 as _RVA2  # RVA2 [ Supported Version: 2.00 ] # Relative volume adjustment (2)
from mutagen.id3 import RVAD as _RVAD  # RVAD [ Supported Version: 4.12 ] # Relative volume adjustment
from mutagen.id3 import RVRB as _RVRB  # RVRB [ Supported Version: 4.14 ] # Reverb
from mutagen.id3 import SEEK as _SEEK  # SEEK [ Supported Version: 2.00 ] # Seek frame.
from mutagen.id3 import SIGN as _SIGN  # SIGN [ Supported Version: 2.00 ] # Signature frame.
from mutagen.id3 import SYLT as _SYLT  # SYLT [ Supported Version: 4.10 ] # Synchronized lyric/text
from mutagen.id3 import SYTC as _SYTC  # SYTC [ Supported Version: 4.08 ] # Synchronized tempo codes
from mutagen.id3 import TALB as _TALB  # TALB [ Supported Version: 2.00 ] # Album/Movie/Show title
from mutagen.id3 import TBPM as _TBPM  # TBPM [ Supported Version: 2.00 ] # BPM (beats per minute)
from mutagen.id3 import TCAT as _TCAT  # TCAT [ Supported Version: 2.00 ] # iTunes Podcast Category
from mutagen.id3 import TCMP as _TCMP  # TCMP [ Supported Version: 2.00 ] # iTunes Compilation Flag
from mutagen.id3 import TCOM as _TCOM  # TCOM [ Supported Version: 2.00 ] # Composer
from mutagen.id3 import TCON as _TCON  # TCON [ Supported Version: 2.00 ] # Content type
from mutagen.id3 import TCOP as _TCOP  # TCOP [ Supported Version: 2.00 ] # Copyright message
from mutagen.id3 import TDAT as _TDAT  # TDAT [ Supported Version: 2.00 ] # Date
from mutagen.id3 import TDEN as _TDEN  # TDEN [ Supported Version: 2.00 ] # Encoding Time
from mutagen.id3 import TDES as _TDES  # TDES [ Supported Version: 2.00 ] # iTunes Podcast Description
from mutagen.id3 import TDLY as _TDLY  # TDLY [ Supported Version: 2.00 ] # Playlist delay
from mutagen.id3 import TDOR as _TDOR  # TDOR [ Supported Version: 2.00 ] # Original Release Time
from mutagen.id3 import TDRC as _TDRC  # TDRC [ Supported Version: 2.00 ] # Recording Time
from mutagen.id3 import TDRL as _TDRL  # TDRL [ Supported Version: 2.00 ] # Release Time
from mutagen.id3 import TDTG as _TDTG  # TDTG [ Supported Version: 2.00 ] # Tagging Time
from mutagen.id3 import TENC as _TENC  # TENC [ Supported Version: 2.00 ] # Encoded by
from mutagen.id3 import TEXT as _TEXT  # TEXT [ Supported Version: 2.00 ] # Lyricist/Text writer
from mutagen.id3 import TFLT as _TFLT  # TFLT [ Supported Version: 2.00 ] # File type
from mutagen.id3 import TGID as _TGID  # TGID [ Supported Version: 2.00 ] # iTunes Podcast Identifier
from mutagen.id3 import TIME as _TIME  # TIME [ Supported Version: 2.00 ] # Time
from mutagen.id3 import TIPL as _TIPL  # TIPL [ Supported Version: 2.00 ] # Involved People List
from mutagen.id3 import TIT1 as _TIT1  # TIT1 [ Supported Version: 2.00 ] # Content group description
from mutagen.id3 import TIT2 as _TIT2  # TIT2 [ Supported Version: 2.00 ] # Title/songname/content description
from mutagen.id3 import TIT3 as _TIT3  # TIT3 [ Supported Version: 2.00 ] # Subtitle/Description refinement
from mutagen.id3 import TKEY as _TKEY  # TKEY [ Supported Version: 2.00 ] # Initial key
from mutagen.id3 import TKWD as _TKWD  # TKWD [ Supported Version: 2.00 ] # iTunes Podcast Keywords
from mutagen.id3 import TLAN as _TLAN  # TLAN [ Supported Version: 2.00 ] # Language(s)
from mutagen.id3 import TLEN as _TLEN  # TLEN [ Supported Version: 2.00 ] # Length
from mutagen.id3 import TMCL as _TMCL  # TMCL [ Supported Version: 2.00 ] # Musicians Credits List
from mutagen.id3 import TMED as _TMED  # TMED [ Supported Version: 2.00 ] # Media type
from mutagen.id3 import TMOO as _TMOO  # TMOO [ Supported Version: 2.00 ] # Mood
from mutagen.id3 import TOAL as _TOAL  # TOAL [ Supported Version: 2.00 ] # Original album/movie/show title
from mutagen.id3 import TOFN as _TOFN  # TOFN [ Supported Version: 2.00 ] # Original filename
from mutagen.id3 import TOLY as _TOLY  # TOLY [ Supported Version: 2.00 ] # Original lyricist(s)/text writer(s)
from mutagen.id3 import TOPE as _TOPE  # TOPE [ Supported Version: 2.00 ] # Original artist(s)/performer(s)
from mutagen.id3 import TORY as _TORY  # TORY [ Supported Version: 2.00 ] # Original release year
from mutagen.id3 import TOWN as _TOWN  # TOWN [ Supported Version: 2.00 ] # File owner/licensee
from mutagen.id3 import TPE1 as _TPE1  # TPE1 [ Supported Version: 2.00 ] # Lead performer(s)/Soloist(s)
from mutagen.id3 import TPE2 as _TPE2  # TPE2 [ Supported Version: 2.00 ] # Band/orchestra/accompaniment
from mutagen.id3 import TPE3 as _TPE3  # TPE3 [ Supported Version: 2.00 ] # Conductor/performer refinement
from mutagen.id3 import TPE4 as _TPE4  # TPE4 [ Supported Version: 2.00 ] # Interpreted, remixed, or otherwise modified by
from mutagen.id3 import TPOS as _TPOS  # TPOS [ Supported Version: 2.00 ] # Part of a set
from mutagen.id3 import TPRO as _TPRO  # TPRO [ Supported Version: 2.00 ] # Produced (P)
from mutagen.id3 import TPUB as _TPUB  # TPUB [ Supported Version: 2.00 ] # Publisher
from mutagen.id3 import TRCK as _TRCK  # TRCK [ Supported Version: 2.00 ] # Track number/Position in set
from mutagen.id3 import TRDA as _TRDA  # TRDA [ Supported Version: 2.00 ] # Recording dates
from mutagen.id3 import TRSN as _TRSN  # TRSN [ Supported Version: 2.00 ] # Internet radio station name
from mutagen.id3 import TRSO as _TRSO  # TRSO [ Supported Version: 2.00 ] # Internet radio station owner
from mutagen.id3 import TSIZ as _TSIZ  # TSIZ [ Supported Version: 2.00 ] # Size
from mutagen.id3 import TSO2 as _TSO2  # TSO2 [ Supported Version: 2.00 ] # iTunes Album Artist Sort
from mutagen.id3 import TSOA as _TSOA  # TSOA [ Supported Version: 2.00 ] # Album Sort Order key
from mutagen.id3 import TSOC as _TSOC  # TSOC [ Supported Version: 2.00 ] # iTunes Composer Sort
from mutagen.id3 import TSOP as _TSOP  # TSOP [ Supported Version: 2.00 ] # Perfomer Sort Order key
from mutagen.id3 import TSOT as _TSOT  # TSOT [ Supported Version: 2.00 ] # Title Sort Order key
from mutagen.id3 import TSRC as _TSRC  # TSRC [ Supported Version: 2.00 ] # ISRC (international standard recording code)
from mutagen.id3 import TSSE as _TSSE  # TSSE [ Supported Version: 2.00 ] # Software/Hardware and settings used for encoding
from mutagen.id3 import TSST as _TSST  # TSST [ Supported Version: 2.00 ] # Set Subtitle
from mutagen.id3 import TXXX as _TXXX  # TXXX [ Supported Version: 2.00 ] # User defined text information frame
from mutagen.id3 import TYER as _TYER  # TYER [ Supported Version: 2.00 ] # Year
from mutagen.id3 import UFID as _UFID  # UFID [ Supported Version: 4.01 ] # Unique file identifier
from mutagen.id3 import USER as _USER  # USER [ Supported Version: 4.23 ] # Terms of use
from mutagen.id3 import USLT as _USLT  # USLT [ Supported Version: 4.09 ] # UnSychronized lyric/text transcription
from mutagen.id3 import WCOM as _WCOM  # WCOM [ Supported Version: 2.00 ] # Commercial information
from mutagen.id3 import WCOP as _WCOP  # WCOP [ Supported Version: 2.00 ] # Copyright/Legal information
from mutagen.id3 import GRP1 as _GRP1  # GRP1 [ Supported Version: 2.00 ] # iTunes Grouping
from mutagen.id3 import WFED as _WFED  # WFED [ Supported Version: 2.00 ] # iTunes Podcast Feed
from mutagen.id3 import WOAF as _WOAF  # WOAF [ Supported Version: 2.00 ] # Official audio file webpage
from mutagen.id3 import WOAR as _WOAR  # WOAR [ Supported Version: 2.00 ] # Official artist/performer webpage
from mutagen.id3 import WOAS as _WOAS  # WOAS [ Supported Version: 2.00 ] # Official audio source webpage
from mutagen.id3 import WORS as _WORS  # WORS [ Supported Version: 2.00 ] # Official internet radio station homepage
from mutagen.id3 import WPAY as _WPAY  # WPAY [ Supported Version: 2.00 ] # Payment
from mutagen.id3 import WPUB as _WPUB  # WPUB [ Supported Version: 2.00 ] # Publishers official webpage
from mutagen.id3 import WXXX as _WXXX  # WXXX [ Supported Version: 2.00 ] # User defined URL link frame

from mutagen.id3 import BUF
from mutagen.id3 import CNT
from mutagen.id3 import COM
from mutagen.id3 import CRA
from mutagen.id3 import CRM
from mutagen.id3 import ETC
from mutagen.id3 import GEO
from mutagen.id3 import GP1
from mutagen.id3 import ID3
from mutagen.id3 import IPL
from mutagen.id3 import LNK
from mutagen.id3 import MCI
from mutagen.id3 import MLL
from mutagen.id3 import MVI
from mutagen.id3 import MVN
from mutagen.id3 import PIC
from mutagen.id3 import POP
from mutagen.id3 import REV
from mutagen.id3 import RVA
from mutagen.id3 import SLT
from mutagen.id3 import STC
from mutagen.id3 import TAL
from mutagen.id3 import TBP
from mutagen.id3 import TCM
from mutagen.id3 import TCO
from mutagen.id3 import TCP
from mutagen.id3 import TCR
from mutagen.id3 import TDA
from mutagen.id3 import TDY
from mutagen.id3 import TEN
from mutagen.id3 import TFT
from mutagen.id3 import TIM
from mutagen.id3 import TKE
from mutagen.id3 import TLA
from mutagen.id3 import TLE
from mutagen.id3 import TMT
from mutagen.id3 import TOA
from mutagen.id3 import TOF
from mutagen.id3 import TOL
from mutagen.id3 import TOR
from mutagen.id3 import TOT
from mutagen.id3 import TP1
from mutagen.id3 import TP2
from mutagen.id3 import TP3
from mutagen.id3 import TP4
from mutagen.id3 import TPA
from mutagen.id3 import TPB
from mutagen.id3 import TRC
from mutagen.id3 import TRD
from mutagen.id3 import TRK
from mutagen.id3 import TS2
from mutagen.id3 import TSA
from mutagen.id3 import TSC
from mutagen.id3 import TSI
from mutagen.id3 import TSP
from mutagen.id3 import TSS
from mutagen.id3 import TST
from mutagen.id3 import TT1
from mutagen.id3 import TT2
from mutagen.id3 import TT3
from mutagen.id3 import TXT
from mutagen.id3 import TXX
from mutagen.id3 import TYE
from mutagen.id3 import UFI
from mutagen.id3 import ULT
from mutagen.id3 import WAF
from mutagen.id3 import WAR
from mutagen.id3 import WAS
from mutagen.id3 import WCM
from mutagen.id3 import WCP
from mutagen.id3 import WPB
from mutagen.id3 import WXX

# =====================================================================================================================
# Four Character Imports
# https://pypi.org/project/mutagen/1.45.1/
# https://mutagen.readthedocs.io/en/latest/changelog.html
# https://mutagen.readthedocs.io/en/latest/api/id3_frames.html?highlight=Group%20identification%20registration
# =============================================================================
# Notes:
# TODO: Share here when done  & https://stackoverflow.com/q/18248200/1896134
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
        self.checkFileTag   = ''
        self.SongArtistName = ''
        self.SongAlbumName  = ''
        self.SongTitleName  = ''
        self.SongPlayCount  = 0
        self.SongSyncLyrcs  = ''
        self.SongPlainLyrcs = ''
        self.SongDuration   = 0
        self.MP3HNDLR       = self.SetMP3Handle()
        self.ID3HNDLR       = self.SetID3Handle()
        self.startFiredUp()

    # =====================================================================================================================
    # Tag Checkers
    # =====================================================================================================================
    def startFiredUp(self):
        self.SongArtistName = self.getSongArtist()
        self.SongAlbumName = self.getSongAlbum()
        self.SongTitleName = self.getSongTitle()
        self.SongPlayCount = self.getSongPlayCount()
        self.SongSyncLyrcs = self.getSongSyncedLyrics()
        self.SongPlainLyrcs = self.getSongUnSyncedLyrics()
        self.SongDuration = self.getSongDuration()


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
                # print(data)
            # print header data check
            with open(self.songpath, 'rb') as a:
                if data[0:3] != b'ID3':
                    print('No ID3 header present in file.')
                else:
                    size_encoded = bytearray(data[-4:])
                    size = functools.reduce(lambda a, b: (a * 128 + b), size_encoded, 0)
                    # print(size)
        except Exception as e:
            print(f"Error: {e}")


    def convertID3Tags2to3(self):
        """Update The ID3 Tags In The Files."""
        try:
            self.ID3HNDLR.update_to_v24()
            self.ID3HNDLR.save(v1=2, v2_version=4, v23_sep='/')
        except Exception as e:
            print(f"Error: {e}")


    def duration_from_seconds(self, s):
        """Module to get the convert Seconds to a time like format."""
        s = s
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        TIMELAPSED  = f"{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}"
        return TIMELAPSED


    # =====================================================================================================================
    # Tag Delete ALL
    # =====================================================================================================================


    def deleteAllTags(self):
        """Remove All ID3 Tags From A File Including The ID3 Header."""
        self.ID3HNDLR.delete(self.songpath)
        self.ID3HNDLR.save()
        return

    # =====================================================================================================================
    # Getters
    # =====================================================================================================================
    def getOneSongToEdit(self):
        """JayRizzo Music Song Meta Mixer."""
        self.songpath = askopenfilename(initialdir=f"{self.CWDIR}/Music/",
                                        title="Choose A Song:",
                                        filetypes=[("MP3", "*.mp3"),
                                                   ("AAC Audio Files", "*.aac"),
                                                   ("AIFF Audio Files", "*.aiff"),
                                                   ("MPEG Audio Files", "*.mpeg"),
                                                   ("Protected Audio Files", "*.m4a"),
                                                   ("all", "*.*")])
        return self.songpath


    def getSongTitle(self):
        """Show Song Song Name/Title."""
        try:
            self.SongTitleName = f"{self.ID3HNDLR.getall('TIT2')[0][0]}"
        except IndexError as e:
            self.SongTitleName = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SongTitleName = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SongTitleName


    def getSongArtist(self):
        """Show Song Artist Name."""
        try:
            self.SongArtistName = f"{self.ID3HNDLR.getall('TPE1')[0][0]}"
        except IndexError as e:
            self.SongArtistName
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SongArtistName = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SongArtistName


    def getSongAlbum(self):
        """Show Song Album Name."""
        try:
            self.SongAlbumName = f"{self.ID3HNDLR.getall('TALB')[0][0]}"
        except IndexError as e:
            self.SongAlbumName = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SongAlbumName = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SongAlbumName


    def getSongPlayCount(self):
        """Show Song Play Count."""
        try:
            self.SongPlayCount = f"{self.ID3HNDLR.getall('PCNT')[0].count}"
        except IndexError as e:
            self.SongPlayCount = 0
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SongPlayCount = 0
        except Exception as e:
            print(f"Error: {e}")
        return self.SongPlayCount


    def getSongYear(self):
        """Show Song Play Count."""
        try:
            self.SongYear = f"{self.ID3HNDLR.getall('TYER')[0][0]}"
        except IndexError as e:
            self.SongYear = 0
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SongYear = 0
        except Exception as e:
            print(f"Error: {e}")
        return self.SongYear


    def getSongSyncedLyrics(self):
        """Show Synced Lyrics."""
        try:
            self.SongSyncLyrcs = self.ID3HNDLR.get('SYLT::eng')
        except IndexError as e:
            self.SongSyncLyrcs = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SongSyncLyrcs = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SongSyncLyrcs


    def getSongUnSyncedLyrics(self):
        """Show UnSynced Lyrics."""
        try:
            self.SongPlainLyrcs = self.ID3HNDLR.get('USLT')
            print(f"{self.ID3HNDLR.get('USLT')}")
        except IndexError as e:
            self.SongPlainLyrcs = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SongPlainLyrcs = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SongPlainLyrcs

    def getSongDuration(self):
        self.SetID3Handle()
        return self.MP3HNDLR.info.length

    def getSongBPM(self):
        """
            Input: filename, BPM (int)
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        try:
            self.SongBPM = f"{self.ID3HNDLR.getall('TBPM')[0][0]}"
        except IndexError as e:
            self.SongBPM = 0
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SongBPM = 0
        except Exception as e:
            print(f"Error: {e}")
        return self.SongBPM


































    # =====================================================================================================================
    # Tag Setters
    # =====================================================================================================================


    def SetMP3Handle(self):
        """
            Input: (None)
            Example: SetMP3Handle(self)
        """
        self.MP3HNDLR = MP3(self.songpath)
        return self.MP3HNDLR


    def SetID3Handle(self):
        """
            Input: (None)
            Example: SetID3Handle(self)
        """
        self.ID3HNDLR = ID3(self.songpath)
        return self.ID3HNDLR


    def setSongArtist(self, ArtistName: str):
        """
            Input: filename, ArtistName (STRING)
            Example: setSongArtist('song', 'Artist Name')
        """
        self.SongArtistName = ArtistName
        self.ID3HNDLR.add(_TPE1(encoding=Encoding.UTF16, text=[ArtistName]))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


    def setSongAlbum(self, AlbumName: str):
        """
            Input: filename, AlbumName (STRING)
            Example: setSongAlbum('song', 'Album Name')
        """
        self.SongAlbumName = AlbumName
        self.ID3HNDLR.add(_TALB(encoding=Encoding.UTF16, text=[AlbumName]))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


    def setSongTitle(self, SongTitle: str):
        """
            Input: filename, SongTitle (STRING)
            Example: setSongTitle('song', 'Song Title')
        """
        self.ID3HNDLR.add(_TIT2(encoding=Encoding.UTF16, text=[SongTitle]))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


    def setSongPlayCount(self, PlayCount: int):
        """
            Input: filename, PlayCount (INTEGER)
            Example: setSongPlayCount('song', 1531]
        """
        self.ID3HNDLR.add(_PCNT(encoding=3, count=PlayCount))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


    def setSongSyncedLyrics(self, sync_lyrics : list):
        """
            Input: filename, sync_lyrics  list((TupledPairs, 1042), (TupledPairs, 2042), (TupledPairs, 3042))
            Example: setSongSyncedLyrics('song', [('Some Lyics at time in MilliSeconds', 1000), ('Some More Lyics, add as many as you'd like, 2000)]
        """
        slrcs = sync_lyrics
        self.ID3HNDLR.setall("SYLT", [SYLT(encoding=Encoding.UTF16, lang='eng', format=2, type=1, text=slrcs)])
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


    def setSongUnSyncedLyrics(self, lyrics : str):
        """
            Input: filename, sync_lyrics (String)
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        slrcs = lyrics
        self.ID3HNDLR.setall("USLT", [USLT(encoding=Encoding.UTF16, lang='eng', format=2, type=1, text=slrcs)])
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


    def setSongBPM(self, bpm : int):
        """
            Input: filename, BPM (int)
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        sBPM = bpm
        self.ID3HNDLR.add(_TBPM(encoding=3, speed=sBPM))
        # self.ID3HNDLR.setall("TBPM", [TBPM(encoding=Encoding.UTF16, lang='eng', format=2, type=1, bpm=sBPM)])
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


# "TCMP": "compilation", # iTunes extension
# "TCOM": "composer",
# "TCOP": "copyright",
# "TENC": "encodedby",
# "TEXT": "lyricist",
# "TLEN": "length",
# "TMED": "media",
# "TMOO": "mood",
# "TIT3": "version",
# "TPE2": "performer",
# "TPE3": "conductor",
# "TPE4": "arranger",
# "TPOS": "discnumber",
# "TPUB": "organization",
# "TRCK": "tracknumber",
# "TOLY": "author",
# "TSO2": "albumartistsort", # iTunes extension
# "TSOA": "albumsort",
# "TSOC": "composersort", # iTunes extension
# "TSOP": "artistsort",
# "TSOT": "titlesort",
# "TSRC": "isrc",
# "TSST": "discsubtitle",

if __name__ == '__main__':
    # =====================================================================================================================
    # Example Song
    # =====================================================================================================================
    filename = '/Users/jkirchoff/Documents/github/MP3Player/Music/Tom MacDonald - Angels (Explicit).mp3'
    song = MP3TagYourSong(filename)
    song.deleteAllTags()  # TUrning this on will clear all headers and you must recreate them manually.  THERE IS NO UNDO!!!!

    # Checkers
    song.CreateMissingTag()
    song.CheckID3Tag()
    song.convertID3Tags2to3()

    # Getters
    print(f"Song Title Name         {song.getSongTitle()}")
    print(f"Song Artist Name:       {song.getSongArtist()}")
    print(f"Song Album Name:        {song.getSongAlbum()}")
    print(f"Song Play Count:        {song.getSongPlayCount()}")
    print(f"Song BPM:               {song.getSongBPM()}")
    print(f"Song Total Duration:    {song.duration_from_seconds(song.SongDuration)}")
    print(f"Song Total Duration(s): {song.SongDuration}")
    print()

    # Setters
    song.setSongTitle("Angels (Explicit)")
    song.setSongArtist("Tom MacDonald")
    song.setSongAlbum("No Guts No Glory")
    song.setSongPlayCount(393)
    song.setSongBPM(393)

    # Check the changes
    print(f"Song Title Name         {song.getSongTitle()}")
    print(f"Song Artist Name:       {song.getSongArtist()}")
    print(f"Song Album Name:        {song.getSongAlbum()}")
    print(f"Song Play Count:        {song.getSongPlayCount()}")
    print(f"Song BPM:               {song.getSongBPM()}")
    print(f"Song Total Duration:    {song.duration_from_seconds(song.SongDuration)}")
    print(f"Song Total Duration(s): {song.SongDuration}")





    print()
    print("Second Song Modification")
    print()
    filename2 = '/Users/jkirchoff/Documents/github/MP3Player/Music/02 Bad Girls Club.mp3'
    song2 = MP3TagYourSong(filename2)
    song2.deleteAllTags()  # TUrning this on will clear all headers and you must recreate them manually.  THERE IS NO UNDO!!!!

    # Checkers
    song2.CreateMissingTag()
    song2.CheckID3Tag()
    song2.convertID3Tags2to3()

    # Getters
    print(f"Song Title Name         {song2.getSongTitle()}")
    print(f"Song Artist Name:       {song2.getSongArtist()}")
    print(f"Song Album Name:        {song2.getSongAlbum()}")
    print(f"Song Play Count:        {song2.getSongPlayCount()}")
    print(f"Song BPM:               {song2.getSongBPM()}")
    print(f"Song Total Duration:    {song2.duration_from_seconds(song2.SongDuration)}")
    print(f"Song Total Duration(s): {song2.SongDuration}")
    print()

    # Setters
    song2.setSongTitle("Bad Girls Club")
    song2.setSongArtist("Falling In Reverse")
    song2.setSongAlbum("Fashionably Late (Deluxe Edition)")
    song2.setSongPlayCount(393)
    song2.setSongBPM(393)

    # Check Second Song Loading the Song captures the initial Song Info
    print(f"Song Title Name         {song2.getSongTitle()}")
    print(f"Song Artist Name:       {song2.getSongArtist()}")
    print(f"Song Album Name:        {song2.getSongAlbum()}")
    print(f"Song Play Count:        {song2.getSongPlayCount()}")
    print(f"Song BPM:               {song2.getSongBPM()}")
    print(f"Song Total Duration:    {song2.duration_from_seconds(song2.SongDuration)}")
    print(f"Song Total Duration(s): {song2.SongDuration}")
    print()



# Example Usage Result:

# No ID3 Header or Tags Exist.
# Default Placeholder Tags Were Created.
# Song Title Name
# Song Artist Name:
# Song Album Name:
# Song Play Count:        0
# Song Total Duration:    000:00:03:17

# Song Title Name         Angels (Explicit)
# Song Artist Name:       Tom MacDonald
# Song Album Name:        No Guts No Glory
# Song Play Count:        393
# Song Total Duration:    000:00:03:17

# Second Song Modification

# No ID3 Header or Tags Exist.
# Default Placeholder Tags Were Created.
# Song Title Name
# Song Artist Name:
# Song Album Name:
# Song Play Count:        0
# Song Total Duration:    000:00:03:42

# Song Title Name         Bad Girls Club
# Song Artist Name:       Falling In Reverse
# Song Album Name:        Fashionably Late (Deluxe Edition)
# Song Play Count:        393
# Song Total Duration:    000:00:03:42

# [Finished in 112ms]
