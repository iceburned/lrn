# from project.space_station import SpaceStation
#
# s = SpaceStation()
# print(s.add_astronaut("Biologist", "Pesho"))
# print(s.add_astronaut("Geodesist", "Qncho"))
# # print(s.add_astronaut("Meteorologist", "Misho"))
# # print(s.add_astronaut("Geodesist", "Sasho"))
# # print(s.add_astronaut("Meteorologist", "Teo"))
# # print(s.add_astronaut("Biologist", "Ivo"))
# # print(s.add_astronaut("Biologist", "Ivan"))
# print(s.add_planet("Pluto", "knife, dog, paper, sugar, knife, dog, paper, sugar, knife, dog, paper, sugar"))
# print(s.retire_astronaut("Pesho"))
# print(s.send_on_mission("Pluto"))
# s.recharge_oxygen()
# print(s.report())
# a = 1


from project.space_station import SpaceStation

space_station = SpaceStation()
print(space_station.add_astronaut("Biologist", "Peter"))
print(space_station.add_astronaut("Meteorologist", "George"))
print(space_station.add_astronaut("Geodesist", "Sam"))
print(space_station.add_planet("Mars", "coal, gold, iron, water, diamonds, silver, platinum, zinc, uranium, aluminum"))
print(space_station.send_on_mission("Mars"))
print(space_station.report())
