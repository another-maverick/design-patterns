#!/Users/vadlakun/.pyenv/shims/python

import json
import xml.etree.ElementTree as et

class JsonSerializer:
    """
    Concrete Implementation.
    """
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    """
    Another Concrete Implementation.
    """

    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')



class SerializerFactory:
    """
    Creator.
    """

    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()

factory = SerializerFactory()
factory.register_format('JSON', JsonSerializer)
factory.register_format('XML', XmlSerializer)


class ObjectSerializer:

    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

    def serialize(self, serializer):
        """
        This is the client.
        The Song class implements the Serializable interface by providing a .serialize(serializer) method.

        :param serializer:
        :return:
        """

        serializer.start_object('song', self.song_id)
        serializer.add_property('song', self.title)
        serializer.add_property('song', self.artist)






if __name__ == '__main__':
    song = Song( '1', 'Adventure of a lifetime', 'Coldplay' )

    serializer = ObjectSerializer()
    print(serializer.serialize( song, 'JSON' ))
