import pygame as pg

pg.init()

# set window
w = 500
h = 650
screen = pg.display.set_mode((w,h))
pg.display.set_caption('Day 4 Challenge')

#music
short_sound = pg.mixer.Sound("short_can.ogg")
long_sound = pg.mixer.Sound("long_can.ogg")

def sqrtt(x):
    return x**0.5
#button class
class button():
    def __init__(self, c,x,y,w,h,t=''):
        self.color = c
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.text = t
        self.over = False

    def draw(self,screen,outline=None,color = (255,255,255)):
        #Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                    
        pg.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
                
        if self.text != '':
            font = pg.font.SysFont('agencyfb', 65, 'bold')
            text = font.render(self.text, 1, color)
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isClick(self, p):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if p[0] > self.x and p[0] < self.x + self.width:
            if p[1] > self.y and p[1] < self.y + self.height:
                return True
        return False

#set colors
white = (255,255,255)

# nums
num1 = button((102,0,204),40,150,70,70, '1')
num2 = button((102,0,204),150,150,70,70, '2')
num3 = button((127,0,255),265,150,70,70, '3')
num4= button((102,0,204),40,250,70,70, '4')
num5 = button((127,0,255),150,250,70,70, '5')
num6= button((153,51,255),265,250,70,70, '6')
num7= button((127,0,255),40,350,70,70, '7')
num8 = button((153,51,255),150,350,70,70, '8')
num9 = button((178,102,255),265,350,70,70, '9')
num0 = button((153,51,255),40,450,70,70, '0')
numbers = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num0]

# signs
plus = button((153,153,255),385,350,70,70, '+')
minus = button((178,102,255),385,250,70,70, '-')
multi = button((153,153,255),150,550,70,70, 'x')
divide = button((178,102,255),150,450,70,70, '÷')
equal = button((153,153,255),385,450,70,70, '=')
clear = button((153,51,255),385,150,70,70, 'C')
fac = button((178,102,255),40,550,70,70, '!')
sqrt = button((153,153,255),275,550,180,70, 'sqrt: √')
expo = button((153,153,255),275,450,70,70, '^')
signs = [plus, minus, multi, divide, equal, clear,fac,sqrt,expo]

def Factorial(x):
    if x<0:
        print("*Negative Numbers don't have Factorials")
        return 'error'
    elif x==0 or x==1:
        return 1
    else:
        return x*Factorial(x-1)

def redraw(t):
    # draw all the numbers
    screen.fill((153, 204, 255))
    #screen.blit(calc_image,(0,0))
    for i in numbers:
        i.draw(screen)
    for j in signs:
        j.draw(screen)
        
    pg.draw.rect(screen, white, (50,25,400,100),0)
    t.draw(screen,color=(0,0,0))

operatorsss=['+','-','/','÷','!','**','^',]
def Symbols():
    global user_input
    global python_input
    if event.type == pg.MOUSEBUTTONDOWN:
        p = pg.mouse.get_pos()

        mouseisover = True
        try:
            if (not user_input[-1] in operatorsss) and (not python_input[-1] in operatorsss):
                if plus.isClick(p):
                    user_input += "+"
                    python_input += "+"
                    if mouseisover:
                        short_sound.play()
                        mouseisover = False

                if minus.isClick(p):
                    user_input += "-"
                    python_input += "-"
                    if mouseisover:
                        short_sound.play()
                        mouseisover = False

                if multi.isClick(p):
                    user_input += "x"
                    python_input += "*"
                    if mouseisover:
                        short_sound.play()
                        mouseisover = False

                if divide.isClick(p):
                    user_input += "÷"
                    python_input += "/"
                    if mouseisover:
                        short_sound.play()
                        mouseisover = False
                
                if fac.isClick(p):
                    user_input += "!"
                    python_input += '!'
                    if mouseisover:
                        short_sound.play()
                        mouseisover = False
                
                if expo.isClick(p):
                    user_input += "^"
                    python_input += '**'
                    if mouseisover:
                        short_sound.play()
                        mouseisover = False
                


        except:
            pass
        try:

                if sqrt.isClick(p):
                    user_input += "√"
                    python_input += 'sqrtt('
                    if mouseisover:
                        short_sound.play()
                        mouseisover = False
        except:
            pass
        tempx=-1
        if equal.isClick(p):
            if '!' in python_input:
                if python_input[-1] == '!':
                    result = round(Factorial(int(python_input[:-1])),4)
                else: result = 'error'
            elif 'sqrtt'in python_input:
                for s in operatorsss+['x','*']:
                    if python_input.find(s)>=tempx:
                        tempx=python_input.find(s)
                if tempx==-1:
                    python_input=python_input+')'
                else:
                    ct=python_input.count('sqrtt')
                    if ct==1:
                        if python_input.find('sqrtt')<tempx:
                            python_input=python_input[:tempx]+')'+python_input[tempx:]
                        else:
                            python_input+=')'
                    elif ct==2:
                        python_input = python_input[:tempx] + ')' + python_input[tempx:]
                        python_input += ')'
                result =round(eval(python_input),4)
                
            elif python_input[-1]=='0' and python_input[-2]=='/':
                result="Can't Divide by 0"
                user_input=''
            else:
                result = round(eval(python_input),4)
                
            python_input = ""
            user_input += f"={result}"
            
            if mouseisover:
                long_sound.play()
                mouseisover = False


        if clear.isClick(p):
            python_input = ""
            user_input = ""
            if mouseisover:
                short_sound.play()
                mouseisover = False
        

def MOUSEOVERnumbers():
    global user_input
    global python_input
    if event.type == pg.MOUSEBUTTONDOWN:
        p = pg.mouse.get_pos()          

        mouseisover = True

        if num1.isClick(p):
            user_input += "1"
            python_input += "1"
            if mouseisover:
                short_sound.play()
                mouseisover = False

            
        if num2.isClick(p):
            user_input += "2"
            python_input += "2"
            if mouseisover:
                short_sound.play()
                mouseisover = False
            
        if num3.isClick(p):
            user_input += "3"
            python_input += "3"
            if mouseisover:
                short_sound.play()
                mouseisover = False


            
        if num4.isClick(p):
            user_input += "4"
            python_input += "4"
            if mouseisover:
                short_sound.play()
                mouseisover = False

            
        if num5.isClick(p):
            user_input += "5"
            python_input += "5"
            if mouseisover:
                short_sound.play()
                mouseisover = False

            
        if num6.isClick(p):
            user_input += "6"
            python_input += "6"
            if mouseisover:
                short_sound.play()
                mouseisover = False

            
        if num7.isClick(p):
            user_input += "7"
            python_input += "7"
            if mouseisover:
                short_sound.play()
                mouseisover = False

            
        if num8.isClick(p):
            user_input += "8"
            python_input += "8"
            if mouseisover:
                short_sound.play()
                mouseisover = False

            
        if num9.isClick(p):
            user_input += "9"
            python_input += "9"
            if mouseisover:
                short_sound.play()
                mouseisover = False

            
        if num0.isClick(p):
            user_input += "0"
            python_input += "0"
            if mouseisover:
                short_sound.play()
                mouseisover = False            

run = True
user_input = ""
python_input = ""

while run:

    t = button((0,0,0),250,75,0,0,f"{user_input}")

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        MOUSEOVERnumbers()

        Symbols()


    redraw(t)
    pg.display.update()

pg.quit()