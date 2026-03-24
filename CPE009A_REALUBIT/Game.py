import random
from Novice import Novice
from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician
from Boss import Boss


# Status display of both characters
def show_status(char1, char2):
    print(f"{char1.getUsername()} HP: {char1.getHp()} | {char2.getUsername()} HP: {char2.getHp()}")

# Role selection menu. include_novice=True adds the Novice option for single player mode.   

def select_role(username, include_novice=False):
    roles = []
    if include_novice:
        roles.append(("Novice", Novice))
    roles.append(("Swordsman", Swordsman))
    roles.append(("Archer", Archer))
    roles.append(("Magician", Magician))

    print("\nSelect your role:")
    for i, (name, _) in enumerate(roles, 1):
        print(f"  [{i}] {name}")

    while True:
        choice = input("  Choice: ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(roles):
                name, cls = roles[idx]
                print(f"  Role selected: {name}")
                return cls(username)
        except ValueError:
            pass
        print("  Invalid choice. Try again.")

# Player's turn

def player_turn(player, opponent):
    print(f"\n{player.getUsername()}'s turn!")
    show_status(player, opponent)
    print("  [1] Basic Attack")

    if isinstance(player, Swordsman):
        print("  [2] Slash Attack")
    elif isinstance(player, Archer):
        print("  [2] Ranged Attack")
    elif isinstance(player, Magician):
        print("  [2] Magic Attack")
        print("  [3] Heal")

    while True:
        choice = input("  Choose: ").strip()
        if choice == "1":
            player.basicAttack(opponent)
            return
        elif choice == "2" and isinstance(player, Swordsman):
            player.slashAttack(opponent)
            return
        elif choice == "2" and isinstance(player, Archer):
            player.rangedAttack(opponent)
            return
        elif choice == "2" and isinstance(player, Magician):
            player.magicAttack(opponent)
            return
        elif choice == "3" and isinstance(player, Magician):
            player.heal()
            return
        print("  Invalid choice. Try again.")

# Program's turn

def computer_turn(boss, player):
    print(f"\n{boss.getUsername()}'s turn!")
    boss.basicAttack(player)

# Match Loop

    player.setHp(100)
    opponent.setHp(100)

    print(f"\n{'=' * 40}")
    print(f"  {player.getUsername()} vs {opponent.getUsername()}")
    print(f"{'=' * 40}")

    # Randomise who goes first for this match
    order = [player, opponent]
    random.shuffle(order)
    first, second = order
    print(f"  {first.getUsername()} goes first!\n")

    while player.getHp() > 0 and opponent.getHp() > 0:
        for attacker in [first, second]:
            if player.getHp() <= 0 or opponent.getHp() <= 0:
                break

            defender = opponent if attacker is player else player

            if attacker is player or pvp:
                player_turn(attacker, defender)
            else:
                computer_turn(attacker, defender)

    print(f"\n{'=' * 40}")
    if player.getHp() > 0:
        print(f"  {player.getUsername()} wins the match!")
        return True
    else:
        print(f"  {opponent.getUsername()} wins the match!")
        return False

#  Game modes


def single_player_mode():
    print("\n── Single Player ──")
    username = input("Enter your username: ").strip()
    player   = Novice(username)
    wins     = 0
    upgraded = False

    print(f"Welcome, {username}! You start as a Novice.")
    print("Defeat Monster twice to unlock an advanced role.\n")

    while True:
        opponent = Boss("Monster")
        won = play_match(player, opponent)

        if won:
            wins += 1
            print(f"  Total wins: {wins}")
            if wins >= 2 and not upgraded:
                print("\n  You've earned 2 wins - choose an advanced role!")
                player   = select_role(username, include_novice=False)
                upgraded = True

        print("\n  [1] Play again   [2] Main menu")
        if input("  Choice: ").strip() != "1":
            break

    return wins

def pvp_mode():
    print("\n── Player vs Player ──")
    p1_name = input("Player 1 username: ").strip()
    p2_name = input("Player 2 username: ").strip()
    p1_wins = 0
    p2_wins = 0

    while True:
        print(f"\n{p1_name}, choose your role:")
        player1 = select_role(p1_name, include_novice=True)

        print(f"\n{p2_name}, choose your role:")
        player2 = select_role(p2_name, include_novice=True)

        if play_match(player1, player2, pvp=True):
            p1_wins += 1
        else:
            p2_wins += 1

        print("\n  [1] Play again   [2] Main menu")
        if input("  Choice: ").strip() != "1":
            break

    return p1_name, p1_wins, p2_name, p2_wins

#  Entry point

def show_wins(sp_wins, pvp_record):
    print(f"\n{'=' * 40}")
    print("  WIN RECORDS")
    print(f"{'=' * 40}")
    print(f"  Single Player : {sp_wins} win(s)")
    print("  Player vs Player:")
    if pvp_record:
        for name, wins in pvp_record.items():
            print(f"    {name}: {wins} win(s)")
    else:
        print("    No PvP matches played yet.")
    print(f"{'=' * 40}")


def main():
    print("=" * 40)
    print("      WELCOME TO THE GAME")
    print("=" * 40)

    sp_wins    = 0
    pvp_record = {}   # { username: total wins }

    while True:
        print("\n  [1] Single Player")
        print("  [2] Player vs Player")
        print("  [3] Show Wins")
        print("  [4] Exit")
        choice = input("  Choice: ").strip()

        if choice == "1":
            sp_wins += single_player_mode()
        elif choice == "2":
            p1_name, p1_wins, p2_name, p2_wins = pvp_mode()
            pvp_record[p1_name] = pvp_record.get(p1_name, 0) + p1_wins
            pvp_record[p2_name] = pvp_record.get(p2_name, 0) + p2_wins
        elif choice == "3":
            show_wins(sp_wins, pvp_record)
        elif choice == "4":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("  Invalid choice. Try again.")


if __name__ == "__main__":
    main()
