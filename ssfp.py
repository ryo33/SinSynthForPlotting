import math

def ssfp(waves, periods, division):
    result = []
    length = 2 * math.pi / min(waves, key=lambda a: a[1])[1] * periods
    for i in range(0, division + 1):
        value = 0;
        for wave in waves:
            value += wave[0] * math.sin(wave[1] * i * length / division)
        result.append(value)
    return result

def sketch(datas, width):
    data_max = max(datas)
    data_min = min(datas)
    ratio = width / (data_max - data_min)
    datas = [int(round(data * ratio)) for data in datas]
    offset = - int(round(data_min * ratio)) + 1
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
        amp_freq = input("frequency and amplitude > ")
        if amp_freq == "":
            break
        amp_freq = amp_freq.split(' ')
        waves.append([float(amp_freq[1]), float(amp_freq[0])])
    periods = float(input("number of periods > "))
    division = int(input("number of division > "))
    mode = int(input("display mode(0 - 2) > "))
    result = ssfp(waves, periods, division)
    if mode == 1:
        ratio = float(input("ratio > "))
        print(", ".join([str(value * ratio) for value in result]))
    elif mode == 2:
        sketch(result, int(input("display width > ")))
    else:
        ratio = float(input("ratio > "))
        for i in range(0, len(result)):
            print(str(i) + " " + str(round(result[i] * ratio, 3)))
