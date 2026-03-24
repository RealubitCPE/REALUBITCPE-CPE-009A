import random
from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss

#Win counters
sp_wins = 0
pvp_wins = {}

def player_turn(player, opponent):
    print(f"\n{player.getUsername()}'s turn!")
    print(f"Your HP: {player.getHp()} | {opponent.getUsername()} HP: {opponent.getHp()}")
    print("[1] Basic Attack")

    if isinstance(player, Swordsman):
        print("[2] Slash Attack")
    elif isinstance(player, Archer):
        print("[2] Ranged Attack")
    elif isinstance(player, Magician):
        print("[2] Magic Attack")
        print("[3] Heal")

    choice = input("Choose: ")

    if choice == "1":
        player.basicAttack(opponent)
    elif choice == "2" and isinstance(player, Swordsman):
        player.slashAttack(opponent)
    elif choice == "2" and isinstance(player, Archer):
        player.rangedAttack(opponent)
    elif choice == "2" and isinstance(player, Magician):
        player.magicAttack(opponent)
    elif choice == "3" and isinstance(player, Magician):
        player.heal()
    else:
        print("Invalid choice, using Basic Attack.")
        player.basicAttack(opponent)

def computer_turn(boss, player):
    print(f"\n{boss.getUsername()}'s turn!")
    boss.basicAttack(player)


def pick_role(username, include_novice):
    print("\nSelect your role:")

    if include_novice:
        print("[1] Novice")
        print("[2] Swordsman")
        print("[3] Archer")
        print("[4] Magician")
    else:
        print("[1] Swordsman")
        print("[2] Archer")
        print("[3] Magician")

    while True:
        choice = input("Choice: ")

        if include_novice:
            if choice == "1":
                return Novice(username)
            elif choice == "2":
                return Swordsman(username)
            elif choice == "3":
                return Archer(username)
            elif choice == "4":
                return Magician(username)
            else:
                print("Invalid choice. Try again.")
        else:
            if choice == "1":
                return Swordsman(username)
            elif choice == "2":
                return Archer(username)
            elif choice == "3":
                return Magician(username)
            else:
                print("Invalid choice. Try again.")

def single_player():
    global sp_wins

    username = input("Enter your username: ")
    player = Novice(username)
    wins = 0
    upgraded = False

    print(f"Welcome {username}! You start as a Novice.")
    print("Win 2 matches to unlock a new role!")

    while True:
        opponent = Boss("Monster")
        player.setHp(100)
        opponent.setHp(100)

        print(f"\n=== {player.getUsername()} vs {opponent.getUsername()} ===")

        # Randomly decide who goes first
        if random.randint(0, 1) == 0:
            first = player
            second = opponent
        else:
            first = opponent
            second = player

        print(f"{first.getUsername()} goes first!")

        while player.getHp() > 0 and opponent.getHp() > 0:
            # First person attacks
            if first is player:
                player_turn(player, opponent)
            else:
                computer_turn(opponent, player)

            if player.getHp() <= 0 or opponent.getHp() <= 0:
                break

            # Second person attacks
            if second is player:
                player_turn(player, opponent)
            else:
                computer_turn(opponent, player)

        if player.getHp() > 0:
            print(f"\n{player.getUsername()} wins!")
            wins += 1
            sp_wins += 1
            print(f"Total wins: {wins}")

            if wins == 2 and not upgraded:
                print("You unlocked advanced roles!")
                player = pick_role(username, include_novice=False)
                upgraded = True
        else:
            print("\nMonster wins!")

        print("\n[1] Play again  [2] Main menu")
        if input("Choice: ") != "1":
            break

def pvp():
    global pvp_wins

    p1_name = input("Player 1 username: ")
    p2_name = input("Player 2 username: ")

    while True:
        print(f"\n{p1_name}, pick your role:")
        player1 = pick_role(p1_name, include_novice=True)

        print(f"\n{p2_name}, pick your role:")
        player2 = pick_role(p2_name, include_novice=True)

        player1.setHp(100)
        player2.setHp(100)

        print(f"\n=== {player1.getUsername()} vs {player2.getUsername()} ===")

        # Randomly decide who goes first
        if random.randint(0, 1) == 0:
            first = player1
            second = player2
        else:
            first = player2
            second = player1

        print(f"{first.getUsername()} goes first!")

        while player1.getHp() > 0 and player2.getHp() > 0:
            # First person attacks
            if first is player1:
                player_turn(player1, player2)
            else:
                player_turn(player2, player1)

            if player1.getHp() <= 0 or player2.getHp() <= 0:
                break

            # Second person attacks
            if second is player1:
                player_turn(player1, player2)
            else:
                player_turn(player2, player1)

        if player1.getHp() > 0:
            print(f"\n{player1.getUsername()} wins!")
            pvp_wins[p1_name] = pvp_wins.get(p1_name, 0) + 1
        else:
            print(f"\n{player2.getUsername()} wins!")
            pvp_wins[p2_name] = pvp_wins.get(p2_name, 0) + 1

        print("\n[1] Play again  [2] Main menu")
        if input("Choice: ") != "1":
            break

def show_wins():
    print("\n=== WIN RECORDS ===")
    print(f"Single Player wins: {sp_wins}")
    print("Player vs Player:")
    if len(pvp_wins) == 0:
        print("  No PvP matches played yet.")
    else:
        for name in pvp_wins:
            print(f"  {name}: {pvp_wins[name]} win(s)")

def main():
    print("=== WELCOME TO THE GAME ===")

    while True:
        print("\n[1] Single Player")
        print("[2] Player vs Player")
        print("[3] Show Wins")
        print("[4] Exit")

        choice = input("Choice: ")

        if choice == "1":
            single_player()
        elif choice == "2":
            pvp()
        elif choice == "3":
            show_wins()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()

if __name__ == "__main__":
    main()
