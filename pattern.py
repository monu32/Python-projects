import pygame,sys,random,time
from pygame.locals import *

window_width=1000
window_height=800

display_surface=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("PATTERN")


#colours
gray= (100, 100, 100)
navyblue= ( 60,  60, 100)
white= (255, 255, 255)
red= (255,   0,   0)
green= (0,255,0)
blue= (  0,   0, 255)
yellow= (255, 255,   0)
orange= (255, 128,   0)
purple= (255,   0, 255)
cyan= (  0, 255, 255)
black=(0,0,0)
dim_red=(100,0,0)
dim_blue=(0,0,100)
dim_green=(0,100,0)
dim_yellow=(100,100,0)


display_surface.fill(black)
top_margin=100
left_margin=100
color=[dim_red,dim_blue,dim_green,dim_yellow]

pygame.font.init()
#Fuction to convert cordinates into pixels            
def get_pixels_cordinate(sq_row,sq_col):
    x=sq_col*250+top_margin
    y=sq_row*250+left_margin
    return (x,y)

def draw_frame():
    c=0
    for i in range(0,2):
        for j in range(0,2):
            x,y=get_pixels_cordinate(i,j)
            pygame.draw.rect(display_surface,color[c],(x,y,200,200))
            c+=1

l=[]    
def show_pattern(val):
    while val>0:
        l.append(random.randint(1,4))
        val-=1
    i=0
    while len(l)>i:
        if l[i]==1:
            x,y=get_pixels_cordinate(0,0)
            pygame.draw.rect(display_surface,red,(x,y,200,200))
            pygame.display.update()
            time.sleep(1)
            pygame.draw.rect(display_surface,dim_red,(x,y,200,200))
            pygame.display.update()
        elif l[i]==2:
            x,y=get_pixels_cordinate(0,1)
            pygame.draw.rect(display_surface,blue,(x,y,200,200))
            pygame.display.update()
            time.sleep(1)
            pygame.draw.rect(display_surface,dim_blue,(x,y,200,200))
            pygame.display.update()
        elif l[i]==3:
            x,y=get_pixels_cordinate(1,0)
            pygame.draw.rect(display_surface,green,(x,y,200,200))
            pygame.display.update()
            time.sleep(1)
            pygame.draw.rect(display_surface,dim_green,(x,y,200,200))
            pygame.display.update()
        elif l[i]==4:    
            x,y=get_pixels_cordinate(1,1)
            pygame.draw.rect(display_surface,yellow,(x,y,200,200))
            pygame.display.update()
            time.sleep(1)
            pygame.draw.rect(display_surface,dim_yellow,(x,y,200,200))
            pygame.display.update()
        i+=1
        
draw_frame()
clicked=True
val=1
order=[]
flag=0
points=0
while True:
    pygame.draw.rect(display_surface,white,(700,100,200,40))
    myfont=pygame.font.SysFont('Comic Sans MS',30)
    text_surface=myfont.render("Show Pattern",True,(0,0,0,))
    display_surface.blit(text_surface,(700,100))

    pygame.draw.rect(display_surface,white,(700,150,200,40))
    text_surface=myfont.render("Points:    "+str(points),True,(0,0,0,))
    display_surface.blit(text_surface,(700,150))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
         
        elif event.type==MOUSEBUTTONUP and clicked:
            mousex,mousey=event.pos
            rectobj=pygame.Rect(700,100,200,40)
            if rectobj.collidepoint(mousex,mousey):
                show_pattern(val)
                val+=1
                clicked=False
                flag=1
                
        elif event.type==KEYDOWN and flag:
            if event.key ==K_KP1:
                order.append(3)
            elif event.key==K_KP2:
                order.append(4)
            elif event.key==K_KP4:
                order.append(1)
            elif event.key==K_KP5:
                order.append(2)
                
    if len(l)>0 and len(order)>=len(l):
        for i in range(0,len(l)):
            if l[i]!=order[i]:
                pygame.quit()
                sys.exit()
        del order[:]
        del l[:]
        clicked=True
        flag=0
        points+=1
                
    pygame.display.update()       
