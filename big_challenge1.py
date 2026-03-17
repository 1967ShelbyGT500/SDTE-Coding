"""
Team captain selection program
By Captain Amazing
"""
MIN_PLAYERS = 11
MAX_PLAYERS = 20
TEAM_CAPTAIN = 3

player_list = [] # A list to store the names of the team players

def get_team_numbers():
    # Reads in a number of players and returns it
    numb_players = int(input("How many players: "))
    while numb_players < 11 or numb_players > 20:
        numb_players = int(input("That number was invalid, try again: "))
    return numb_players

def read_in_list(count):
    # Reads in the names of the players and saves to the list
    for i in range(count):
        player_list.append(input("Enter next player: "))

def show_team_captain():
    print(f"The team captain is {player_list[TEAM_CAPTAIN-1]}")

def main():
    # find the numbers of players
    player_count = get_team_numbers()
    # read in the list of players
    read_in_list(player_count)
    # print the team captain
    show_team_captain()

if __name__ == "__main__":
    main()