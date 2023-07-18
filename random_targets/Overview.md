## Overview
Magic the Gathering is a state based card game. Cards are played in various zones with different effects to the game state. Some cards become permanent features in the game zones while others have affects on cards in zones or player's hands.

Cards often require a declaration of *target(s)* in order to be played. Some cards have an additional requirement that the *target(s)* are randomly selected.

## Motivation
This document is a description of a method for selecting randomized targets with the resources available to the players.

My beloved play group has an abundant supply of 6-sided die. We utilize this resource to make a random selection from a set containing multiple valid targets.

## Method
The following steps complete the selection:

- Let $n$ be the number of valid targets
- Let $d_i$ be the value of pips rolled on the $i$th die

1. Assign each of the *targets* a unique value $v \in \{0,1,\cdots,n-1\}$
2. Roll $n$ 6-sided dice
3. Select the *target* that corresponds to the assigned value, $v$, such that:
	
$$ v = (\sum_{i=1}^{n}d_i)\mod n $$

## Justification
This section will attempt to show that each value $v$ has nearly equal probability of occurring. 

### mod
We use **mod** to create $v$ *bins*; we will expect there to be a unique *bin* for each valid target.

Simply stated, this function returns the value of the remainder for integer division.

if $$ a = kb | k \in Z^* $$ then:
$$ a \mod b = 0 $$

For example:
- Let $ a = 7 $
- Let $ b = 5 $

$$ a \mod b \implies 7 \mod 5 = 2 $$ 

### probability
The number of occurrences of a particular dice roll is given by the multinomial theorem.

$$ \binom{n}{k_1,k_2,\cdots,k_m} = \dfrac{n!}{k_1!k_2!\cdots k_m!} $$

Where $k_i$ is the number of occurrences of dice showing $i$ pips. Here, using 6-sided dice for example, $k_m$ would be the number of dice that rolled 6. $n$ is the total number of dice rolled.

The probability of a particular sum of pips is the product of its combinations and occurrences over all possible combinations.

