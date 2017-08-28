import numpy as np


def monty_hall_simulation(n_doors=3, n_samples=10):
    correct_choice = np.random.choice(n_doors, n_samples)
    initial_choice = np.random.choice(n_doors, n_samples)

    goats = np.ones((n_samples, n_doors))
    goats[np.arange(n_samples), correct_choice] = False
    goats[np.arange(n_samples), initial_choice] = False

    goat_doors = np.array([np.random.choice([index for index, prob in enumerate(row) if prob == 1]) for row in goats])

    new_choices = np.ones((n_samples, n_doors))
    new_choices[np.arange(n_samples), initial_choice] = False
    new_choices[np.arange(n_samples), goat_doors] = False

    _, new_choice = np.where(new_choices == True)

    success_rate_no_switch = (initial_choice == correct_choice).mean()
    success_rate_switch = (new_choice == correct_choice).mean()

    return success_rate_switch, success_rate_no_switch


def main():
    # These should be very close to 66.67% and 33.33%
    success_rate_switch, success_rate_no_switch = monty_hall_simulation(n_samples=10000)

    print(f"Switch:    {success_rate_switch * 100}% success rate")
    print(f"No switch: {success_rate_no_switch * 100}% success rate")


if __name__ == "__main__":
    main()
