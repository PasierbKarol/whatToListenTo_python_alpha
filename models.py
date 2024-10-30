from dataclasses import dataclass
from typing import List, Optional

#artist classes
@dataclass
class Image:
    height: int
    url: str
    width: int

@dataclass
class Followers:
    href: Optional[str]
    total: int

@dataclass
class ExternalUrls:
    spotify: str

@dataclass
class Artist:
    external_urls: ExternalUrls
    followers: Followers
    genres: List[str]
    href: str
    id: str
    images: List[Image]
    name: str
    popularity: int
    type: str
    uri: str

#album classes
@dataclass
class AlbumArtist:
    external_urls: ExternalUrls
    href: str
    id: str
    name: str
    type: str
    uri: str

@dataclass
class Album:
    album_type: str
    total_tracks: int
    available_markets: List[str]
    external_urls: ExternalUrls
    href: str
    id: str
    images: List[Image]
    name: str
    release_date: str
    release_date_precision: str
    type: str
    uri: str
    artists: List[AlbumArtist]
    album_group: str
