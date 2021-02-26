import pygame
import random
import time


class Player:
    def __init__(self, x, y, width, height, lastMove):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 8
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.animationCount = 0
        self.lastMove = lastMove
        self.hp = 5
        self.wave = 1
        self.hitbox = (self.x + 16, self.y, 30, 65)

    def draw(self, window):
        if self.animationCount + 1 >= 30:
            self.animationCount = 0
        if self.left:
            window.blit(walkLeft[self.animationCount // 5], (self.x, self.y))
            self.animationCount += 1
        elif self.right:
            window.blit(walkRight[self.animationCount // 5], (self.x, self.y))
            self.animationCount += 1
        else:
            window.blit(playerStand, (self.x, self.y))
        self.hitbox = (self.x + 16, self.y, 30, 65)
        #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)
        pygame.draw.rect(window, (255, 0, 0), (960, 10, 200, 30))
        if self.hp > 0:
            pygame.draw.rect(window, (0, 255, 0), (960, 10, 200 - ((200 / 5) * (5 - self.hp)), 30))

    def hit(self, type):
        self.isJump = False
        self.jumpCount = 10
        for goblin in type:
            if goblin.x > 990:
                self.x = goblin.x - 200
            elif goblin.x < 210:
                self.x = goblin.x + 200
            else:
                self.x = goblin.x + 150
        self.y = 525
        if self.hp > 0:
            self.hp -= 1

    def new_wave(self, wave):
        if score == (2 * 2 + wave - 1) * wave / 2:
            self.wave += 1
            if self.wave - 1 == 1:
                text3 = font.render("YOU'VE OVERCOME " + str(self.wave - 1) + "st WAVE!", 1, (220, 200, 5))
            elif self.wave - 1 == 2:
                text3 = font.render("YOU'VE OVERCOME " + str(self.wave - 1) + "nd WAVE!", 1, (220, 200, 5))
            elif self.wave - 1 == 3:
                text3 = font.render("YOU'VE OVERCOME " + str(self.wave - 1) + "rd WAVE!", 1, (220, 200, 5))
            else:
                text3 = font.render("YOU'VE OVERCOME " + str(self.wave - 1) + "th WAVE!", 1, (220, 200, 5))
            window.blit(text3, (600 - text3.get_width() // 2, 360))
            pygame.display.update()
            pygame.time.wait(2000)


class Shell:
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.velocity = 18 * direction

    def draw_bullets(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


class Enemies:
    enemyWalkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'),
                     pygame.image.load('L3E.png'), pygame.image.load('L4E.png'),
                     pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                     pygame.image.load('L7E.png'), pygame.image.load('L8E.png'),
                     pygame.image.load('L9E.png'), pygame.image.load('L10E.png'),
                     pygame.image.load('L11E.png')]

    enemyWalkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'),
                     pygame.image.load('R3E.png'), pygame.image.load('R4E.png'),
                     pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                     pygame.image.load('R7E.png'), pygame.image.load('R8E.png'),
                     pygame.image.load('R9E.png'), pygame.image.load('R10E.png'),
                     pygame.image.load('R11E.png')]

    knightWalkLeft = [pygame.image.load('knight iso char_run left_0.png'),
                      pygame.image.load('knight iso char_run left_1.png'),
                      pygame.image.load('knight iso char_run left_2.png'),
                      pygame.image.load('knight iso char_run left_3.png'),
                      pygame.image.load('knight iso char_run left_4.png'),
                      pygame.image.load('knight iso char_run left_5.png')]

    knightWalkRight = [pygame.image.load('knight iso char_run right_0.png'),
                       pygame.image.load('knight iso char_run right_1.png'),
                       pygame.image.load('knight iso char_run right_2.png'),
                       pygame.image.load('knight iso char_run right_3.png'),
                       pygame.image.load('knight iso char_run right_4.png'),
                       pygame.image.load('knight iso char_run right_5.png')]

    knightSliceLeft = [pygame.image.load('knight iso char_slice left_1.png'),
                       pygame.image.load('knight iso char_slice left_1.png'),
                       pygame.image.load('knight iso char_slice left_2.png')]

    knightSliceRight = [pygame.image.load('knight iso char_slice right_1.png'),
                        pygame.image.load('knight iso char_slice right_1.png'),
                        pygame.image.load('knight iso char_slice right_2.png')]

    skeleton1WalkLeft = [pygame.image.load('walk left1.png'),
                         pygame.image.load('walk left2.png'),
                         pygame.image.load('walk left3.png'),
                         pygame.image.load('walk left4.png'),
                         pygame.image.load('walk left5.png'),
                         pygame.image.load('walk left6.png')]

    skeleton1WalkRight = [pygame.image.load('walk right1.png'),
                          pygame.image.load('walk right2.png'),
                          pygame.image.load('walk right3.png'),
                          pygame.image.load('walk right4.png'),
                          pygame.image.load('walk right5.png'),
                          pygame.image.load('walk right6.png')]

    skeleton1SliceLeft = [pygame.image.load('attack left1.png'),
                          pygame.image.load('attack left2.png'),
                          pygame.image.load('attack left3.png'),
                          pygame.image.load('attack left4.png'),
                          pygame.image.load('attack left5.png'),
                          pygame.image.load('attack left6.png')]

    skeleton1SliceRight = [pygame.image.load('attack right1.png'),
                           pygame.image.load('attack right2.png'),
                           pygame.image.load('attack right3.png'),
                           pygame.image.load('attack right4.png'),
                           pygame.image.load('attack right5.png'),
                           pygame.image.load('attack right6.png')]

    bossWalkLeft = [pygame.image.load('walk-with-weapon-left1.png'),
                            pygame.image.load('walk-with-weapon-left2.png'),
                            pygame.image.load('walk-with-weapon-left3.png'),
                            pygame.image.load('walk-with-weapon-left4.png'),
                            pygame.image.load('walk-with-weapon-left5.png'),
                            pygame.image.load('walk-with-weapon-left6.png'),
                            pygame.image.load('walk-with-weapon-left7.png'),
                            pygame.image.load('walk-with-weapon-left8.png'),
                            pygame.image.load('walk-with-weapon-left9.png'),
                            pygame.image.load('walk-with-weapon-left10.png'),
                            pygame.image.load('walk-with-weapon-left11.png')]

    bossWalkRight = [pygame.image.load('walk-with-weapon-right1.png'),
                             pygame.image.load('walk-with-weapon-right2.png'),
                             pygame.image.load('walk-with-weapon-right3.png'),
                             pygame.image.load('walk-with-weapon-right4.png'),
                             pygame.image.load('walk-with-weapon-right5.png'),
                             pygame.image.load('walk-with-weapon-right6.png'),
                             pygame.image.load('walk-with-weapon-right7.png'),
                             pygame.image.load('walk-with-weapon-right8.png'),
                             pygame.image.load('walk-with-weapon-right9.png'),
                             pygame.image.load('walk-with-weapon-right10.png'),
                             pygame.image.load('walk-with-weapon-right11.png')]

    bossSliceLeft = [pygame.image.load('attack-D-Left1.png'),
                     pygame.image.load('attack-D-Left2.png'),
                     pygame.image.load('attack-D-Left3.png'),
                     pygame.image.load('attack-D-Left4.png'),
                     pygame.image.load('attack-D-Left5.png'),
                     pygame.image.load('attack-D-Left6.png'),
                     pygame.image.load('attack-D-Left7.png'),
                     pygame.image.load('attack-D-Left8.png'),
                     pygame.image.load('attack-D-Left9.png')]

    bossSliceRight = [pygame.image.load('attack-D-Right1.png'),
                      pygame.image.load('attack-D-Right2.png'),
                      pygame.image.load('attack-D-Right3.png'),
                      pygame.image.load('attack-D-Right4.png'),
                      pygame.image.load('attack-D-Right5.png'),
                      pygame.image.load('attack-D-Right6.png'),
                      pygame.image.load('attack-D-Right7.png'),
                      pygame.image.load('attack-D-Right8.png'),
                      pygame.image.load('attack-D-Right9.png')]

    def __init__(self, x, y, width, height, end, side):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.side = side
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.walkCountKnight = 0
        self.walkCountSkeleton1 = 0
        self.walkCountBoss = 0
        self.vel = 3 * self.side
        self.velKnight = 4.5 * self.side
        self.velSkeleton1 = 2.5 * self.side
        self.velBoss = 1.7 * self.side
        self.hitbox = (self.x + 22.5, self.y + 7, 22, 42)
        self.hitbox_s = (self.x, self.y, 22, 42)
        self.health = 12
        self.healthSkeleton1 = 18
        self.healthKnight = 24
        self.healthBoss = 32
        self.visible = True

    def draw_enemy(self, window):
        self.move_enemy()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                window.blit(self.enemyWalkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                window.blit(self.enemyWalkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20,
                                                   50 - ((50 / 12) * (12 - self.health)), 10))
            self.hitbox = (self.x + 22.5, self.y + 7, 22, 42)
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def draw_knight(self, window):
        self.move_knight()
        if self.visible:
            if self.walkCountKnight + 1 >= 18:
                self.walkCountKnight = 0
            if self.velKnight > 0:
                if 0 < round(man.x + man.width) - round(self.x + self.width) <= 70 and man.hp > 0:
                    window.blit(self.knightSliceLeft[self.walkCountKnight // 6], (self.x, self.y))
                    self.walkCountKnight += 1
                else:
                    window.blit(self.knightWalkRight[self.walkCountKnight // 3], (self.x, self.y))
                    self.walkCountKnight += 1
            else:
                if 0 < round(self.x + self.width) - round(man.x + man.width) <= 70 and man.hp > 0:
                    window.blit(self.knightSliceRight[self.walkCountKnight // 6], (self.x, self.y))
                    self.walkCountKnight += 1
                else:
                    window.blit(self.knightWalkLeft[self.walkCountKnight // 3], (self.x, self.y))
                    self.walkCountKnight += 1
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20,
                                                   50 - ((50 / 24) * (24 - self.healthKnight)), 10))
            self.hitbox = (self.x + 22.5, self.y + 7, 22, 42)
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox, 2)

    def draw_skeleton1(self, window):
        self.move_skeleton1()
        if self.visible:
            if self.walkCountSkeleton1 + 1 >= 18:
                self.walkCountSkeleton1 = 0
            if self.velSkeleton1 > 0:
                if 0 < round(man.x + man.width) - round(self.x + self.width) <= 58 and man.hp > 0:
                    window.blit(self.skeleton1SliceRight[self.walkCountSkeleton1 // 3], (self.x, self.y))
                    self.walkCountSkeleton1 += 1
                else:
                    window.blit(self.skeleton1WalkRight[self.walkCountSkeleton1 // 3], (self.x, self.y))
                    self.walkCountSkeleton1 += 1
            else:
                if 0 < round(self.x + self.width) - round(man.x + man.width) <= 58 and man.hp > 0:
                    window.blit(self.skeleton1SliceLeft[self.walkCountSkeleton1 // 3], (self.x, self.y))
                    self.walkCountSkeleton1 += 1
                else:
                    window.blit(self.skeleton1WalkLeft[self.walkCountSkeleton1 // 3], (self.x, self.y))
                    self.walkCountSkeleton1 += 1
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox_s[0], self.hitbox_s[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 255, 0), (self.hitbox_s[0], self.hitbox_s[1] - 20,
                                                   50 - ((50 / 18) * (18 - self.healthSkeleton1)), 10))
            self.hitbox_s = (self.x + 28, self.y + 37, 30, 42)
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox_s, 2)

    def draw_boss(self, window):
        self.move_boss()
        if self.visible:
            if self.walkCountBoss + 1 >= 33:
                self.walkCountBoss = 0
            if self.velBoss > 0:
                if 0 < round(man.x + man.width) - round(self.x + self.width) <= 70 and man.hp > 0:
                    window.blit(self.bossSliceRight[self.walkCountBoss // 4], (self.x, self.y))
                    self.walkCountBoss += 2
                else:
                    window.blit(self.bossWalkRight[self.walkCountBoss // 3], (self.x, self.y))
                    self.walkCountBoss += 1
            else:
                if 0 < round(self.x + self.width) - round(man.x + man.width) <= 70 and man.hp > 0:
                    window.blit(self.bossSliceLeft[self.walkCountBoss // 4], (self.x, self.y))
                    self.walkCountBoss += 2
                else:
                    window.blit(self.bossWalkLeft[self.walkCountBoss // 3], (self.x, self.y))
                    self.walkCountBoss += 1
            pygame.draw.rect(window, (255, 0, 0), (self.hitbox_s[0], self.hitbox_s[1] - 20, 50, 10))
            pygame.draw.rect(window, (0, 255, 0), (self.hitbox_s[0], self.hitbox_s[1] - 20,
                                                   50 - ((50 / 32) * (32 - self.healthBoss)), 10))
            self.hitbox_s = (self.x + 20, self.y + 20, 46, 42)
            #pygame.draw.rect(window, (255, 0, 0), self.hitbox_s, 2)

    def move_enemy(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0
        else:
            if self.x - self.vel > 5:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

    def move_knight(self):
        if self.velKnight > 0:
            if self.x + self.velKnight < self.path[1]:
                self.x += self.velKnight
            else:
                self.velKnight *= -1
                self.walkCountKnight = 0
        else:
            if self.x - self.velKnight > 5:
                self.x += self.velKnight
            else:
                self.velKnight *= -1
                self.walkCountKnight = 0

    def move_skeleton1(self):
        if self.velSkeleton1 > 0:
            if self.x + self.velSkeleton1 < self.path[1]:
                self.x += self.velSkeleton1
            else:
                self.velSkeleton1 *= -1
                self.walkCountSkeleton1 = 0
        else:
            if self.x - self.velSkeleton1 > 5:
                self.x += self.velSkeleton1
            else:
                self.velSkeleton1 *= -1
                self.walkCountSkeleton1 = 0

    def move_boss(self):
        if self.velBoss > 0:
            if self.x + self.velBoss < self.path[1]:
                self.x += self.velBoss
            else:
                self.velBoss *= -1
                self.walkCountBoss = 0
        else:
            if self.x - self.velBoss > 5:
                self.x += self.velBoss
            else:
                self.velBoss *= -1
                self.walkCountBoss = 0

    def hit_enemy(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            deathSound.play()

    def hit_knight(self):
        if self.healthKnight > 0:
            self.healthKnight -= 1
        else:
            self.visible = False
            deathSound.play()

    def hit_skeleton1(self):
        if self.healthSkeleton1 > 0:
            self.healthSkeleton1 -= 1
        else:
            self.visible = False
            deathSound.play()

    def hit_boss(self, bullet_given):
        if self.healthBoss > 0:
            self.healthBoss -= 1
            if bullet_given.direction * self.velBoss > 0:
                self.velBoss *= -1
        else:
            self.visible = False
            deathSound.play()


pygame.init()
window = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Trump VS Mexicans")

clock = pygame.time.Clock()

walkRight = [pygame.image.load('pygame_right_1.png'),
             pygame.image.load('pygame_right_2.png'),
             pygame.image.load('pygame_right_3.png'),
             pygame.image.load('pygame_right_4.png'),
             pygame.image.load('pygame_right_5.png'),
             pygame.image.load('pygame_right_6.png')]

walkLeft = [pygame.image.load('pygame_left_1.png'),
            pygame.image.load('pygame_left_2.png'),
            pygame.image.load('pygame_left_3.png'),
            pygame.image.load('pygame_left_4.png'),
            pygame.image.load('pygame_left_5.png'),
            pygame.image.load('pygame_left_6.png')]

playerStand = pygame.image.load('pygame_idle.png')

backGround = pygame.image.load('desert.png')

shootSound = pygame.mixer.Sound('shoot.wav')
deathSound = pygame.mixer.Sound('died.wav')
emptySound = pygame.mixer.Sound('emty.wav')
reloading = pygame.mixer.Sound('reloading.wav')

mzusic = pygame.mixer.music.load('cyka.mp3')
pygame.mixer.music.play(-1)


def draw_window():
    window.blit(backGround, (0, -300))
    text1 = fontStart.render('PRESS F2 TO START', 1, (220, 200, 5))
    text2 = font.render("TRUMP'S HP", 1, (100, 100, 5))
    text = font.render('SCORE: ' + str(score), 1, (225, 0, 5))
    ammo = font.render('AMMO: ' + str(clip), 1, (100, 100, 5))
    text3 = font.render("--> & <--  -  Move", 1, (84, 255, 159, 255))
    text4 = font.render("SPACE  -  Jump", 1, (84, 255, 159, 255))
    text5 = font.render("Z  -  Fire", 1, (84, 255, 159, 255))
    text6 = font.render("X  -  Reload", 1, (84, 255, 159, 255))
    text7 = font.render('WELL, GG', 1, (218, 165, 32, 255))
    if score == 0:
        text8 = font.render("YOU'VE STOPPED NONE OF MEXICANS((", 1, (0, 238, 0, 255))
    elif score == 1:
        text8 = font.render("YOU'VE MANAGED TO STOP ONLY " + str(score) + " MEXICAN(", 1, (0, 238, 0, 255))
    elif 1 < score <= 26:
        text8 = font.render("YOU'VE MANAGED TO STOP ONLY " + str(score) + " MEXICANS(", 1, (0, 238, 0, 255))
    else:
        text8 = font.render("YOU'VE STOPPED " + str(score) + " MEXICANS!", 1, (0, 238, 0, 255))
    if begin:
        if man.hp > 0:
            man.draw(window)
        else:
            if score > 26:
                window.blit(text7, (600 - text7.get_width() // 2, 270))
                window.blit(text8, (600 - text8.get_width() // 2, 350))
            else:
                window.blit(text8, (600 - text8.get_width() // 2, 360))
        window.blit(text2, (700, 10))
        window.blit(text, (3, 10))
        window.blit(ammo, (800, 50))
        for now__e in bad_guys:
            now__e.draw_enemy(window)
        for now__k in knights:
            now__k.draw_knight(window)
        for now__s1 in skeleton1:
            now__s1.draw_skeleton1(window)
        for now__b in bullets:
            now__b.draw_bullets(window)
        for now__b in bosses:
            now__b.draw_boss(window)
    else:
        window.blit(text1, (600 - text1.get_width() // 2, 240))
        window.blit(text3, (900 - text3.get_width() // 2, 320))
        window.blit(text4, (900 - text4.get_width() // 2, 350))
        window.blit(text5, (900 - text5.get_width() // 2, 380))
        window.blit(text6, (900 - text6.get_width() // 2, 410))
    pygame.display.update()


def create_enemies(m1):
    for i in range(m1):
        q = random.randint(1, 2)
        if q == 2:
            p = 1
        else:
            p = -1

        r = 544
        if man.x <= 200:
            bad_guys.append(Enemies(random.randint(round(man.x) + 150, 1149), r, 64, 64, 1150, p))
        elif man.x >= 1000:
            bad_guys.append(Enemies(random.randint(6, round(man.x) - 150), r, 64, 64, 1150, p))
        else:
            spawn = man.x
            while man.x - 150 <= spawn <= man.x + 150:
                spawn = random.randint(6, 1119)
            bad_guys.append(Enemies(spawn, r, 64, 64, 1150, p))


def create_knights(m2):
    for i1 in range(m2):
        q = random.randint(1, 2)
        if q == 2:
            p = 1
        else:
            p = -1

        r = 516
        if man.x <= 200:
            knights.append(Enemies(random.randint(round(man.x) + 150, 1149), r, 64, 64, 1150, p))
        elif man.x >= 1000:
            knights.append(Enemies(random.randint(6, round(man.x) - 150), r, 64, 64, 1150, p))
        else:
            spawn = man.x
            while man.x - 150 <= spawn <= man.x + 150:
                spawn = random.randint(6, 1119)
            knights.append(Enemies(spawn, r, 64, 64, 1150, p))


def create_skeleton(m3):
    for i2 in range(m3):
        q = random.randint(1, 2)
        if q == 2:
            p = 1
        else:
            p = -1

        r = 500
        if man.x <= 200:
            skeleton1.append(Enemies(random.randint(round(man.x) + 150, 1149), r, 64, 64, 1150, p))
        elif man.x >= 1000:
            skeleton1.append(Enemies(random.randint(6, round(man.x) - 150), r, 64, 64, 1150, p))
        else:
            spawn = man.x
            while man.x - 150 <= spawn <= man.x + 150:
                spawn = random.randint(6, 1119)
            skeleton1.append(Enemies(spawn, r, 64, 64, 1150, p))


def create_boss(m4):
    for i3 in range(m4):
        q = random.randint(1, 2)
        if q == 2:
            p = 1
        else:
            p = -1

        r = 520
        if man.x <= 200:
            bosses.append(Enemies(random.randint(round(man.x) + 150, 1149), r, 64, 64, 1150, p))
        elif man.x >= 1000:
            bosses.append(Enemies(random.randint(6, round(man.x) - 150), r, 64, 64, 1150, p))
        else:
            spawn = man.x
            while man.x - 150 <= spawn <= man.x + 150:
                spawn = random.randint(6, 1119)
            bosses.append(Enemies(spawn, r, 64, 64, 1150, p))


# _MAIN_ #
font = pygame.font.SysFont('comicsans', 50, True, True)
fontStart = pygame.font.SysFont('comicsans', 100, True, True)
man = Player(500, 529, 60, 71, 'right')
bad_guys = []
knights = []
skeleton1 = []
bosses = []
n = 2
create_enemies(n)
# create_skeleton(n)
# create_boss(n)
shootLoop = 0
k = 0
s = 0
z = 0
clip = 25
score = 0
hp = 5
wave_defeated = 1
bullets = []
GameOn = True
begin = False
countdown = False
pause = False
flag = True
kl = pygame.key.get_pressed()
while GameOn:
    clock.tick(30)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_F2]:
        countdown = True
        begin = True

    for now in bad_guys:
        if now.visible:
            if man.hitbox[1] < now.hitbox[3] + now.hitbox[1] and man.hitbox[1] + man.hitbox[3] > now.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > now.hitbox[0] and man.hitbox[0] < now.hitbox[0] + now.hitbox[2]:
                    man.hit(bad_guys)
                    hp -= 1

    for now_k in knights:
        if now_k.visible:
            if man.hitbox[1] < now_k.hitbox[3] + now_k.hitbox[1] and man.hitbox[1] + man.hitbox[3] > now_k.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > now_k.hitbox[0] and man.hitbox[0] < now_k.hitbox[0] + now_k.hitbox[2]:
                    man.hit(knights)
                    hp -= 1

    for now_s in skeleton1:
        if now_s.visible:
            if man.hitbox[1] < now_s.hitbox_s[3] + now_s.hitbox_s[1] and man.hitbox[1] + man.hitbox[3] > now_s.hitbox_s[1]:
                if man.hitbox[0] + man.hitbox[2] > now_s.hitbox_s[0] and man.hitbox[0] < now_s.hitbox_s[0] + now_s.hitbox_s[2]:
                    man.hit(skeleton1)
                    hp -= 1

    for now_b in bosses:
        if now_b.visible:
            if man.hitbox[1] < now_b.hitbox_s[3] + now_b.hitbox_s[1] and man.hitbox[1] + man.hitbox[3] > now_b.hitbox_s[1]:
                if man.hitbox[0] + man.hitbox[2] > now_b.hitbox_s[0] and man.hitbox[0] < now_b.hitbox_s[0] + now_b.hitbox_s[2]:
                    man.hit(bosses)
                    hp -= 1


    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 1:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameOn = False

    for bullet in bullets:
        for now in bad_guys:
            if now.visible:
                if bullet.y - bullet.radius < now.hitbox[3] + now.hitbox[1] and bullet.y + bullet.radius > now.hitbox[1]:
                    if bullet.x + bullet.radius > now.hitbox[0] and bullet.x - bullet.radius < now.hitbox[0] + now.hitbox[2]:
                        now.hit_enemy()
                        if not now.visible:
                            # bad_guys.pop(bad_guys.index(now))
                            score += 1
                        try:
                            bullets.pop(bullets.index(bullet))
                        except:
                            ValueError
        for now_k in knights:
            if now_k.visible:
                if bullet.y - bullet.radius < now_k.hitbox[3] + now_k.hitbox[1] and bullet.y + bullet.radius > now_k.hitbox[1]:
                    if bullet.x + bullet.radius > now_k.hitbox[0] and bullet.x - bullet.radius < now_k.hitbox[0] + now_k.hitbox[2]:
                        now_k.hit_knight()
                        if not now_k.visible:
                            # bad_guys.pop(bad_guys.index(now))
                            score += 1
                        try:
                            bullets.pop(bullets.index(bullet))
                        except:
                            ValueError
        for now_s in skeleton1:
            if now_s.visible:
                if bullet.y - bullet.radius < now_s.hitbox_s[3] + now_s.hitbox_s[1] and bullet.y + bullet.radius > now_s.hitbox_s[1]:
                    if bullet.x + bullet.radius > now_s.hitbox_s[0] and bullet.x - bullet.radius < now_s.hitbox_s[0] + now_s.hitbox_s[2]:
                        now_s.hit_skeleton1()
                        if not now_s.visible:
                            # bad_guys.pop(bad_guys.index(now))
                            score += 1
                        try:
                            bullets.pop(bullets.index(bullet))
                        except:
                            ValueError
        for now_b in bosses:
            if now_b.visible:
                if bullet.y - bullet.radius < now_b.hitbox_s[3] + now_b.hitbox_s[1] and bullet.y + bullet.radius > now_b.hitbox_s[1]:
                    if bullet.x + bullet.radius > now_b.hitbox_s[0] and bullet.x - bullet.radius < now_b.hitbox_s[0] + now_b.hitbox_s[2]:
                        now_b.hit_boss(bullet)
                        if not now_b.visible:
                            # bad_guys.pop(bad_guys.index(now))
                            score += 1
                        try:
                            bullets.pop(bullets.index(bullet))
                        except:
                            ValueError
        if 0 < bullet.x < 1200:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    if score == (2 * 2 + wave_defeated - 1) * wave_defeated / 2:
        man.new_wave(wave_defeated)
        wave_defeated += 1
        if wave_defeated % 4 == 0:
            z += 1
        elif wave_defeated % 3 == 0:
            k += 1
        elif wave_defeated % 2 == 0:
            s += 1
        else:
            n += 1
        create_enemies(n)
        create_skeleton(s)
        create_knights(k)
        create_boss(z)

    """____________________________
            РАБОТА С КЛАВИШАМИ
    _______________________________"""

    if keys[pygame.K_x]:
        clip = 25
        reloading.play()

    if clip > 0:
        if keys[pygame.K_z] and shootLoop == 0:
            if len(bullets) < 3:
                shootSound.play(0, 0, 100)
            if man.lastMove == 'right':
                direction = 1
            else:
                direction = -1
            if len(bullets) < 3:
                bullets.append(Shell(round(man.x + man.width // 2),
                                     round(man.y + man.height // 2),
                                     5, (255, 0, 0), direction))
                clip -= 1
            shootLoop = 1
    else:
        if keys[pygame.K_z]:
            emptySound.play()

    if keys[pygame.K_LEFT] and man.x > 5:
        man.x -= man.speed
        man.left = True
        man.right = False
        man.lastMove = 'left'
    elif keys[pygame.K_RIGHT] and man.x < 1195 - man.width:
        man.x += man.speed
        man.left = False
        man.right = True
        man.lastMove = 'right'
    else:
        man.left = False
        man.right = False
        man.animationCount = 0
    if not man.isJump:
        if keys[pygame.K_SPACE]:
            man.isJump = True
    else:
        if man.jumpCount >= -10:
            if man.jumpCount < 0:
                man.y += man.jumpCount ** 2 / 2
            else:
                man.y -= man.jumpCount**2 / 2
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    if keys[pygame.K_ESCAPE]:
        pygame.quit()

    draw_window()

pygame.quit()
