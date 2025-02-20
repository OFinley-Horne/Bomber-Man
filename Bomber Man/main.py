import pgzrun
import random
from pgzhelper import *


WIDTH = 800
HEIGHT = 800


bomber = Actor('bomber\\idle\\1', (800//2, HEIGHT//2))


bomber.scale = 1


bomber.images = []


# use UP, RIGHT, LEFT to move
# use Z to shoot
# use D to open the door


# the first bomb is going to be wacky
# you can control the bombs in the air by pressing Right or Left


# kill all the enemies to open the door


# player images
bomber_idle = ['bomber\\idle\\1', 'bomber\\idle\\2', 'bomber\\idle\\3', 'bomber\\idle\\4', 'bomber\\idle\\5', 'bomber\\idle\\6', 'bomber\\idle\\7', 'bomber\\idle\\8', 'bomber\\idle\\9', 'bomber\\idle\\10', 'bomber\\idle\\11', 'bomber\\idle\\12', 'bomber\\idle\\13',
               'bomber\\idle\\14', 'bomber\\idle\\15', 'bomber\\idle\\16', 'bomber\\idle\\17', 'bomber\\idle\\18', 'bomber\\idle\\19', 'bomber\\idle\\21', 'bomber\\idle\\2', 'bomber\\idle\\22', 'bomber\\idle\\23', 'bomber\\idle\\24', 'bomber\\idle\\25', 'bomber\\idle\\26']
bomber_run = ['bomber\\run\\1', 'bomber\\run\\2', 'bomber\\run\\3', 'bomber\\run\\4', 'bomber\\run\\5', 'bomber\\run\\6', 'bomber\\run\\7',
              'bomber\\run\\8', 'bomber\\run\\9', 'bomber\\run\\10', 'bomber\\run\\11', 'bomber\\run\\12', 'bomber\\run\\13', 'bomber\\run\\14']
jump = ['bomber\\jump\\1', 'bomber\\jump\\2',
        'bomber\\jump\\3', 'bomber\\jump\\4', 'bomber\\jump\\5']
bomber_hit = ['bomber\\hit\\1', 'bomber\\hit\\2', 'bomber\\hit\\3', 'bomber\\hit\\4',
              'bomber\\hit\\5', 'bomber\\hit\\6', 'bomber\\hit\\7', 'bomber\\hit\\8']
bomber_death_hit = ['bomber\\dead hit\\1', 'bomber\\dead hit\\2', 'bomber\\dead hit\\3',
                    'bomber\\dead hit\\4', 'bomber\\dead hit\\5', 'bomber\\dead hit\\6']
bomber_death_ground = ['bomber\\dead ground\\1', 'bomber\\dead ground\\2',
                       'bomber\\dead ground\\3', 'bomber\\dead ground\\4', ]
bomber.images = bomber_idle
bomber.fps = 20


# player variables
bomber.is_alive = True
bomber.is_idle = False
bomber.is_jumping = False
bomber.is_running = False
bomber.runningR = False
bomber.runningL = False
bomber.is_hit = False
bomber.is_dead = False
bomber.is_crouching = False
bomber.is_attacking = False
bomber.is_falling = False
bomber.invinc = False
bomber.hp = 1
bomber.dx = 0
bomber.dy = 5
bomber.start = True


# bomb images
bomb = Actor('objects\\bomb\\bomb off\\1')
bomb.images = []
bomb_off = ['objects\\bomb\\bomb off\\1']
bomb_on = ['objects\\bomb\\bomb on\\1', 'objects\\bomb\\bomb on\\2', 'objects\\bomb\\bomb on\\3',
           'objects\\bomb\\bomb on\\4', 'objects\\bomb\\bomb on\\5', 'objects\\bomb\\bomb on\\6']
bomb_explosion = ['objects\\bomb\\explosion\\1', 'objects\\bomb\\explosion\\2', 'objects\\bomb\\explosion\\3', 'objects\\bomb\\explosion\\4',
                  'objects\\bomb\\explosion\\5', 'objects\\bomb\\explosion\\6', 'objects\\bomb\\explosion\\7', 'objects\\bomb\\explosion\\8', 'objects\\bomb\\explosion\\9']
bomb.images = bomb_off
bomb.fps = 10


# bomb variables
bomb.is_alive = False
bomb.explosion = False
bomb.throwR = False
bomb.throwL = False
bomb.place = False
bomb.grav = True
bomb.off = True
bomb.on = False
bomb.dy = 5
bomb.dx = 0


# enemy cucumber
cucumber = Actor('cucumber\\idle\\1')
cucumber.images = []
cucumber_idle = ['cucumber\\idle\\1', 'cucumber\\idle\\2', 'cucumber\\idle\\3', 'cucumber\\idle\\4', 'cucumber\\idle\\5', 'cucumber\\idle\\6', 'cucumber\\idle\\7', 'cucumber\\idle\\8', 'cucumber\\idle\\9', 'cucumber\\idle\\10', 'cucumber\\idle\\11', 'cucumber\\idle\\12', 'cucumber\\idle\\13', 'cucumber\\idle\\14', 'cucumber\\idle\\15', 'cucumber\\idle\\16', 'cucumber\\idle\\17', 'cucumber\\idle\\18',
                 'cucumber\\idle\\19', 'cucumber\\idle\\20', 'cucumber\\idle\\21', 'cucumber\\idle\\22', 'cucumber\\idle\\23', 'cucumber\\idle\\24', 'cucumber\\idle\\25', 'cucumber\\idle\\26', 'cucumber\\idle\\27', 'cucumber\\idle\\28', 'cucumber\\idle\\29', 'cucumber\\idle\\30', 'cucumber\\idle\\31', 'cucumber\\idle\\32', 'cucumber\\idle\\33', 'cucumber\\idle\\34', 'cucumber\\idle\\35', 'cucumber\\idle\\36']
cucumber_dead_ground = ['cucumber\\dead ground\\1', 'cucumber\\dead ground\\2',
                        'cucumber\\dead ground\\3', 'cucumber\\dead ground\\4']
cucumber_dead_hit = ['cucumber\\dead hit\\1', 'cucumber\\dead hit\\2', 'cucumber\\dead hit\\3',
                     'cucumber\\dead hit\\4', 'cucumber\\dead hit\\5', 'cucumber\\dead hit\\6']
cucumber.images = cucumber_idle
cucumber.fps = 20


# cucumber variables
cucumber.hp = 1
cucumber.dx = 0
cucumber.dy = 5
cucumber.run_once = 0
cucumber.moveR = False
cucumber.moveL = True
cucumber.invinc = False
cucumber.spawn = False
cucumber.is_alive = True


# enemy big guy aka CHAD
big_guy = Actor('big guy\\run\\1')
big_guy.images = []
big_guy_run = ['big guy\\run\\1', 'big guy\\run\\2', 'big guy\\run\\3', 'big guy\\run\\4', 'big guy\\run\\5', 'big guy\\run\\6', 'big guy\\run\\7', 'big guy\\run\\8',
               'big guy\\run\\9', 'big guy\\run\\10', 'big guy\\run\\11', 'big guy\\run\\12', 'big guy\\run\\13', 'big guy\\run\\14', 'big guy\\run\\15', 'big guy\\run\\16']
big_guy_hit = ['big guy\\hit\\1', 'big guy\\hit\\2', 'big guy\\hit\\3', 'big guy\\hit\\4',
               'big guy\\hit\\5', 'big guy\\hit\\6', 'big guy\\hit\\7', 'big guy\\hit\\8']
big_guy_dead_hit = ['big guy\\dead hit\\1', 'big guy\\dead hit\\2', 'big guy\\dead hit\\3',
                    'big guy\\dead hit\\4', 'big guy\\dead hit\\5', 'big guy\\dead hit\\6']
big_guy_dead_ground = ['big guy\\dead ground\\1', 'big guy\\dead ground\\2',
                       'big guy\\dead ground\\3', 'big guy\\dead ground\\4']
big_guy.images = big_guy_run
big_guy.fps = 20


# big guy variables
big_guy.is_alive = True
big_guy.moveR = False
big_guy.moveL = True
big_guy.spawn = False
big_guy.hp = 1
big_guy.dx = 0
big_guy.dy = 5
big_guy.run_once = 0


# enemy pirate
pirate = Actor('pirate\\run\\1')
pirate.images = []
pirate_run = ['pirate\\run\\1', 'pirate\\run\\2', 'pirate\\run\\3', 'pirate\\run\\4', 'pirate\\run\\5', 'pirate\\run\\6', 'pirate\\run\\7',
              'pirate\\run\\8', 'pirate\\run\\9', 'pirate\\run\\10', 'pirate\\run\\11', 'pirate\\run\\12', 'pirate\\run\\13', 'pirate\\run\\14']
pirate_dead_hit = ['pirate\\dead hit\\1', 'pirate\\dead hit\\2', 'pirate\\dead hit\\3',
                   'pirate\\dead hit\\4', 'pirate\\dead hit\\5', 'pirate\\dead hit\\6']
pirate_dead_ground = ['pirate\\dead ground\\1', 'pirate\\dead ground\\2',
                      'pirate\\dead ground\\3', 'pirate\\dead ground\\4']
pirate.images = pirate_run
pirate.fps = 20


# pirate variables
pirate.is_alive = True
pirate.hp = 1
pirate.moveR = False
pirate.moveL = True
pirate.spawn = False
pirate.run_once = 0
pirate.dx = 0
pirate.dy = 5


# making a lists for platforms and walls and then putting them into them
floors = []
floor_a = Actor('background\\platforms', (330, 630))
floor_b = Actor('background\\platforms', (470, 430))
floor_c = Actor('background\\platforms', (330, 230))


floors.append(floor_a)
floors.append(floor_b)
floors.append(floor_c)
housing = []
platform_a = (Rect((0, 600), (660, 50)))
platform_b = (Rect((140, 400), (660, 50)))
platform_c = (Rect((0, 200), (660, 50)))
housing.append(Rect((0, 750), (WIDTH, 50)))
housing.append(Rect((0, 0), (WIDTH, 50)))
housing.append(Rect((760, 0), (40, HEIGHT)))
housing.append(Rect((0, 0), (40, HEIGHT)))
housing.append(platform_a)
housing.append(platform_b)
housing.append(platform_c)


# the door
door = Actor('objects\\door\\closed\\1', (100, 150))
door.images = []
door_closed = ['objects\\door\\closed\\1']
door_open = ['objects\\door\\opening\\1', 'objects\\door\\opening\\2',
             'objects\\door\\opening\\3', 'objects\\door\\opening\\4', 'objects\\door\\opening\\5']
door_opened = ['objects\\door\\opening\\5']
door.images = door_closed
door.all_enemies = 3
door.no_entry = True
door.run_once1 = 0
door.run_once2 = 0
door.run_once3 = 0


# background and stuff
bg = Actor('background\\background')


# levels
level1 = True
# if ya win
bomber.you_win = False


def draw():
    screen.clear()

    for i in housing:
        screen.draw.rect(i, (0, 255, 0))

    bg.draw()
    for floor in floors:
        floor.draw()

    door.draw()
    if door.no_entry == True:
        screen.draw.text(
            f"kill all enemies: {door.all_enemies} enemies left", (100, 150))
    pirate.draw()
    big_guy.draw()
    cucumber.draw()
    bomber.draw()
    if bomber.is_alive == False:
        screen.draw.text('!!! YOU LOSE !!!', (270, 400),
                         color='red', fontsize=50)
    if bomber.you_win == True and door.no_entry == False:
        screen.draw.text("!!! YOU WIN !!!", (270, 400),
                         color='green', fontsize=50)
    if bomb.is_alive:
        bomb.draw()


# if the keys are pressed
def on_key_down(key):

    if bomber.is_alive == True:
        # moving right and left
        if key == keys.LEFT and bomber.runningR == False:
            bomber.is_running = True
            bomber.is_attacking = False
            bomber.runningL = True

            bomber.flip_x = True
            bomber.images = bomber_run
        if key == keys.RIGHT and bomber.runningL == False:
            bomber.is_running = True
            bomber.is_attacking = False
            bomber.runningR = True

            bomber.flip_x = False
            bomber.images = bomber_run
        if bomber.colliderect(door):
            if key == keys.D and door.all_enemies == 0:
                door.images = door_open
                bomber.you_win = True
            else:
                door.images = door_closed


# shooting the bomb
        if key == keys.Z and bomb.is_alive == False:
            bomb.grav = True
            bomb.dx = 6
            bomb.dy = 6
            bomb.is_alive = True


# to throw bomb left or right
            if bomber.flip_x == False:
                bomb.x = bomber.x + 30
                bomb.y = bomber.y - 30
            if bomber.flip_x == True:
                bomb.x = bomber.x - 30
                bomb.y = bomber.y - 30

        if bomber.is_falling == False:
            if key == keys.UP:
                bomber.images = jump

                bomber.dy = 15
                bomber.is_falling = True


# if the keys are lifted up
def on_key_up(key):
    # checking if the right or left keys are lifted
    if bomber.is_alive == True:
        if key == keys.LEFT:
            bomber.runningL = False
            if bomber.runningR == False:
                bomber.is_running = False
                bomber.is_idle = True
                bomber.images = bomber_idle
        if key == keys.RIGHT:
            bomber.runningR = False
            if bomber.runningL == False:
                bomber.is_running = False
                bomber.is_idle = True
                bomber.images = bomber_idle


# spawn big_guy
def enable_big_guy():
    big_guy.spawn = True

# spawn pirate


def enable_pirate():
    pirate.spawn = True

# spawn_cucumber


def enable_cucumber():
    cucumber.spawn = True


# make cucumber follow you
def cucumber_follow():
    if cucumber.is_alive == True:
        if bomber.flip_x == False:
            cucumber.x = bomber.x - 100
            cucumber.y = bomber.y
        if bomber.flip_x == True:
            cucumber.x = bomber.x + 100
            cucumber.y = bomber.y

# spawning everything


def spawn_everything():

    if bomber.start == True:
        # makes the enemies start off the map
        start_positionsX = []
        start_positionsX.append(big_guy)
        start_positionsX.append(pirate)
        start_positionsX.append(cucumber)

        for i in start_positionsX:
            i.x = 0

        bomber.x = 50
        bomber.y = 750
        bomber.start = False
    if cucumber.spawn == False:
        clock.schedule(enable_cucumber, 1.0)
    if big_guy.spawn == False:
        clock.schedule(enable_big_guy, 5.0)
    if pirate.spawn == False:
        clock.schedule(enable_pirate, 10.0)


# update player
def update_bomber():
    # if the bomber wins

    if bomber.you_win == True:
        bomber.hp = 9999
        if bomber.images == bomber_death_ground or bomber_death_hit:
            bomber.images = bomber_idle
    # if the bomber dies
    if bomber.hp < 1:
        bomber.is_alive = False
        if bomber.images == bomber_death_hit:

            bomber.images = bomber_death_ground
            bomber.fps = 5

    # if the bomber jumps and isnt running make the images idle
    if bomber.image == 'bomber\\jump\\5' and bomber.is_running == False:
        bomber.is_idle = True
        bomber.images = bomber_idle
    # if the bomber is running keep him in the running animation after the end of the jump
    if bomber.image == 'bomber\\jump\\5' and bomber.is_running == True:
        bomber.images = bomber_run


# to make sure the bomber falls
    if bomber.images == bomber_run:
        bomber.is_falling = True


def update_bomb():

    if bomb.is_alive:

        if bomb.off == True:
            bomb.images = bomb_off
        if bomb.on == True:
            bomb.images = bomb_on
            bomb.on = False
        if bomb.image == 'objects\\bomb\\bomb on\\6':
            bomb.explosion = True
            bomb.images = bomb_explosion
        if bomb.image == 'objects\\bomb\\explosion\\9':
            bomb.is_alive = False
            bomb.explosion = False
            bomb.off = True
            bomb.x = 900
            bomb.y = 900


def update_cucumber():

    # I decided to have him to start following you

    if cucumber.spawn == True:

        if cucumber.run_once == 0:
            cucumber.x = 60
            cucumber.y = 90
            cucumber.run_once = 1

        if cucumber.run_once == 1:
            clock.schedule_interval(cucumber_follow, 3.0)

    if cucumber.hp != 1:
        cucumber.is_alive = False
        if cucumber.images == cucumber_dead_hit:

            cucumber.images = cucumber_dead_ground

    if cucumber.is_alive == False:
        cucumber.invinc = True


def update_big_guy():

    # spawn the dude
    if big_guy.spawn == True:

        if big_guy.run_once == 0:
            big_guy.x = 740
            big_guy.y = 320
            big_guy.run_once = 1

    if big_guy.is_alive == True:
        if big_guy.moveR == True:
            big_guy.x += 3
        if big_guy.moveL == True:
            big_guy.x -= 3

    if big_guy.hp != 1:
        big_guy.is_alive = False
        big_guy.moveR = False
        big_guy.moveL = False
        big_guy.x = big_guy.x

        if big_guy.images == big_guy_dead_hit:
            big_guy.images = big_guy_dead_ground


def update_pirate():

    if pirate.spawn == True:

        if pirate.run_once == 0:
            pirate.x = 60
            pirate.y = 90
            pirate.run_once = 1

    if pirate.is_alive == True:
        if pirate.moveR == True:
            pirate.x += 5
        if pirate.moveL == True:
            pirate.x -= 5

    if pirate.hp != 1:
        pirate.is_alive = False
        pirate.moveR = False
        pirate.moveL = False
        pirate.x = pirate.x

        if pirate.images == pirate_dead_hit:
            pirate.images = pirate_dead_ground


def update_door():
    if door.all_enemies == 0:
        door.no_entry = False
        if door.image == 'objects\\door\\opening\\5' and door.images == door_open:
            door.images = door_opened
        if door.images == door_opened and bomber.you_win == True:
            door.images == door_opened
    else:
        door.no_entry = True


# player collision
def player_collisions():  # I took it from Srosh :D

    for plats in housing:
        if bomber.colliderect(plats):
            bottom = ((bomber.top - plats.bottom)*-1)
            top = (bomber.bottom - plats.top)
            right = ((bomber.left - plats.right)*-1)
            left = (bomber.right - plats.left)
            if bottom < top and bottom < left and bottom < right:
                bomber.dy = 0
                bomber.top = plats.bottom

            elif top < bottom and top < left and top < right:
                bomber.bottom = plats.top
                bomber.is_falling = False
                bomber.dy = 0

            elif left < right and left < top and left < bottom:
                bomber.right = plats.left

            elif right < left and right < top and right < bottom:
                bomber.left = plats.right

    if cucumber.is_alive and bomber.is_alive:
        if bomber.colliderect(cucumber):
            bomber.hp -= 1
            bomber.images = bomber_death_hit

    if pirate.is_alive and bomber.is_alive:
        if bomber.colliderect(pirate):
            bomber.hp -= 1
            bomber.images = bomber_death_hit

    if big_guy.is_alive and bomber.is_alive:
        if bomber.colliderect(big_guy):
            bomber.hp -= 1
            bomber.images = bomber_death_hit


# bomb collision
def bomb_collisions():

    for plats in housing:
        if bomb.colliderect(plats):
            bottom = ((bomb.top - plats.bottom)*-1)
            top = (bomb.bottom - plats.top)
            right = ((bomb.left - plats.right)*-1)
            left = (bomb.right - plats.left)
            if bottom < top and bottom < left and bottom < right:
                bomb.dy = 0
                bomb.top = plats.bottom

            elif top < bottom and top < left and top < right:
                bomb.bottom = plats.top
                bomb.is_falling = False
                bomb.dy = 0
                if bomb.image == 'objects\\bomb\\bomb off\\1':
                    bomb.off = False
                    bomb.on = True
                    bomb.throwR = False
                    bomb.throwL = False
                    bomb.grav = False

            elif left < right and left < top and left < bottom:
                bomb.right = plats.left

            elif right < left and right < top and right < bottom:
                bomb.left = plats.right

    # if the bomb hits the bomber man
    if bomb.colliderect(bomber):
        if bomb.images == bomb_explosion:
            bomber.images = bomber_death_hit
            bomber.hp -= 1

    # the bomb hits the cucumber

    if bomb.colliderect(cucumber):
        if bomb.images == bomb_explosion:
            cucumber.images = cucumber_dead_hit
            cucumber.hp -= 1

    if bomb.colliderect(big_guy):
        if bomb.images == bomb_explosion:
            big_guy.images = big_guy_dead_hit
            big_guy.hp -= 1

    if bomb.colliderect(pirate):
        if bomb.images == bomb_explosion:
            pirate.images = pirate_dead_hit
            pirate.hp -= 1


def pathing():

    for plats in housing:
        if cucumber.colliderect(plats):
            bottom = ((cucumber.top - plats.bottom)*-1)
            top = (cucumber.bottom - plats.top)
            right = ((cucumber.left - plats.right)*-1)
            left = (cucumber.right - plats.left)

            if top < bottom and top < left and top < right:
                cucumber.bottom = plats.top
                cucumber.is_falling = False
                cucumber.dy = 0

            elif left < right and left < top and left < bottom:
                cucumber.right = plats.left
                cucumber.moveR = False
                cucumber.moveL = True
                cucumber.flip_x = True

            elif right < left and right < top and right < bottom:
                cucumber.left = plats.right
                cucumber.moveR = True
                cucumber.moveL = False
                cucumber.flip_x = False

    for plats in housing:
        if big_guy.colliderect(plats):
            bottom = ((big_guy.top - plats.bottom)*-1)
            top = (big_guy.bottom - plats.top)
            right = ((big_guy.left - plats.right)*-1)
            left = (big_guy.right - plats.left)

            if bottom < top and bottom < left and bottom < right:
                pirate.dy = 0
                pirate.top = plats.bottom

            if top < bottom and top < left and top < right:

                big_guy.bottom = plats.top
                big_guy.dy = 0

            elif left < right and left < top and left < bottom:
                big_guy.right = plats.left
                big_guy.moveR = False
                big_guy.moveL = True
                big_guy.flip_x = True

            elif right < left and right < top and right < bottom:
                big_guy.left = plats.right
                big_guy.moveL = False
                big_guy.moveR = True
                big_guy.flip_x = False

    for plats in housing:
        if pirate.colliderect(plats):
            bottom = ((pirate.top - plats.bottom)*-1)
            top = (pirate.bottom - plats.top)
            right = ((pirate.left - plats.right)*-1)
            left = (pirate.right - plats.left)

            if top < bottom and top < left and top < right:
                pirate.bottom = plats.top
                pirate.is_falling = False
                pirate.dy = 0

            elif left < right and left < top and left < bottom:
                pirate.right = plats.left
                pirate.moveL = True
                pirate.moveR = False
                pirate.flip_x = True

            elif right < left and right < top and right < bottom:
                pirate.left = plats.right
                pirate.moveL = False
                pirate.moveR = True
                pirate.flip_x = False


def enemies_left():
    if cucumber.is_alive == False:
        if door.run_once1 == 0:
            door.all_enemies -= 1
            door.run_once1 = 1

    if big_guy.is_alive == False:
        if door.run_once2 == 0:
            door.all_enemies -= 1
            door.run_once2 = 1

    if pirate.is_alive == False:
        if door.run_once3 == 0:
            door.all_enemies -= 1
            door.run_once3 = 1


def gravity():
    # for the player
    if bomber.is_falling == True:
        if bomber.dy > - 25:
            bomber.dy -= 0.5
        bomber.y -= bomber.dy

    if cucumber.dy > - 25:
        cucumber.dy -= 0.5
    cucumber.y -= cucumber.dy

    if pirate.dy > - 25:
        pirate.dy -= 0.5
    pirate.y -= pirate.dy

    if big_guy.dy > - 25:
        big_guy.dy -= 0.5
    big_guy.y -= big_guy.dy


# special gravity for the bomb
def bomb_gravity():

    if bomber.flip_x == True:
        bomb.y -= bomb.dy
        bomb.x -= bomb.dx
    if bomber.flip_x == False:
        bomb.y -= bomb.dy
        bomb.x += bomb.dx
    if bomb.dy > - 25:
        bomb.dy -= 0.5


def update():

    if bomber.is_running == True and bomber.is_alive == True:
        if keyboard.RIGHT and bomber.runningR == True:
            bomber.x += 5
        if keyboard.LEFT and bomber.runningL == True:
            bomber.x -= 5

    spawn_everything()
    enemies_left()
    update_door()
    update_pirate()
    update_cucumber()
    update_bomber()
    update_big_guy()
    update_bomb()

    door.animate()
    big_guy.animate()
    cucumber.animate()
    pirate.animate()
    bomber.animate()
    bomb.animate()

    # stops the bomb moving on the ground
    if bomb.grav == True:
        bomb_gravity()
    gravity()
    player_collisions()
    pathing()
    bomb_collisions()

pgzrun.go()
