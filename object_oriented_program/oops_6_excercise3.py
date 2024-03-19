"""
In the previous exercises we created 3 classes Song, Album and Artist. We created objects
for the said classes and created functions that would operate on the members of the said
classes through those instances. To a normal eye, this would look like a simulation of
object-oriented programming, however, it is not. In object-oriented programming the
attributes and the methods that operate on those attributes are encapsulated within classes.
Even though our classes have both attributes and methods, most of the heavy lifting in the
previous 2 exercises is done by the load_data() function which is outside the classes.
If we think logically, the operations regarding the albums should be handled by the Artist
class because it stores a list of the all the albums associated with the particular instance.
Similarly, operations that pertain to songs should be carried out by the Album class.
In this module we will rewrite the classes and functions, but this time using a more
object-oriented programming approach. Please refer below:
"""


class Song:
    """
    Class to represent a song.

    Attributes:
        name (str): The title of the song.
        artist(Artist): An Artist object representing the song's creator.
        duration(int): Duration of the song in seconds.
            May be zero.
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method.

        :param title (str): Initialises the song title.
        :param artist (Artist): An Artist object representing the song's creator.
        :param duration (Optional(int)): Initial value for the duration attribute.
            Will default to zero if not specified.
        """
        self.name = title
        self.artist = artist
        self.duration = duration


class Album:
    """
    Class to represent an album using its track list.

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist (Artist): The artist reponsible for the album. If not specified,
            the artist will default to an artist with the name "Various Artists"
        tracks (List(Song)): A list of songs on the album.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
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
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album "+name)
        album_found.add_song(title)


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


"""
Before we begin updating the load_data() function we need to understand the structure of the
classes.First of all, the Artist class instance contains references to all the Album 
instances stored within a list attribute. Similarly, the individual Album instances contain 
references to the Song objects associated with the album.
Our approach should be such that the load_data() function initialised the Artist class 
instance and then hands over the rest of the operation to the methods within the Artist class.
The methods within of the Artist class handle the operations on the Album class instances 
and hand over the operations on Song instances to the Album class methods.
Knowing this, we can start redesigning the new load_data() method.
"""


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


"""
Code in the load_data() function looks much more concise and is carrying out the minimum 
operations. We are just creating an Artist class instance and handing over rest of the 
details read from the current line of the file to the add_song() method of Artist class 
which carries out the rest of the operations. Now lets understand what other changes have 
been made to the methods of the classes.
1.  For the Artist class in between line 106 ro 124 we have added the add_song() method.
    This method takes the album name, year and song name as its arguments. It then uses the 
    find_object() function to search for the existence of an Album instance with the same 
    album name in 'albums' list of the Artist class. If found the 'album_found' variable is 
    pointed to that object. If not a new Album object us created and assigned to the 
    album_found variable. The object is then immediately appended to the albums list.
    Finally, the add_song method of the Album class is invoked with the song name.

2.  The add_song method of the Album class does a similar job as the add_song() method of the 
    Artist class. It checks for the existence of a Song class object with the same name as 
    the song name passed in the argument using the find_object() method from the tracks list
    of the Album instance. If found the song_found variable is pointed to the existing Song
    object. Else, a new Song object is created and assigned to the song_found variable. 
    Finally, the Song object is added to the tracks list of the current Album instance.
"""


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
The current program delegates responsibilities to different methods than having single 
function handle all of the heavy lifting. 
1.  The load_data() function reads data from the file, creates a new Artist instance and 
    hands over the rest of the operations to the Artist class add_song() method.
2. The add_song() method of the Artist class effectively searches for or creates a new Album
    class instance and hands over the data of the song to the Album class add_song() method.
3.  Finally, the Album class add_song method uses the song data from the argument list, 
    creates a new Song object and adds it to the tracks list of the current Album instance.

Although the above program looks much better now, there are still a few aspects of this 
program that create issues in the long and we must know to identify and resolve them. For 
example, The Artist class contains Album object. The Artist class method add_song() is also 
equipped to create an Album class instance. At the same time the Album class contains Artist
class objects. The Album class constructor is also equipped to create an Artist class object.
This is called a Circular Reference. In the next excercise we will learn why circular 
references are bad and how we can remove them. 
"""