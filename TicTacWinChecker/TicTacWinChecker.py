''' Question: Design an algorithm to figure out if someone has won a game of tic tac toe 
 * Time: 60 minutes 
 * 9/24/17 
 * Complexity O(n^2) in the worst case, if called on an empty board looking for s string of length 1. Most of the time it will be much quicker
 * 
 * In a game of tic tac toe, you can win with three in a row horizontally, vertically, or diagnally. You just have to check the board in these
 * 3 orientations for a group of 3 cells with the same piece in a row. We will assume the board is a one-dimensional list with 0 starting in the 
 * left corner, 1 to its right, and 3 beneth it. I generalized the algorithm to check any NxN board for strings of pieces of s length. 
 * The algoirthm is not optimized if we are going to use it many times. If you wanted to check for a winner after every move, you would want 
 * to save the board state and only take in the last move made to check if there is a winner. Then, you would just have to check the row, column, 
 * and diagnal that last move is a part of. 
 * @author Christopher 
 '''
class TicTacWinChecker(): 
    def checkWin(self, column):
        #if(column[0] is None): return None
        type = column[0]
        count = 0
        for x in column:
            if(x != type or type == 2): 
                count = 1
                type = x
            else:
                count += 1
                if(count == s): return type
        return None

    def checkDiagnals(self, board, n, s):
        # do all the diagnals going lrighteft starting in the top row
        x = 0
        for x in range(0, n-s+1):
                mod = x%n
                if((mod) <= (n-s)): 
                    y = x
                    diag = range(y, n*n, n+1)
                    #while y < n*n:
                    #    diag.append(board[y])
                     #   y += n+1
                    winner = self.checkWin(diag)
                    if(winner is not None): return winner
        # do all the diagnals going right in the left column
        x = n
        while x <= ((n*(n-s))):
            diag = range(x, n*n, n+1)
            winner = self.checkWin(diag)
            if(winner is not None): return winner
            x+=n

        # do all the diagnals going left starting in the right of the top row
        x = n-1
        for x in range(n-1, -2+s, -1):
                mod = x%n
                if((mod) >= (-1+s)): 
                    y = x
                    diag = range(y, n*n, n-1)
                    #while y < n*n:
                    #    diag.append(board[y])
                     #   y += n+1
                    winner = self.checkWin(diag)
                    if(winner is not None): return winner
        # do all the diagnals going left in the right column. Start at the right most cell of the second row
        x = 2*n - 1
        while x <= ((n*(n-s))):
            diag = range(x, n*n, n-1)
            winner = self.checkWin(diag)
            if(winner is not None): return winner
            x+=n

    def checkTicTacWin(self, board: "A list reprsenting the board state. We will assume the list is one-dimensional with 0 corresponding to the top left square.", n: "size of the board", s: "length of string of pieces needed to win" ):
        # 0 | 1 | 2
        # ---------
        # 3 | 4 | 5
        # ---------
        # 6 | 7 | 8
        # we will also assume that this list will have 2 for empty, 0 for 0's and 1 for X's  
        # there are only 8 ways and  you can win and 3 kinds of wins in a game of tic tac toe. So we can just check ieach way if it has three of the same to check for a winner
        # to generalize to an NxN board is relatively straightforward for the rows and columns for solutions, but the diagnals are more tricky. 
        # 
        #check all the horizontal rows for a winner 
        if(s > n or n<1 or s<1): return None
        x=0
        while x < (n*n):
            winner = self.checkWin(board[x:x+n]) 
            if(winner is not None):
                return winner
            else: x+=n

        #check all the vertical columns on the board
        x=0
        while x<n:
            winner = self.checkWin(range(x, n*n, n))
            if(winner is not None):
                return winner
            else: x+=1
        #check diagnals. Works for any board looking for a matching string of any length
        self.checkDiagnals(board, n, s)
        ''' This only works if the board is 3x3
        winner = __checkWin(filter(lambda y: return (y%(n+1) == 0, board))) 
        if(winner is not None):
            return winner
        while 
        winner = __checkWin((board[2], board[4], board[6])) 
        if(winner is not None):
            return winner
        '''
        #if a winner has not been found, return none
        return None
    

ttc = TicTacWinChecker()
board = [2, 2, 1, 2, 1, 1, 2, 1, 1, 0, 0, 2, 2, 1, 2, 1]
n = 4
s = 3

print(str(ttc.checkTicTacWin(board, n, s)) + " Wins!")    


