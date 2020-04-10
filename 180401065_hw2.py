file = open(r"input_hw_2.csv", "r+")
import sys
ay = []
frekans = []



def hist(file):
  histogram = hist(file)
    for i in file:
        check = False
        frekans.append(int(i.split(";")[3].split("-")[1]))
        
    for k in frekans:
        if(k in ay.keys()):
            ay[k] = ay[k] + 1
        else:
            ay[k] = 1
    return hist,ay

def sort(list):
    for a in range(len(list)-1,-1,-1):
        for b in range(0,a):
            if not list[b]<list[b+1]:
                temp=list[b]
                list[b],list[b+1]=list[b+1],temp
    return list

def average(list):
    toplam=0
    for i in list:
        toplam+=i
    return toplam/len(list)

def median():
    MedyanBul = sort(ay)
    if len(MedyanBul) % 2 == 1:
        orta = int(len(MedyanBul)/2)
        return MedyanBul[orta]


    else:
        orta1,orta2 = MedyanBul[int(len(MedyanBul)/2)],MedyanBul[int(len(MedyanBul)/2)-1]
        return (orta1 + orta2)/2

def yazma(average, median):
    yaz = open(w"180401070_hw_2_output.txt", "w+")
    yaz.write(f"Medyan : {str(median)}")
    yaz.write("\n")
    yaz.write(f"Ortalama : {str(average)}")
    f.close()

print(histogram)