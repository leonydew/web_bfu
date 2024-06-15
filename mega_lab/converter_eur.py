import csv


from_ = input('Введите валюту из которой переводить: ')


to_ = input('Введите валюту в которую переводить: ')


amount_ = float(input('Введите кол-во: '))


def add(dict, cur, rate):
    dict.append({cur: rate})

def delt(dict, cur):
    for i in range(len(dict)):
        if dict[i].get(cur):
            del (dict[i])[cur]


def convert(from_, to_, amount_):
    with open("cnic_price.csv", newline= '') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")
        payload = list()
        adder_wal_name = 'JJJ'
        adder_wal_price = 129
        add(payload, adder_wal_name, adder_wal_price) 
        value = 0
        for row in reader:
            currency = row["currency"]
            rate = float(row["rate"])
            payload.append({currency: rate})
    
         
         # 1=1   
            if from_ == to_: 
                print(amount_)
                value += 1
                break

        # straight
            if from_.upper() == 'EUR':
                if currency == to_.upper() :
                    print("Текущий курс " + str(amount_) + " EUR к " + to_.upper()+ ": " + str(amount_ * rate) + to_.upper())
                    value += 1
                    break
                elif to_.upper() == adder_wal_name:
                    print("Текущий курс " + str(amount_) + " EUR к " + to_.upper()+ ": " + str(amount_ * adder_wal_price) + to_.upper())
                    value += 1
                    break
            if to_.upper() == 'EUR':
                if currency == from_.upper() :
                    print("Текущий курс " + str(amount_) + " " + from_.upper()+ " к EUR: " + str(amount_ / rate) + from_.upper())
                    value += 1
                    break
                elif from_.upper() == adder_wal_name:
                    print("Текущий курс " + str(amount_) + " " + from_.upper()+ " к EUR: " + str(amount_ / adder_wal_price) + from_.upper())
                    value += 1
                    break         
        #cross
        if value == 0:        
            for first in range(len(payload)):
                if payload[first].get(from_.upper()):
                    price_from = payload[first].get(from_.upper())
                if payload[first].get(to_.upper()):
                    price_to = payload[first].get(to_.upper())
            if price_from and price_to:     
                print("Текущий курс "+ from_.upper()+ " к " + to_.upper() + ": " + str(amount_/price_from/price_to) + " " + to_.upper() )
            else:
                print("Такой валютной пары нет")
        print(payload)
        delt(payload, 'JJJ')
        print(payload)



def main():
    convert(from_, to_, amount_)

main()
