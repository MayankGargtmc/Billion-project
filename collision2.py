import pygame, sys, time
from pygame.locals import *
import math
from itertools import combinations

pygame.init()
clock = pygame.time.Clock()

screen_width = 800
screen_height = 800
surface = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Single Player Collision')

SW = 1
SE = 3
NW = 7
NE =9
N = 8
S = 2
W = 4
E = 6

speed=8

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (250,250,0)
brown = (244, 164, 96)

st = {'rect': pygame.Rect(400,690,20,20),'color':green,'dir':N}
b1 = {'rect': pygame.Rect(450,400,20,20),'color':yellow,'dir':NE}
b2 = {'rect': pygame.Rect(360,350,20,20),'color':yellow,'dir':S}
b3 = {'rect': pygame.Rect(400,330,20,20),'color':yellow,'dir':N}
b4 = {'rect': pygame.Rect(360,440,20,20),'color':yellow,'dir':N}
b5 = {'rect': pygame.Rect(440,360,20,20),'color':yellow,'dir':NW}
b6 = {'rect': pygame.Rect(350,400,20,20),'color':yellow,'dir':N}
b7 = {'rect': pygame.Rect(400,390,20,20),'color':yellow,'dir':S}
b8 = {'rect': pygame.Rect(440,440,20,20),'color':yellow,'dir':SE}
b9 = {'rect': pygame.Rect(400,420,20,20),'color':yellow,'dir':S}
b10 = {'rect': pygame.Rect(400,480,20,20),'color':yellow,'dir':S}

#block_set = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
block = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
block_set_2d = [list(i) for i in combinations(block, 2)]

c1=[45,45]
c2=[755,45]
c3=[755,755]
c4=[45,755]
#background
def background():
    surface.fill(brown)
    pygame.draw.rect(surface, black, (0, 0, 30, 800))
    pygame.draw.rect(surface, black, (0, 0, 800, 30))
    pygame.draw.rect(surface, black, (770, 0, 800, 800))
    pygame.draw.rect(surface, black, (0, 770, 800, 800))

    # bade patte
    pygame.draw.line(surface, black, (90, 120), (90, 680), 2)
    pygame.draw.line(surface, black, (110, 120), (110, 680), 2)
    pygame.draw.line(surface, black, (120, 90), (680, 90), 2)
    pygame.draw.line(surface, black, (120, 110), (680, 110), 2)
    pygame.draw.line(surface, black, (690, 120), (690, 680), 2)
    pygame.draw.line(surface, black, (710, 120), (710, 680), 2)
    pygame.draw.line(surface, black, (120, 690), (680, 690), 2)
    pygame.draw.line(surface, black, (120, 710), (680, 710), 2)

    # tedhi line
    pygame.draw.line(surface, black, (60, 60), (280, 280), 2)
    pygame.draw.line(surface, black, (60, 740), (280, 520), 2)
    pygame.draw.line(surface, black, (520, 280), (740, 60), 2)
    pygame.draw.line(surface, black, (520, 520), (740, 740), 2)

    # beech ke circle
    pygame.draw.circle(surface, black, (400, 400), 100, 2)
    pygame.draw.circle(surface, black, (400, 400), 110, 2)
    pygame.draw.circle(surface, black, (400, 400), 120, 2)

    # chote circle
    pygame.draw.circle(surface, red, (100, 120), 10, 0)
    pygame.draw.circle(surface, red, (120, 100), 10, 0)
    pygame.draw.circle(surface, red, (680, 100), 10, 0)
    pygame.draw.circle(surface, red, (700, 120), 10, 0)
    pygame.draw.circle(surface, red, (700, 680), 10, 0)
    pygame.draw.circle(surface, red, (680, 700), 10, 0)
    pygame.draw.circle(surface, red, (120, 700), 10, 0)
    pygame.draw.circle(surface, red, (100, 680), 10, 0)

    # beech the star
    pygame.draw.polygon(surface, blue, (
    (400, 300), (392.93, 392.93), (300, 400), (392.93, 407.07), (400, 500), (407.07, 407.07), (500, 400),
    (407.07, 392.93)))

    # holes
    pygame.draw.circle(surface, black, (45, 45), 15, 0)
    pygame.draw.circle(surface, black, (755, 45), 15, 0)
    pygame.draw.circle(surface, black, (755, 755), 15, 0)
    pygame.draw.circle(surface, black, (45, 755), 15, 0)

    # color bands
    pygame.draw.polygon(surface, green, ((0, 0), (60, 30), (30, 30), (30, 60)))
    pygame.draw.polygon(surface, green, ((800, 0), (770, 60), (770, 30), (740, 30)))
    pygame.draw.polygon(surface, green, ((800, 800), (770, 740), (770, 770), (740, 770)))
    pygame.draw.polygon(surface, green, ((0, 800), (30, 740), (30, 770), (60, 770)))
    pygame.display.flip()


def after_collision(bal1,bal2):
    if do_collide(bal1['rect'],bal2['rect']):
        if bal1['dir'] == N:
            if bal2['dir'] == NE:
                bal1['dir'] = NE
                bal2['dir'] = N
            if bal2['dir'] == E:
                bal1['dir'] = E
                bal1['dir'] = N
            if bal2['dir'] == SE:
                bal1['dir'] = SE
                bal2['dir'] = NE
            if bal2['dir'] == S:
                bal1['dir'] = S
                bal2['dir'] = N
            if bal2['dir'] == SW:
                bal1['dir'] = SW
                bal2['dir'] = NW
            if bal2['dir'] == W:
                bal1['dir'] = W
                bal2['dir'] = N
            if bal2['dir'] == NW:
                bal1['dir'] = W
                bal2['dir'] = N

        if bal1['dir'] ==NE:
            if bal2['dir'] == N:
                bal1['dir'] =NW
                bal2['dir'] =E
            if bal2['dir'] == E:
                bal1['dir'] =SE
                bal1['dir'] =N
            if bal2['dir'] ==SE:
                bal1['dir'] =SE
                bal2['dir'] =NE
            if bal2['dir'] ==S:
                bal1['dir'] =SE
                bal2['dir'] =E
            if bal2['dir'] ==SW:
                bal1['dir'] =SW
                bal2['dir'] =NE
            if bal2['dir'] ==W:
                bal1['dir'] =NW
                bal2['dir'] =N
            if bal2['dir'] ==NW:
                bal1['dir'] =NW
                bal2['dir'] =NE

        if bal1['dir'] ==E:
            if bal2['dir'] == N:
                bal1['dir'] =N
                bal2['dir'] =NE
            if bal2['dir'] == NE:
                bal1['dir'] =N
                bal1['dir'] =SE
            if bal2['dir'] ==SE:
                bal1['dir'] =S
                bal2['dir'] =NE
            if bal2['dir'] ==S:
                bal1['dir'] =S
                bal2['dir'] =E
            if bal2['dir'] ==SW:
                bal1['dir'] =S
                bal2['dir'] =SE
            if bal2['dir'] ==W:
                bal1['dir'] =W
                bal2['dir'] =E
            if bal2['dir'] ==NW:
                bal1['dir'] =N
                bal2['dir'] =NE

        if bal1['dir'] ==SE:
            if bal2['dir'] == N:
                bal1['dir'] =NE
                bal2['dir'] =E
            if bal2['dir'] == NE:
                bal1['dir'] =NE
                bal1['dir'] =SE
            if bal2['dir'] ==E:
                bal1['dir'] =NE
                bal2['dir'] =S
            if bal2['dir'] ==S:
                bal1['dir'] =SW
                bal2['dir'] =E
            if bal2['dir'] ==SW:
                bal1['dir'] =SW
                bal2['dir'] =SE
            if bal2['dir'] ==W:
                bal1['dir'] =SW
                bal2['dir'] =S
            if bal2['dir'] ==NW:
                bal1['dir'] =NE
                bal2['dir'] =SW

        if bal1['dir'] ==S:
            if bal2['dir'] == N:
                bal1['dir'] =N
                bal2['dir'] =S
            if bal2['dir'] == NE:
                bal1['dir'] =E
                bal1['dir'] =SE
            if bal2['dir'] ==E:
                bal1['dir'] =E
                bal2['dir'] =S
            if bal2['dir'] ==SE:
                bal1['dir'] =E
                bal2['dir'] =SW
            if bal2['dir'] ==SW:
                bal1['dir'] =W
                bal2['dir'] =SE
            if bal2['dir'] ==W:
                bal1['dir'] =W
                bal2['dir'] =S
            if bal2['dir'] ==NW:
                bal1['dir'] =W
                bal2['dir'] =SE

        if bal1['dir'] == SW:
            if bal2['dir'] == N:
                bal1['dir'] = NW
                bal2['dir'] = SW
            if bal2['dir'] == NE:
                bal1['dir'] = NE
                bal1['dir'] = SE
            if bal2['dir'] == SE:
                bal1['dir'] = SW
                bal2['dir'] = SW
            if bal2['dir'] == S:
                bal1['dir'] = W
                bal2['dir'] = SW
            if bal2['dir'] == W:
                bal1['dir'] = S
                bal2['dir'] = NW
            if bal2['dir'] == NW:
                bal1['dir'] = NW
                bal2['dir'] = SW
            if bal2['dir'] == E:
                bal1['dir'] = SE
                bal2['dir'] = S

        if bal1['dir'] ==W:
             if bal2['dir'] == N:
                    bal1['dir'] =N
                    bal2['dir'] =W
             if bal2['dir'] == NE:
                    bal1['dir'] =N
                    bal1['dir'] =NW
             if bal2['dir'] ==SE:
                    bal1['dir'] =S
                    bal2['dir'] =SW
             if bal2['dir'] ==S:
                    bal1['dir'] =S
                    bal2['dir'] =W
             if bal2['dir'] ==E:
                    bal1['dir'] =E
                    bal2['dir'] =W
             if bal2['dir'] ==SW:
                    bal1['dir'] =S
                    bal2['dir'] =NW
             if bal2['dir'] ==NW:
                    bal1['dir'] =N
                    bal2['dir'] =SW

        if bal1['dir'] ==NW:
             if bal2['dir'] == N:
                    bal1['dir'] =NE
                    bal2['dir'] =W
             if bal2['dir'] == NE:
                    bal1['dir'] =NE
                    bal1['dir'] =NW
             if bal2['dir'] ==SE:
                    bal1['dir'] =SE
                    bal2['dir'] =NE
             if bal2['dir'] ==S:
                    bal1['dir'] =SW
                    bal2['dir'] =W
             if bal2['dir'] ==SW:
                    bal1['dir'] =SW
                    bal2['dir'] =NW
             if bal2['dir'] ==W:
                    bal1['dir'] =SW
                    bal2['dir'] =N
             if bal2['dir'] ==E:
                    bal1['dir'] =NE
                    bal2['dir'] =N


def do_collide(r1,r2):
    for a,b in [(r1,r2),(r2,r1)]:
        if ((is_inside(a.left,a.top,b)) or (is_inside(a.right,a.top,b)) or (is_inside(a.left,a.bottom,b)) or (is_inside(a.right, a.bottom,b))):
            return True
    return False

def is_inside(x, y, r3):
    if ((x>r3.left) and (x<r3.right) and (y>r3.top) and (y<r3.bottom)):
        return True
    else:
        return False


start_ticks=pygame.time.get_ticks() #starter tick

radius = math.sqrt(math.pow(st['rect'].width, 2) + math.pow(st['rect'].height, 2))/1.5
radius_b = math.sqrt(math.pow(b1['rect'].width, 2) + math.pow(b1['rect'].height, 2))/2
#pygame.draw.rect(80,80,80,80)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            st['rect'].centerx, st['rect'].centery = event.pos
            l , k = event.rel

    #surface.fill(white)
    background()
    pygame.draw.circle(surface, st['color'], (st['rect'].centerx, st['rect'].centery), radius, 0)

    for b in block:
        if b['dir'] == SW:
            b['rect'].left -= speed
            b['rect'].top += speed
        if b['dir'] == SE:
            b['rect'].left += speed
            b['rect'].top += speed
        if b['dir'] == NW:
            b['rect'].left -= speed
            b['rect'].top -= speed
        if b['dir'] == NE:
            b['rect'].left += speed
            b['rect'].top -= speed
        if b['dir'] == N:
            #b['rect'].left += speed
            b['rect'].top -= speed
        if b['dir'] == E:
            b['rect'].left += speed
            #b['rect'].top -= speed
        if b['dir'] == S:
            #b['rect'].left += speed
            b['rect'].top += speed
        if b['dir'] == W:
            b['rect'].left -= speed
            #b['rect'].top -= speed

        if b['rect'].top < 30:
            if b['dir'] == N:
                b['dir'] =S
            if b['dir'] == NE:
                b['dir'] = SE
            if b['dir'] == NW:
                b['dir'] = SW
        if b['rect'].left <30:
            if b['dir'] == W:
                b['dir'] = E
            if b['dir'] == NW:
                b['dir'] = NE
            if b['dir'] == SW:
                b['dir'] = SE
        if b['rect'].top > screen_height - 50:
            if b['dir'] == S:
                b['dir'] = N
            if b['dir'] == SE:
                b['dir'] = NE
            if b['dir'] == SW:
                b['dir'] = NW
        if b['rect'].left > screen_width -50:
            if b['dir'] == E:
                b['dir'] = W
            if b['dir'] == NE:
                b['dir'] = NW
            if b['dir'] == SE:
                b['dir'] = SW


#mouse directions
        if k == 0:
            if l>0:
                st['dir'] = E
            if l<0:
                st['dir'] = W
        elif l==0:
            if k>0:
                st['dir'] = S
            if k<0:
                st['dir'] = N
        elif l<0 and k<0:
            st['dir'] = NW
        elif l>0 and k<0:
            st['dir'] = NE
        elif l>0 and k>0:
            st['dir'] = SE
        else:
            st['dir'] = SW

#now collisions
        after_collision(b, st)

        # Collisions Between Pieces and other Pieces
        for (Piece_A, Piece_B) in block_set_2d:
            after_collision(Piece_A, Piece_B)

        d1=math.dist(b['rect'].center,c1)
        d2=math.dist(b['rect'].center,c2)
        d3=math.dist(b['rect'].center,c3)
        d4=math.dist(b['rect'].center,c4)
        if d1<15 or d2<15 or d3<15 or d4<15:
            block.remove(b)

        pygame.draw.circle(surface, b['color'], (b['rect'].centerx, b['rect'].centery), radius_b, 0)

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        if len(block)==0:
            surface.fill(black)
            basicFont=pygame.font.SysFont(None,48)
            text = basicFont.render("Yess You Have Done IT!! hope u enjoyed it ",True,white,blue)
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            print("your total time taken is : ",seconds)aq

            sys.exit()

    #for bals in block[:]:




    pygame.display.update()
    clock.tick(40)

