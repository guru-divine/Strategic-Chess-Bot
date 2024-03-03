import pygame as p
import engine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}

#Initialize a global dictionary of images. This will be callled once only
def loadImages():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "wR", "wN", "wB", "wQ", "wK", "bp", "wp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))



def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.GameState()
    # print(gs.board)
    loadImages() #load once
    running = True
    sqSelected = () #keep track of last click of the user (6,4)
    playerClicks = [] #keep track of player clicks: [(6,4), (4,4)]
    while(running):
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x, y) of cursor
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): #user clicked the same square twice
                    sqSelected = () #deselect
                    playerClicks = [] #clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if(len(playerClicks) == 2): #after 2nd click
                    if gs.board[playerClicks[0][0]][playerClicks[0][1]] == "--": #first click is on empty square
                        sqSelected = ()  # Reset the sqSelected value.
                        playerClicks = []  # Reset the playerClicks list.
                    else:
                        move = engine.Move(playerClicks[0], playerClicks[1], gs.board)
                        print(move.getChessNotation())
                        gs.makeMove(move)
                        sqSelected = ()
                        playerClicks = []

            drawGameState(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

#Draw the squares on the board
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    # colors = [p.Color("white"), p.Color("brown")]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



#Draw the pieces on the board
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))




if __name__ == "__main__":
    main()