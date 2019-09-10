# tic-tac-toe는 두 명의 플레이어가 턴을 돌아가면서 1부터 9까지 포지션을 선택하는 게임 입니다.
# 선택된 포지션은 X나 0로 표시가 되며, 선택된 포지션은 다시 선택할 수가 없습니다.
# 게임 그리드는 3*3으로 다음과 같습니다.

# tic-tac-toe is a game which two players take each turns and choose numbers from 1 to 9
# each selected positions are marked either X or O and you cannot choose the position that is already occupied
# the grid looks like as follow

#   *   *
# 1 * 2 * 3
#   *   *
#   *   *
# 4 * 5 * 6
#   *   *
#   *   *
# 7 * 8 * 9
#   *   *

# 가로 세로 대각선으로 먼저 세 줄을 연속으로 만드는 플레이어가 우승하게 되며 무승부인 경우도 생깁니다.
# (매 턴마다 포지션을 입력해야 하지만, 출력은 게임이 끝이 났을 때만 하셔도 됩니다)
# 입력의 예 : Player 1 - please type a position (available position(s) are 1,2,3,4,5,6,7,8,9):
# 출력의 예: Win player is: player 1

# the player who makes a line horizontally or vertically or diagonally wins and there are a draw as well
# (you have got to input your position every single turn but you can print the grid only when the game is over if you wnat so)
# input example : Player 1 - please type a position (available position(s) are 1,2,3,4,5,6,7,8,9):
# output example : Win player is: player 1

#   *   *
# X * X * 0
#   *   *
#   *   *
# X * 0 * 6
#   *   *
#   *   *
# X * 8 * 9
#   *   *

class Tic_tac_toe:
    def __init__(self):
        self.available_position = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.bingo = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]

    def start(self):
        player_li = ['player1', 'player2']
        all_player_selection = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(len(player_li)) :
            player_li[i] = []

        while True :
            for i in range(len(player_li)) :
                player_name = "player {}".format(i+1)
                while True :
                    if len(self.available_position) == 0:
                        print("Game Draw")
                        self.output(all_player_selection)
                        return

                    player_selection = player_li[i]
                    try:
                        player_input = input("{} - please type a position (available position(s) are {}):".format(player_name, self.available_position))
                        player_input = int(player_input)
                        self.available_position.remove(player_input)
                        break
                    except Exception as e :
                            print("Wrong number. Select again")

                player_selection.append(player_input)
                for selection in range(len(all_player_selection)) :
                    if selection+1 == player_input :
                        if i == 0 :
                            all_player_selection[selection] = "O"
                            break
                        else :
                            all_player_selection[selection] = "X"
                            break
                if len(player_selection) >= 3 :
                    result = self.isBingo(player_name, player_selection)
                    if result != None :
                        print("Win player is: {}".format(result))
                        self.output(all_player_selection)
                        return

    def isBingo(self, player_name, player_selection):
        # sorting the list
        sorted_selection = []
        selection = []
        for i in player_selection :
            selection.append(i)
        for i in range(len(selection)) :
            min_val = min(selection)
            selection.remove(min_val)
            sorted_selection.append(min_val)

        # pick three
        for i in range(len(sorted_selection)) :
            picked_li = []
            for j in range(i+1, len(sorted_selection)) :
                for z in range(j+1, len(sorted_selection)) :
                    picked_li.append(sorted_selection[i])
                    picked_li.append(sorted_selection[j])
                    picked_li.append(sorted_selection[z])
                    if picked_li in self.bingo :
                        return player_name
                    else :
                        picked_li = []
        return None

    def output(self, all_player_selection):
        print("  *   *")
        for i in range(0, len(all_player_selection), 3) :
            print("{} * {} * {}".format(all_player_selection[i], all_player_selection[i+1], all_player_selection[i+2]))
        print("  *   *")



if __name__ == "__main__" :
    game = Tic_tac_toe()
    game.start()
