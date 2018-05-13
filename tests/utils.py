from chapter_5.exercises import DynamicArray


def create_dynamic_array_with_specific_number_of_elements(
        how_many_elements_to_add,
        capacity=1
) -> DynamicArray:
    array = DynamicArray(capacity=capacity)
    for i in range(how_many_elements_to_add):
        array.append(i)

    return array
