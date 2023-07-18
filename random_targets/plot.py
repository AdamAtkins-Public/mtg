import matplotlib.pyplot as plt
import argparse

#bar plot (names,values) names = range(num_dice) values = sum(dice_roll_combination)
#bar plot (names,values) names = range(num_dice-1) values = sum(dice_roll_combination) % num_dice

def plot_dice_combinations(number_of_dice,max_die_value):
    """generates bar plots for number of dice with max die value sides

    assumes: min die value is 1

    dice_roll_sum: dict(key: dice roll pip sum, value: number of occurrences)
    dice_roll_mod: dict(key: dice roll pip sum % number of dice, value: number of occurrences)

    plot1: number of occurrences by sum of dice roll
    plot2: number of occurrences by sum of dice roll mod number of dice
    """
    dice_roll_sum = dict()
    dice_roll_mod = dict()

    for i in range(number_of_dice,number_of_dice*max_die_value+1):
        dice_roll_sum[i] = 0
    for i in range(number_of_dice):
        dice_roll_mod[i] = 0

    factorials = factorial_dict(max_die_value 
                                if max_die_value > number_of_dice
                                else number_of_dice)

    multinomial_numerator = factorials[number_of_dice]

    combination = [1]*number_of_dice
   
    while not len(combination) == 0:
        occurrences = multinomial_numerator // multinomial_denom(combination,max_die_value,factorials)
        dice_roll_sum[sum(combination)] += occurrences
        dice_roll_mod[sum(combination)%(number_of_dice)] += occurrences
        next_combination_of_dice(combination,max_die_value)

    #plots; dicts are iterated by insertion order, keys are inserted in ascending order
    plt.suptitle('Rolling ' + number_of_dice.__str__() + ' dice')
    plt.subplot(121)
    plt.ylabel('occurrences')
    plt.xlabel('sum of pips')
    plt.bar(dice_roll_sum.keys(),dice_roll_sum.values())
    plt.subplot(122)
    plt.ylabel('occurrences')
    plt.xlabel('sum of pips mod number of dice')
    plt.bar(dice_roll_mod.keys(),dice_roll_mod.values())
    plt.show()


def next_combination_of_dice(combination,max_die_value):
    """returns the next combination of dice values according to invariant

    This function is used to enumerate all possible dice combinations.

    invariant: '<=' ordering

    combination: list of integers; integer representation of pips on die

    returns empty list when combinations have been exhausted
    """
    number_of_dice = len(combination)

    while True:
        die = combination.pop()
        die += 1
        if die > max_die_value:
            if len(combination) > 0: continue
            else: break
        else:
            while len(combination) < number_of_dice:
                combination.append(die)
            break
    return combination

def factorial_dict(max_die_value):
    """returns dictionary containing factorials up to max_die_value

    key: n
    value: n!
    """
    factorials = dict([(0,1)])
    for n in range(1,max_die_value+1):
        factorials[n] = n*factorials[n-1]
    return factorials

def multinomial_denom(dice_roll,max_die_value,factorials):
    """returns integer denominator to be used with multinomial theorem

    dice_roll: list of integers representing dice roll
    max_die_value: integer representing number of die sides
    factorials: dict(key: n, value: n!)
    """
    denominator = int(1)
    for die in range(1,max_die_value+1):
        denominator *= factorials[dice_roll.count(die)]
    return int(denominator)

if __name__ == "__main__":
    ##test next_combination_of_dice
    #max_die_value = 6
    #combination = [1,1]
    #i = int(0)
    #while not len(combination) == 0:
    #    i += 1
    #    print(combination.__str__() + " " + i.__str__())
    #    next_combination_of_dice(combination,max_die_value)

    ##test factorials_dict
    #max_die_value = 6
    #factorials = factorial_dict(max_die_value)
    #for n in range(max_die_value+1):
    #    print(n.__str__() + " " + factorials[n].__str__())

    parser = argparse.ArgumentParser(description='Generates a bar plots of distribution of sums and mod values for n k-sided dice')
    parser.add_argument('n',type=int,nargs='?',default=2,
                        help='number of dice to be rolled')
    parser.add_argument('k',type=int,nargs='?',default=6,
                        help='max value on dice (assuming min value is 1)')

    args = parser.parse_args()
    plot_dice_combinations(args.n,args.k)
