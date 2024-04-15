import random

class Board():

    def __init__(self):
        self.board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.generate_two()
        self.generate_two()
        self.max=2

    def generate_two(self):
        new_x=random.randint(0,3)
        new_y=random.randint(0,3)
        while(self.board[new_x][new_y]!=0):
            new_x=random.randint(0,3)
            new_y=random.randint(0,3)
        self.board[new_x][new_y]=2

    def visualize_board(self):
        print("_______________________________________________________________________________")
        for l1 in range(0,len(self.board)):
            string=""
            for l2 in range(0,len(self.board[l1])):
                string+=(str(self.board[l1][l2])+" "*(6-len(str(self.board[l1][l2]))))
            print()
            print(string)

    def right(self):
        for l1 in range(0,4):
            for l2 in range(3,0,-1):
                if(self.board[l1][l2]!=0):
                    if(self.board[l1][l2-1]==0):
                        self.board[l1][l2-1]=self.board[l1][l2]
                        self.board[l1][l2]=0
                    if(self.board[l1][l2]==self.board[l1][l2-1]):
                        self.board[l1][l2]=self.board[l1][l2-1]*2
                        if(self)
                        self.board[l1][l2-1]=0
            self.board[l1]=[x for x in self.board[l1] if x!=0]
            self.board[l1]=((4-len(self.board[l1]))*[0])+self.board[l1]
        self.generate_two()
        """
        for l1 in range(0,4):
            for l2 in range(0,3):
                if(self.board[l1][l2]!=0):
                    if(self.board[l1][l2+1]==0):
                        self.board[l1][l2+1]=self.board[l1][l2]
                        self.board[l1][l2]=0
                    if(self.board[l1][l2]==self.board[l1][l2+1]):
                        self.board[l1][l2+1]=self.board[l1][l2+1]*2
                        self.board[l1][l2]=0
            self.board[l1]=[x for x in self.board[l1] if x!=0]
            self.board[l1]=((4-len(self.board[l1]))*[0])+self.board[l1]
        self.generate_two()"""

    def left(self):
        for l1 in range(0,4):
            for l2 in range(0,3):
                if(self.board[l1][l2]!=0):
                    if(self.board[l1][l2+1]==0):
                        self.board[l1][l2+1]=self.board[l1][l2]
                        self.board[l1][l2]=0
                    if(self.board[l1][l2]==self.board[l1][l2+1]):
                        self.board[l1][l2]=self.board[l1][l2+1]*2
                        self.board[l1][l2+1]=0
            self.board[l1]=[x for x in self.board[l1] if x!=0]
            self.board[l1]=self.board[l1]+((4-len(self.board[l1]))*[0])
        self.generate_two()

    def up(self):
        self.board= list(map(list, zip(*self.board)))
        self.left()
        self.board= list(map(list, zip(*self.board)))

    def down(self):
        self.board= list(map(list, zip(*self.board)))
        self.right()
        self.board= list(map(list, zip(*self.board)))

    

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Get the transpose using zip()
transpose = list(map(list, zip(*matrix)))


game=Board()
x='lfdsjal'
while(x!='0'):
    game.visualize_board()
    x=input("Enter move: ")
    if(x=="r"):
        game.right()
    if(x=="l"):
        game.left()
    if(x=="u"):
        game.up()
    if(x=="d"):
        game.down()
            



