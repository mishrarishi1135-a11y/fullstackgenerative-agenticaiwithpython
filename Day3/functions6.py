# handle multiple return in python
def make_chai():
    return "Here is your masala chai"

print(make_chai())

return_value = make_chai()

print(return_value)    # both result is completely same but return_value is much easier.


def make_chai():
    print("Here is your masala chai")   # this provide the none.

return_value = make_chai()

print(return_value)
# nothing -> implicitly return none

def idle_chaiwala():
    pass

print(idle_chaiwala())   # this also give none.
# that means when you give nothing then it prints none.

def sold_cups():
    return 120

total = sold_cups()
print(total)   #It print 120, here we see about the one value.

def chai_status(cups_left):
    if cups_left == 0:
        return"sorry, chai over"   # once the function hits returns no matter what happens and other code will not executed.
    return"chai is ready"
print("chai")   # that is early from a function
print(chai_status(0))
print(chai_status(5))

# now we talk about returning multiple value.

def chai_report():
    return 100, 20  #sold, remaining

sold, remaining = chai_report()
print("sold:", sold)
print("Remaining:", remaining)     # here, it return multiple value.


# if you give three values in return like 100, 20, 10  for sold, remaining then it show error but
# write this "sold, remaining, _ = chai_report" then it will not show any error