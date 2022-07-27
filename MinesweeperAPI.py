from field2 import Field

field = Field(22, 23, 66)
field.create_field()
field.set_mines()
print(field.print_field(False))
field.set_flag(0, 0)
print(field.print_field())
