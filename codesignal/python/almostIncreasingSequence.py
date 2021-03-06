#!/usr/local/bin/python3

#def almostIncreasingSequence(sequence):
    #f1 = sum([1 for a, b in zip(sequence[:-1], sequence[1:]) if a>=b ]) <= 1 
    #f2 = sum([1 for a, c in zip(sequence[:-2], sequence[2:]) if a>=c ]) <= 1
    #return f1 and f2

# s = [1, 2, 3, 4]

############################## GOOD STUFF
# x = sum([1 for a, b in [(1, 9), (1, 8)] if a>=b ])  <= 1  # I get what this does now!
                                                          # It simply sets x to True
                                                          # IF A is > B only 1 or less times for each
                                                          # number set iterated through the loop!
                                                          # It's just a fancy counter really.

#SO, THE ONLY NEXT THING TO DO IS, UNDERSTAND THE LOGIC BEHIND WHY WE ARE DOING THE ZIP
# STUFF THE WAY WE ARE DOING IT...
# zip(sequence[:-1], sequence[1:])


#So what does the raw data look like here?
#So f1 does this...
#print(s[:-1], s[1:])
# Removes the first element, and remove the last element..
# [1, 2, 3, 4, 5] [2, 3, 4, 5, 6] 

#And f2 does this...
#print(s[:-2], s[2:])
# Removes BOTH 1st and 2nd element, and removes the Next to last and last element..
# [1, 2, 3, 4] [3, 4, 5, 6]

# And then, we have 2 checks, to check each f1 and f2 , and we check the same condition!
# AND ONLY IF BOTH "and" IS TRUE, DO WE RETURN TRUE! ..MEANS ALMOST INCREASING SEQUENCE!

# s = [1, 2, 3, 4, 5, 6]

#def almostIncreasingSequence(sequence):
    #f1 = sum([1 for a, b in zip(sequence[:-1], sequence[1:]) if a>=b ]) <= 1 
    # [1, 2, 3, 4, 5] [2, 3, 4, 5, 6]  => SO THIS REPRESENTS OUR 1ST CHANCE!

    #f2 = sum([1 for a, c in zip(sequence[:-2], sequence[2:]) if a>=c ]) <= 1
    # [1, 2, 3, 4] [3, 4, 5, 6]        => AND THIS REPRESENTS OUR 2ND (AND LAST) CHANCE!

    #return f1 and f2

  
#[1, 2, 3, 4, 5] [2, 3, 4, 5, 6] -> THIS IS NOT FROM ZIP, JUST A STARTING POINT!

# [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)] -> LOOKS LIKE THIS FROM list of zip , zip changes everything!

#x = list(zip(s[:-1], s[1:]))
#x = sum([1 for a, b in zip(s[:-1], s[1:]) if a>=b ]) #<= 1 

############################### 

s = [1, 2, 3, 4, 5, 6]
# so this data below is what the data that comes from zip looks like...
# SO NOW, WE UNDERSTAND WHAT ZIP IS DOING FOR US! IT GIVES US AN A/ B PAIR FOR EACH ITERATION 
# OF THE LOOP THAT WE CAN COMPARE a>=b !
# NEXT WE NEED TO UNDERSTAND WHAT THE DIFF BETWEEN f1 AND f2 ARE! THAT'S THE LAST STEP!

#F1
print("f1 data before zip...")
print(s[:-1], s[1:]) 
x = list(zip(s[:-1], s[1:]))
print("f1 data...")
print(x)
# f1 .. [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)] -> ZIP CHANGES EVERYTHING!
f1 = sum([1 for a, b in [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)] if a>=b ]) #<= 1
print(f1)

#F2
print("f2 data before zip...")
print(s[:-2], s[2:])
x = list(zip(s[:-2], s[2:]))
print("f2 data...")
print(x)
# f2 .. [(1, 3), (2, 4), (3, 5), (4, 6)] -> ZIP CHANGES EVERYTHING!
f2 = sum([1 for a, b in [(7, 3), (9, 4), (9, 5), (9, 6)] if a>=b ]) #<= 1
print(f2)

# SCRATCH
#[1, 2, 3, 4, 5] # This is what the ZIP does, it PAIRS the offsetted lists up so we can compare a>=b
#[2, 3, 4, 5, 6] # But how does this help us? Why are we doing it? Why does it work? 
                # Should be simple, but I am STUMPED! THINK WITH A FRESH BRAIN!
                # IT'S PROB THE SAME DAMN THING AS MY FOR LOOP, THINK ABOUT THAT, IT'S A SIMPLE
                # OFFSET, AND IT PROB ACCOMPLISHES SAME THING AS JUST LOOKING BACK -1 ELEMENT
                # IN A LIST IN A FOR LOOP TO SEE IF A>B, I BET THAT'S ALL THIS IS, SIMPLE! YEP, THAT'S
                # IT! AND IF YOU HIT THE CONDITION 1 TIME OR LESS, YOUR SUM DOES NOT GO TO "1", WHICH
                # MEANS F1 CAN NOT BE MET, WHICH MEANS YOUR FINAL "F1 AND F2" CONDITION CAN NOT BE MET!
                # THAT'S WHAT'S GOING ON HERE!

# ORIGINAL DATA
# [1, 2, 3, 4, 5, 6]

# F1 BEFORE ZIP: [1, 2, 3, 4, 5] [2, 3, 4, 5, 6]
# F1 AFTER ZIP:  [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]

# F2 BEFORE ZIP: [1, 2, 3, 4] [3, 4, 5, 6]
# F2 AFTER ZIP:  [(1, 3), (2, 4), (3, 5), (4, 6)]

# SO FIRST COMPARISIONS LOOK LIKE THIS: *Asks, Is the number 1 ahead of me greater than me?
#[1, 2, 3, 4, 5]  
#[2, 3, 4, 5, 6]

# SECOND COMPARISONS LOOK LIKE THIS:    *Asks, is the number 2 ahead of me greater than me?
#[1, 2, 3, 4] 
#[3, 4, 5, 6]




