# String -> String
def read_file(filename):
    """ Read contents of file. """
    f = open(filename)
    contents = f.read()
    f.close()
    return contents

# String -> List String
split_lines = lambda s: s.split('\n')
    
# String -> List String
read_lines = lambda filename: split_lines(read_file(filename))

# String -> String
def strip_suffix(s, suffixes):
    """ If s ends with any of the given suffixes, remove that suffix. """
    for suffix in suffixes:
        if s.endswith(suffix):
            return s.rstrip(suffix)
    return s

# Set a -> Set a -> (Set a, Set a, Set a)
def venn(a,b):
    """ Return triple with elements found only in a, in both a and b, and only b. """
    a = set(a)
    b = set(b)
    return map(list, (a.difference(b), a.intersection(b), b.difference(a)))

# Set a -> Set a -> (Int, Int, Int)
def nvenn(a,b):
    """ Return triple with number of elements found
        only in a, in both a and b, and only in b. """
    return map(len, venn(a,b))    