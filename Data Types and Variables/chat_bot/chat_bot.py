from nltk.chat.util import Chat, reflections

pairs = [
    [r"(hi|hey|hello|hola|holla|hallo|greetings|sup)(.*)", ["Hello", "Hey there", "Hey :)"]],

    ["my name is (.*)", ["Hello %1, how are you today?\n(happy, sad, angry etc.)"]],

    ["(good|well|okay|ok|super|hyped|fantastic|perfect|perfekt)", ["Nice to hear "
      "that! If you still want me to send you a song, tell a joke, or suggest a movie, then please enter 'song', "
                                                                                                "'joke' or 'movie'"]],

    ["(sad|not well|not ok|not okay|disappointed|dissappointed|disapointed|dissapointed|angry|drunk|bored)",
     ["I'm really sorry to hear that. Do you want me to send you a song to cheer you up? If you do, then please type "
      "'song'. \nIf you want me to tell joke, or suggest a movie, then simply type 'joke' or 'movie'"]],


    # songs

    ["song", ["John Lennon - Imagine: https://www.youtube.com/watch?v=v27CEFE02Hs Did this cheer you up?",
              "Katrina & The Waves - Walking On Sunshine: https://www.youtube.com/watch?v=iPUmE-tne5U "
              "Did this cheer you up?",
              "Katy Perry - Firework: https://www.youtube.com/watch?v=QGJuMBdaqIw Did this cheer you up?",
              "Pharrell Williams - Happy: https://www.youtube.com/watch?v=ZbZSe6N_BXs Did this cheer you up?",
              "Mark Ronson - Uptown Funk ft. Bruno Mars: https://www.youtube.com/watch?v=OPf0YbXqDm0 "
              "Did this cheer you up?"]],

    ["(no|nope|nah)", ["Oh, then you probably like a certain genre? Enter genre:"
                       "(Examples: dance, rock, jazz, dubstep, rnb, techno, country, heavy metal):"]],

    ["dance", ["Surprise: https://www.youtube.com/watch?v=ZDrlmlzY7cE\nDid this cheer you up?",
               "Surprise: https://www.youtube.com/watch?v=UxxajLWwzqY\nDid this cheer you up?"]],

    ["rock", ["Surprise: https://www.youtube.com/watch?v=v2AC41dglnM\nDid this cheer you up?",
              "Surprise: https://www.youtube.com/watch?v=GgnClrx8N2k\nDid this cheer you up?"]],

    ["jazz", ["Surprise: https://www.youtube.com/watch?v=ZEcqHA7dbwM\nDid this cheer you up?",
              "Surprise: https://www.youtube.com/watch?v=ylXk1LBvIqU\nDid this cheer you up?"]],

    ["dubstep", ["Surprise: https://www.youtube.com/watch?v=YJVmu6yttiw\nDid this cheer you up?",
                 "Surprise: https://www.youtube.com/watch?v=3Q9rewnLFYw\nDid this cheer you up?"]],

    ["(rnb|r&b|r nb|rn b|r n b)", ["Surprise: https://www.youtube.com/watch?v=3KL9mRus19o\nDid this cheer you up?",
                                   "Surprise: https://www.youtube.com/watch?v=U0CGsw6h60k\nDid this cheer you up?"]],

    ["(techno|tehno)", ["Surprise: https://www.youtube.com/watch?v=SnPWNOmd5dU\nDid this cheer you up?",
                        "Surprise: https://www.youtube.com/watch?v=5IrHzrg4qdQ\nDid this cheer you up?"]],

    ["country", ["Surprise: https://www.youtube.com/watch?v=1vrEljMfXYo\nDid this cheer you up?",
                 "Surprise: https://www.youtube.com/watch?v=sgJXbIP83A8\nDid this cheer you up?"]],

    ["(heavy metal|heavy-metal|heavy_metal)", ["Surprise: https://www.youtube.com/watch?v=S7blkui3nQc\n"
                                               "Did this cheer you up?",
                                               "Surprise: https://www.youtube.com/watch?v=AkFqg5wAuFk\n"
                                               "Did this cheer you up?"]],

    ["(yes|yeah|yep)", ["Nice! I'm glad I could help :)\nIf you want to exit the chat, type 'exit'"]],


    # jokes

    ["joke", ["What did one ocean say to the other ocean?\nNothing, it just waved.",
              "What’s the difference between a hippo and a zippo?\nOne is really heavy and the other’s a little "
              "lighter.",
              "What’s the best thing about Switzerland?\nI don’t know, but the flag is a big plus.",
              "I’ve been trying to make a sarcastic club, but it’s been really hard to tell if people are interested in "
              "joining or not."]],


    # movies

    ["movie", ["Action: https://www.imdb.com/title/tt7888964",
               "Drama: https://www.imdb.com/title/tt1798709",
               "Horror: https://www.imdb.com/title/tt4160708",
               "Sci-fi: https://www.imdb.com/title/tt0470752",
               "Comedy: https://www.imdb.com/title/tt1411697",
               "Documentary: https://www.imdb.com/title/tt11464826"]],

    [r"(.*) your name?", ['My name is Robo']],

    [r"quit", ["I hope I was able to cheer you up. Bye for now hooman :) it was nice talking to you.",
                              "I hope I could help. Bye for now and have a nice day!",
                              "Hopefully, you feel better! Bye and stay safe :)"]],

    [r"(.*)", ["Sorry, I'm not trained to answer this question. Please try with something else."]],

]

# default message at the start of chat
print("\nPlease type in English."
      "Type quit to leave the chat.\n\nHi, I'm Robo :)\nWhat is your name? (please start with 'my name is ...')")

# Create Chat Bot
chat = Chat(pairs, reflections)
# Start conversation
chat.converse()
