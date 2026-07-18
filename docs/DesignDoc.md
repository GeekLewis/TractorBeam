*Tractor Beam Design Document V 1.0*

# Lore and theme Sketch

The goal of *Tractor Beam* is to defend the mother ship as it follows you though the space between gates. You do this with an array of weapons but most importantly with your tractor beam. 

The beam is what makes the gameplay of *Tractor Beam* different from other bullet hell shooters. It can be used to move objects, including enemies around. It is also used to harvest powerups and repair items from destroyed enemies to fix the mother ship. 

# Visual Layout and control Scheme.

*Tractor Beam* has two main zones. 

- The forward flight zone. (FFZ) This is the main area where the Player’s ship will maneuver and where enemies will appear. This takes up about ¾ of the screen’s upper half.   
- The Mothership (MS). This is at the bottom of the screen and is laid out in cubes of different colored modules. These modules. 

## Player Ship

- **Theme**
    - *Tractor Beam* has a small fighter sized ship as its main player character. This ship should be small to show scale but detailed enough to see upgrades as they are attached.   
- **Movement**
    - The ship moves on screen in a constant upward direction relative to the background. In a similar way to [**Raptor**](https://www.youtube.com/watch?v=taa6RzhoQGw)   
    - The ship is moved with the left analog stick.
    - Pressing down on the left stick will use a turbo boost feature allowing you to move quickly When the speed boost is used, the outermost shield (see shields below) is disabled.
    - The ship can move anywhere on screen including over the mother ship at the bottom of the screen.  
- **Weapons**
    - Weapons are fired by pressing the left trigger.
    - Left bumper activates special one time use power up weapons.
    - The ship fires weapons towards the top of the screen in various patterns based on upgrades.
        - To start we should copy the upgrade systems in raptor or a similar game. But there are 4 main types of weapons.
            - Forward direction guns
            - Directional guns that shoot out one side or the back of the ship.
            - Coaxil weapons (always on, does not damage modules or the mother ship) follow the sweep of the tractor beam.
            - Missiles that have various degrees and ranges of seeking.
        - There are also single use weapons that destroy or damage enemys in large areas of the screen. These are more “death blossom” than bomb  
- **Shields**
    - The ship has a forward facing shield that is displayed as layers of translucent arch ahead of the ship.
    - Each shield can take a single or multiple hits from enemy fire. We should gauge the number of hits by player enjoyment. Initially I want to make the ship somewhat durable to make using the tractor beam easier.
- **Tractor Beam**
    - The tractor beam is controlled by the left analog Stick. It selects targets to grab in a discrete way locking on from one to the other by moving the stick around.
    - The left trigger engages the beam; this is a switch. One pull grabs an object the next one lets it go.
    - The beam can grab any of the following
        - Power ups
        - Smaller enemy ships
        - Modules (these are the remains of the enemy ships used to repair the mother ship)
    - Once grabbed, the beam can be used to position items in a smooth way and allow them to encounter various parts of the mother ship either as repair items, upgrade or by putting enemy ships into the path of various defenses.
    - Once grabbed, enemy ships can also be made to crash into other enemy ships. This should be more of a fun add on then a general tactic.
    - Enemy ships grabbed by the tractor beam resist movement and make the beam move slower. 

## The Mothership

- **Theme**
    - The Mothership is a collection of modules laid out in a grid. These are color coded and have themes. Think Galaxy trucker.
- **Game mechanics**
    - The shield wall. At the start of a level, at the top of the mothership portion of the screen there is a shield wall. As enemy ships make it past the player’s ship they weaken the shield wall.
    - Modules
        - Habitation (Green)
            - These are the main parts of the ship that have to be defended and repaired. If you lose too much green this is a lost game state.
        - Armor (red) these are parts of the ship that can be lost and which protect other parts they take more shots from enemy ships/asteroids to damage.
        - Shield arrays
        - Defense weapons.
        - Power transmitters: these are turrets that power the player ship’s shield when they are in range.
    - Modules can be 1-4 squares tetris style. Adding one anywhere will always allow it to function but concentrating them or arranging them in certain ways will improve their function. In addition any shape can go anywhere in the grid. Modules will not override existing modules but if there is not enough space to place them, the extra squares will be lost so better fitting into slots gives more modules.
- Damage to the mother ship.
    - Generally projectiles that can damage the mother ship should be rare and reserved for harder enemies;
    - most enemy ships need to pass the leading shieldwall in order for their weapons to have an effect on the modules.
    - When an enemy ship penetrates the shield wall, they will do an “attack run”
        - The size of the ship is expressed as the number of modules wide. As the ship flies over the mothership it will deal a set number of damage destroying modules at random as it flies over.
        *For example a weak enemy might deal 2 damage as it flys over. A path that is 2 modules wide and 20 (or the whole ship) deep.*
        - Color coded ships will target various colors of modules. For example a red ship getting past the Shield wall will target red modules in its path. Greens will target greens and so forth.
        - Color coded enemies will also drop the corresponding modules. 
- Repairing and upgrading the mothership.
    - The mothership starts with randomly placed crew modules and enough power modules to power them. They also start with shield generators.
    - Placing a module in a grid location on the mother ship repairs those locations.
    - Creating various shapes/clusters of module types will start a chain of built upgrades that help protect the ship from incoming fire and enemy ships. Module types are as follows
        - Superstructure
            - Modules of any color can be used to repair superstructure damage. 
        - Crew compartments: the more crew space the more possibility of saving the colonists. These must be repaired when damage or a fail state will result. Upgrades increase the armor of these locations.
            - Upgraded crew compartments have more armor.
        - Reactors: reactors power whatever is in immediate contact with them. Reactors will power various adjacent colors in the following priority. Crew>sheilds>weapons
            - Upgraded reactors produce more power and are able to power other module clusters more fully.
        - Weapons these are turrets that defend the mother ship and assist in defeating enemy waves
            - Upgraded weapons do more damage and fire more projectiles.
        - Shields reinforce the lead shield wall
            - Upgraded shields heal the shield wall faster and make a beam that heals player ship shields when they are within range. 

## Level progression.

Each level is fought as a trip between 2 ancient alien stargates. Getting to then ending gate ends the level and your score is based on some math about how many modules where upgraded or survived. 
