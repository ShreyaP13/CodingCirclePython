birth_year = raw_input("What is the birth year for the milestones?")
# raw_input always gives strings, so convert to int
birth_year = int(birth_year)

# Calculate milestone years
driving_year = birth_year + 16
drinking_year = birth_year + 21
president_year = birth_year + 35

print "You are able to drive in " + driving_year
print "You are able to drink in " + drinking_year
print "You are able to run for president in " + president_year