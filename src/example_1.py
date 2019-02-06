print(
"""
The Python interpreter starts at the top and works it's way down.
"""
)
print(
"""
Python uses namespaces to manage variables/environments. For example,
since we ran this from the command line, we're in the __main__ namespace.
"""
)

def main():
    print(
"""
I'm inside the main function! You don't need to have a main "
function, but it's good practice!
""")

if __name__ == "__main__":
    print(
"""
This is where the program *should* start (if we follow good object oriented
Python practices). Python doesn't prevent you from doing dumb things.
You're free to do it as you please!
"""
)
    main()

    # This is how you write comments in Python.
    import example_1_import_this
    print(example_1_import_this.a)
