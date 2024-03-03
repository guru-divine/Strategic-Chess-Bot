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
        # IMAGES[piece] = p.transform.scale(p.image.load("img/" + piece + ".svg"), (SQ_SIZE, SQ_SIZE))



def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = engine.GameState()
    # print(gs.board)
    loadImages() #load once
    running = True
    while(running):
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            drawGameState(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

#Draw the squares on the board
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    # colors = [p.Color("white"), p.Color("lightgreen")]

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