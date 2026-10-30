# Make a file named inputs_tracker.py inside the same folder
import inputs_tracker
inputs = inputs_tracker.InputsTracker()

while True:
    a = inputs.ask("testing: ")
    b = inputs.ask("testing: ")

    if inputs.any == 'exit':
        print("\nExiting the program.")
        break

    elif inputs.all == 'test':
        print("\nAll inputs are 'test'.")

    else:
        print("\nInputs received")

    inputs.reset()
