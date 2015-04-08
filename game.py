import action
import random

class GameState:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.PlayerList = []
        self.Deck = []

    def requestBlocks(self, activePlayer, action):
        """ 
        Ask each player if they want to block active player's action.
        If someone wants to block, return the tuple (player, action). Else, return (None, None)
        """
        for player in self.PlayerList:
            if player == activePlayer: 
                continue
            
            blockingAction = player.confirmBlock(action)
            
            if blockingAction != None: 
                # check that the block is valid
                if not action in blockingAction.blocks:
                    continue       
            
                return player, blockingAction
            
        return None, None

    def requestCallForBluffs(self, activePlayer, action):
        """ 
        Ask each player if they want to call active player's (possible) bluff.
        If someone wants to call, return the player. Else, return None
        """
        for player in self.PlayerList:
            if player == activePlayer: continue
            if player.confirmCall(activePlayer, action): return player
        return None

    def AddToDeck(self, card):
        self.Deck.append(card)
    
    def DrawCard(self):
        if not len(self.Deck): return False
        
        card = random.choice(self.Deck)
        self.Deck.remove(card)
        return card
                
GameState = GameState()     # global variable
