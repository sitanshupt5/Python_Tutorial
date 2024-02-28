"""
In the below code we have a tuple 'albums' with 3 layers of nesting. The tuple albums
is constituted of individual tuples containing data regarding the individual album.
Consequently, each tuple corresponding to an album contains another tuple with a list of
songs contained on the album.
"""

albums = (
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     (
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     )
     ),
    ("Bad Company", "Bad Company", 1974,
     (
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     )
     ),
    ("Nightflight", "Budgie", 1981,
     (
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     )
     ),
    ("More Mayhem", "Imelda May", 2011,
     (
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     )
     ),
)
"""
In order to parse the above-mentioned tuple albums and print the contents on the console
we will have to use nested loops. Since, there are 3 layers of nesting, 2 layers of nested
loops will be required to parse data structure efficiently.
"""

for album in albums:
    title, artist, year, tracks = album
    print("Album: {} ({}), Artist: {}".format(title, year, artist))
    for track_number, track_title in tracks:
        print(f"{track_number}.{track_title}")

"""
The above piece of code has a few things to note. 
The first loop executes on the contents of the tuple 'albums' and picks up one individual
constituent tuple at a time 'album'. The code on line 54 is used to unpack the contents of
tuple album and assign the individual values to the variables 'title', 'artist', 'year' and
'tracks'(which is another tuple).
In line 55 we use the format function to replace the values in our print output.

In the second loop we are parsing through the contents of the tuple 'tracks'. The tuple
'tracks' contains individual tuples containing track details. Unlike the first loop where 
we assign the value of the individual tuple to a variable and then unpack the contents and
assign the constituting elements to variables, we directly unpack the tuple on the loop
level.
In line 57 we print the output but here instead of using the format function we use the 'f'
prefix to replace the values.

To conclude, parsing sequences such as tuples and lists is very simple. Tuples are usually
preferred in case elements are supposed to be heterogenous i.e of different data types. It
is also necessary to analyse whether the data would need to be updated at runtime. In such
a case using lists would be more appropriate.
"""