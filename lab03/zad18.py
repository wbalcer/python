def convert_temperature(value, from_scale, to_scale):
    from_scale = from_scale.lower()
    to_scale = to_scale.lower()
    
    if from_scale == to_scale:
        return value
    
    if from_scale == "c":
        celsius = value
    elif from_scale == "f":
        celsius = (value - 32) * 5/9
    elif from_scale == "k":
        celsius = value - 273.15
    else:
        raise ValueError("Nieznana skala temperatury: {}".format(from_scale))
    
    if to_scale == "c":
        return celsius
    elif to_scale == "f":
        return celsius * 9/5 + 32
    elif to_scale == "k":
        return celsius + 273.15
    else:
        raise ValueError("Nieznana skala temperatury: {}".format(to_scale))

print(convert_temperature(100, "C", "F"))
