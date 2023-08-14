from itertools import islice

class Plot:
    def __init__(self):
        self.events = {}  # Dictionary to store events and their corresponding index
        self.next_index = 0  # Next available index for events

    def add_event(self, evt):
        self.events[evt] = self.next_index  # Add an event to the dictionary with its index
        self.next_index += 1  # Increment the next available index

    def dreamify(self, amount):
        for _ in range(amount):
            self.events.popitem()  # Remove the last added event (LIFO for Python dictionaries)
            self.next_index -= 1  # Decrement the next available index

    def check_scenario(self, scenarios):
        to_rem, must_remain = 0, -1
        for s in scenarios:
            if s[0] == '!':  # If the scenario starts with '!', it means the event should not be present
                ev = s[1:]
                if ev in self.events:
                    to_rem = max(to_rem, len(self.events) - self.events[ev])  # Calculate events to be removed
            else:
                if s not in self.events:
                    return 'Plot Error'  # The required event is not present
                else:
                    must_remain = max(self.events[s], must_remain)  # Update the required event index
        if to_rem == 0:
            return 'Yes'  # The scenario can be achieved
        if must_remain >= len(self.events) - to_rem:
            return 'Plot Error'  # Not enough events left to achieve the scenario
        return f'{to_rem} Just A Dream'  # The scenario can be achieved by removing certain events

def main():
    plot = Plot()
    for _ in range(int(input())):
        line = input().split()
        if line[0] == 'E':
            plot.add_event(line[1])  # Add an event
        elif line[0] == 'D':
            plot.dreamify(int(line[1]))  # Remove the last N added events
        else:
            print(plot.check_scenario(islice(line, 2, None)))  # Check if a scenario is achievable

if __name__ == "__main__":
    main()
