import matplotlib.pyplot as plt

def extract_filter(model, layer_name):
    filters =  model.get_layer(layer_name).get_weights()[0]
    filters = filters[:,:,:,:6]
    # normalize values to 0-1
    f_min, f_max = filters.min(), filters.max()
    filters = (filters - f_min)/(f_max - f_min)

    return filters
