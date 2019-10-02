with open("../data/saida_todos.txt", "r") as myoutfile, open(
    "../data/saida_todos_gabriel.txt", "r"
) as refoutputfile:
    myanswers = {}
    for line in myoutfile:
        filename = line.split(" ")[0].split("/")[-1]
        answer = line.split(" ")[1]
        myanswers[filename] = answer

    refanswers = {}
    for line in refoutputfile:
        filename = line.split(" ")[0].split("/")[-1]
        answer = line.split(" ")[1]
        refanswers[filename] = answer

    same = 0
    diff = 0
    empty = 0
    for filename in myanswers.keys():
        if len(myanswers[filename]) == 0:
            empty += 1
        elif myanswers[filename] == refanswers[filename]:
            same += 1
        else:
            diff += 1

    print("-- Results --")
    print("Same: {}".format(same))
    print("Diff: {}".format(diff))
    print("Empty: {}".format(empty))
