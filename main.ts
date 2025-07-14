sprites.onCreated(SpriteKind.Enemy, function (sprite) {
    sprite.setFlag(SpriteFlag.GhostThroughWalls, true)
    sprite.x = randint(0, 160)
    if (Math.percentChance(50)) {
        sprite.y = -10
    } else {
        sprite.y = 140
    }
    sprite.follow(player1, 20)
})
function CreatePowerup (enemyKilled: Sprite) {
    mySprite2 = powerupList._pickRandom()
    console.logValue("sprite", mySprite2.x)
    mySprite.setPosition(enemyKilled.x, enemyKilled.y)
}
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite3, otherSprite) {
    sprites.destroy(otherSprite)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    isFiring = !(isFiring)
})
controller.right.onEvent(ControllerButtonEvent.Repeated, function () {
	
})
sprites.onCreated(SpriteKind.Projectile, function (sprite2) {
    sprite2.setFlag(SpriteFlag.GhostThroughWalls, true)
    sprite2.setFlag(SpriteFlag.AutoDestroy, true)
    sprite2.setBounceOnWall(false)
    sprite2.setFlag(SpriteFlag.RelativeToCamera, false)
    scene.cameraShake(2, 100)
})
controller.A.onEvent(ControllerButtonEvent.Repeated, function () {
    rotationProj += retationSpeed2
    projectile = sprites.createProjectileFromSprite(img`
        2 2 2 2 
        2 2 2 2 
        2 2 2 2 
        2 2 2 2 
        `, player1, 75 * Math.cos(rotationProj), 75 * Math.sin(rotationProj))
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    if (true) {
    	
    }
})
sprites.onDestroyed(SpriteKind.Enemy, function (sprite) {
    info.changeScoreBy(1)
    if (Math.percentChance(50)) {
        CreatePowerup(sprite)
    }
})
controller.left.onEvent(ControllerButtonEvent.Repeated, function () {
	
})
let projectile: Sprite = null
let rotationProj = 0
let isFiring = false
let mySprite: Sprite = null
let mySprite2: Sprite = null
let powerupList: Sprite[] = []
let player1: Sprite = null
let retationSpeed2 = 0
retationSpeed2 = 0.4
info.setScore(0)
player1 = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(player1)
tiles.setCurrentTilemap(tilemap`level1`)
scene.cameraFollowSprite(player1)
tiles.placeOnRandomTile(player1, sprites.dungeon.stairLarge)
let rateOfFire2 = 200
info.setLife(100)
let next_level = 5
powerupList = [sprites.create(assets.image`speedUp`, SpriteKind.Food), sprites.create(assets.image`rateOfFire`, SpriteKind.Food), sprites.create(assets.image`nuke`, SpriteKind.Food)]
forever(function () {
    if (isFiring) {
        rotationProj += retationSpeed2
        projectile = sprites.createProjectileFromSprite(img`
            2 2 2 2 
            2 2 2 2 
            2 2 2 2 
            2 2 2 2 
            `, player1, 75 * Math.cos(rotationProj), 75 * Math.sin(rotationProj))
    }
    pause(rateOfFire2)
})
game.onUpdateInterval(200, function () {
    mySprite = sprites.create(img`
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
        `, SpriteKind.Enemy)
})
