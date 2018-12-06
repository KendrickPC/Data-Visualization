# To plot random_walk.py, run rw_visual.py file with Python3.
# Change code in line 3 for importing.

from random import choice

class RandomWalk():
    """ A class to generate random walks. """

    def __init__(self, num_points=5000):
        """ Initialize attributes of a walk. """
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction * distance
        direction = ([1, -1])
        distance = ([0, 1, 2, 3, 4])

    def fill_walk(self):

        direction = ([1, -1])
        distance = ([0, 1, 2, 3, 4])
        x_step = get_step()
        y_step = get_step()
        """ Calculate all points in the random walk. """

        # Keep taking steps until the random walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            """
            Decide which direction to go and how far to go in that
            direction.
            """

            # x_direction = choice([1, -1])
            # x_distance = choice([0, 1, 2, 3, 4])
            # x_step = x_direction * x_distance

            # y_direction = choice([1, -1])
            # y_distance = choice([0, 1, 2, 3, 4])
            # y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    # def get_step(self):
    #     direction = ([1, -1])
    #     distance = ([0, 1, 2, 3, 4])
    #     x_step = direction * distance
    #     y_step = direction * distance
