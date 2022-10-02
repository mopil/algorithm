"""
fees = 기본시간(분), 기본요금, 단위시간, 단위요금
records = "시각 차량번호 내역" ex. "22:00 0000 IN"
가장 번호가 낮은 차 부터 요금을 계산해서 리턴할 것
"""
import math


def parse(record):
    time = record.split()[0]
    car_num = record.split()[1]
    in_out = record.split()[2]
    return time, car_num, in_out


def calc_time(start, end):
    s_h = start.split(":")[0]
    s_m = start.split(":")[1]
    e_h = end.split(":")[0]
    e_m = end.split(":")[1]
    t1 = int(s_h)*60+int(s_m)
    t2 = int(e_h)*60+int(e_m)
    return abs(t1-t2)

# fees = 0: 기본시간(분), 1: 기본요금, 2: 단위시간, 3: 단위요금
def calc_pay(time, fees):
    if time <= fees[0]:
        return fees[1]
    else:
        over_time = abs(fees[0] - time)
        per_time = fees[2]
        per_pay = fees[3]
        return fees[1] + (math.ceil(over_time / per_time) * per_pay)



def solution(fees, records):
    cars = {}
    answer = []
    for record in records:
        time, car_num, in_out = parse(record)
        cars[car_num] = []

    for record in records:
        time, car_num, in_out = parse(record)
        cars[car_num].append((time, in_out))
    #
    # print(cars)
    for car in sorted(cars.keys()):
        # print(f"car = {car}")
        tmp = cars[car]
        total_time = 0
        record_idx = 0
        while record_idx < len(tmp)-1:
            if len(tmp) % 3 == 0:
                tmp.append(('23:59', 'OUT'))
            time1, in_out1 = tmp[record_idx][0], tmp[record_idx][1]
            time2, in_out2 = tmp[record_idx+1][0], tmp[record_idx+1][1]
            if in_out1 == 'IN' and in_out2 == 'OUT':
                r = calc_time(time1, time2)
                record_idx += 2
                # print(f"time = {r}")
                total_time += r
        total_pay = calc_pay(total_time, fees)
        # print(total_pay)
        answer.append(total_pay)
        # print(total_time)
    return answer


records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
fees = [180, 5000, 10, 600]
print(solution(fees, records))
