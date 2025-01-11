import time

import codecs

from typing import Any, Dict, Optional

from .game.hex import HexGame


class HumanAgent:
    """Interactive human player."""

    def __init__(self):
        self.game = HexGame()
        self.last_move = None
        self.settings: Dict[str, Any] = {}

    def reset(self) -> None:
        """Start a new game."""
        self.game.reset()

    def seed(self, seed: Optional[int] = None) -> None:
        """Seed random number generator."""
        pass

    def choose_action(self) -> int:
        """Plan next move."""
        print_board(self.game.io, self.game.state.board, self.last_move)
        move = ask_move(self.game.io,
                        self.game.state.board,
                        self.game.state.legal_moves)
        return move

    def execute_action(self, move: int) -> int:
        """Execute move.
        :returns: Game result
        """
        self.game.step(move)
        self.last_move = move
        return self.game.state.result


def ask_move(io, board, moves):
    while True:
        # move_txt = input('Your move? ')
        move_txt = txt_read(r"D:\Desktop\azalea_hex\azalea_hex\game.txt")
        try:
            move = io.parse_move(board, moves, move_txt)
            if move in moves:
                return move
        except io.ParseError:
            print(io.ParseError)
            print('illegal move:', move_txt)



def txt_read(filename):
    # 以只读方式打开原文件，并用 utf-8_sig 解码，得到字符串类型的内容
    with codecs.open(filename, 'r', 'utf_8_sig') as f:
        content = f.read()

    # 将内容重新编码为 utf-8 格式，并写回到原文件中
    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write(content)
    time.sleep(0.1)

    # 读取文件名为 game.txt 的文本文件
    move_string = None

    with open(filename, 'r', encoding='utf-8') as f:
        # 读取文件中的前两行数据，并去除两端空格
        line1 = f.readline().strip()
        # 替换BOM字符
        line1 = line1.replace('\ufeff', '')
        line2 = f.readline().strip()
        # 替换BOM字符
        line2 = line2.replace('\ufeff', '')

        # 持续读取和处理前两行数据
        while True:
            # 读取文件中的前两行数据，并去除两端空格
            f.seek(0)
            new_line1 = f.readline().strip()
            # 替换BOM字符
            new_line1 = new_line1.replace('\ufeff', '')
            new_line2 = f.readline().strip()
            # 替换BOM字符
            new_line2 = new_line2.replace('\ufeff', '')

            if new_line1 != line1 or new_line2 != line2:
                # 如果一行或两行数据都被修改，输出新的两行数据
                line1, line2 = new_line1, new_line2
                # print(len(line1))
                # print(line1)
                # print(repr(new_line1))
                # print(len(line2))
                move_string = line1 + line2

                print(f"Player moves to positions {move_string}")

            # 延迟一段时间，等待文件更新
            time.sleep(0.1)
            if move_string is not None:
                return move_string


# def print_board(io, board, computer_move):
#     """"用于打印棋盘和落子信息"""
#     print('\033[2J')
#     io.print_board(board)
#     if computer_move:
#         move_txt = io.format_move(board, computer_move)
#         # print(f'value: {value:.2f}')
#         print(f'last move: {move_txt}')

# def print_board(io, board, computer_move, move_file="D:/Desktop/azalea_hex/azalea_hex/print.txt"):
#     print('\033[2J')
#     io.print_board(board)
#     if computer_move:
#         move_txt = io.format_move(board, computer_move)
#         print(f'last move: {move_txt}')
#         with open(move_file, 'w') as f:
#             f.write(f'{move_txt}\n')

# def print_board(io, board, computer_move, move_file="D:/Desktop/azalea_hex/azalea_hex/print.txt"):
#     print('\033[2J')
#     io.print_board(board)
#     if computer_move:
#         move_txt = io.format_move(board, computer_move)
#         print(f'last move: {move_txt[0]}\n{move_txt[1:]}')
#         with open(move_file, 'w') as f:
#             f.write(f'{move_txt[0]}\n{move_txt[1:]}\n')

def print_board(io, board, computer_move, move_file="D:/Desktop/azalea_hex/azalea_hex/print.txt"):
    print('\033[2J')
    io.print_board(board)
    if computer_move:
        move_txt = io.format_move(board, computer_move)
        move_txt_lines = [f'{move_txt[0]}\n', f'{move_txt[1:]}\n']
        print(f'last move: {move_txt}')
        with open(move_file, 'w') as f:
            f.writelines(move_txt_lines)