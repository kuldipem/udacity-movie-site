import movie
import fresh_tomatoes

# I have collecte my favourite movie and its most important
# details together to build an intresting webpage

dangal = movie.Movie('Dangal',
                     'Story about first indian woman wrestler.',
                     'https://upload.wikimedia.org/wikipedia/en/9/99/Dan'
                     +'gal_Poster.jpg',
                      '')
adhm = movie.Movie('Ae Dil Hai Muskil',
                   'A chance meeting between Ayan Senger and Alizeh Khan ends'+
                   'up with both kissing instinctively.',
                   'https://upload.wikimedia.org/wikipedia/en/2/2a/Ae_Dil_Hai'+
                   '_Mushkil2.jpg',
                   'https://www.youtube.com/watch?v=Z_PODraXg4E')
pink = movie.Movie('Pink', 'The movie is based on an event near south Delhi.'+
                   ' Three friends, Rajveer, Ankit, and Dumpy, were hurried'+
                   ' up in a hospital after an accident. Rajveer had been'+
                   ' seriously hit on his forehead. ',
                   'http://t0.gstatic.com/images?q=tbn:ANd9GcSm-BfN-7qAQEf61YA'+
                   'Td5irTYPGn2JDNHvF676M6kuujpUTeJkv', 'https://www.youtube.'+
                   'com/watch?v=AL2TShb6fFs')
rustom = movie.Movie('Rustom',
                     'The story dates back to the late 1950\'s and revolves'+
                     ' around an Indian Naval Officer Rustom Pavri (Akshay'+
                     ' Kumar), who is happily married to Cynthia Pavri ('+
                     'Ileana D\'Cruz).',
                     'https://upload.wikimedia.org/wikipedia/en/9/96/Akshay'+
                     '_Kumar%27s-Rustom_poster.jpg',
                     'https://www.youtube.com/watch?v=L83qMnbJ198')

fresh_tomatoes.open_movies_page([dangal, adhm, pink, rustom])
