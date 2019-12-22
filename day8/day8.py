def part1():
    data = open('input').readline()
    layers = []

    layer_size = 25 * 6
    start = 0
    end = start + layer_size
    min_zeroes = layer_size
    min_zeroes_i = 0
    while start < len(data):
        layer = data[start:end]
        start += layer_size
        end += layer_size
        if layer.count('0') < min_zeroes:
            min_zeroes = layer.count('0')
            min_zeroes_i = len(layers)
        layers.append(layer)

    print(len(layers))
    zero_layer = layers[min_zeroes_i]
    print(zero_layer.count('1') * zero_layer.count('2')) # 1215



part1()


def part2():
    data = open('input').readline()

    layer_size = 25 * 6
    img = ['2'] * layer_size
    start = 0
    end = start + layer_size
    while start < len(data):
        layer = data[start:end]
        for i in range(0, layer_size):
            if img[i] == '2':
                img[i] = layer[i]

        start += layer_size
        end += layer_size
    
    for y in range(0, 6):
        row = ''
        for x in range(0, 25):
            here = img[x+y*25]
            pixel = '?'
            if here == '2':
                assert False
            elif here == '1':
                pixel = '*'
            elif here == '0':
                pixel = ' '
            row = row + pixel
        print(row)

part2() # LHCPH
