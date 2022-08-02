class Validator:

    @staticmethod
    def speed_limiter(value, min_speed_limit, max_speed_limit, message):
        if min_speed_limit > value or value > max_speed_limit:
            raise ValueError(message)

    @staticmethod
    def string_should_be_no_less_than_4_characters(value, message):
        if len(value) < 4:
            raise ValueError(message)

    @staticmethod
    def check_for_empty_or_white_space(value, message):
        if value.strip() == '':
            raise ValueError(message)
