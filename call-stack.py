def funcThree() -> None:
    print('Three')

def funcTwo() -> None:
    funcThree() # Call funcThree()
    print('Two')

def funcOne() -> None:
    funcTwo() # Call funcTwo()
    print('One')

# Call a Base Case
funcOne()