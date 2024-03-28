"""
We have already discusses docstrings for functions and their purpose. We have also discussed in
previous sections how functions can be called from within other functions. In this exercise we
will discuss docstrings for classes and methods. Also, we will discuss how class objects can
be used as attributes for other classes. Please refer to the below code:
"""


class Song:
    """
    Class to represent a song.

    Attributes:
        title(str): The title of the song.
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
        self.title = title
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
            song (Song): A song to add.
            position (Optional(int)): If specified the song will be added to the position in
                the track list inserting it between other songs if necessary. Otherwise,
                the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """
    Basic class to store artist details.

    Attributes:
        name (str): The name of the artist.
        albums (List(ALbum)): A list of albums by the artist.
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


"""
In the above code we have created 3 classes namely Song, Album and Artist. The Song class 
contains Artist class instance as one of its attributes. Similarly, Artist class contains 
Albums class instance as one of its attributes. Finally, Album class contains instances of 
both Song class and Artist class as its attributes. Now, lets see how we can make these 
classes work together. For our data we will use the 'albums.txt' file. It has data in 4 columns
artist, album name, year and song each separated by a tab character.
"""


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r", encoding="utf-8") as album:
        for line in album:
            artist_field, album_field, year_field, song_field = tuple(line.strip(
                '\n').split('\t'))
            year_field = int(year_field)

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    return artist_list


"""
We will try to understand what the above code is trying to do. It should be clear that in 
line 111 we are opening a csv file 'albums.txt' and in the following lines we are looping 
through each line of data from the file. We are converting the data into a tuple and then 
unpacking it to store the data in the individual fields to the variables artist_field, 
album_field, year_field, song_field. Now for the rest of the code within the for loop, 
we will try to understand it from bottom to top.
1.  The code in line 131 creates a new Song object (new_song) using the data received from the 
    file. That should be adequately clear. It is then adding the newly created Song instance
    new_song to and instance of the Album object (new_album) using the add_song() method.
    Now, we need to figure out where does this new_album instance come from and where it 
    gets initialised.
2.  We know that the variable new_artist, new_album were initialised to 'None' in lines 107 
    and 108. Similarly the artist_list variable is also initialised to an empty list in line
    109.
3.  Now we refer to the code in between line 125 and 129. The code first checks if the 
    variable new_album has yet been initialised. If not, then it gets initialised with the 
    details of the album that has been currently read from the file. If the album has 
    already been initialised then it checks if album name read from the current line in the 
    file matches the album name of the current album instance. If not, then it could only 
    mean that a new album name was encountered from the current line of the file. In such a 
    case the details of the album stored in the instance 'new_album' is stored into the 
    instance of the Artist class (new_artist). Following that, a new Album class instance is
    created with the current album details read from the file and stored in the new_album 
    variable.
4.  Now we will refer to the code in between line 117 and 123. The code first checks if the 
    variable 'new_artist' has been initialised with an instance of the Artist class. If not, 
    then it gets initialised with the details of the artist read from the current line in 
    the file. If the variable has already been initialised, then it checks if the 
    artist_name encountered in the current line of the file matches the artist name of the 
    new_artist instance. If not, it means that a new artist has been encountered in the file.
    It would also imply that with a new artist there comes a new album. Hence, firstly the 
    the current album details are added to the new_artist instance. Then, the current artist
    details are added to the artist_list. A new artist object is initialised and pointed to 
    the new_artist variable. Finally, the details of the previous album are cleaned and the 
    variable new_album is re-initialised to 'None'.
5.  Finally, although the loop parses the entire file, details of the last line from the 
    are not added to the instances within the loop. Hence, those details are added to the 
    instances outside the loop between lines 134-137.

Although, the above points explain the code and its purpose thoroughly, it will be more 
clear if the one debugs the code themselves.
    
"""


def create_checkfile(artist_list):
    """
    Create a checkfile from the object data for comparison with the original file.

    :param artist_list: A list containing objects of Artist class.
    """
    with open("checkfile.txt", "w", encoding="utf-8") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(f"{new_artist.name}\t", end='', file=checkfile)
                    print(f"{new_album.name}\t", end='', file=checkfile)
                    print(f"{new_album.year}\t", end='', file=checkfile)
                    print(f"{new_song.title}\t", end='\n', file=checkfile)


"""
The above code writes the data that has been read and transformed from the albums.txt file 
to a new file. This file can be useful to compare the two files later.
After comparing the two files we will see that both files match perfectly. However, 
that is because the data in the file has been arranged in such a way. Here's an example:
Imagine a situation where we have read details of an artist, the albums of the corresponding
artist and the songs associated with the respective albums and stored them in an Artist 
class instance. This instance is then added to the artist list. After reading through the 
file for a few more lines we encounter credits for the same artist again, for a new album.
Our code will again create another object for the same artist and then finally add it to the
artist_list, even though another object containing the details of the same artist is already
present in the list. Although the two objects are for the same artist they are not exactly 
duplicate.
In the next exercise we will write code the overcome the shortcomings of the current program.
"""

if __name__ == '__main__':
    artists = load_data()
    create_checkfile(artists)
    print(len(artists))
