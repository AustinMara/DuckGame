def on_on_created(sprite):
    sprite.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
    sprite.x = randint(0, 160)
    if Math.percent_chance(50):
        sprite.y = -10
    else:
        sprite.y = 140
    sprite.follow(player1, 20)
sprites.on_created(SpriteKind.enemy, on_on_created)

def CreatePowerup(enemyKilled: Sprite):
    mySprite2
    if Math.percent_chance(90):

        mySprite2 = sprites.all_of_kind(SpriteKind.food)._pick_random()
        console.log_value("sprite", mySprite2.x)
        mySprite2.set_position(enemyKilled.x, enemyKilled.y)
    else:
        pass
    sprites.destroy(enemyKilled)

def on_on_overlap(sprite3, otherSprite):
    CreatePowerup(otherSprite)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_a_pressed():
    global isFiring
    isFiring = not (isFiring)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_right_repeated():
    pass
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_on_created2(sprite2):
    sprite2.set_flag(SpriteFlag.GHOST_THROUGH_WALLS, True)
    sprite2.set_flag(SpriteFlag.AUTO_DESTROY, True)
    sprite2.set_bounce_on_wall(False)
    sprite2.set_flag(SpriteFlag.RELATIVE_TO_CAMERA, False)
    scene.camera_shake(2, 100)
sprites.on_created(SpriteKind.projectile, on_on_created2)

def on_a_repeated():
    global rotationProj, projectile
    rotationProj += retationSpeed2
    projectile = sprites.create_projectile_from_sprite(img("""
            2 2 2 2
            2 2 2 2
            2 2 2 2
            2 2 2 2
            """),
        player1,
        75 * Math.cos(rotationProj),
        75 * Math.sin(rotationProj))
controller.A.on_event(ControllerButtonEvent.REPEATED, on_a_repeated)

def on_on_overlap2(sprite4, otherSprite2):
    if sprite4.overlaps_with(powerupList[0]):
        print("boots")
    if sprite4.overlaps_with(powerupList[1]):
        print("rof")
    if sprite4.overlaps_with(powerupList[2]):
        print("nuke")
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_on_destroyed(sprite5):
    info.change_score_by(1)
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

def on_left_repeated():
    pass
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

mySprite: Sprite = None
projectile: Sprite = None
rotationProj = 0
isFiring = False
mySprite2: Sprite = None
powerupList: List[Sprite] = []
player1: Sprite = None
retationSpeed2 = 0
retationSpeed2 = 0.4
info.set_score(0)
player1 = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . b 2 2 b . . .
        . . . . . . b b b b b b . . . .
        . . . . . b b 2 2 2 2 2 b . . .
        . b b b b b 2 2 2 2 2 2 2 b . .
        . b d 2 b 2 2 2 2 2 2 2 2 b . .
        . . b 2 2 b 2 d 1 f 2 d 4 f . .
        . . b d 2 2 b 1 f f 2 4 4 c . .
        b b d b 2 2 2 d f b 4 4 4 4 b .
        b d d c d 2 2 b 2 4 4 4 4 4 4 b
        c d d d c c b 2 2 2 2 2 2 2 b .
        c b d d d d d 2 2 2 2 2 2 2 b .
        . c d d d d d d 2 2 2 2 2 d b .
        . . c b d d d d d 2 2 2 b b . .
        . . . c c c c c c c c b b . . .
        """),
    SpriteKind.player)
controller.move_sprite(player1)
tiles.set_current_tilemap(tilemap("""
    level1
    """))
scene.camera_follow_sprite(player1)
tiles.place_on_random_tile(player1, sprites.dungeon.stair_large)
rateOfFire2 = 200
info.set_life(100)
next_level = 5
powerupList = [sprites.create(assets.image("""
        speedUp
        """), SpriteKind.food),
    sprites.create(assets.image("""
        rateOfFire
        """), SpriteKind.food),
    sprites.create(assets.image("""
        nuke
        """), SpriteKind.food)]

def on_forever():
    global rotationProj, projectile
    if isFiring:
        rotationProj += retationSpeed2
        projectile = sprites.create_projectile_from_sprite(img("""
                2 2 2 2
                2 2 2 2
                2 2 2 2
                2 2 2 2
                """),
            player1,
            75 * Math.cos(rotationProj),
            75 * Math.sin(rotationProj))
    pause(rateOfFire2)
forever(on_forever)

def on_update_interval():
    global mySprite
    mySprite = sprites.create(img("""
            . . . . . . . . . . . . . .
            e e e . . . . e e e . . . .
            c d d c . . c d d c . . . .
            c b d d f f d d b c . . . .
            c 3 b d d b d b 3 c . . . .
            f b 3 d d d d 3 b f . . . .
            e d d d d d d d d e . . . .
            e d f d d d d f d e . b f b
            f d d f d d f d d f . f d f
            f b d d b b d d 2 b f f d f
            . f 2 2 2 2 2 2 d b b d b f
            . f d d d d d d d f f f f .
            . . f d b d f d f . . . . .
            . . . f f f f f f . . . . .
            """),
        SpriteKind.enemy)
game.on_update_interval(200, on_update_interval)
