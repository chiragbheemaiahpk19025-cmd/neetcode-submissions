class Solution:
    def _rowCheck(self, board: List[List[str]]) -> bool:
        r, c = 9, 9
        for i in range(r):
            hash_map = defaultdict(int)
            for j in range(c):
                number = int(board[i][j]) if board[i][j] != '.'else None
                if number is not None:
                    hash_map[number] += 1
                    if hash_map[number] > 1:
                        return False

        return True



    def _colCheck(self, board: List[List[str]]) -> bool:
        r, c = 9, 9
        for i in range(r):
            hash_map = defaultdict(int)
            for j in range(c):
                number = int(board[j][i]) if board[j][i] != '.'else None
                if number is not None:
                    hash_map[number] += 1
                    if hash_map[number] > 1:
                        return False

        return True


    def _gridCheck(self, board: List[List[str]]) -> bool:
        r, c = 9, 9
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                hash_map = defaultdict(int)
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        number = int(board[k][l]) if board[k][l] != '.'else None
                        if number is not None:
                            hash_map[number] += 1
                            if hash_map[number] > 1:

                                return False
        return True



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print(self._rowCheck(board))
        print(self._colCheck(board))
        print(self._gridCheck(board))

        return self._rowCheck(board) and self._colCheck(board) and self._gridCheck(board)
            