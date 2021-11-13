# declares a variable named "log_file" and assigns to it the data from "um-server-01.txt" by opening that file
log_file = open("um-server-01.txt")

# defines a function named "sales_reports" that takes in one argument called "log_file" 
def sales_reports(log_file):
    # begins a for-loop that interates through each row in "log_file" passed to the function and declares each row as "line"
    for line in log_file:
        # removes any trailing white space from line and reassigns the altered string to "line"
        line = line.rstrip()
        # declares the variable "day" and assigns to it the slice of "line" from the 0th to 3rd index
        day = line[0:3]
        # checks if the value of "day" is equivalent to the string "Mon" with a conditional statement
        if day == "Mon":
            # if the conditional statement returns True, this prints the row that is assigned to "line" in the current iteration
            print(line)

# calls the function "sales_reports", passing into it the variable "log_file"
sales_reports(log_file)

log_file.seek(0)

def lotsa_melons(log_file):
    for line in log_file:
        line_list = line.split(' ')
        if float(line_list[2]) > 10:
            print(line)

lotsa_melons(log_file)

