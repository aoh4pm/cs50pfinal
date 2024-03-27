import random


class Dice:
    @staticmethod
    def roll(amount, dice):
        count = 0
        sum_roll = 0
        highest = 0
        lowest = 20

        # Multiple Rolls
        while count < amount:
            count += 1
            true_roll = random.randint(1, dice)
            sum_roll += true_roll

            print(f"Roll {count}: {true_roll}")

            if true_roll > highest:
                highest = true_roll

            if true_roll < lowest:
                lowest = true_roll

        rolls = {
            "sum": sum_roll,
            "highest": highest,
            "lowest": lowest
        }

        return rolls
