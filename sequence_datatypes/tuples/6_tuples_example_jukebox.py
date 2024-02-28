"""
The following program emulates a juke box. The program displays a list of albums to be
chosen from to the user. Depending upon the choice of the user the songs corresponding to
the album is displayed to the user. If the user does not provide he correct album index
the program should exit.
Once the list of songs is displayed the user must provide input based on the song index to
play the song. If the index provided is incorrect then the user should be redirected to
the albums list.
"""

from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
    print("Please choose your album (Invalid choice exits):")
    # Unpacking at the loop level
    for index, (title, artist, year, songs) in enumerate(albums):
        print(f"{index + 1}: {title}")

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice-1][SONG_LIST_INDEX]
    else:
        break
    print("Please choose your song:")
    for index, (track_number, track_title) in enumerate(songs_list):
        print(f"{track_number}:{track_title}")
    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        song_title = songs_list[song_choice-1][SONG_TITLE_INDEX]
        print(f"Playing {song_title}")
    print("="*40)