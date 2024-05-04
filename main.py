from functions.ballRollChallenge import ballRollChallenge
from functions.testIfOutputIsProper import testIfOutputIsProper

if __name__ == '__main__':
    testInputValues = [
        [(1, 6), (-1, 2), (1, 4), (1, 2), (-1, 0), (-1, 3), (1, 10)],
        [(-1, 6), (-1, 2), (1, 7), (1, 8), (-1, 2), (-1, 9), (1, 10)],
        [(-1, 6), (1, 2), (-1, 1), (1, 8), (1, 8)],
        [(1, 5), (1, 2), (-1, 5), (1, 1)]
    ]

    testTrueOutputValues = [
        [0, 2, 6],
        [0, 1, 5, 6],
        [0, 1, 3, 4],
        [None, 3]  # None stands for any index (should be one of two indexes, but I simplified it)
    ]

    for idx, (inputIt, trueOutputIt) in enumerate(zip(testInputValues, testTrueOutputValues)):
        outOfChallenge = ballRollChallenge(inputIt, verbose=False)
        print(f"{idx}) {outOfChallenge}")
        outTest = testIfOutputIsProper(outOfChallenge, trueOutputIt)
        print(f'is proper: {"True" if outTest else "False"}')

        if idx != (len(testInputValues) - 1):
            print("-------------")

    print("--END OF SCRIPT--")
