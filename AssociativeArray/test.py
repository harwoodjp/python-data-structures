from impl import AssociativeArray

associative_array = AssociativeArray()

associative_array.put("hello", "world")
associative_array.put("hello", "world2")
associative_array.put("uno", "dos")
associative_array.put(5, 10)
associative_array.put("foo", 0)

associative_array.print()

print(associative_array.lookup("uno")) # "dos"