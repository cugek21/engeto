def je_anagram(*args):
    vzor = sorted(args[0])

    for slovo in args:
        if vzor != sorted(slovo):
            return False
    else:
        return True

print(
    je_anagram("ship", "hips", "phis"),
    je_anagram("ship", "hips", "duck"),
    sep='\n'
)