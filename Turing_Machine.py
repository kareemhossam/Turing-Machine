#Python code for Turing machine Simulation
class Transistion:
    def __init__(self, state, character, newState, newCharacter, action):
        self.state = state
        self.character = character
        self.newState = newState
        self.newCharacter = newCharacter
        self.action = action


def main():
    # User Input:
    number_of_states = int(input("Enter number of states"))
    alphabet = input(
        "Enter alphabet (Gamma) in comma separated list").split(",")
    number_of_trasition_fn = number_of_states * len(alphabet)
    transition_fns = []
    for i in range(number_of_trasition_fn):
        temp = input("Enter Transition Function number " +
                     i + " in a comma separated list").split(",")
        if (len(temp) != 5):
            print("Invalid Input!!!")
            exit(1)
        transition_fn = Transistion(
            temp[0], temp[1], temp[2], temp[3], temp[4])
        transition_fns.append(transition_fn)
    loop = True
    # Main Loop:
    while (loop):
        rounds = 0
        tape = input("Enter input tape")
        head_pos = int(input("Enter head Position"))

        # Consuming the tape:
        tr_fn_found = False
        current_state = 0

        while (not tr_fn_found):
            rounds += 1
            for i in transition_fns:
                if (head_pos >= len(tape)):
                    print("Index out of Bound!!!")
                    exit(1)
                if (i.state != current_state or i.character != tape[head_pos]):
                    continue
                else:
                    current_state = i.newState
                    if (i.action == "R"):
                        head_pos += 1
                    elif (i.action == "L"):
                        head_pos -= 1
                    elif (i.action == "Y"):
                        complete = True
                    elif (i.action == "N"):
                        complete = False

        if (complete != False):
            print("YY")
        else:
            print("NN")
        question = input("Try again [y/N]")
        if (question != 'y' or question != 'Y'):
            loop = False


if __name__ == "__main__":
    main()
