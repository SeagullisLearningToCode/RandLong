from random import choice


class movieNight:
    def __init__(self, movies: list):
        # LIST
        self.movies = movies

    def rollDice(self):
        # LIST
        mutable_movies_list = [movie for movie in self.movies] # ;Gets all entries and puts it into a mutable list as removing them from call will result in an error
        watched_movies_list = [] # ; Finished movies list
        # CODE
        while not len(mutable_movies_list) <= 0: # ;Continuous loop that will only stop when the entries on the mutable_movies_list is 0
            pick = choice(mutable_movies_list) # ;Chooses movie randomly
            print(f"\nMovie Picked: '{pick}'") # ;Shows selected movie from pick
            input("Is movie done?\n ") # ;Waits for confirmation from user if movie is done
            watched_movies_list.append(pick) # ;Puts watched movie in watched_movies_list
            mutable_movies_list.remove(pick) # ;Removes currently picked movie from the mutable_movies_list
            print(f"\nMovies watched: {len(watched_movies_list)}\nWatched Movies: {watched_movies_list}") # ;Shows current information
            print(f"\n{mutable_movies_list}")
        print("Movie List is empty")


movies = movieNight(
    []) # ;Takes strings as in ["Billy Bob", "Ecco"]
movies.rollDice()
