def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if nums != None and nums != []: return (min(nums), max(nums))
    else: return "ValueError"

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))     

print('\n\n#########\n\n')
def unique_sorted(nums: list[float | int]) -> tuple[float | int, float | int]:
    return sorted(set(nums))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))    
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print('\n\n#########\n\n')

def flatten(mat: list[list | tuple]) -> list:
    new_list = []
    for lists in mat:
        if type(lists) != list and type(lists) != tuple: return "TypeError"
        for element_of_list in lists:
            new_list.append(element_of_list)
    return sorted(new_list)

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))