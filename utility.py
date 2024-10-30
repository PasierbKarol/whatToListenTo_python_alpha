from models import Album, ExternalUrls, Artist, AlbumArtist
from typing import List

# def convert_to_artists(items) -> List[Artist]:
def convert_to_artist(data) -> Artist:
    # artists = []
    # for item in items:
    print('item')
    print(data)
    artist = Artist(
        external_urls=ExternalUrls(spotify=data['external_urls']['spotify']),
        href=data['href'],
        id=data['id'],
        name=data['name'],
        type=data['type'],
        uri=data['uri'],
        followers=data['followers'],
        images=None,
        popularity=data['popularity'],
        genres=data['genres']
    )
    # artists.append(artist)
    return artist


def convert_to_albums(data) -> List[Album]:
    albums = []
    
    for item in data:
        external_urls = ExternalUrls(spotify=item['external_urls']['spotify'])

        # Convert album artists list
        album_artists = [AlbumArtist(
            external_urls=ExternalUrls(spotify=artist['external_urls']['spotify']),
            href=artist['href'],
            id=artist['id'],
            name=artist['name'],
            type=artist['type'],
            uri=artist['uri']
        ) for artist in item['artists']]
        
        album = Album(
            album_type=item['album_type'],
            total_tracks=item['total_tracks'],
            available_markets=item.get('available_markets', []),  # Default to empty list if not present
            external_urls=external_urls,
            href=item['href'],
            id=item['id'],
            name=item['name'],
            release_date=item['release_date'],
            release_date_precision=item['release_date_precision'],
            type=item['type'],
            images=None,
            uri=item['uri'],
            artists=album_artists,
            album_group=item['album_group'],
        )
        albums.append(album)
    
    return albums
