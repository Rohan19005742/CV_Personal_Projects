from enum import Enum
import random

class DayState(Enum):
    SUNNY = 0
    CLOUDY = 1
    RAINY = 2


class WeatherMarkovChain:
    def __init__(self):
        self.transition_matrix = {
            DayState.SUNNY: {DayState.SUNNY: 0.8, DayState.CLOUDY: 0.15, DayState.RAINY: 0.05},
            DayState.CLOUDY: {DayState.SUNNY: 0.2, DayState.CLOUDY: 0.6, DayState.RAINY: 0.2},
            DayState.RAINY: {DayState.SUNNY: 0.1, DayState.CLOUDY: 0.3, DayState.RAINY: 0.6},
        }
        self.current_state = DayState.SUNNY

    def next_day(self):
        rand_val = random.random()
        cumulative_prob = 0.0
        for next_state, prob in self.transition_matrix[self.current_state].items():
            cumulative_prob += prob
            if rand_val < cumulative_prob:
                self.current_state = next_state
                break
        return self.current_state

    def simulate_days(self, num_days):
        weather_sequence = []
        for _ in range(num_days):
            weather_sequence.append(self.next_day())
        return weather_sequence
    

if __name__ == "__main__":
    weather_chain = WeatherMarkovChain()
    days = 10
    weather_forecast = weather_chain.simulate_days(days)
    for day, weather in enumerate(weather_forecast, start=1):
        print(f"Day {day}: {weather.name}")