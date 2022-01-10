import pygame
import sys
import math
BLACK = (65, 74, 76)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 640
WINDOW_WIDTH = 640

WHITE_PAWN = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\white_pawn.png')
WHITE_KNIGHT = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\white_knight.png')
WHITE_BISHOP = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\white_bishop.png')
WHITE_ROOK = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\white_rook.png')
WHITE_QUEEN = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\white_queen.png')
WHITE_KING = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\white_king.png')
BLACK_PAWN = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\black_pawn.png')
BLACK_KNIGHT = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\black_knight.png')
BLACK_BISHOP = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\black_bishop.png')
BLACK_ROOK = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\black_rook.png')
BLACK_QUEEN = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\black_queen.png')
BLACK_KING = pygame.image.load(r'C:\Users\Joshua\Pictures\chess\black_king.png')

locations = [[(40, 40), (40, 120), (40, 200), (40, 280), (40, 360), (40, 440), (40, 520), (40, 600)], [(120, 40),
             (120, 120), (120, 200), (120, 280), (120, 360), (120, 440), (120, 520), (120, 600)], [(200, 40), (200, 120),
             (200, 200), (200, 280), (200, 360), (200, 440), (200, 520), (200, 600)], [(280, 40), (280, 120), (280, 200),
             (280, 280), (280, 360), (280, 440), (280, 520), (280, 600)], [(360, 40), (360, 120), (360, 200), (360, 280),
             (360, 360), (360, 440), (360, 520), (360, 600)], [(440, 40), (440, 120), (440, 200), (440, 280), (440, 360),
             (440, 440), (440, 520), (440, 600)], [(520, 40), (520, 120), (520, 200), (520, 280), (520, 360), (520, 440),
             (520, 520), (520, 600)], [(600, 40), (600, 120), (600, 200), (600, 280), (600, 360), (600, 440), (600, 520),
             (600, 600)]]


class King(pygame.sprite.Sprite):
    def __init__(self, isWhite):
        super().__init__()

        self.isWhite = isWhite
        self.clicked = False

        if self.isWhite:
            self.image = WHITE_KING
            self.image = pygame.transform.scale(self.image, (64,64))
            self.rect = self.image.get_rect(center=(360,600))

        else:
            self.image = BLACK_KING
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect(center=(360, 40))




class Queen(pygame.sprite.Sprite):
    def __init__(self, isWhite):
        super().__init__()

        self.isWhite = isWhite
        self.clicked = False
        self.val = 9
        self.dead = False

        if isWhite:
            self.image = WHITE_QUEEN
            self.image = pygame.transform.scale(self.image, (64,64))
            self.rect = self.image.get_rect(center=(280,600))
        else:
            self.image = BLACK_QUEEN
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect(center=(280, 40))




class Rook(pygame.sprite.Sprite):
    def __init__(self, isWhite, num):
        super().__init__()

        self.isWhite = isWhite
        self.num = num
        self.clicked = False
        self.isDead = False
        self.val = 5

        if self.isWhite:
            self.image = WHITE_ROOK
            self.image = pygame.transform.scale(self.image, (64,64))
            if self.num == 0:
                self.rect = self.image.get_rect(center=(40,600))
            else:
                self.rect = self.image.get_rect(center=(600,600))

        else:
            self.image = BLACK_ROOK
            self.image = pygame.transform.scale(self.image, (64,64))
            if self.num == 0:
                self.rect = self.image.get_rect(center=(40,40))
            else:
                self.rect = self.image.get_rect(center=(600,40))


class Bishop(pygame.sprite.Sprite):
    def __init__(self, isWhite, num):
        super().__init__()

        self.isWhite = isWhite
        self.num = num
        self.clicked = False
        self.isDead = False
        self.val = 3

        if self.isWhite:
            self.image = WHITE_BISHOP
            self.image = pygame.transform.scale(self.image, (64,64))
            if self.num == 0:
                self.rect = self.image.get_rect(center=(120,600))
            else:
                self.rect = self.image.get_rect(center=(520,600))

        else:
            self.image = BLACK_BISHOP
            self.image = pygame.transform.scale(self.image, (64,64))
            if self.num == 0:
                self.rect = self.image.get_rect(center=(120,40))
            else:
                self.rect = self.image.get_rect(center=(520,40))



class Knight(pygame.sprite.Sprite):
    def __init__(self, isWhite, num):
        super().__init__()

        self.isWhite = isWhite
        self.num = num
        self.clicked = False
        self.isDead = False
        self.val = 3

        if self.isWhite:
            self.image = WHITE_KNIGHT
            self.image = pygame.transform.scale(self.image, (64,64))
            if self.num == 0:
                self.rect = self.image.get_rect(center=(200,600))
            else:
                self.rect = self.image.get_rect(center=(440,600))

        else:
            self.image = BLACK_KNIGHT
            self.image = pygame.transform.scale(self.image, (64,64))
            if self.num == 0:
                self.rect = self.image.get_rect(center=(200,40))
            else:
                self.rect = self.image.get_rect(center=(440,40))


class Pawn(pygame.sprite.Sprite):
    def __init__(self, isWhite, num):
        super().__init__()


        self.isWhite = isWhite
        self.num = num
        self.clicked = False
        self.isDead = False
        self.val = 1

        if self.isWhite:
            self.image = WHITE_PAWN
            self.image = pygame.transform.scale(self.image, (64,64))
            if self.num == 0:
                self.rect = self.image.get_rect(center=(40,520))
            elif self.num == 1:
                self.rect = self.image.get_rect(center=(120,520))
            elif self.num == 2:
                self.rect = self.image.get_rect(center=(200,520))
            elif self.num == 3:
                self.rect = self.image.get_rect(center=(280,520))
            elif self.num == 4:
                self.rect = self.image.get_rect(center=(360,520))
            elif self.num == 5:
                self.rect = self.image.get_rect(center=(440,520))
            elif self.num == 6:
                self.rect = self.image.get_rect(center=(520,520))
            else:
                self.rect = self.image.get_rect(center=(600,520))

        else:
            self.image = BLACK_PAWN
            self.image = pygame.transform.scale(self.image, (64,64))
            if self.num == 0:
                self.rect = self.image.get_rect(center=(40,120))
            elif self.num == 1:
                self.rect = self.image.get_rect(center=(120,120))
            elif self.num == 2:
                self.rect = self.image.get_rect(center=(200,120))
            elif self.num == 3:
                self.rect = self.image.get_rect(center=(280,120))
            elif self.num == 4:
                self.rect = self.image.get_rect(center=(360,120))
            elif self.num == 5:
                self.rect = self.image.get_rect(center=(440,120))
            elif self.num == 6:
                self.rect = self.image.get_rect(center=(520,120))
            else:
                self.rect = self.image.get_rect(center=(600,120))



def drawGrid():
    blockSize = 80 #Set the size of the grid block
    z = False
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            if z:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, BLACK, rect, 0)
            z = not z
        z = not z

def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(None)
    return board

def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = [int(v // 80) for v in mouse_pos]
    try:
        if x >= 0 and y >= 0: return (board[y][x], x, y)
    except IndexError: pass
    return None, None, None





def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(WHITE)
    board = create_board()


    pieces_group = pygame.sprite.LayeredUpdates()
    pawn_group = pygame.sprite.Group()
    rook_group = pygame.sprite.Group()
    bishop_group = pygame.sprite.Group()
    knight_group = pygame.sprite.Group()
    king_group = pygame.sprite.Group()
    queen_group = pygame.sprite.Group()
    white_group = pygame.sprite.Group()
    black_group = pygame.sprite.Group()

    ##--------KINGS----------------------------##
    whiteKing = King(True)
    pieces_group.add(whiteKing)
    king_group.add(whiteKing)
    white_group.add(whiteKing)


    blackKing = King(False)
    pieces_group.add(blackKing)
    king_group.add(blackKing)
    white_group.add(blackKing)


    ##--------QUEENS-----------------------------##
    whiteQueen = Queen(True)
    pieces_group.add(whiteQueen)
    queen_group.add(whiteQueen)
    white_group.add(whiteQueen)

    blackQueen = Queen(False)
    pieces_group.add(blackQueen)
    queen_group.add(blackQueen)
    black_group.add(blackQueen)


    ##-----------ROOKS--------------------------##
    whiteRook0 = Rook(True, 0)
    pieces_group.add(whiteRook0)
    rook_group.add(whiteRook0)
    white_group.add(whiteRook0)

    whiteRook1 = Rook(True, 1)
    pieces_group.add(whiteRook1)
    rook_group.add(whiteRook1)
    white_group.add(whiteRook1)

    blackRook0 = Rook(False, 0)
    pieces_group.add(blackRook0)
    rook_group.add(blackRook0)
    black_group.add(blackRook0)

    blackRook1 = Rook(False, 1)
    pieces_group.add(blackRook1)
    rook_group.add(blackRook1)
    black_group.add(blackRook1)


    ##-----------BISHOPS--------------------------##
    whiteBishop0 = Bishop(True, 0)
    pieces_group.add(whiteBishop0)
    bishop_group.add(whiteBishop0)
    white_group.add(whiteBishop0)

    whiteBishop1 = Bishop(True, 1)
    pieces_group.add(whiteBishop1)
    bishop_group.add(whiteBishop1)
    white_group.add(whiteBishop1)

    blackBishop0 = Bishop(False, 0)
    pieces_group.add(blackBishop0)
    bishop_group.add(blackBishop0)
    black_group.add(blackBishop0)

    blackBishop1 = Bishop(False, 1)
    pieces_group.add(blackBishop1)
    bishop_group.add(blackBishop1)
    black_group.add(blackBishop1)

    ##-----------KNIGHTS--------------------------##
    whiteKnight0 = Knight(True, 0)
    pieces_group.add(whiteKnight0)
    knight_group.add(whiteKnight0)
    white_group.add(whiteKnight0)

    whiteKnight1 = Knight(True, 1)
    pieces_group.add(whiteKnight1)
    knight_group.add(whiteKnight1)
    white_group.add(whiteKnight1)

    blackKnight0 = Knight(False, 0)
    pieces_group.add(blackKnight0)
    knight_group.add(blackKnight0)
    black_group.add(blackKnight0)

    blackKnight1 = Knight(False, 1)
    pieces_group.add(blackKnight1)
    knight_group.add(blackKnight1)
    black_group.add(blackKnight1)

    ##-----------PAWN--------------------------##
    whitePawn0 = Pawn(True, 0)
    pieces_group.add(whitePawn0)
    pawn_group.add(whitePawn0)
    white_group.add(whitePawn0)

    whitePawn1 = Pawn(True, 1)
    pieces_group.add(whitePawn1)
    pawn_group.add(whitePawn1)
    white_group.add(whitePawn1)

    whitePawn2 = Pawn(True, 2)
    pieces_group.add(whitePawn2)
    pawn_group.add(whitePawn2)
    white_group.add(whitePawn2)

    whitePawn3 = Pawn(True, 3)
    pieces_group.add(whitePawn3)
    pawn_group.add(whitePawn3)
    white_group.add(whitePawn3)

    whitePawn4 = Pawn(True, 4)
    pieces_group.add(whitePawn4)
    pawn_group.add(whitePawn4)
    white_group.add(whitePawn4)

    whitePawn5 = Pawn(True, 5)
    pieces_group.add(whitePawn5)
    pawn_group.add(whitePawn5)
    white_group.add(whitePawn5)

    whitePawn6 = Pawn(True, 6)
    pieces_group.add(whitePawn6)
    pawn_group.add(whitePawn6)
    white_group.add(whitePawn6)

    whitePawn7 = Pawn(True, 7)
    pieces_group.add(whitePawn7)
    pawn_group.add(whitePawn7)
    white_group.add(whitePawn7)

    blackPawn0 = Pawn(False, 0)
    pieces_group.add(blackPawn0)
    pawn_group.add(blackPawn0)
    black_group.add(blackPawn0)

    blackPawn1 = Pawn(False, 1)
    pieces_group.add(blackPawn1)
    pawn_group.add(blackPawn1)
    black_group.add(blackPawn1)

    blackPawn2 = Pawn(False, 2)
    pieces_group.add(blackPawn2)
    pawn_group.add(blackPawn2)
    black_group.add(blackPawn2)

    blackPawn3 = Pawn(False, 3)
    pieces_group.add(blackPawn3)
    pawn_group.add(blackPawn3)
    black_group.add(blackPawn3)

    blackPawn4 = Pawn(False, 4)
    pieces_group.add(blackPawn4)
    pawn_group.add(blackPawn4)
    black_group.add(blackPawn4)

    blackPawn5 = Pawn(False, 5)
    pieces_group.add(blackPawn5)
    pawn_group.add(blackPawn5)
    black_group.add(blackPawn5)

    blackPawn6 = Pawn(False, 6)
    pieces_group.add(blackPawn6)
    pawn_group.add(blackPawn6)
    black_group.add(blackPawn6)

    blackPawn7 = Pawn(False, 7)
    pieces_group.add(blackPawn7)
    pawn_group.add(blackPawn7)
    black_group.add(blackPawn7)


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if event.button == 1:
                    for spr in pieces_group:
                        if spr.rect.collidepoint((mx, my)):
                            spr.clicked = True
                            pieces_group.move_to_front(spr)


            if event.type == pygame.MOUSEBUTTONUP:
                for spr in pieces_group:
                    if spr.clicked == True:
                        spr.clicked = False

                        piece, x, y = get_square_under_mouse(board)
                        spr.rect.x = locations[x][y][0] - (spr.rect.width / 2)
                        spr.rect.y = locations[x][y][1] - (spr.rect.height / 2)


                        for spr2 in pieces_group:
                            if spr2.rect.x == spr.rect.x and spr2.rect.y == spr.rect.y and spr2 is not spr:
                                spr2.kill()



        piece, x, y = get_square_under_mouse(board)

        for spr in pieces_group:
            if spr.clicked == True:
                pos = pygame.mouse.get_pos()
                spr.rect.x = pos[0] - (spr.rect.width/2)
                spr.rect.y = pos[1] - (spr.rect.height / 2)


        SCREEN.fill(WHITE)
        drawGrid()
        if x != None:
            rect = (x * 80, y * 80, 80, 80)
            pygame.draw.rect(SCREEN, (255, 0, 0, 50), rect, 2)


        pieces_group.draw(SCREEN)
        pygame.display.update()


main()