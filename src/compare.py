with open("../data/saida_todos_to.txt", "r") as myouttofile, open(
    "../data/saida_todos.txt", "r"
) as myoutfile, open("../data/saida_todos_gabriel.txt", "r") as refoutputfile:
    myanswers = {}
    for line in myoutfile:
        filename = line.split(" ")[0].split("/")[-1]
        answer = line.split(" ")[1]
        myanswers[filename] = answer

    mytoanswers = {}
    for line in myouttofile:
        filename = line.split(" ")[0].split("/")[-1]
        answer = line.split(" ")[1]
        mytoanswers[filename] = answer
    print(mytoanswers)

    refanswers = {}
    for line in refoutputfile:
        filename = line.split(" ")[0].split("/")[-1]
        answer = line.split(" ")[1]
        refanswers[filename] = answer

    same = 0
    diff = 0
    empty = 0
    for filename in myanswers.keys():
        if myanswers[filename] == refanswers[filename]:
            same += 1
        else:
            diff += 1

    print("-- Results without timeout --")
    print("Same: {}".format(same))
    print("Diff: {}".format(diff))
    print("Empty: {}".format(empty))

    same = 0
    diff = 0
    empty = 0
    for filename in mytoanswers.keys():
        if mytoanswers[filename] == "\n":
            empty += 1
        elif mytoanswers[filename] == refanswers[filename]:
            same += 1
        else:
            diff += 1

    print("-- Results with timeout 5 --")
    print("Same: {}".format(same))
    print("Diff: {}".format(diff))
    print("Empty: {}".format(empty))
