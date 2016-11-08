#sets the variable x to have an array of 4,6,1,3,5
x =[4,6,1,3,5]
#defines the function(draw_stars1) and calls this_list
def draw_stars1(this_list):
    #for the numbes in this_list
    #output a blank function ('')
    for num in this_list:
        output = ''
        #for i in range (num)
        for i in range(num):
            #output *
            output += '*'
            print output



#set variable x to 4, tom,1, michael, 5,7, jimmy smith
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
#def defines the function, def defines draw_stars in this case
def draw_stars(list_items):
    #for the items in list_items
    for item in list_items:
        output = ''
        if type(item) is int:
            #for variables in the range output *
            for i in range(item):
                output += '*'
    # otherwise type the items as a string
    elif type(item) is str:
        #first_letter sets the output to print the first letters of the names only and to lower case with .lower
        first_letter = item[0].lower()
        for i in range (len(item)):
            output += first_letter
        print output
