def outer_function(func):
    def inner_function():
        print("This will always be run before!!")
        func()
    return inner_function

@outer_function
def display():
    print("display function run!")

display()

# test_display = outer_function(display)
# test_display()

# test_bye = outer_function("bye")
# test_hi()
# test_bye()