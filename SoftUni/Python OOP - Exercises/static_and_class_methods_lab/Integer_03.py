class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not float_value.__class__.__name__ == 'float':
            return f"value is not a float"
        return int(float_value)

    @classmethod
    def from_roman(cls, value):
        pass

    @classmethod
    def from_string(cls, value):
        try:
            a = int(value)
            return a
        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
