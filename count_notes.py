# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.
amount = int (input("Enter the amount"))
# 2) Find how many 100-rupee notes are needed:
#    Divide `Amount` by 100 (whole number division) and store it in `note_1`.
note_1 = amount // 100  # for 150 amount note_1 that is for 100 dollars
# 3) Find the remaining amount after taking out 100-rupee notes:
#    Use the remainder of `Amount` after dividing by 100.
amount = amount%100
# 4) From the remaining amount, find how many 50-rupee notes are needed:
#    Divide the remainder by 50 (whole number division) and store it in `note_2`.
note_2 = amount // 50
# 5) Find the remaining amount after taking out 50-rupee notes:
#    Use the remainder after dividing by 50.
amount = amount%50
# 6) From the remaining amount, find how many 10-rupee notes are needed:
#    Divide the remainder by 10 (whole number division) and store it in `note_3`.
note_3 = amount // 10
# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.
print("Note 100",note_1)

print("Note 50",note_2)

print("Note 10",note_3)