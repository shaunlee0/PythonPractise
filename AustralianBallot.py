from random import randint
__author__ = 'shaun'
def main():
    numberOfCandidates = input ("Number of Candidates? ")
    numberOfCandidates = int(numberOfCandidates)
    candidates = []

    for i in range(0, int(numberOfCandidates)):
        candidates.append(input("Enter the name for candidate "+ str(i) +" "))

    for x in range (0,len(candidates)):
        print("The name of candidate " + str(x) + " is " + candidates[x])

    canidate0Votes = 0
    canidate1Votes = 0
    canidate2Votes = 0

    voter1 = []
    voter2 = []
    voter3 = []
    voter4 = []
    voter5 = []

    for i in range (0,3):
        voter1.append(randint(1,3))
        voter2.append(randint(1,3))
        voter3.append(randint(1,3))
        voter4.append(randint(1,3))
        voter5.append(randint(1,3))

    printVoter(voter1)
    defineVotes(voter1)

def printVoter(votes):
    strVotes = ""
    for x in votes:
        strVotes += " " + str(x)

    print(strVotes)

def defineVotes(votes):
    candidate = 0
    can1 = 0
    can2 = 0
    can3 = 0

    if(votes[0] == 1):
        can1 +=1
    if(votes[1] == 1):
        can2 +=1
    if(votes[2] == 1):
        can3 +=1
    if(can1>can2 & can3):
        print("Candidate 1 won")
    if(can2>can1 & can3):
        print("Candidate 2 won")
    if(can3>can2 & can1):
        print("Candidate 3 won")


if __name__ == "__main__":
    main()
