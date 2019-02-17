#!/usr/bin/env checkio --domain=py run pawn-brotherhood

# https://py.checkio.org/mission/pawn-brotherhood/

# 
# END_DESC

def safe_pawns(pawns):
    num_pawns = set()
    for el in pawns:
        row = int(el[1])
        col = ord(el[0])
        num_pawns.add((row, col))

    count = 0
    for row, col in num_pawns:
        if (row -1 , col + 1) in num_pawns or (row - 1, col - 1) in num_pawns:
            count += 1

    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")