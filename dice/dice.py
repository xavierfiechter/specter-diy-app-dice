from app import BaseApp 
from gui.screens import Menu
from .screen import DiceRollScreen
from .utils import roll_dice



DICE_ROLL_DEFAULT = 6 #TODO: get default dice from config
DICE_ROLL_D3 = 3
DICE_ROLL_D4 = 4
DICE_ROLL_D6 = 6
DICE_ROLL_D8 = 8
DICE_ROLL_D10 = 10
DICE_ROLL_D12 = 12
DICE_ROLL_D20 = 20
DICE_ROLL_D100 = 100


class DiceApp(BaseApp):
    """ """
    prefixes = [b"dice"]
    button = "Dice Roller" # this lists "Dice Roller" as app in Applications

    async def menu(self, show_screen):
        buttons = [
            (None, "Dice Roller"),
            (DICE_ROLL_DEFAULT, "Roll default (d6) dice"),
            (DICE_ROLL_D3, "Roll d3 dice"),
            (DICE_ROLL_D4, "Roll d4 dice"),
            (DICE_ROLL_D6, "Roll d6 dice"),
            (DICE_ROLL_D8, "Roll d8 dice"),
            (DICE_ROLL_D10, "Roll d10 dice"),
            (DICE_ROLL_D12, "Roll d12 dice"),
            (DICE_ROLL_D20, "Roll d20 dice"),
        ]
        menuitem = await show_screen(Menu(buttons, title="Which dice do you want to roll?", last=(255, None)))
        while menuitem != 255:
            if menuitem in [DICE_ROLL_DEFAULT,
                            DICE_ROLL_D3,
                            DICE_ROLL_D4,
                            DICE_ROLL_D6,
                            DICE_ROLL_D8,
                            DICE_ROLL_D10,
                            DICE_ROLL_D12,
                            DICE_ROLL_D20,
                            DICE_ROLL_D100]:
                roll = True
                while roll:
                    scr = DiceRollScreen(
                            title="Rolled dice ",
                            note="Choosen dice: d%s" % menuitem,
                            message ="%s" % roll_dice(menuitem),
                    )
                    roll = await show_screen(scr)
                menuitem = await show_screen(Menu(buttons, last=(255, None)))
            
