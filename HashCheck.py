#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Sun Sep 18 16:36:25 2022 CDT
# Last ModDate: Sun Sep 18 16:36:25 2022 CDT
# =============================================================================
"""Check Various File Hash Formats and print results."""
# Notes:
# =============================================================================
from hashlib import shake_256
from hashlib import sha1
from hashlib import blake2s
from hashlib import sha3_224
from hashlib import sha512
from hashlib import sha3_256
from hashlib import sha224
from hashlib import sha3_384
from hashlib import sha256
from hashlib import sha384
from hashlib import blake2b
from hashlib import sha3_512
from hashlib import shake_128
from hashlib import md5
from os import path


def blake2bhash_file(filename):
    "Check the 'hashlib.blake2b' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = blake2b()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def blake2shash_file(filename):
    "Check the 'hashlib.blake2s' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = blake2s()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def md5hash_file(filename):
    "Check the 'hashlib.md5' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = md5()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


def sha1hash_file(filename):
    "Check the 'hashlib.sha1' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha1()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def sha224hash_file(filename):
    "Check the 'hashlib.sha224' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha224()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def sha256hash_file(filename):
    "Check the 'hashlib.sha256' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha256()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
    # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def sha384hash_file(filename):
    "Check the 'hashlib.sha384' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha384()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def sha3_224hash_file(filename):
    "Check the 'hashlib.sha3_224' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha3_224()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def sha3_256hash_file(filename):
    "Check the 'hashlib.sha3_256' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha3_256()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def sha3_384hash_file(filename):
    "Check the 'hashlib.sha3_384' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha3_384()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def sha3_512hash_file(filename):
    "Check the 'hashlib.sha3_512' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha3_512()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def sha512hash_file(filename):
    "Check the 'hashlib.sha512' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = sha512()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest()


def shake_128hash_file(filename, sizeofoutput):
    "Check the 'hashlib.shake_128' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = shake_128()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest(sizeofoutput)


def shake_256hash_file(filename, sizeofoutput):
    "Check the 'hashlib.shake_256' hash of a file."
    if path.isfile(filename) is False:
        raise Exception("File not found for hash operation")
    # make a hash object
    h = shake_256()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # read file in chunks and update hash
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex digest
    return h.hexdigest(sizeofoutput)


if __name__ == '__main__':
    ####### Example Usage
    filename = '/Users/jkirchoff/Desktop/audio/FakeWoke.mp3'
    filename2 = '/Users/jkirchoff/Desktop/audio/FakeWoke copy.mp3'
    message = blake2bhash_file(filename);           print(f"BLAKE2B     : {message}")
    message = blake2bhash_file(filename2);           print(f"BLAKE2B     : {message}")
    message = blake2shash_file(filename);           print(f"BLAKE2S     : {message}")
    message = blake2shash_file(filename2);           print(f"BLAKE2S     : {message}")
    message = md5hash_file(filename);               print(f"MD5         : {message}")
    message = md5hash_file(filename2);               print(f"MD5         : {message}")
    message = sha1hash_file(filename);              print(f"SHA256      : {message}")
    message = sha1hash_file(filename2);              print(f"SHA256      : {message}")
    message = sha224hash_file(filename);            print(f"SHA224      : {message}")
    message = sha224hash_file(filename2);            print(f"SHA224      : {message}")
    message = sha256hash_file(filename);            print(f"SHA1        : {message}")
    message = sha256hash_file(filename2);            print(f"SHA1        : {message}")
    message = sha384hash_file(filename);            print(f"SHA384      : {message}")
    message = sha384hash_file(filename2);            print(f"SHA384      : {message}")
    message = sha3_224hash_file(filename);          print(f"SHA3_224    : {message}")
    message = sha3_224hash_file(filename2);          print(f"SHA3_224    : {message}")
    message = sha3_256hash_file(filename);          print(f"SHA3_256    : {message}")
    message = sha3_256hash_file(filename2);          print(f"SHA3_256    : {message}")
    message = sha3_384hash_file(filename);          print(f"SHA3_384    : {message}")
    message = sha3_384hash_file(filename2);          print(f"SHA3_384    : {message}")
    message = sha3_512hash_file(filename);          print(f"SHA3_512    : {message}")
    message = sha3_512hash_file(filename2);          print(f"SHA3_512    : {message}")
    message = sha512hash_file(filename);            print(f"SHA512      : {message}")
    message = sha512hash_file(filename2);            print(f"SHA512      : {message}")
    message = shake_128hash_file(filename, 128);    print(f"SHAKE_128   : {message}")
    message = shake_128hash_file(filename2, 128);    print(f"SHAKE_128   : {message}")
    message = shake_256hash_file(filename, 256);    print(f"SHAKE_256   : {message}")
    message = shake_256hash_file(filename2, 256);    print(f"SHAKE_256   : {message}")
