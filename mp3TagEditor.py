# TODO: Share here when done https://stackoverflow.com/q/37414448/1896134  &   https://stackoverflow.com/q/18248200/1896134
# TODO: embed album art in an MP3
# TODO: Produced By Tom MacDonald
# TODO: Written By Tom MacDonald
# TODO: Mixing Engineer Evan Morgan
# TODO: Mastering Engineer Evan Morgan
# TODO: Release Date December 25, 2020

import mutagen
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.id3 import ID3Tags
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import Encoding  # Required for SYLT SYNC'D Lyrics
from functools import reduce  # Required for ID3 Header Checks
# =====================================================================================================================
# Four Character Imports
# https://pypi.org/project/mutagen/1.45.1/
# https://mutagen.readthedocs.io/en/latest/changelog.html
# https://mutagen.readthedocs.io/en/latest/api/id3_frames.html?highlight=Group%20identification%20registration
# =====================================================================================================================
from mutagen.id3 import AENC  # AENC    [[#sec4.20|Audio encryption]]   Supported Version: (4.20)
from mutagen.id3 import APIC  # APIC    [[#sec4.20|Audio encryption]]   Supported Version: (4.20)
from mutagen.id3 import ASPI  # ASPI    [Audio seek point index. Attributes: S, L, N, b, and Fi. For the meaning of these, see the ID3v2.4 specification. Fi is a list of integers.]
from mutagen.id3 import CHAP  # CHAP    [Chapter propertyHashKey An internal key used to ensure frame uniqueness in a tag]
from mutagen.id3 import COMM  # COMM    [#sec4.11 Comments]   Supported Version: (4.11)
from mutagen.id3 import COMR  # COMR    [#sec4.25 Commercial frame]   Supported Version: (4.25)
from mutagen.id3 import CTOC  # CTOC    [Table of contents propertyHashKey An internal key used to ensure frame uniqueness in a tag]
from mutagen.id3 import ENCR  # ENCR    [#sec4.26 Encryption method registration]   Supported Version: (4.26)
from mutagen.id3 import EQU2  # EQU2    [Equalisation (2).  Attributes: method - interpolation method (0 = band, 1 = linear) desc - identifying description adjustments - list of (frequency, vol_adjustment) pairs]
from mutagen.id3 import ETCO  # ETCO    [#sec4.6 Event timing codes]   Supported Version: (4.6)
from mutagen.id3 import GEOB  # GEOB    [#sec4.16 General encapsulated object]   Supported Version: (4.16)
from mutagen.id3 import GRID  # GRID    [#sec4.27 Group identification registration]   Supported Version: (4.27)
from mutagen.id3 import GRP1  # GRP1    [iTunes Grouping]
from mutagen.id3 import IPLS  # IPLS    [#sec4.4 Involved people list]   Supported Version: (4.4)
from mutagen.id3 import LINK  # LINK    [#sec4.21 Linked information]   Supported Version: (4.21)
from mutagen.id3 import MCDI  # MCDI    [#sec4.5 Music CD identifier]   Supported Version: (4.5)
from mutagen.id3 import MLLT  # MLLT    [#sec4.7 MPEG location lookup table]   Supported Version: (4.7)
from mutagen.id3 import MVIN  # MVIN    [iTunes Movement Number/Count]
from mutagen.id3 import MVNM  # MVNM    [iTunes Movement Name]
from mutagen.id3 import OWNE  # OWNE    [#sec4.24 Ownership frame]   Supported Version: (4.24)
from mutagen.id3 import PCNT  # PCNT    [#sec4.17 Play counter]   Supported Version: (4.17)
from mutagen.id3 import PCST  # PCST    [iTunes Podcast Flag]
from mutagen.id3 import POPM  # POPM    [#sec4.18 Popularimeter]   Supported Version: (4.18)
from mutagen.id3 import POSS  # POSS    [#sec4.22 Position synchronisation frame]   Supported Version: (4.22)
from mutagen.id3 import PRIV  # PRIV    [#sec4.28 Private frame]   Supported Version: (4.28)
from mutagen.id3 import RBUF  # RBUF    [#sec4.19 Recommended buffer size]   Supported Version: (4.19)
from mutagen.id3 import RVA2  # RVA2    [Relative volume adjustment (2).]
from mutagen.id3 import RVAD  # RVAD    [#sec4.12 Relative volume adjustment]   Supported Version: (4.12)
from mutagen.id3 import RVRB  # RVRB    [#sec4.14 Reverb]   Supported Version: (4.14)
from mutagen.id3 import SEEK  # SEEK    [Seek frame.]
from mutagen.id3 import SIGN  # SIGN    [Signature frame.]
from mutagen.id3 import SYLT  # SYLT    [#sec4.10 Synchronized lyric/text]   Supported Version: (4.10)
from mutagen.id3 import SYTC  # SYTC    [#sec4.8 Synchronized tempo codes]   Supported Version: (4.8)
from mutagen.id3 import TALB  # TALB    [#TALB Album/Movie/Show title]   Supported Version: (4.2.1)
from mutagen.id3 import TBPM  # TBPM    [#TBPM BPM (beats per minute)]   Supported Version: (4.2.1)
from mutagen.id3 import TCAT  # TCAT    [iTunes Podcast Category]
from mutagen.id3 import TCMP  # TCMP    [iTunes Compilation Flag]
from mutagen.id3 import TCOM  # TCOM    [#TCOM Composer]   Supported Version: (4.2.1)
from mutagen.id3 import TCON  # TCON    [#TCON Content type]   Supported Version: (4.2.1)
from mutagen.id3 import TCOP  # TCOP    [#TCOP Copyright message]   Supported Version: (4.2.1)
from mutagen.id3 import TDAT  # TDAT    [#TDAT Date]   Supported Version: (4.2.1)
from mutagen.id3 import TDEN  # TDEN    [Encoding Time]
from mutagen.id3 import TDES  # TDES    [iTunes Podcast Description]
from mutagen.id3 import TDLY  # TDLY    [#TDLY Playlist delay]   Supported Version: (4.2.1)
from mutagen.id3 import TDOR  # TDOR    [Original Release Time]
from mutagen.id3 import TDRC  # TDRC    [Recording Time]
from mutagen.id3 import TDRL  # TDRL    [Release Time]
from mutagen.id3 import TDTG  # TDTG    [Tagging Time]
from mutagen.id3 import TENC  # TENC    [#TENC Encoded by]   Supported Version: (4.2.1)
from mutagen.id3 import TEXT  # TEXT    [#TEXT Lyricist/Text writer]   Supported Version: (4.2.1)
from mutagen.id3 import TFLT  # TFLT    [#TFLT File type]   Supported Version: (4.2.1)
from mutagen.id3 import TGID  # TGID    [iTunes Podcast Identifier]
from mutagen.id3 import TIME  # TIME    [#TIME Time]   Supported Version: (4.2.1)
from mutagen.id3 import TIPL  # TIPL    [Involved People List]
from mutagen.id3 import TIT1  # TIT1    [#TIT1 Content group description]   Supported Version: (4.2.1)
from mutagen.id3 import TIT2  # TIT2    [#TIT2 Title/songname/content description]   Supported Version: (4.2.1)
from mutagen.id3 import TIT3  # TIT3    [#TIT3 Subtitle/Description refinement]   Supported Version: (4.2.1)
from mutagen.id3 import TKEY  # TKEY    [#TKEY Initial key]   Supported Version: (4.2.1)
from mutagen.id3 import TKWD  # TKWD    [iTunes Podcast Keywords]
from mutagen.id3 import TLAN  # TLAN    [#TLAN Language(s)]   Supported Version: (4.2.1)
from mutagen.id3 import TLEN  # TLEN    [#TLEN Length]   Supported Version: (4.2.1)
from mutagen.id3 import TMCL  # TMCL    [Musicians Credits List]
from mutagen.id3 import TMED  # TMED    [#TMED Media type]   Supported Version: (4.2.1)
from mutagen.id3 import TMOO  # TMOO    [Mood]
from mutagen.id3 import TOAL  # TOAL    [#TOAL Original album/movie/show title]   Supported Version: (4.2.1)
from mutagen.id3 import TOFN  # TOFN    [#TOFN Original filename]   Supported Version: (4.2.1)
from mutagen.id3 import TOLY  # TOLY    [#TOLY Original lyricist(s)/text writer(s)]   Supported Version: (4.2.1)
from mutagen.id3 import TOPE  # TOPE    [#TOPE Original artist(s)/performer(s)]   Supported Version: (4.2.1)
from mutagen.id3 import TORY  # TORY    [#TORY Original release year]   Supported Version: (4.2.1)
from mutagen.id3 import TOWN  # TOWN    [#TOWN File owner/licensee]   Supported Version: (4.2.1)
from mutagen.id3 import TPE1  # TPE1    [#TPE1 Lead performer(s)/Soloist(s)]   Supported Version: (4.2.1)
from mutagen.id3 import TPE2  # TPE2    [#TPE2 Band/orchestra/accompaniment]   Supported Version: (4.2.1)
from mutagen.id3 import TPE3  # TPE3    [#TPE3 Conductor/performer refinement]   Supported Version: (4.2.1)
from mutagen.id3 import TPE4  # TPE4    [#TPE4 Interpreted, remixed, or otherwise modified by]   Supported Version: (4.2.1)
from mutagen.id3 import TPOS  # TPOS    [#TPOS Part of a set]   Supported Version: (4.2.1)
from mutagen.id3 import TPRO  # TPRO    [Produced (P)]
from mutagen.id3 import TPUB  # TPUB    [#TPUB Publisher]   Supported Version: (4.2.1)
from mutagen.id3 import TRCK  # TRCK    [#TRCK Track number/Position in set]   Supported Version: (4.2.1)
from mutagen.id3 import TRDA  # TRDA    [#TRDA Recording dates]   Supported Version: (4.2.1)
from mutagen.id3 import TRSN  # TRSN    [#TRSN Internet radio station name]   Supported Version: (4.2.1)
from mutagen.id3 import TRSO  # TRSO    [#TRSO Internet radio station owner]   Supported Version: (4.2.1)
from mutagen.id3 import TSIZ  # TSIZ    [#TSIZ Size]   Supported Version: (4.2.1)
from mutagen.id3 import TSO2  # TSO2    [iTunes Album Artist Sort]
from mutagen.id3 import TSOA  # TSOA    [Album Sort Order key]
from mutagen.id3 import TSOC  # TSOC    [iTunes Composer Sort]
from mutagen.id3 import TSOP  # TSOP    [Perfomer Sort Order key]
from mutagen.id3 import TSOT  # TSOT    [Title Sort Order key]
from mutagen.id3 import TSRC  # TSRC    [#TSRC ISRC (international standard recording code)]   Supported Version: (4.2.1)
from mutagen.id3 import TSSE  # TSSE    [#TSEE Software/Hardware and settings used for encoding]   Supported Version: (4.2.1)
from mutagen.id3 import TSST  # TSST    [Set Subtitle]
from mutagen.id3 import TXXX  # TXXX    [#TXXX User defined text information frame]   Supported Version: (4.2.2)
from mutagen.id3 import TYER  # TYER    [#TYER Year]   Supported Version: (4.2.1)
from mutagen.id3 import UFID  # UFID    [#sec4.1 Unique file identifier]   Supported Version: (4.1)
from mutagen.id3 import USER  # USER    [#sec4.23 Terms of use]   Supported Version: (4.23)
from mutagen.id3 import USLT  # USLT    [#sec4.9 Unsychronized lyric/text transcription]   Supported Version: (4.9)
from mutagen.id3 import WCOM  # WCOM    [#WCOM Commercial information]   Supported Version: (4.3.1)
from mutagen.id3 import WCOP  # WCOP    [#WCOP Copyright/Legal information]   Supported Version: (4.3.1)
from mutagen.id3 import WFED  # WFED    [iTunes Podcast Feed]
from mutagen.id3 import WOAF  # WOAF    [#WOAF Official audio file webpage]   Supported Version: (4.3.1)
from mutagen.id3 import WOAR  # WOAR    [#WOAR Official artist/performer webpage]   Supported Version: (4.3.1)
from mutagen.id3 import WOAS  # WOAS    [#WOAS Official audio source webpage]   Supported Version: (4.3.1)
from mutagen.id3 import WORS  # WORS    [#WORS Official internet radio station homepage]   Supported Version: (4.3.1)
from mutagen.id3 import WPAY  # WPAY    [#WPAY Payment]   Supported Version: (4.3.1)
from mutagen.id3 import WPUB  # WPUB    [#WPUB Publishers official webpage]   Supported Version: (4.3.1)
from mutagen.id3 import WXXX  # WXXX    [#WXXX User defined URL link frame]   Supported Version: (4.3.2)

# =====================================================================================================================
# Tag Checkers
# =====================================================================================================================
def CreateMissingTag(filename):
    """Credit: https://github.com/quodlibet/mutagen/issues/327#issuecomment-339316014"""
    try:
        mp3 = MP3(filename)
        if mp3.tags is None:
            print(f"No ID3 Header or Tags Exist.")
            mp3.add_tags()
            print(f"Default Placeholder Tags Were Created.")
        tags = mp3.tags
        mp3.save()
    except Exception as e:
        print(f"{e}")

def CheckID3Tag(filename):
    """Check for Header Size."""
    try:
        # print header data
        with open(filename, 'rb') as a:
            data = a.read(10)
            print(data)
        # print header data check
        with open(filename, 'rb') as a:
            if data[0:3] != b'ID3':
                print('No ID3 header present in file.')
            else:
                size_encoded = bytearray(data[-4:])
                size = reduce(lambda a, b: (a * 128 + b), size_encoded, 0)
                print(size)
    except Exception as e:
        print(f"Error: {e}")

def convertID3Tags2to3(filename):
    try:
        tags = ID3(filename)
        tags.update_to_v24()
        tags.save(v1=2, v2_version=4, v23_sep='/')
    except Exception as e:
        print(f"Error: {e}")

# =====================================================================================================================
# Tag Delete ALL
# =====================================================================================================================
def deleteAllTags(filename):
    """Remove All ID3 Tags."""
    tags = ID3(filename)
    tags.delete(filename)

# =====================================================================================================================
# Tag Getters
# =====================================================================================================================
def getSongArtist(filename):
    tags = ID3(filename)
    try:
        print(f"{tags.getall('TPE1')[0][0]}")
    except IndexError as e:
        print(None)
    except ID3NoHeaderError as e:
        print(None)
    except Exception as e:
        print(f"Error: {e}")
    return tags.getall('TPE1')[0][0]

def getSongTitle(filename):
    tags = ID3(filename)
    try:
        print(f"{tags.getall('TIT2')[0][0]}")
    except IndexError as e:
        print(None)
    except Exception as e:
        print(f"Error: {e}")
    return tags.getall('TIT2')[0][0]

def getSongAlbum(filename):
    tags = ID3(filename)
    try:
        print(f"{tags.getall('TALB')[0][0]}")
    except IndexError as e:
        print(None)
    except Exception as e:
        print(f"Error: {e}")
    return tags.getall('TALB')[0][0]

def getSongAlbum(filename):
    tags = ID3(filename)
    try:
        print(f"{tags.getall('TDOR')[0][0]}")  # Original Release Time
        # print(f"{tags.getall('TDRL')[0][0]}") # Release Time
    except IndexError as e:
        print(None)
    except Exception as e:
        print(f"Error: {e}")
    return tags.getall('TALB')[0][0]

def getSongPlayCount(filename):
    tags = ID3(filename)
    try:
        print(f"{tags.getall('PCNT')[0].count}")
    except IndexError as e:
        print(0)
    except Exception as e:
        print(f"Error: {e}")
    return tags.getall('PCNT')[0].count

def getSongSyncedLyrics(filename):
    """
    # [1000ms]: It's not the liquor I'm addicted to, it's feeling brave
    # [2000ms]: The feeling of not feeling the pain
    # [3000ms]: I been on and off the bottle, I put oxys up my nostrils, believe me
    """
    tags = ID3(filename)
    try:
        print(f"{tags.get('SYLT::eng')}")
    except IndexError as e:
        print(0)
    except Exception as e:
        print(f"Error: {e}")
    return tags.get('SYLT::eng')

def getSongUnSyncedLyrics(filename):
    """
    Input: filename, sync_lyrics
    Example: setSongSyncedLyrics('song', [('Some Lyics at time in MilliSeconds', 1000), ('Some More Lyics, add as many as you'd like, 2000)]
    """
    tags = ID3(filename)
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

def setSongArtist(filename, ArtistName):
    tags = ID3(filename)
    tags.add(TPE1(encoding=3, text=[ArtistName]))
    tags.save(v1=50000000, v2_version=4, v23_sep='/')

def setSongAlbum(filename, AlbumName):
    tags = ID3(filename)
    tags.add(TALB(encoding=3, text=[AlbumName]))
    tags.save(v1=1, v2_version=4, v23_sep='/')

def setSongTitle(filename, SongTitle):
    tags = ID3(filename)
    tags.add(TIT2(encoding=3, text=[SongTitle]))
    tags.save(v1=1, v2_version=4, v23_sep='/')

def setSongPlayCount(filename, PlayCount):
    tags = ID3(filename)
    tags.add(PCNT(encoding=3, count=PlayCount))
    tags.save(v1=1, v2_version=4, v23_sep='/')

def setSongSyncedLyrics(filename, sync_lyrics : list):
    """
    Input: filename, sync_lyrics
    Example: setSongSyncedLyrics('song', [('Some Lyics at time in MilliSeconds', 1000), ('Some More Lyics, add as many as you'd like, 2000)]
    """
    tags = ID3(filename)
    slrcs = sync_lyrics
    tags.setall("SYLT", [SYLT(encoding=Encoding.UTF16, lang='eng', format=2, type=1, text=slrcs)])
    tags.save(v1=1, v2_version=4, v23_sep='/')

def setSongUnSyncedLyrics(filename, sync_lyrics : list):
    """
    Input: filename, sync_lyrics
    Example: setSongSyncedLyrics('song', [('Some Lyics at time in MilliSeconds', 1000), ('Some More Lyics, add as many as you'd like, 2000)]
    """
    tags = ID3(filename)
    slrcs = sync_lyrics
    tags.setall("SYLT", [USLT(encoding=Encoding.UTF16, lang='eng', desc=u'desc', text=slrcs)])
    tags.save(v1=1, v2_version=4, v23_sep='/')

# =====================================================================================================================
# Example Song
# =====================================================================================================================
# filename = '/Users/jkirchoff/Documents/github/MP3Player/Music/02 Bad Girls Club.mp3'
filename = '/Users/jkirchoff/Documents/github/MP3Player/Music/Tom MacDonald - Angels (Explicit).mp3'
# https://genius.com/Tom-macdonald-angels-lyrics

# tags = ID3(filename)
# tags.delete(filename)  # Remove All ID3 Tags.


CreateMissingTag(filename)
CheckID3Tag(filename)
convertID3Tags2to3(filename)
getSongArtist(filename)
setSongArtist(filename, "Tom MacDonald")
getSongArtist(filename)
getSongTitle(filename)
setSongTitle(filename, "Angels (Explicit)")
getSongTitle(filename)
getSongAlbum(filename)
setSongAlbum(filename, "No Guts No Glory")
getSongAlbum(filename)
getSongPlayCount(filename)
setSongPlayCount(filename, 123)
getSongPlayCount(filename)
getSongSyncedLyrics(filename)
# setSongSyncedLyrics(filename, sync_lyrics)
# getSongSyncedLyrics(filename)

# Released September 3, 2021

class MP3TagButler(object):
    """MP3TagButler Handle Getters & Setters for Mutagen ID3 Tags"""
    def __init__(self, arg):
        super(MP3TagButler, self).__init__()
        self.arg = arg

def duration_from_seconds(s):
    """Module to get the convert Seconds to a time like format."""
    s = s
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    TIMELAPSED  = f"{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}"
    return TIMELAPSED

def duration_from_millseconds(ms):
    """Module to get the convert Seconds to a time like format."""
    ms = ms
    s, ms = divmod(ms, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    TIMELAPSED  = f"{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}:{ms:03.0f}"
    return TIMELAPSED

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
# tag = MP3(filename)
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
# m = ID3(filename)
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
# id3.AENC(owner='', preview_start=0, preview_length=0, data='')
# id3.TextFrame('')
# id3.TimeStampTextFrame('')
# id3.NumericPartTextFrame('')
# id3.NumericTextFrame('')
# id3.PairedTextFrame(encoding=<Encoding.UTF16: 1>, people=[])
# id3.UrlFrame(url='')
# id3.UrlFrameU(url='')
# id3.add(APIC(encoding=3, mime=u'image/jpeg', type=3, desc=u'Front Cover', data=self.get_cover(info)))
# id3.add(APIC(encoding=3, mime=u'image/jpg', type=3, # #desc=u'Front Cover', data=self.get_cover(info)))
# id3.add(APIC(encoding=3, mime=u'image/jpg', type=3, desc=u'Cover', data=self.get_cover(info['album_pic_url'])))
# id3.add(APIC(encoding=3, mime=u'image/jpg', type=3, desc=u'Front Cover', data=self.get_cover(info)))
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

# Remove old 'APIC' frame
# Because two 'APIC' may exist together with the different description
# For more information visit: http://mutagen.readthedocs.io/en/latest/user/id3.html
# if id3.getall('APIC'): id3.delall('APIC')


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
