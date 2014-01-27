import random

# Load the hat file into a memory
f = open("hat.txt", "r")
lines = f.readlines()
f.close()

# Extract the different pieces of information from the file
empty_seats = int(lines[0])
groups = []
for group_line in lines[1:]:
  if group_line.strip() == "":  # Divider between two groups, add new group on
    groups += [[]]
  else:
    groups[-1] += [group_line.strip()]

# Until there are no empty seats or no groups left, select a group at random
# and add it to the list of successful groups
# Keep track of how many tries this took in case we fail to find a solution
successful_groups = []
tries = 0
while empty_seats > 0 and len(groups) > 0 and tries < 10000:
  tries += 1

  # Generate a random number indicating which group to select
  selected_group_number = random.randrange(0, len(groups))
  
  # If this group is small enough to fit in the remaining empty seats, include
  # it; otherwise, select another group
  if len(groups[selected_group_number]) <= empty_seats:
    # Add that group to the list of successful groups
    successful_groups += [groups[selected_group_number]]

    # Decrease the number of empty seats by the required amount
    empty_seats -= len(groups[selected_group_number])

    # Remove the group from the hat
    groups.remove(groups[selected_group_number])
    
# Now output a list of the results
f = open("results.txt", "w")
f.write("SUCCESSFUL GROUPS:\n\n")
for successful_group in successful_groups:
  f.write("\n".join(successful_group))
  f.write("\n\n")
f.write(str(empty_seats) + " EMPTY SEAT" + ("" if empty_seats == 1 else "S"))
f.close()
