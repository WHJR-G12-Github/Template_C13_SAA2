import pygame,random
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)
groundx=0
speed=0

score=0
state="play"
score_font=pygame.font.Font('freesansbold.ttf', 20)

class Bird:
    bird=pygame.Rect(100,250,30,30)
    

    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        speed=speed-5
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    def __init__(self,x):
        self.height=random.randint(150,400)
        self.tpipe=pygame.Rect(x,self.height-400,40,300)
        self.bpipe=pygame.Rect(x,self.height+150,40,300)
    def display(self):
      screen.blit(images["pipe"],self.bpipe)
      screen.blit(images["invertedpipe"],self.tpipe)
    def move(self):
        self.tpipe.x-=2
        self.bpipe.x-=2
        if self.tpipe.x<-40:
            self.tpipe.x=450
            self.bpipe.x=450
            self.height=random.randint(150,400)
            self.tpipe.y=self.height-400
            self.bpipe.y=self.height+150
bird1=Bird()
pipe1=Pipe(250)
while True:  
  # Print the value of 'state' on the console
  
  screen.blit(images["bg"],[0,0])
  score_text=score_font.render("Score:"+str(score), True, (0,0,255))
  screen.blit(score_text,[10,10])
  
  screen.blit(images["ground"],[groundx,550])
  bird1.movedown()
  bird1.display()
  pipe1.display()
  
  if state=="play":
      groundx-=5
      if groundx<-450:
       groundx=0
      if pipe1.tpipe.x == bird1.bird.x:
       score=score+1
      pipe1.move() 
      
      
         
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE and state=="play":
            bird1.moveup()  
  
  if bird1.bird.colliderect(pipe1.bpipe) or bird1.bird.colliderect(pipe1.tpipe) or bird1.bird.y>=600:
      state="over"
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
