def comb_sort(array: list[float], shrink: float = 1.3) -> list[float]:
    length = len(array)
    _gap = length
    output = list(array)
    is_sorted = False
    while not is_sorted:
        _gap /= shrink
        gap = int(_gap)
        if gap <= 1:
            is_sorted = True
            gap = 1
        for index in range(length - gap):
            __gap = gap + index
            if output[index] > output[__gap]:
                output[index], output[__gap] = output[__gap], output[index]
                is_sorted = False
    return output
