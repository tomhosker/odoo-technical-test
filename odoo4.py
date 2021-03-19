def add_integers_recursively(list_of_strings, result=0, index=0):
    string = list_of_strings[index]
    try:
        float_ = float(string)
    except ValueError:
        pass
    else:
        if float_.is_integer():
            result = result+int(float_)
    if index == len(list_of_strings)-1:
        return result
    return add_integers_recursively(list_of_strings, result, index+1)

def test():
    assert add_integers_recursively(["1", "2", "3"]) == 6
    assert add_integers_recursively(["1", "smeg", "3"]) == 4
    assert add_integers_recursively(["1", "2.5", "3"]) == 4
    print("Tests passed!")

if __name__ == "__main__":
    test()
