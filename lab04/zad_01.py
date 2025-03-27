import math

def fctAct(x):
    return 1 / (1 + math.exp(-x))   # to samo co math.e**(-x), ale bardziej optymalne

def forwardPass(wiek, waga, wzrost):
    hidden1 = (wiek * -0.46122) + (waga * 0.97314) + (wzrost * -0.39203)
    hidden1_po_aktywacji = fctAct(hidden1 + 0.80109)

    hidden2 = (wiek * 0.78548) + (waga * 2.10584) + (wzrost * -0.57847)
    hidden2_po_aktywacji = fctAct(hidden2 + 0.43529)

    output = (hidden1_po_aktywacji * -0.81546) + (hidden2_po_aktywacji * 1.03775) + -0.2368
    return output


wiek = [23, 25, 28, 22, 46, 50, 48]
waga = [75, 67, 120, 65, 70, 68, 97]
wzrost = [176, 180, 175, 165, 187, 180, 178]

def processData(wiek, waga, wzrost):
    results = []
    for wi, wa, wz in zip(wiek, waga, wzrost):
        results.append(forwardPass(wi, wa, wz))
    return results

output_values = processData(wiek, waga, wzrost)
print(output_values)

# print(forwardPass(23, 75, 176))
# print(forwardPass(28, 120, 175))
