from inputs_lower import InputsTracker
inputs = InputsTracker()

while True:
    user_input1 = inputs.ask("Type anything ('exit' to quit): ")
    user_input2 = inputs.ask("Type anything ('exit' to quit): ")
    if inputs.any == "exit":
        break

    elif inputs.all == "test":
        print("All inputs were 'test'")

    else:
        print("Random else statement hit")

    inputs.reset()