from pygame import*
mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,x,y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_frect(x=x,y=y)
    def reset(self):
        window.blit(self.image,self.rect)
    def collide(self,other):
        return self.rect.colliderect(other.rect)
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.right > 0:
            self.rect.x += self.speed
        if keys_pressed[K_LEFT] and self.rect.left < win_width  :
            self.rect.x -= self.speed
        if keys_pressed[K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.bottom < win_height:
            self.rect.y += self.speed
class Monster(GameSprite):
    def __init__(self,player_image,x,y,speed, start_x,start_y,end_x,end_y):
        super().__init__(player_image,x,y, speed)
        self.start = Vector2(start_x,start_y)
        self.end = Vector2(end_x,end_y)
    def update(self):
        move_vector = (self.end - Vector2(self.rect.center))
        length = move_vector.length()
        move_vector = move_vector.normalize()
        self.rect.x += move_vector.x * self.speed
        self.rect.y += move_vector.y * self.speed
        if length <= self.speed:
            self.end, self.start = self.start, self.end
win_width = 700
win_height = 500
class Wall(GameSprite):
    def __init__(self,widht, height,x,y,color):
        self.image = Surface((widht,height))
        self.rect = self.image.get_rect(x=x,y=y)
        self.image.fill(color)
walls = [
    Wall(10,win_height -100,200,0,'green'),
    Wall(10,win_height -100,400,100,'green'),
    Wall(150,10,400,100,'green'),
    ]
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(700,500))
game = True
sprite_1 = Player('hero.png', 5, win_height - 80, 4)
sprite_2 = Monster('cyborg.png', 2, 80, 280, 180, 280, 700, 200)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
x1,x2,y1,y2 = 50,500,60,300
lose  = False
win = False
mixer.music.load('jungles.ogg')
mixer.music.play()
font.init()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not lose and not win:
        sprite_1.update()
        sprite_2.update()
    if sprite_1.collide(final):
        win = True
    if sprite_1.collide(sprite_2):
        lose = True
    for wall in walls:
        if sprite_1.collide(wall):
            lose = True
    window.blit(background,(0,0))
    sprite_1.reset()
    sprite_2.reset()
    for wall in walls:
        wall.reset()
    if win:
        f = font.Font(None,32)
        text = font.SysFont('Arial','YOU WIN!!',True,'green')
        window.blit(text,text.get_rect(
            centerx = win_width/2,
            centery =win_height/2
            ))
    if lose:
        window.fill((randint))
    display.update()
    clock.tick(60)