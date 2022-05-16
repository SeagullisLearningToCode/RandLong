from random import choice
import os
import datetime


class MovieNight:
    def __init__(self, file):
        # FILE
        self.file = open(file, "r+")
        # STR
        self.contents = self.file.read()
        self.write = ""
        # LIST
        self.movie_data = self.contents.split("\n")
        # DATETIME
        self.run_date = f"{datetime.datetime.now().strftime('%Y-%m-%d %I:%M %p')}"
        # CODE
        if os.path.exists(file) is True:
            self.file_watched = open(f"{file[:file.index('.')]}_watched.txt", "a")
        else:
            self.file_watched = open(f"{file[:file.index('.')]}_watched.txt", "w+")
            print(f"Created '{file}_watched.txt'")
        self.file_watched.write(f"\n==========================\n{self.run_date}\n==========================\n")

    def remove_from_list(self, refer, var, saver):
        saver.append(var)  # ;Puts watched movie in watched_movies_list
        refer.remove(var)  # ;Removes currently picked movie from the mutable_movies_list

    def roll_dice(self):
        # LIST
        watched_movies_list = []  # ; Finished movies list
        # CODE
        while not len(
                self.movie_data) <= 0:  # ;Continuous loop that will only stop when the entries on the mutable_movies_list is 0
            pick = choice(self.movie_data)  # ;Chooses movie randomly
            print(f"\nMovie Picked: '{pick}'")  # ;Shows selected movie from pick
            command = input("Is movie done?\n ")  # ;Waits for confirmation from user if movie is done
            if command == "e":
                break
            self.remove_from_list(self.movie_data, pick, watched_movies_list)
            self.file_watched.write(f"{pick}\n")  # ;Save the watched movie in a file for referrence
            print(
                f"\nMovies watched: {len(watched_movies_list)}\nWatched Movies: {watched_movies_list}\n{self.movie_data}")  # ;Shows current information
        if len(self.movie_data) <= 0:
            print("Movie List is empty")


movies = MovieNight("Movies.txt")
movies.roll_dice()
