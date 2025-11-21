"""Functions to determine the type of triangle based on its side lengths."""

def checkTriangle(sides: list[int]) -> bool:
    """Return True if valid triangle."""
    
    return (sides[0] > 0 and sides[1] > 0 and sides[2] > 0 and 
            sides[0] + sides[1] >= sides[2] and 
            sides[1] + sides[2] >= sides[0] and 
            sides[0] + sides[2] >= sides[1])

def equilateral(sides: list[int]) -> bool:
    """Return True if equilateral."""
    
    return checkTriangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides: list[int]) -> bool:
    """Return True if isosceles."""

    return (checkTriangle(sides) and (sides[0] == sides[1] or 
            sides[0] == sides[2] or sides[1] == sides[2]))


def scalene(sides: list[int]) -> bool:
    """Return True if scalene."""

    return (checkTriangle(sides) and sides[0] != sides[1] and 
            sides[0] != sides[2] and sides[1] != sides[2])
