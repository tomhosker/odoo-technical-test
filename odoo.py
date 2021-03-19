def add_integers(list_of_strings):
    result = 0
    for string in list_of_strings:
        try:
            float_ = float(string)
        except ValueError:
            continue
        if float_.is_integer():
            result = result+int(float_)
    return result

def test():
    assert add_integers(["1", "2", "3"]) == 6
    assert add_integers(["1", "smeg", "3"]) == 4
    assert add_integers(["1", "2.5", "3"]) == 4
    print("Tests passed!")

if __name__ == "__main__":
    test()
