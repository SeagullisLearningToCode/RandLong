from PF import *

backup_project(filter=[".txt", ".py"])

class ShowTime:
    """
    SHARGS (Show Time Kwargs)
    --------------------------
    debug_mode (Prints information)
        0 = Off
        1 = Lists
    """

    def __init__(self, file, **shargs):
        # SHARGS
        self.debug_mode = shargs.get("debug_mode", 0)
        # FILE
        self.file = open(file, "r+")
        self.filename = file
        # INT
        self.show_data_len = 0
        # LIST
        self.show_data = []
        self.contents = self.file.read().split("\n")
        # DICT
        self.dbg_data = {}
        # DATETIME
        self.run_date = f"{datetime.now().strftime('%Y-%m-%d %I:%M %p')}"
        # CODE
        if os.path.exists(file) is True:
            self.file_watched = open(f"{file[:file.index('.')]}_watched.txt", "a")
        else:
            self.file_watched = open(f"{file[:file.index('.')]}_watched.txt", "w+")
            p(f"Created {file}_watched.txt")

        if os.path.exists(f"{file[:file.index('.')]}_user_suggestion.txt") is True:
            self.file_user_suggested = open(f"{file[:file.index('.')]}_user_suggestion.txt", "r+")
            self.suggested_data = self.file_user_suggested.read().split("\n")
        else:
            self.file_user_suggested = open(f"{file[:file.index('.')]}_user_suggestion.txt", "w+")
            p(f"Created '{file[:file.index('.')]}_user_suggestion.txt'")
        self.file_watched.write(f"\n==========================\n{self.run_date}\n==========================\n")

        for suggestion in self.contents:
            if suggestion in ["", "\n", " "]:
                pass
            else:
                data = suggestion.split(" | ")
                self.show_data.append([data[0], data[1]])
                self.show_data_len += 1

    def remove_from_list(self, refer, var, svar):
        # CODE
        svar.append(var) # ;Puts referred var in a list
        refer.remove(var) # ;Removes the var from the list

    def list_data(self, **options):
        # OPTIONS
        list_data_get = options.get("search", None)
        # CODE
        if self.debug_mode == 1:
            p("\t| DEBUG LIST DATA\n\t---------------------------------------------")
            for list_data in vars(self):
                if type(vars(self)[list_data]) is list or type(vars(self)[list_data]) is dict:
                    if list_data_get is None:
                        p(f"\t|\t{list_data}: {vars(self)[list_data]}")
                    else:
                        list_data_get_alternative_listing = options.get("use_alt_list", True)
                        if list_data == list_data_get:
                            if list_data_get_alternative_listing is True:
                                p(f"\t|\t{list_data}")
                                for nested_data in vars(self)[list_data]:
                                    p(f"\t|\t|\t{nested_data}: {vars(self)[list_data][nested_data]}")
                            else:
                                p(f"\t|\t{list_data}: {vars(self)[list_data]}")
            p("\t---------------------------------------------\n-------------------------------------------------")

    def save_to_counter_file_from_list(self, main_list, main_list_unknowns):
        # CODE
        with open(f"{self.filename[:self.filename.index('.')]}_user_suggestion.txt", "r") as counter_file:  # ;Opens the counter file (it should be FILE_user_suggestion.txt)
            counter_file_contents = counter_file.read()
            counter_file_table = counter_file_contents.split("\n")  # ;Converts string to list
            user_table = {}  # ;Usernames with counters
            for user in counter_file_table:  # ;Loops through the converted string
                if user not in ["", "\n", " "]:  # ;Filters unneeded content such as lines with just spaces, empty newlines and empty strings
                    user_data = user.split(": ")
                    user_table.update({user_data[0]: int(user_data[1])})

            for username in main_list:  # ;Loops through the usernames list
                if username in user_table.keys():  # ;Checks if the 'username' is in the 'user_table', if not skip this and put it in 'unknown_usernames'
                    user_table[username] += 1
                    counter_file_contents = counter_file_contents.replace(f"{username}: {user_table[username] - 1}\n", f"{username}: {user_table[username]}\n")
                else:
                    if username not in main_list_unknowns:  # ;Checks if the 'username' is in 'unknown_users', if not add it, this is only executed when the 'username' is not in the 'user_table'
                        main_list_unknowns.append(username)  # ;Add 'username' to 'unknown_users' list
                        counter_file_contents += f"{username}: 1\n"  # ;Add 'username' with the value of 1 to the 'counter_file_contents'
                        user_table.update({username: 1})  # ;Update the 'user_table' by adding the unknown username to the list with the value of 1
            write = counter_file_contents  # ;Transfer string to a new string
            counter_file.close()
        with open(f"{self.filename[:self.filename.index('.')]}_user_suggestion.txt", "w+") as new_data:  # ;Opens the 'FILE_user_suggestion.txt' with write access with updating functions (should clear the contents of the file)
            new_data.write(write)
            new_data.close()
        self.file.close()
        self.file_watched.close()
        self.file_user_suggested.close()

    def run(self):
        # LIST
        watched_shows_list = []  # ; Finished movies list
        usernames = []  # ;User list without counter
        unknown_users = []  # ;Names that aren't in the counter file go here
        # DICT
        user_data_dict = {}  # ;Counters
        while len(self.show_data) != 0:  # ;Continuous loop that will only stop when the entries on the show_data list is 0
            if self.debug_mode == 1:
                self.dbg_data.update({
                    "watched_shows_list": watched_shows_list,
                    "usernames": usernames,
                    "user_data_dict": user_data_dict,
                    "unknown_users": unknown_users
                })
            else:
                if 'dbg_data' in vars(self).keys():
                    del self.dbg_data  # ;Removes 'self.dbg_data' from this class since self.debug_mode isn't 1

            first = self.show_data[0]  # ;Points to the first thing on the list
            p(f"\nSeries: {first[0]}\nSuggested By: {first[1]}\n")  # ;Shows selected show/series with whom suggested it
            command = input("Done watching? ")  # ;Waits for confirmation from user if the show one/more are watching is done
            p("-------------------------------------------------")

            if first[1] not in user_data_dict:
                user_data_dict.update({first[1]: 1})
            else:
                user_data_dict[first[1]] += 1
            usernames.append(first[1])

            if command in ["e", "E"]:  # ;If the input equals 'e', then start quit program sequence
                if randint(1, 100000) == 2 / 100000:  # ;Added a little fun to the mix
                    p("The cycle is broken! :D")
                self.remove_from_list(self.show_data, first, watched_shows_list)
                self.file_watched.write(f"{first[0]}\n")
                p(f"\nShows watched: {len(watched_shows_list)}\n\nWatched Shows: {watched_shows_list}")  # ;Shows current information
                self.save_to_counter_file_from_list(usernames, unknown_users)
                break

            self.list_data(search="dbg_data", use_alt_list=True)

            self.remove_from_list(self.show_data, first, watched_shows_list)
            self.file_watched.write(f"{first[0]} | {first[1]}\n")  # ;Saves the watched show/series with the user whom suggested it in a file for referrence
            p(f"\nShows watched: {len(watched_shows_list)}\n\nWatched Shows: {watched_shows_list}\n\nShows: {self.show_data}")  # ;Shows current information
            p("-------------------------------------------------")

            if len(self.show_data) == 0:
                p(f"Show List is empty\nSaving Usernames to {self.filename[:self.filename.index('.')]}_user_suggestion.txt")
                self.save_to_counter_file_from_list(usernames, unknown_users)
                break

# ;ShowTime("Shows.txt").run()

class MovieNight:
    """
    Optionals
    --------------------------
    debug_mode
        0 = Off <-- Default
        1 = Lists
    """

    def __init__(self, file, **options):
        # OPTIONS
        self.debug_mode = options.get("debug_mode", 0)
        # FILE
        self.file = open(file, "r+")
        self.filename = file
        # INT
        self.movie_data_len = 0
        # LIST
        self.movie_data = []
        self.contents = self.file.read().split("\n")
        # DICT
        self.dbg_data = {}
        # DATETIME
        self.run_date = f"{datetime.now().strftime('%Y-%m-%d %I:%M %p')}"
        # CODE
        if os.path.exists(file) is True:
            self.file_watched = open(f"{file[:file.index('.')]}_watched.txt", "a")
        else:
            self.file_watched = open(f"{file[:file.index('.')]}_watched.txt", "w+")
            p(f"Created {file}_watched.txt")

        if os.path.exists(f"{file[:file.index('.')]}_user_suggestion.txt") is True:
            self.file_user_suggested = open(f"{file[:file.index('.')]}_user_suggestion.txt", "r+")
            self.suggested_data = self.file_user_suggested.read().split("\n")
        else:
            self.file_user_suggested = open(f"{file[:file.index('.')]}_user_suggestion.txt", "w+")
            p(f"Created '{file[:file.index('.')]}_user_suggestion.txt'")
        self.file_watched.write(f"\n==========================\n{self.run_date}\n==========================\n")

        for suggestion in self.contents:
            if suggestion in ["", "\n", " "]:
                pass
            else:
                data = suggestion.split(" | ")
                self.movie_data.append([data[0], data[1]])
                self.movie_data_len += 1

    def remove_from_list(self, refer, var, saver):
        saver.append(var)  # ;Puts watched movie in watched_movies_list
        refer.remove(var)  # ;Removes currently picked movie from the mutable_movies_list

    def list_data(self, **options):
        # OPTIONS
        list_data_get = options.get("search", None)
        # CODE
        if self.debug_mode == 1:
            p("\t| DEBUG LIST DATA\n\t---------------------------------------------")
            for list_data in vars(self):
                if type(vars(self)[list_data]) is list or type(vars(self)[list_data]) is dict:
                    if list_data_get is None:
                        p(f"\t|\t{list_data}: {vars(self)[list_data]}")
                    else:
                        list_data_get_alternative_listing = options.get("use_alt_list", True)
                        if list_data == list_data_get:
                            if list_data_get_alternative_listing is True:
                                p(f"\t|\t{list_data}")
                                for nested_data in vars(self)[list_data]:
                                    p(f"\t|\t|\t{nested_data}: {vars(self)[list_data][nested_data]}")
                            else:
                                p(f"\t|\t{list_data}: {vars(self)[list_data]}")
            p("\t---------------------------------------------\n-------------------------------------------------")

    def save_to_counter_file_from_list(self, main_list, main_list_unknowns):
        # CODE
        with open(f"{self.filename[:self.filename.index('.')]}_user_suggestion.txt", "r") as counter_file:  # ;Opens the counter file (it should be FILE_user_suggestion.txt)
            counter_file_contents = counter_file.read()
            counter_file_table = counter_file_contents.split("\n")  # ;Converts string to list
            user_table = {}  # ;Usernames with counters
            for user in counter_file_table:  # ;Loops through the converted string
                if user not in ["", "\n", " "]:  # ;Filters unneeded content such as lines with just spaces, empty newlines and empty strings
                    user_data = user.split(": ")
                    user_table.update({user_data[0]: int(user_data[1])})

            for username in main_list:  # ;Loops through the usernames list
                if username in user_table.keys():  # ;Checks if the 'username' is in the 'user_table', if not skip this and put it in 'unknown_usernames'
                    user_table[username] += 1
                    counter_file_contents = counter_file_contents.replace(f"{username}: {user_table[username] - 1}\n", f"{username}: {user_table[username]}\n")
                else:
                    if username not in main_list_unknowns:  # ;Checks if the 'username' is in 'unknown_users', if not add it, this is only executed when the 'username' is not in the 'user_table'
                        main_list_unknowns.append(username)  # ;Add 'username' to 'unknown_users' list
                        counter_file_contents += f"{username}: 1\n"  # ;Add 'username' with the value of 1 to the 'counter_file_contents'
                        user_table.update({username: 1})  # ;Update the 'user_table' by adding the unknown username to the list with the value of 1
            write = counter_file_contents  # ;Transfer string to a new string
            counter_file.close()
        with open(f"{self.filename[:self.filename.index('.')]}_user_suggestion.txt", "w+") as new_data:  # ;Opens the 'FILE_user_suggestion.txt' with write access with updating functions (should clear the contents of the file)
            new_data.write(write)
            new_data.close()
        self.file.close()
        self.file_watched.close()
        self.file_user_suggested.close()

    def roll_dice(self):
        # LIST
        watched_movies_list = []  # ;Finished movies list
        usernames = []  # ;User list without counter (it's literally 'watched_movies_list' without the movie being added)
        unknown_users = []  # ;Names that aren't in the counter file go here
        # DICT
        user_data_dict = {}  # ;Counters
        # CODE
        while len(self.movie_data) != 0:  # ;Continuous loop that will only stop when the entries on the 'show_data' list is 0
            if self.debug_mode == 1:
                self.dbg_data({
                    "watched_movies_list": watched_movies_list,
                    "usernames": usernames,
                    "user_data_dict": user_data_dict,
                    "unknown_users": unknown_users
                })
            else:
                if 'dbg_data' in vars(self).keys():
                    del self.dbg_data

            pick = choice(self.movie_data)  # ;Chooses movie randomly
            pick_movie = pick[0]  # ;Movie
            pick_suggested_by = pick[1]  # ;Gets the user who suggested the movie
            p(f"Movie Picked '{pick}'\nSuggested By: {pick_suggested_by}\n")  # ;Chooses movie randomly and shows who suggested it
            command = input("Is movie done? ")  # ;Waits for confirmation from user if the show one/more are watching is done
            p("-------------------------------------------------")

            if pick_suggested_by not in user_data_dict:
                user_data_dict.update({pick_suggested_by: 1})
            else:
                user_data_dict[pick_suggested_by] += 1
            usernames.append(pick_suggested_by)

            if command in ["e", "E"]:  # ;If the input equals 'e', then start quit program sequence
                p("The cycle is broken! :D", cond=randint(1, 100000), value=2 / 100000)
                self.remove_from_list(self.movie_data, pick, watched_movies_list)
                self.file_watched.write(f"{pick_movie} | {pick_suggested_by}\n")  # ;Save the watched movie with whom suggested it in a file for referrence
                p(f"\nMovies watched: {len(watched_movies_list)}\nWatched Movies: {watched_movies_list}\nMovie List: {self.movie_data}\n")  # ;Shows current information
                p(f"Saving Suggestion counters to {self.filename[:self.filename.index('.')]}_user_suggestion.txt")
                self.save_to_counter_file_from_list(usernames, unknown_users)
                break

            self.list_data(search="dbg_data", use_alt_list=True)

            self.remove_from_list(self.movie_data, pick, watched_movies_list)
            self.file_watched.write(f"{pick_movie} | {pick_suggested_by}\n")  # ;Save the watched movie with whom suggested it in a file for referrence
            p(f"\nMovies watched: {len(watched_movies_list)}\n\nWatched Movies: {watched_movies_list}\n\nMovie List: {self.movie_data}\n")  # ;Shows current information
            p("-------------------------------------------------")

            if len(self.movie_data) == 0:
                p(f"Show List is empty\nSaving Suggestion counters to {self.filename[:self.filename.index('.')]}_user_suggestion.txt")
                self.save_to_counter_file_from_list(usernames, unknown_users)
                break

movies = MovieNight("Movies.txt")
movies.roll_dice()
