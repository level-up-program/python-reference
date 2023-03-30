from levelup.controller import GameController
from robot.libraries.BuiltIn import BuiltIn

class GameControllerLibrary:
    ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

    def initialize_controller(self):
        self.controller = GameController()

    def create_character_with_name(self, charactername):
        self.controller.create_character(charactername)

    def character_name_should_be(self, expected):
        if self.controller.status.character_name != expected:
            raise AssertionError(
                f"{self.controller.status.character_name} != {expected}"
            )

    def number_of_map_positions_should_be(self, expected):
        pass  # Not implemented

    def starting_X_coordinate_should_be(self, expected):
        pass  # Not implemented

    def starting_Y_coordinate_should_be(self, expected):
        pass  # Not implemented

    def starting_move_count_should_be(self, expected):
        pass  # Not implemented
