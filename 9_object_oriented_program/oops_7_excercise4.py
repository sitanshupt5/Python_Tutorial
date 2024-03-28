"""
In the previous excercise we mentioned circular references. Circular references in python
classes occur when two or more objects reference each other in a loop, forming a cycle of
references. This mean Object A holds a reference to Object B and in turn Object B holds a
reference to Object A, creating a closed loop. Having circular references in a program
confuses python's garbage collector making it difficult to determine which objects are still
in use and which can be safely garbage collected. This causes memory leaks and slows down
the overall performance of the application.
Also, a code containing circular references can be difficult to understand and maintain
leading to subtle bugs and unexpected behavior especially when dealing with large codebases
and complex data structures. Hence, it is better to avoid having circular references in our
code to the utmost extent. In this program we will try to remove the circular references
from our code.
But before that lets take a look at the existing attributes in the classes Song, Album and
Artist as per the previous excercise:
1.  Artist class consists of the artist name and a list of album objects.
2.  The Album class consists of album name, year, Artist reference object and list of song
    objects.
3. Finally, the Song class consists of song name, duration and Artist reference object.

Now, in order to remove circular references, the reference system must go from top to bottom
and not both ways. Hence, Artist should contain references to Album objects, and Album
should contain references to Song objects. Album and Song do not need to have Artist
reference objects. Knowing this we can modify our code likewise.
"""


class Song:
    """
    Class to represent a song.

    Attributes:
        name (str): The title of the song.
        artist(str): The name of the song's creator
        duration(int): Duration of the song in seconds.
            May be zero.
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method.

        :param title (str): Initialises the song title.
        :param artist (str): The name of the song's creator.
        :param duration (Optional(int)): Initial value for the duration attribute.
            Will default to zero if not specified.
        """
        self.name = title
        self.artist = artist
        self.duration = duration


"""
As per our analysis above, we need to remove all references to Artist class instances from 
the Song class. We can do this in 2 ways. 
1.  Remove the Song class reference attribute completely from the class definition of the 
    Song class.
2.  Change the behavior of the attribute 'artist' to refer to the artist name instead of an 
    Artist class object.

We will employ the second one to avoid any conflicts with the calling code for this class 
methods. Although both approaches are correct,  in case of presence of code that already 
makes use of the class objects, it is safer to use the second approach.
"""


class Album:
    """
    Class to represent an album using its track list.

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (str): The name of the album's creator.
        tracks (List(Song)): A list of songs on the album.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various Artists"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """
        Adds a song to the track list.

        Args:
            song (Song): The title of the song to add.
            position (Optional(int)): If specified the song will be added to the position in
                the track list inserting it between other songs if necessary. Otherwise,
                the song will be added to the end of the list.
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


"""
Following the same approach as used in case of the Song class, we remove the circular 
references form the Album class by converting the attribute artist to accept string value 
rather than an Artist instance.
"""


class Artist:
    """
    Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List(Album)): A list of albums by the artist.
            The list includes only those albums in its collection, it is
            not an exhaustive list of artist's published albums.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        Adds a new album to the list.

        :param album: Album object to add to the list.
            If the albums is already present, it will not be added again(Yet to be implemented)
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """
        Add a new song to the collection of albums

        This method will add the song to the album in the collection.
        A new album will be created in the collection if it doesn't already exist.

        :param name: Name of the album.
        :param year: Year of release of the album
        :param title: Name of the song.
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album "+name)
        album_found.add_song(title)


"""
Final change done is on line 151 where we are sending the artist name rather than the artist
object as an argument in the Album class constructor.
"""


def find_object(field, object_list):
    """
    Check object list to see if an object with the name attribute equal to 'field' exists,
        return if so.
    :param field:  Expected value of the name attribute of the object.
    :param object_list: List of objects.
    :return: object
    """
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    artist_list = []

    with open("albums.txt", "r", encoding="utf-8", newline='') as album:
        for line in album:
            artist_field, album_field, year_field, song_field = tuple(line.strip(
                '\n').split('\t'))
            year_field = int(year_field)

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

        return artist_list


def create_checkfile(artist_list):
    """Create a checkfile from the object data for comparison with the  original file."""
    with open("checkfile.txt", "w", encoding="utf-8") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(
                        "{0.name}\t{1.name}\t{1.year}\t{2.name}".format(
                            new_artist, new_album, new_song
                        ), file=checkfile
                    )


if __name__ == '__main__':
    artists = load_data()
    create_checkfile(artists)
    print(len(artists))

"""
Now that we have removed all the circular references, i.e all the references to the Artist 
class objects from Album and Song class and run the code, we see no discrepancies and our 
code runs perfectly without any loss of data.
Moreover now, since the circular references have been removed the garbage collection in the 
case of program will be easy. This would prevent memory leaks and upgrade the overall 
performance of our program.
Removing the circular references also makes our program more readable and reduces chances of
confusion.
"""