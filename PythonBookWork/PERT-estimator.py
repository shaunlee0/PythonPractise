print("Welcome to the PERT estimation script\n=====================================")
optimal = int(input("Please enter the optimistic estimation in man days for your task...\n> "))
nominal = int(input("Please enter the nominal estimation in man days for your task...\n> "))
pessimistic = int(input("Please enter the pessimistic estimation in man days for your task...\n> "))

# Duration of task estimate
probabilityDistribution = ((optimal + (4 * nominal) + pessimistic) / 6)

# The deviation of this estimate
standardDeviation = ((pessimistic - optimal) / 6)

print("\nProbability distribution\t: " + str(probabilityDistribution))
print("Standard deviation\t\t\t: " + str(standardDeviation))
