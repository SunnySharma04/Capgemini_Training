from Signal.city_signal import CitySignal
from Signal.highway_signal import HighwaySignal
from Controller.controller import SignalController
from app_logger import logger


logger.info("Traffic Simulation Started.......")

controller = SignalController()

no_vehicle = int(input("Enter the number of vehicles: "))

city_signal = CitySignal(no_vehicle)
highway_signal = HighwaySignal(no_vehicle)

controller.operate(city_signal)
controller.operate(highway_signal)

logger.info(f"Simulation Completed")