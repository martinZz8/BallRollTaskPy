from typing import List, Tuple
import random


def ballRollChallenge(inputBalls: List[Tuple[int, int]],
                      verbose: bool = True) -> List[int]:
    """Challenges the input list of balls.

    Method compares balls in the list. Balls are challenged when left ball has direction of 1 (right)
    and right ball -1 (left). Only in that case ball with hit each other.
    Every ball has its weight (from 0 to 10). Ball with higher weight wins.
    In case balls have same weights, there is randomly chosed ball, that wins.

    Args:
    inputBalls: List of tuples, where one tuple means one ball.
        Tuple consists of direction (-1 - left or 1 - right) and weight (int from 0 to 10).
        Both values are integers.
    verbose: Boolean value whether logs should be printed. Default value is "True"

    Returns:
    A list of indexes from origin list. It says whose indexes won the challenge.
    """
    idxsOfOneElem = []
    destroyedIdxs = []

    for i in range(len(inputBalls)):
        if inputBalls[i][0] == 1:
            idxsOfOneElem.append(i)
        elif inputBalls[i][0] == -1:
            rightWeight = inputBalls[i][1]  # Weight of element with direction -1

            # Check for weights of current element and every element from list
            liToRemoveFromIdxsOfOneElem = []
            for j in range(len(idxsOfOneElem) - 1, -1, -1):  # Or instead use: a = len(idxsOfOneElem); a.reverse()
                leftWeight = inputBalls[idxsOfOneElem[j]][1]  # Weight of element with direction 1

                # Mark right element to destroy (and break the input loop)
                if leftWeight > rightWeight:
                    doWeDeleteLeftItem = False
                # Mark left element to destroy (remove from 'idxsOfOneElem' and append to list 'destroyedIdxs')
                elif leftWeight < rightWeight:
                    doWeDeleteLeftItem = True
                else:  # leftWeight == rightWeight (mark random random element to destroy)
                    doWeDeleteLeftItem = random.randint(0, 1) == 0

                # Perform destroy of proper element
                if doWeDeleteLeftItem:
                    liToRemoveFromIdxsOfOneElem.append(j)
                    destroyedIdxs.append(idxsOfOneElem[j])
                else:
                    destroyedIdxs.append(i)
                    break

            # Make sure, that elements are sorted in descending order (redundant)
            # liToRemoveFromIdxsOfOneElem.sort(reverse=True)

            # Remove elements from 'idxsOfOneElem' list
            for idxToRemove in liToRemoveFromIdxsOfOneElem:
                del idxsOfOneElem[idxToRemove]

    # Create list to return
    if verbose:
        print(f"Destroy idxs are: {destroyedIdxs}")
    liToRet = []

    for i in range(len(inputBalls)):
        if i not in destroyedIdxs:
            liToRet.append(i)

    return liToRet
