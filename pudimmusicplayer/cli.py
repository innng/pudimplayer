"""Simple CLI for the music player."""

from PyInquirer import prompt


quit_option = "Quit"
play_option = "Start playing"
spotify_playlist_option = "Choose playlists from Spotify"
youtube_playlist_option = "Choose playlists from Youtbe"

main_question = [
    {
        "type": "list",
        "qmark": ".",
        "name": "main_question",
        "message": "Welcome to the pudim music player!",
        "choices": [spotify_playlist_option, youtube_playlist_option, play_option, quit_option],
    }
]

login_question = [
    {"type": "input", "qmark": ".", "name": "login", "message": "Login:"},
    {"type": "password", "qmark": ".", "name": "password", "message": "Password:"},
]

play_loop_exit = [
    {
        "type": "confirm",
        "name": "play_loop_exit",
        "message": "Pause music and go back to main menu?",
        "default": False,
    }
]


def _playlist_selection(playlists):
    return [
        {
            "type": "checkbox",
            "qmark": ".",
            "name": "playlist_selection_question",
            "message": "Select playlists:",
            "choices": [{"name": playlist} for playlist in playlists],
        },
    ]


if __name__ == "__main__":
    spotify_login = None
    spotify_psswd = None
    youtube_login = None
    youtube_psswd = None

    selected_playlists = []

    quit_selected = False
    pause_selected = False

    while not quit_selected:
        main_answer = prompt(main_question)["main_question"]

        if main_answer == quit_option:
            quit_selected = True

        elif main_answer == spotify_playlist_option:
            if not spotify_login or not spotify_psswd:
                answer = prompt(login_question)
                spotify_login = answer["login"]
                spotify_psswd = answer["password"]

            selected_playlists.extend(
                prompt(_playlist_selection(["a", "b", "c"]))["playlist_selection_question"]
            )

        elif main_answer == youtube_playlist_option:
            if not youtube_login or not youtube_psswd:
                answer = prompt(login_question)
                youtube_login = answer["login"]
                youtube_psswd = answer["password"]

            selected_playlists.extend(
                prompt(_playlist_selection(["a", "b", "c"]))["playlist_selection_question"]
            )

        elif main_answer == play_option:
            if len(selected_playlists) == 0:
                print("No playlist selected!")
            else:
                while not pause_selected:
                    answer = prompt(play_loop_exit)["play_loop_exit"]

                    if answer:
                        pause_selected = True
