"""
The below code is the optimized version of the code in excercise 1. We understand the code
as go on.
"""
from oops_4_excercise1 import Song, Album, Artist


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
As explained at the end of the previous excercise, the code was not capable of handling all 
sets of data and could possibly give us erroneous results. For example if we have a dataset 
where the rows are unorganised like the one below:
1000 Maniacs	Our Time in Eden	1992	Candy Everybody Wants
10cc	The Best Of The Early Years	2002	Rubber Bullets
AC DC	If You Want Blood, You've Got It	1978	Riff Raff
1000 Maniacs	Our Time in Eden	1992	Circle Dream
AC DC	For Those About To Rock (We Salute You)	1981	For Those About To Rock (We Salute You)
AC DC	If You Want Blood, You've Got It	1978	Bad Boy Boogie

In such a case the code will create and insert a new object into the artists_list and albums
list even though the same artist and same album were encountered before. Hence, a better 
approach would be to check for the existence of the artist or the album in the object list 
before creating a new object. If the object already exists, then we can update it. 
Otherwise, we can create a new object. This would prevent duplication.
The find_object() in line 8 is created to check whether an object with the same artist name 
or album name exists in the object list. If so, the object is returned. Otherwise a value of
'None' is returned.
"""


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r", encoding="utf-8", newline='') as album:
        for line in album:
            artist_field, album_field, year_field, song_field = tuple(line.strip(
                '\n').split('\t'))
            year_field = int(year_field)

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                new_artist = find_object(artist_field, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        return artist_list


"""
The load_data() function above is different from the one in the previous excercise. Let's 
see how.
1.  In the code between line 55 and 63, it is checked if the new_artist variable has been 
    initialised with and Artist class instance. If not the object is initialised with the 
    details from the current line of the file and added immediately to the 'artist_list'.
    If the variable new_artist was already initialised with an Artist class instance, 
    in that case it is checked if the artist name encountered in the current line of the 
    file matches the artist name of the new_artist instance. If not, it means that a new 
    artist name and details has been encountered in the file. In that case the code calls 
    the find_object() method created above to check if the object for the artist encountered
    in the file exists in the artist_list. If so, the new_artist variable is repointed to 
    the object returned by the find_object() method. Else, a new_artist variable is assigned
    to a newly created Artist class instance (with the details from the current line of the 
    file) and the object is immediately added to the artist_list.
    Encountering a new artist in the file also means that a new album corresponding to the 
    artist will be encountered. Hence, the new_album variable is assigned a null value.

2.  Now we will understand the code between lines 65 and 72. Before that we must keep in 
    mind that in line 63 we assigned the new_album variable with value 'None' as mentioned 
    in the above point. In this case the code checks if the new_album object has been 
    initialised with an Album class instance. If not the new_album variable is initialised to
    a newly created object of the Album class with the details from the current line from 
    the file and immediately added to the new_artist.albums list. If the variable is already
    initialised with an Album class instance, it checks if the album name read from the 
    current line of the file matches the album name of the instance. If not, it means a new 
    album name has been encountered in the file. The find_object() method is invoked to 
    check if and Album object with the same name as in the file is already present in the 
    new_artist.albums list. If so the new_album variable is repointed to the object returned
    by the find_object() method. Else, new_album variable is initialised to a newly created 
    Album object and is immediately added to the new_artist.albums list.

The rest of the code is pretty much same and carries out the same operations as in the 
previous excercise.    
"""


def create_checkfile(artist_list):
    """Create a checkfile from the object data for comparison with the  original file."""
    with open("checkfile.txt", "w", encoding="utf-8") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(
                        "{0.name}\t{1.name}\t{1.year}\t{2.title}".format(
                            new_artist, new_album, new_song
                        ), file=checkfile
                    )


if __name__ == '__main__':
    artists = load_data()
    create_checkfile(artists)
    print(len(artists))
