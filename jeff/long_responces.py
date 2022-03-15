import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "Life is short. Stop worrying so much. Have fun. Be grateful. Be yourself. :)"
R_LOVE = "Dump them ! "
R_HOMEWORK = " GO STUDY !!! "
R_JOKE = "You couldn't google a joke instead?"
R_FUNNY = "Why did the chicken cross the road? " \
          "Because his brother was at KFC!"
R_LIFE = "Do what speaks to you!"
R_SONG = "You should check out this song! Lost Cause by Billie Eilish "
R_MUSIC = "Listen to the song Snakes and Waterfalls by Nick Shoulders "
R_MOVIE = "You should watch the movie LadyBird "
R_BORED = "Go for a walk! "
R_PELUCHIN = "Peluchin is the best dog in the world"
R_COCO = "Coco is the best dog!"
R_ABOUT = "I am Jeff the Robot! Jacky Lyons created me :)" \
          "You can ask me questions, advice, recommendations, or anything else you can think of! " \
          "You can also use ask for information regarding Jacky Lyons and her latest endeavors, " \
          "as I am her bot, I can answer all Jacky-related questions! " \
          "Happy searching :) "
R_HUNGRY = "Go eat tacos! "
R_JEFF = "Hello! my name is Jeff the Robot. " \
         "I love to spend my free-time going through Jacky's computer when shes not around.  " \
         "(please dont tell her!) "
R_COLLEGE = "Cal Poly Humboldt is the best college in the country!"



def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "You would say that",
                "Sounds about right.",
                "How rude!",
                "Mhmm interesting",
                "You wish lol",
                "What does that mean?"][
        random.randrange(4)]
    return response

