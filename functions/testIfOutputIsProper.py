from typing import List


def testIfOutputIsProper(outputIndexes: List[int],
                         trueOutputIndexes: List[int]) -> bool:
    # Check if two lists have same lengths
    if len(outputIndexes) != len(trueOutputIndexes):
        print("Note: Output and trueOutput lists have different number of elements!")
        return False

    for i in range(len(trueOutputIndexes)):
        if trueOutputIndexes[i] is not None:  # For 'None', any index of two indexes is proper
            if outputIndexes[i] != trueOutputIndexes[i]:
                return False

    return True
