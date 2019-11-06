import sys
import time
import random
import pygame

area = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 500

bg = (250, 250, 250)
black = (0, 0, 0)
white = (255, 255, 255)
ruo = (190, 194, 63)
lemon = (239, 215, 0)
tiffany = (129, 216, 207)
wood = (201, 186, 131)


class Paddle(pygame.sprite.Sprite):
    paddle_width = 5
    paddle_length = 75
    paddle_buffer = 10
    move_speed = 10

    def __init__(self, up_input, down_input, initial_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((Paddle.paddle_width, Paddle.paddle_length))
        self.image.fill(tiffany)
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos  # Position the paddle to given initial position

        # The controls for the paddle
        self.up_key = up_input
        self.down_key = down_input

    def update(self):
        """reads user input and calls the move function"""
        key = pygame.key.get_pressed()

        if key[self.up_key]:
            direction = -1
            self.move(direction)
        if key[self.down_key]:
            direction = 1
            self.move(direction)

    def move(self, direction):
        """moves the paddle in the direction of user input"""
        move_speed = Paddle.move_speed * direction
        current_pos = self.rect
        new_pos = self.rect.move((0, move_speed))

        # Check if new_pos is still within the screen
        if new_pos.y >= (SCREEN_HEIGHT - Paddle.paddle_length - Paddle.paddle_buffer):  # Stop the paddle moving off
            # bottom of the screen. Small buffer exists between bottom of screen and paddle.
            new_pos = current_pos
        elif new_pos.y <= Paddle.paddle_buffer:  # Stop the paddle moving off top of the screen. Small buffer exists
            # between top of screen and paddle.
            new_pos = current_pos

        self.rect = new_pos


class Ball(pygame.sprite.Sprite):
    def __init__(self, initial_pos, vx, vy, n):
        pygame.sprite.Sprite.__init__(self)

        self.images = [
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/0.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/1.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/2.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/3.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/4.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/5.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/6.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/7.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/8.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/9.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/10.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/11.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/12.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/lxh_0/13.png')
        ]
        self.image = self.images[n]
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos  # Position the ball to given initial position

        self.move_x = vx
        self.move_y = vy


class Score(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('/Users/soul/PycharmProjects/games/LXH/simsun.ttc', 70)
        self.score = 0
        self.image = self.font.render('00', 0, ruo)
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos  # Position the score to given initial position


class Match(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('/Users/soul/PycharmProjects/games/LXH/simsun.ttc', 30)
        self.match = 0
        self.image = self.font.render(str(self.match), 0, wood)
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos


class Win(pygame.sprite.Sprite):
    def __init__(self, initial_pos, win):
        pygame.sprite.Sprite.__init__(self)
        list_win = ['Player One Win', 'Player Two Win']
        self.font = pygame.font.Font('/Users/soul/PycharmProjects/games/LXH/simsun.ttc', 70)
        self.image = self.font.render(list_win[win], 0, ruo)
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos


class Start(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('/Users/soul/PycharmProjects/games/LXH/simsun.ttc', 50)
        self.image = self.font.render('<-START', 0, ruo)
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos  # Position the score to given initial position


class Time(pygame.sprite.Sprite):
    def __init__(self, initial_pos):
        my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font('/Users/soul/PycharmProjects/games/LXH/simsun.ttc', 20)
        self.image = self.font.render(my_time, 0, wood)
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos  # Position the score to given initial position


class Cat(pygame.sprite.Sprite):
    def __init__(self, initial_pos, c):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load('/Users/soul/Desktop/LXH/l/0.png'),
            pygame.image.load('/Users/soul/Desktop/LXH/l/1.png'),
            pygame.image.load('/Users/soul/Desktop/LXH/l/2.png'),
            pygame.image.load('/Users/soul/Desktop/LXH/l/3.png'),
            pygame.image.load('/Users/soul/Desktop/LXH/l/4.png'),
            pygame.image.load('/Users/soul/Desktop/LXH/l/5.png'),
            pygame.image.load('/Users/soul/Desktop/LXH/l/6.png'),
            pygame.image.load('/Users/soul/Desktop/LXH/l/7.png')
        ]
        self.image = self.images[c]
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos


class Judge(pygame.sprite.Sprite):
    def __init__(self, initial_pos, p):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/0.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/1.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/2.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/3.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/4.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/5.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/6.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/7.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/8.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/bidiu/9.png')
        ]
        self.image = self.images[p]
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos


class Truck(pygame.sprite.Sprite):
    def __init__(self, initial_pos, t):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/truck/0.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/truck/1.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/truck/2.png'),
            pygame.image.load('/Users/soul/PycharmProjects/games/LXH/Scripts/truck/3.png')
        ]
        self.image = self.images[t]
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos


class Loading(pygame.sprite.Sprite):
    def __init__(self, initial_pos, loading):
        pygame.sprite.Sprite.__init__(self)
        list_load = []
        list_path = []
        for l in range(37):
            path = '/Users/soul/Desktop/cat/%s.png' % str(l)
            list_path.append(path)
        list_path = list(reversed(list_path))

        for path_2 in list_path:
            list_load.append(pygame.image.load(path_2))

        self.images = list_load
        self.image = self.images[loading]
        self.rect = self.image.get_rect()
        self.rect.center = initial_pos


def music():
    list_music = ['/Users/soul/PycharmProjects/games/LXH/music/xu.flac',
                  '/Users/soul/PycharmProjects/games/LXH/music/晚安喵.flac',
                  '/Users/soul/PycharmProjects/games/LXH/music/猫宁孜然.flac',
                  '/Users/soul/PycharmProjects/games/LXH/music/嘘.mp3']
    mu = random.choice(list_music)
    pygame.mixer.music.load(mu)
    pygame.mixer.music.play()


def main():
    x = (SCREEN_WIDTH / 2)
    y = SCREEN_HEIGHT - 80
    vx = random.choice([v for v in [-7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12]])
    vy = random.randint(12, 26)

    gy = 1
    FPS = 10
    fps = 10

    n = 0
    p = 0
    c = 0
    t = 0
    win = 0
    cat_pos = ((SCREEN_WIDTH / 2 - 100), (SCREEN_HEIGHT / 2))
    sta_pos = ((SCREEN_WIDTH / 2 + 55), (SCREEN_HEIGHT / 2))
    list_score = ['00', '15', '30', '40', '45', 'AD']
    # Basic initialisation
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('LuoXiaoHei V1.2')
    clock = pygame.time.Clock()

    # Prepare the background
    background = pygame.Surface(screen.get_size())
    background.fill(white)  # Make sure the background is bg colour

    # add background music
    music()

    starting = 1

    while True:
        # Start
        while starting:
            clock.tick(fps)
            fps += 1
            if fps > 30:
                fps = 20
            if pygame.mixer.music.get_busy():
                pass
            else:
                sys.exit()
            xiaohei = Cat(initial_pos=cat_pos, c=c)
            xiaohei_sprite = pygame.sprite.RenderPlain(xiaohei)
            start = Start(initial_pos=sta_pos)
            start_sprite = pygame.sprite.RenderPlain(start)
            xhtime = Time(initial_pos=((SCREEN_WIDTH - 105), 15))
            xhtime_sprite = pygame.sprite.RenderPlain(xhtime)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                # Click cat to start the game
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        rect_mouse = pygame.draw.rect(screen, ruo, (event.pos[0], event.pos[1], 10, 10), 0)
                        if xiaohei.rect.colliderect(rect_mouse):
                            starting = 0
                # Cat move with mouse
                elif event.type == pygame.MOUSEMOTION:
                    if event.buttons[0] == 1:
                        cat_pos = (event.pos[0], event.pos[1])

            if c < 7:
                c += 1
            else:
                c = 0

            screen.blit(background, (0, 0))  # Draw the background
            xiaohei_sprite.draw(screen)
            start_sprite.draw(screen)
            xhtime_sprite.draw(screen)

            pygame.display.flip()

        # Loading
        loading = 37
        while loading:
            clock.tick(15)
            loading -= 1
            heiqiu = Loading(initial_pos=((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2)), loading=loading)
            heiqiu_sprite = pygame.sprite.RenderPlain(heiqiu)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

            screen.blit(background, (0, 0))  # Draw the background
            heiqiu_sprite.draw(screen)
            pygame.display.flip()

        # Gaming
        # Load in all the sprites
        player_one = Paddle(up_input=pygame.K_w, down_input=pygame.K_s, initial_pos=(50, (SCREEN_HEIGHT / 2)))
        player_two = Paddle(up_input=pygame.K_o, down_input=pygame.K_l, initial_pos=(950, (SCREEN_HEIGHT / 2)))
        score_one = Score(initial_pos=(225, 100))
        score_two = Score(initial_pos=(745, 100))
        match_one = Match(initial_pos=(290, 115))
        match_two = Match(initial_pos=(810, 115))
        player_sprites = pygame.sprite.RenderPlain(player_one, player_two, score_one, score_two, match_one, match_two)

        running = 1

        while running:
            clock.tick(FPS)
            if FPS > 60:
                FPS = 10

            if pygame.mixer.music.get_busy():
                pass
            else:
                music()

            xhtime = Time(initial_pos=(105, SCREEN_HEIGHT - 15))
            xhtime_sprite = pygame.sprite.RenderPlain(xhtime)
            bidiu = Judge(initial_pos=((SCREEN_WIDTH / 2), 40), p=p)
            bidiu_sprite = pygame.sprite.RenderPlain(bidiu)
            if p < 9:
                p += 1
            else:
                p = 0

            # Detect closing of program
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        rect_mouse = pygame.draw.rect(screen, ruo, (event.pos[0], event.pos[1], 10, 10), 0)
                        if bidiu.rect.colliderect(rect_mouse):
                            FPS += 10

            vy = vy + gy
            if y > 450:
                vy = -(vy - 1)
                if vx > 0:
                    vx += random.choice([v for v in [-2, -1, 0, 1, 2, 3, 4, 5]])
                elif vx < 0:
                    vx -= random.choice([v for v in [-2, -1, 0, 1, 2, 3, 4, 5]])
                elif vx == 0:
                    vx += random.choice([v for v in [-8, -9, -10, 8, 9, 10]])

            if x > 1080 or x < -90:
                if x > 1080:
                    score_one.score += 1
                    if score_one.score > 4 and score_one.score - score_two.score > 1:
                        score_one.score = 0
                        score_two.score = 0
                        score_two.image = score_two.font.render(list_score[score_two.score], 0, ruo)
                        match_one.match += 1
                    elif score_one.score > 4 and score_one.score - score_two.score == 1:
                        score_one.score = 5
                    elif score_one.score > 4 and score_one.score - score_two.score == 0:
                        score_one.score = 4
                        score_two.score = 4
                        score_two.image = score_two.font.render(list_score[score_two.score], 0, ruo)
                    score_one.image = score_one.font.render(list_score[score_one.score], 0, ruo)
                    match_one.image = match_one.font.render(str(match_one.match), 0, ruo)

                    # player one win
                    if match_one.match == 7:
                        running = 0
                        win = 0

                elif x < -90:
                    score_two.score += 1
                    if score_two.score > 4 and score_two.score - score_one.score > 1:
                        score_two.score = 0
                        score_one.score = 0
                        score_one.image = score_one.font.render(list_score[score_one.score], 0, ruo)
                        match_two.match += 1
                    elif score_two.score > 4 and score_two.score - score_one.score == 1:
                        score_two.score = 5
                    elif score_two.score > 4 and score_two.score - score_one.score == 0:
                        score_one.score = 4
                        score_two.score = 4
                        score_one.image = score_one.font.render(list_score[score_one.score], 0, ruo)
                    score_two.image = score_two.font.render(list_score[score_two.score], 0, ruo)
                    match_two.image = match_two.font.render(str(match_two.match), 0, ruo)

                    # player two win
                    if match_two.match == 7:
                        running = 0
                        win = 1

                x = (SCREEN_WIDTH / 2)
                y = SCREEN_HEIGHT - 80
                vx = random.choice([v for v in [-7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12]])
                vy = random.randint(12, 26)

                n = 0

            x += vx
            y += vy

            if 14 <= vy < 15:
                n = 0
            elif vy >= 15:
                n = 1
            elif vy < -14:
                n = 2
            elif -14 <= vy < -10:
                n = 3
            elif -10 <= vy < -1:
                n = 4
            elif -1 <= vy < 1:
                n = 5
            elif 1 <= vy < 4:
                n = 6
            elif 4 <= vy < 12:
                n = 7
            elif 12 <= vy < 14:
                n = 8

            ball = Ball(initial_pos=(x, y), vx=vx, vy=vy, n=n)
            ball_sprite = pygame.sprite.RenderPlain(ball)

            player_rect = [player_one.rect, player_two.rect]  # Create list which contains the most up-to-date rect of p

            # paddle_rect represents a list which contains the rect of both player one paddle and player two paddle
            for rect in player_rect:
                rect_collision = rect.inflate(0, 0)  # Decrease the hit-box of paddle
                if ball.rect.colliderect(rect_collision):
                    vx = -vx

            player_sprites.update()  # Update all sprites
            ball_sprite.update()

            screen.blit(background, (0, 0))  # Draw the background
            pygame.draw.line(screen, lemon, ((SCREEN_WIDTH / 2), 0), ((SCREEN_WIDTH / 2), SCREEN_HEIGHT))
            # Draw middle line
            pygame.draw.rect(screen, ruo, (275, 100, 30, 30), 2)
            pygame.draw.rect(screen, ruo, (795, 100, 30, 30), 2)

            player_sprites.draw(screen)  # Draw the sprites to the screen
            bidiu_sprite.draw(screen)
            ball_sprite.draw(screen)
            xhtime_sprite.draw(screen)

            pygame.display.flip()  # Update the whole screen

        # Replay or End
        truck_x = -100
        replaying = 1
        start_time = time.time()
        while replaying:
            clock.tick(10)
            if pygame.mixer.music.get_busy():
                pass
            else:
                music()

            end_time = time.time()
            if end_time - start_time > 60:
                sys.exit()

            xhtime = Time(initial_pos=(105, SCREEN_HEIGHT - 15))
            xhtime_sprite = pygame.sprite.RenderPlain(xhtime)
            truck = Truck(initial_pos=(truck_x, 400), t=t)
            winner = Win(initial_pos=((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 30)), win=win)
            truck_sprite = pygame.sprite.RenderPlain(truck)
            winner_sprite = pygame.sprite.RenderPlain(winner)
            truck_x += 10
            if truck_x > 1100:
                truck_x = -100

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                # Click cat to start the game
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        rect_mouse = pygame.draw.rect(screen, ruo, (event.pos[0], event.pos[1], 10, 10), 0)
                        if truck.rect.colliderect(rect_mouse):
                            replaying = 0

            if t < 3:
                t += 1
            else:
                t = 0

            screen.blit(background, (0, 0))  # Draw the background
            truck_sprite.draw(screen)
            winner_sprite.draw(screen)
            xhtime_sprite.draw(screen)

            pygame.display.flip()


if __name__ == '__main__':
    main()
