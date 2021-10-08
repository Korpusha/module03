"""Constants and Help"""

ENEMY_LIVES = ENEMY_LEVEL = 1
ALLOWED_MOVES = range(1, 4)
PLAYER_LIVES = 5
SCORE = 0
TOP = 10


class Help:
    def __init__(self):
        print("""

        +========================+
        |  help commands:        |
        |    Help.description()  |
        |    Help.rules()        |
        |    Help.warriors()     |
        |    Help.enemy()        |
        |    Help.full()         |
        +========================+

        """)

    @staticmethod
    def rules():
        print(""" 

         +==========+           
         |  *Rules  |     Where: -> - kills
         |  ------  |            W - Wizard
         |  W -> K  |            K - Knight
         |  K -> R  |            R - Robber
         |  R -> W  |
         +==========+

        """)

    @staticmethod
    def warriors():
        print(""" 

        +==========================+
        | Warriors to choose from: |
        |        Wizard - 1        |
        |        Knight - 2        |
        |        Robber - 3        |
        +==========================+

        """)

    @staticmethod
    def description():
        print("""

         +================================================================================+
         |   This is the game that brought its concept from another popular               |
         |   game Rock-Paper-Scissors.                                                    |
         |                                                                                |
         |   But main choices were changed on different 3 warriors (type Help.warriors()) |
         |   and steps were changed.                                                      |
         |                                                                                |
         |   There has appeared steps like attack and defence, where player               |
         |   fights with bot using different warriors (type Help.rules()).                |
         |                                                                                |
         |   The game has got no end, as new enemies will appear (type Help.enemy()).     |
         |                                                                                |
         |   Get your dexterous fingers and beat as much bots as you can!                 |
         +================================================================================+ 

        """)

    @staticmethod
    def enemy():
        print("""

         +============================================================================+
         |   Your enemy is bot.                                                       |
         |   His choice of warriors is random (type Help.warriors, Help.rules).       |
         |   When he dies - appears new enemy but his level and HP is greater by one. |
         |   So this game is infinite till you lose.                                  |
         +============================================================================+

        """)

    @staticmethod
    def full():
        Help.rules()
        Help.enemy()
        Help.description()
        Help.warriors()


while True:
    user = input('Print \'start\' to begin. Use Help() for more info: ')
    if user == 'Help()':
        Help()
    if user == 'Help.description()':
        Help.description()
    if user == 'Help.rules()':
        Help.rules()
    if user == 'Help.warriors()':
        Help.warriors()
    if user == 'Help.enemy()':
        Help.enemy()
    if user == 'Help.full()':
        Help.full()
    if user.lower() == 'start':
        print()
        break
