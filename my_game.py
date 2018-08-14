import pygame,sys,random,time
from pygame.locals import *

FPS=30
window_width=1000
window_height=600
reveal_speed=15
square_size=40
gap_size=10
board_width=4
board_height=8

pygame.font.init()
#set condtion if (board_width*board_heigth) is not event number then program terminate with below statement
assert((board_width*board_height)%2==0),"Board needs an even number of size"

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

display_surface=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("CALL TO MIND")
display_surface.fill(navyblue)

colors=[white,green,yellow,cyan]
shapes=['square','circle','ellipse','cross']

random.shuffle(colors)
random.shuffle(shapes)

for_store_shape_color=[]
extra=[]
for i in colors:
    for j in shapes:
        extra.append((i,j))
        
random.shuffle(extra)
for_store_shape_color.append(extra)
for_store_shape_color=for_store_shape_color[:len(for_store_shape_color)]*2

shape_color=[]
for i in range(0,2):
    extra_arr=[]
    extra_arr=for_store_shape_color[i]
    j=0
    while j<board_width*board_height/2:
        shape_color.append(extra_arr[j:j+board_width])
        j+=board_width
for i in range(0,board_height):        
    random.shuffle(shape_color[i])        
        
#margin from left and top for first_square
left_margin=50
top_margin=50


for_check_reveal=[]

#Function to draw starting sqare boxes on screen
def draw_board():
    display_surface.fill(navyblue)
    for i in range(0,board_height):
        for j in range(0,board_width):
            k=j*(square_size+gap_size)+left_margin
            l=i*(square_size+gap_size)+top_margin
            pygame.draw.rect(display_surface,red,(k,l,square_size,square_size))
        
#Fuction to convert cordinates into pixels            
def get_pixels_cordinate(sq_row,sq_col):
    x=sq_col*(square_size+gap_size)+top_margin
    y=sq_row*(square_size+gap_size)+left_margin
    return (x,y)
    
#Fucntion to verify the pixels is lie in square cordinates or not
def get_row_col_at(mouse_x,mouse_y):
    for i in range(0,board_height):
        for j in range(0,board_width):
            x,y=get_pixels_cordinate(i,j)
            rectobj=pygame.Rect(x,y,square_size,square_size)
            if rectobj.collidepoint(mouse_x,mouse_y):
                return (i,j)
    return (None,None)

#Fuction to verify the range of clicked pixels
def for_verify_range(sq_row,sq_col):
    for i in range(0,board_height):
        for j in range(0,board_width):
            if i==sq_row and j==sq_col:
                return True
    return False

#Function to return shape and color of cordinate
def get_shape_and_color(sq_row,sq_col):
    return shape_color[sq_row][sq_col]


#Fucntion to uncover shape and colour 
def uncover_shape_and_color(sq_row,sql_col):
    top_of_sq,left_of_sq=get_pixels_cordinate(sq_row,sq_col)
    store=get_shape_and_color(sq_row,sq_col)
    color=store[0]
    shape=store[1]
    if shape=='circle':
        pygame.draw.circle(display_surface,color,(top_of_sq+square_size//2,left_of_sq+square_size//2),int(square_size*0.37))
    elif shape=='square':
        pygame.draw.rect(display_surface,color,(top_of_sq+10,left_of_sq+10,square_size//2,square_size//2))
    elif shape=='ellipse':
        pygame.draw.ellipse(display_surface,color,(top_of_sq+10,left_of_sq+10,square_size//2,int(square_size*0.70)))
    elif shape=='cross':
        pygame.draw.line(display_surface,color,(top_of_sq+int(square_size*(3/40)),left_of_sq+int(square_size*(3/40))),(top_of_sq+int(square_size*(3/4)),left_of_sq+int(square_size*(3/4))),3)
        pygame.draw.line(display_surface,color,(top_of_sq+int(square_size*(3/4)),left_of_sq+int(square_size*(3/40))),(top_of_sq+int(square_size*(1/8)),left_of_sq+int(square_size*(3/4))),3)  
    return (color,shape)

#Function for cover shape and color
def cover_shape_and_color(first_index_1,first_index_2,second_index_1,second_index_2):
    x,y=get_pixels_cordinate(first_index_1,first_index_2)
    pygame.draw.rect(display_surface,red,(x,y,square_size,square_size))
    x,y=get_pixels_cordinate(second_index_1,second_index_2)
    pygame.draw.rect(display_surface,red,(x,y,square_size,square_size))

#Function to check for all uncover boxes
def check_for_all_uncover():
    for i in for_check_reveal:
        extra=i
        for j in extra:
            if j==False:
                return False
    return True

def highlight(sq_row,sq_col):
    x,y=get_pixels_cordinate(sq_row,sq_col)
    pygame.draw.rect(display_surface,yellow,(x-10,y-10,60,10))
    pygame.draw.rect(display_surface,yellow,(x-10,y-10,10,60))
    pygame.draw.rect(display_surface,yellow,(x-10,y+40,60,10))
    pygame.draw.rect(display_surface,yellow,(x+40,y-10,10,60))
    
def for_remove_highlight(sq_row,sq_col):
    x,y=get_pixels_cordinate(sq_row,sq_col)
    pygame.draw.rect(display_surface,navyblue,(x-10,y-10,60,10))
    pygame.draw.rect(display_surface,navyblue,(x-10,y-10,10,60))
    pygame.draw.rect(display_surface,navyblue,(x-10,y+40,60,10))
    pygame.draw.rect(display_surface,navyblue,(x+40,y-10,10,60))            

#GAME BEGIN
draw_board() #Initialize Board
c1=red
c2=yellow
attempt=0 #For check number of attempt
store1=-1
store2=-1
points=0
minus_points=0
for i in range(0,board_height):
    for_check_reveal.append([False]*board_width)
while True:
    clicked=False
    for event in pygame.event.get():
        if event.type==QUIT:  #check for terminate
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEBUTTONUP: #check for mouse click
            mouse_x,mouse_y=event.pos
            clicked=True
        elif event.type==MOUSEMOTION: #check for mouse motion
            mouse_x,mouse_y=event.pos
    sq_row,sq_col=get_row_col_at(mouse_x,mouse_y)
    
    print(sq_row,sq_col)
    if clicked and attempt==0 and for_verify_range(sq_row,sq_col) and for_check_reveal[int(sq_row)][int(sq_col)]==False:
        for_check_reveal[int(sq_row)][int(sq_col)]=True
        color1,shape1=uncover_shape_and_color(sq_row,sq_col)
        first_index_1=sq_row
        first_index_2=sq_col
        attempt=1
        
    elif clicked and attempt==1 and for_verify_range(sq_row,sq_col) and for_check_reveal[int(sq_row)][int(sq_col)]==False:
        for_check_reveal[int(sq_row)][int(sq_col)]=True
        color2,shape2=uncover_shape_and_color(sq_row,sq_col)
        second_index_1=sq_row
        second_index_2=sq_col
        attempt=2

    elif attempt==2 and (color1!=color2 or shape1!=shape2):
        cover_shape_and_color(first_index_1,first_index_2,second_index_1,second_index_2)
        for_check_reveal[first_index_1][first_index_2]=False
        for_check_reveal[second_index_1][second_index_2]=False
        attempt=0
        time.sleep(1)
        minus_points+=0.25
        
    elif attempt==2:
        attempt=0
        points+=2
    elif store1!=-1 and store2!=-1:
        x,y=get_pixels_cordinate(store1,store2)
        if for_verify_range(sq_row,sq_col)==False:
            for_remove_highlight(store1,store2)
            store1=-1
            store2=-1
        
    elif sq_row!=None and sq_col!=None and for_check_reveal[sq_row][sq_col]==False and for_verify_range(sq_row,sq_col):
        highlight(sq_row,sq_col)
        store1=sq_row
        store2=sq_col
    '''    
    x,y=get_pixels_cordinate(0,board_width-1) 
    pygame.draw.rect(display_surface,white,(x+100,y,250,45))
    myfont5=pygame.font.SysFont('Comic Sans MS',30)
    text_surface5=myfont5.render("HINT",False,(0,0,0))
    display_surface.blit(text_surface5,(x+100,y))

    rectobj2=pygame.Rect(x+100,y,250,45)
    if clicked and rectobj2.collidepoint(mouse_x,mouse_y):
        for_hint()
    '''

    if check_for_all_uncover():
        c1,c2=c2,c1
        x,y=get_pixels_cordinate(0,board_width-1)
        pygame.draw.rect(display_surface,c1,(x+300,y,square_size+600,square_size+400))
        myfont=pygame.font.SysFont('Comic Sans MS',30)
        text_surface=myfont.render("Congratulation.... You Won the Game",False,(0,0,0))
        display_surface.blit(text_surface,(x+300,y))

        pygame.draw.rect(display_surface,white,(x+300,y+50,250,45))
        myfont3=pygame.font.SysFont('Comic Sans MS',30)
        text_surface3=myfont3.render("Points",False,(0,0,0))
        display_surface.blit(text_surface3,(x+300,y+50))

        pygame.draw.rect(display_surface,white,(x+400,y+50,150,45))
        myfont4=pygame.font.SysFont('Comic Sans MS',30)
        text_surface4=myfont4.render(str(points-minus_points),False,(0,0,0))
        display_surface.blit(text_surface4,(x+400,y+50))
          
        pygame.draw.rect(display_surface,white,(x+300,y+400,250,45))
        myfont2=pygame.font.SysFont('Comic Sans MS',30)
        text_surface2=myfont2.render("Restart Game",False,(0,0,0))
        display_surface.blit(text_surface2,(x+300,y+400))  
  
    if check_for_all_uncover() and clicked:
        x,y=get_pixels_cordinate(0,board_width-1) 
        rectobj=pygame.Rect(x+300,y+400,250,45)  #For restart Game
        if rectobj.collidepoint(mouse_x,mouse_y):
            draw_board()
            points=0
            minus_points=0
            attempt=0
            store1=-1
            store2=-1
            for i in range(1,board_height):
                for j in range(1,board_width):
                    for_check_reveal[i][j]=False

    pygame.display.update()

