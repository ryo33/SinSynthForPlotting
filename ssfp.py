import math

def ssfp(waves, periods, plots):
    result = []
    length = 2 * math.pi / min(waves, key=lambda a: a[1])[1] * periods
    ratio = length / plots
    for i in range(0, plots):
        value = 0;
        for wave in waves:
            value += wave[0] * math.sin(wave[1] * i * ratio)
        result.append(value)
    return result

def sketch(datas, width):
    data_max = max(datas)
    data_min = min(datas)
    ratio = width / (data_max - data_min)
    datas = [int(round(data * ratio)) for data in datas]
    offset = - int(round(data_min * ratio)) + 1
    print("offset", offset, "ratio", ratio)
    for data in datas:
        if data == 0:
            print(" " * (offset - 1) + "*")
        elif data > 0:
            print(" " * (offset - 1) + "|" + " " * (data - 1) + "*")
        else:
            data = - data
            print(" " * (offset - data - 1) + "*" + " " * (data - 1) + "|")

if __name__ == "__main__":
    waves = []
    while True:
        amp = input("amplitude > ")
        if amp == "":
            break
        freq = input("frequency > ")
        waves.append([float(amp), float(freq)])
    periods = float(input("number of periods > "))
    plots = int(input("number of plots > "))
    mode = int(input("display mode(0 - 3) > "))
    result = ssfp(waves, periods, plots)
    if mode == 1:
        sketch(result, int(input("display width > ")))
    else:
        ratio = float(input("ratio > "))
        print("\n".join([str(value * ratio) for value in result]))
