import pandas as pd
import random
class SnakeRoll:
    def __init__(self,players,dice):
        self.players = players
        self.target = dice**2
        self.dice_roll_history = {f"player_{i}":[] for i in range(1,players+1)}
        self.position_history = {f"player_{i}":[] for i in range(1,players+1)}
        self.current_position = {f"player_{i}":0 for i in range(1,players+1)}
        self.winner = None

    def diceRollResult(self):
        while True:
            if self.winner is not None:
                break
            for i in range(1,self.players+1):
                roll = random.randint(1,6)
                new_position = self.current_position[f'player_{i}']+roll
                self.dice_roll_history[f'player_{i}'].append(roll)
                if new_position==self.target:
                    self.current_position[f'player_{i}']=new_position
                    self.winner=f'player_{i}'
                    self.position_history[f'player_{i}'].append(new_position)
                    print("positon_history==",self.position_history)
                    print("diceroll_history==",self.dice_roll_history)
                    print("Winner==",self.winner)
                    
                elif new_position>self.target:
                    self.position_history[f'player_{i}'].append(self.current_position[f'player_{i}'])
                else:
                    self.position_history[f'player_{i}'].append(new_position)
                    self.current_position[f'player_{i}']=new_position

    def get_print_result_to_pdf(self):
        data = {
            "players":[i for i in self.position_history.keys()],
            "winner":[0 if i != self.winner else 1 for  i in self.position_history.keys()],
            "position_history":[(",".join([str(i) for i in history])) for history in self.position_history.values()],
            "dice_history":[(",".join([str(i) for i in roll])) for roll in self.dice_roll_history.values()],

        }
        dataframe = pd.DataFrame(data)
        dataframe.to_csv("playing_record1.csv")
        

if __name__=="__main__":
    game = SnakeRoll(2,4)
    game.diceRollResult()
    game.get_print_result_to_pdf()