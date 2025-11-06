from main import LinkedList

run_cases = [
    (
        [
            ("push_back", 1),
            ("push_back", 2),
            ("push_back", 3),
            ("pop_back", None),
        ],
        [3],
        [1, 2],
    ),
    (
        [
            ("push_front", "A"),
            ("push_front", "B"),
            ("pop_front", None),
            ("push_back", "C"),
        ],
        ["B"],
        ["A", "C"],
    ),
    (
        [
            ("push_back", 42),
            ("pop_back", None),
        ],
        [42],
        [],
    ),
]

submit_cases = run_cases + [
    (
        [
            ("pop_front", None),
            ("pop_back", None),
        ],
        [None, None],
        [],
    ),
    (
        [
            ("push_front", 1),
            ("push_back", 2),
            ("push_front", 0),
            ("pop_front", None),
            ("pop_back", None),
            ("push_back", 3),
        ],
        [0, 2],
        [1, 3],
    ),
    (
        [
            ("push_back", 1),
            ("push_back", 2),
            ("push_back", 3),
            ("push_front", 0),
            ("pop_front", None),
            ("push_back", 4),
            ("pop_back", None),
        ],
        [0, 4],
        [1, 2, 3],
    ),
]


def apply_ops(ops):
    ll = LinkedList()
    popped = []
    for op, val in ops:
        if op == "push_front":
            ll.push_front(val)
        elif op == "push_back":
            ll.push_back(val)
        elif op == "pop_front":
            popped.append(ll.pop_front())
        elif op == "pop_back":
            popped.append(ll.pop_back())
    return popped, ll.to_list()


def format_ops(ops):
    lines = []
    for op, val in ops:
        if val is None or op.startswith("pop"):
            lines.append(f"- {op}()")
        else:
            lines.append(f"- {op}({repr(val)})")
    return "\n".join(lines)


def test(ops, expected_popped, expected_final):
    print("---------------------------------")
    print("Input operations:\n" + format_ops(ops))
    popped, final_list = apply_ops(ops)
    print(f"\nExpected popped: {expected_popped}")
    print(f"Actual popped:   {popped}")
    print(f"Expected final list: {expected_final}")
    print(f"Actual final list:   {final_list}")
    if popped == expected_popped and final_list == expected_final:
        return True
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for case in test_cases:
        correct = test(*case)
        if correct:
            passed += 1
            print("Pass")
        else:
            failed += 1
            print("Fail")
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
