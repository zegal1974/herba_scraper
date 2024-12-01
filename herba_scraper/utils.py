import os
import re

from urllib.parse import urlparse, parse_qs


class Utils:
    FILETYPE_IMAGE = "image"
    FILETYPE_MOVIE = "movie"
    FILETYPE_SUBTT = "subtitle"
    FILETYPE_TORRENT = "torrent"
    FILETYPE_OTHER = "other"

    MAP_FILE_TYPE = {
        "png": FILETYPE_IMAGE,
        "jpg": FILETYPE_IMAGE,
        "jpeg": FILETYPE_IMAGE,
        "mp4": FILETYPE_MOVIE,
        "mkv": FILETYPE_MOVIE,
        "wmv": FILETYPE_MOVIE,
        "srt": FILETYPE_SUBTT,
        "ass": FILETYPE_SUBTT,
        "ssa": FILETYPE_SUBTT,
        "torrent": FILETYPE_TORRENT,
    }

    @staticmethod
    def get_file_type(filename):
        nodes = filename.split(".")
        if len(nodes) > 1:
            ext = nodes[-1].lower().strip()
            if Utils.MAP_FILE_TYPE.get(ext):
                return Utils.MAP_FILE_TYPE[ext]
        return Utils.FILETYPE_OTHER

    @staticmethod
    def is_image(filename):
        return Utils.get_file_type(filename) == Utils.FILETYPE_IMAGE

    @staticmethod
    def is_movie(filename):
        return Utils.get_file_type(filename) == Utils.FILETYPE_MOVIE

    @staticmethod
    def is_subtitle(filename):
        return Utils.get_file_type(filename) == Utils.FILETYPE_SUBTT

    @staticmethod
    def get_code(path):
        filename = os.path.basename(path)
        basename, extname = os.path.splitext(filename)
        rn = basename[::-1].upper()

        match = re.search(r"(\d{3,7})-?([A-Z]{2,6})", rn)

        if not match:
            match = re.search(r"[^0-9]+(\d{3,7})-?([A-Z]{2,6})", rn)

        if match:
            prefix = match.group(2)[::-1]
            number = int(match.group(1)[::-1])
            return prefix, number

        return None, None

    CODE_FILTERS = {
        r"^SET-": ""  # SET-AKDL-004
    }

    @staticmethod
    def decode(movie_code):
        mcode = movie_code.upper()
        match = re.search(r"^([A-Z\d]+)-(\d{2,})[A-Z]?[_-]?([A-Z\d-]*)?", mcode)

        if not match:
            match = re.search(r"^([A-Z]+)(\d{2,})[A-Z]?[_-]?([A-Z\d-]*)?", mcode)

        if match:
            return match.group(1).upper(), match.group(2), match.group(3)
        else:
            return None, None, None

    @staticmethod
    def convert_size(size_str):
        ssize = size_str.strip().upper()
        if ssize.endswith("GB"):  # GB
            return int(float(ssize[:-2]) * 1024 * 1024 * 1024)
        elif ssize.endswith("MB"):  # MB
            return int(float(ssize[:-2]) * 1024 * 1024)
        elif ssize.endswith("KB"):
            return int(float(ssize[:-2]) * 1024)
        elif ssize.endswith("B"):
            return int(float(ssize[:-1].strip()))
        return int(ssize)

    @staticmethod
    def get_magnet_info_hash(magnet_uri):
        uri = urlparse(magnet_uri)
        print(uri)
        if uri.scheme != "magnet":
            return None

        query_string = uri.query
        query_params = parse_qs(query_string)
        print(query_params)
        return query_params.get("xt", [""])[0].split(":")[-1]

    @staticmethod
    def parse_magnet_url(magnet_uri):
        uri = urlparse(magnet_uri)
        if uri.scheme != "magnet":
            return None

        query_string = uri.query
        query_params = parse_qs(query_string)
        info_hash = query_params.get("xt", [""])[0].split(":")[-1]
        display_name = query_params.get("dn", [""])[0]
        trackers = query_params.get("tr", [])

        return info_hash, display_name, trackers
