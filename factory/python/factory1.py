#!/Users/vadlakun/.pyenv/shims/python

# Here, we will be using an input called format to decide which implementation to use for serializing the data
import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, name, singer):
        self.song_id = song_id
        self.name = name
        self.singer = singer

class SongSerializer:
    def serialize(self, song, format):
        """
        This is the client.

        :param song: song object
        :param format: string
        :return: implentation function
        """

        serializer = get_serializer(format)
        return serializer(song)


def get_serializer(format):
    """
    This is the creator that determines which implementation to use.

    :param format: string
    :return: implentation function
    """

    if format.upper() == 'JSON':
        return _serialize_to_json
    elif format.upper() == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError('Unexpected format!')

def _serialize_to_json(song):
    """
    This is one of the concrete implementation.

    :param song: song object
    :return: serialized data
    """

    payload = {
        'id': song.song_id,
        'name': song.name,
        'singer': song.singer
    }

    return json.dumps(payload)

def _serialize_to_xml(song):
    """
    This is one of the concrete implementations.

    :param song: song obj
    :return: serialized xml content
    """

    song_element = et.Element('song', attrib={'id': song.song_id})
    name = et.SubElement(song_element, 'name')
    name.text = song.name

    singer = et.SubElement( song_element, 'singer' )
    singer.text = song.name

    return et.tostring(song_element, encoding='unicode')


if __name__ == '__main__':
    my_song = Song(1, "Adventure of a lifetime", "coldplay")

    serializer = SongSerializer()

    print(serializer.serialize(my_song, 'json'))





