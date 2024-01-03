# I created the variable lr to store the value of the largest row. In this instance - that is 5.
# This variable represents tha maximum amount of '*' I will use in my pattern.
lr = 5

# The first for loop is for the top half of the pattern. As the increments are easy to manage in one way first i.e and then down.
# The first loop will increment the star pattern up to the 5th star.


# I created a variable called i to represent each increment passed.
# I used the range function to start the pattern at index 1 and end the pattern at the value of index (lr + 1) as the last index is skipped and 0 is not the start - 1 is. Therefore, 5 '*' and not 6 will be printed.
# By using algebra (adding a numerical and the lr variable) I am able to alter the pattern without scripting a new pattern. 
# I created the pattern in 2 parts (the top & the bottom).
for i in range(1, lr + 1):

    # I created a nested for loop with the variable called p - for pattern - to highlight the patterns for loop.
    # I used the range (i) - which will prompt the for p loop to print a maximum of 5 '*'.
    for p in range(i):

        # I used the print() function to start the string with "*" and instead of printing on a new line - I used the end= variable with "" to pass an empty string
        print("*", end="")

    # I created a variable called s - for spaces - to highlight the spaces for loop.
    # I set the end of the spaces to be 2 times the length of largest star pattern row to format the pattern.
    for s in range(2 * (lr - i)):
        print(" ", end="")
    # I used the print() function with an empty string to format the pattern with the bottom half of the pattern.
    print()

# The for loop below is the second half of the pattern.

# This for loop begins after the previous for loop. The value of i now starts at 4 - therefore printing 4 '*'.
for i in range(4, 0, -1):
    # Following the range value of i - this nested loop will print "*"s and end the string with a space.
    for p in range(i):
        print("*", end="")
    # The spaces used as 2 times the value of the maximum length of "*" in a row.
    for s in range(2 * (lr - i)):
        print(" ", end="")
    # I ended the for loop with an empty print() function to format the pattern.
    print()