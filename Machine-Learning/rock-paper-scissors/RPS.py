# This example uses basic markov chains to win
# Note that playing 1000 games against abbey is not sufficient to win
# A total of 2000 games had to be played before we can win
import random
from collections import defaultdict

winning_moves = {
    'R': 'P',
    'P': 'S',
    'S': 'R'
}

available_moves = ['R', 'P', 'S']
opponent_history = []
chain = defaultdict(int)
mlen = 7

def player(prev_play):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Pick randomly until sufficient data
    if (len(opponent_history) < mlen):
        return random.choice(available_moves)

    # Use abbey solution as an inspiration
    last_five = "".join(opponent_history[-mlen:])
    chain[last_five] += 1

    # Enumerate over the last 4 + potential current plays
    # Track the one with the highest probability of winning
    prev_opponent_plays = last_five[1:]
    potential_plays = [
        prev_opponent_plays + move for move in available_moves
    ]

    maximum = 0
    move_idx = 0
    for i, play in enumerate(potential_plays):
        if chain[play] > maximum:
            maximum = chain[play]
            move_idx = i

    return winning_moves[available_moves[move_idx]]