def simple_test(func, tests_and_expected_results):
    for test, expected in tests_and_expected_results:
        actual = func(test)
        if expected != actual:
            print(f"{test=}")
            print(f"{expected=}")
            print(f"{actual=}")
        else:
            print("pass")


def simple_test_in_place(func, tests_and_expected_results):
    from copy import deepcopy
    for test, expected in tests_and_expected_results:
        input = deepcopy(test)
        func(test)
        if expected != test:
            print(f"{test=}")
            print(f"{expected=}")
            print(f"{input=}")
        else:
            print("pass")
