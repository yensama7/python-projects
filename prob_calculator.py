import copy
import random

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        # Copy the hat contents
        hat_contents = copy.deepcopy(hat)

        # Shuffle the hat contents
        random.shuffle(hat_contents)

        # Draw balls from the hat
        chosen_balls = random.sample(hat_contents, num_balls_drawn)

        # Check if the balls meet the expected conditions
        expected_balls_met = True
        for color, count in expected_balls.items():
            if chosen_balls.count(color) < count:
                expected_balls_met = False
                break

        # If the balls meet the expected conditions, increment the success counter
        if expected_balls_met:
            successes += 1

    # Calculate the probability as the number of successful experiments divided by the total number of experiments
    probability = successes / num_experiments

    return probability