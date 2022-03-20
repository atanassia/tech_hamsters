import csv
import random
import copy
from datetime import datetime, date
from collections import Counter
import calendar
from datetime import date, timedelta

from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

############## ИСПРАВЬ НА ПРОДЕ УЧЕТ РАЗМЕРА СПИСКА норм

def read_csv_oblig(filename):
    # SECID, SHORTNAME,FACEVALUE,CouponspPerYear,FACEUNIT,MaturityDate,IncomPerYear,risk_category,COUPON
    with open(BASE_DIR / "business_services" / filename,  encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = []
        for row in reader:
            data.append(list(row.values())[1:])
            # print(list(row.values())[1:])
        csvfile.close()
    return data


# print(read_csv_oblig("ru_A.csv"))

def min_cost_in_range_obl(left_range,right_range, list_tickers):
    X = copy.deepcopy(list_tickers[left_range: right_range])
    m = X.index(min(X, key=lambda i: float(i[-1])))
    return X[m]

def convert(money, currency): #------------------------------------------------------------------------------------------------------
    if currency == "$":
        return money * 110
    if currency == "RUB":
        return money / 110

def return_oblig(money, type):
    sorted_info_by_total = read_csv_oblig(f'ru_{type}.csv')
    list_for_buy = []
    while money > float(min_cost_in_range_obl(0, 300, sorted_info_by_total)[-1]):
        slot = random.randint(0, 300)
        while money < float(sorted_info_by_total[slot][-1]):
            slot = random.randint(0, 300)
        list_for_buy.append(sorted_info_by_total[slot])
        money = money - float(sorted_info_by_total[slot][-1])

    return list_for_buy

def react_oblig(money, vremya, profile):

    if vremya == "6_months":
        timester = 6
    if vremya == "12_months":
        timester = 12
    if vremya == "3_years":
        timester = 36

    end_spisok = []
    spoe_time = date.today()
    days = calendar.monthrange(spoe_time.year, spoe_time.month)[1]

    for _ in range(timester):
        if profile == "passive":
            list_of_oblig = return_oblig(money, "A")
        if profile == "normal":
            list_of_oblig = return_oblig(money, "B")
        if profile == "aggressive":
            list_of_oblig = return_oblig(money, "C")

        end_spisok.append([spoe_time.strftime("%d.%m.%y"), list_of_oblig])
        spoe_time = spoe_time + timedelta(days=days)
    return end_spisok

#--------------------------------------------------------------------------------

def read_csv(filename):
    with open(BASE_DIR / "business_services" / filename, "r") as file:
        information = csv.reader(file, delimiter=',', quotechar='\t')
        real_info =[]
        for row in information:
            if row:
                real_info.append(row)
        return real_info

def good_print(sposok):
    for row in sposok:
        print(row)

def min_cost_in_range(left_range,right_range, list_tickers):
    X = copy.deepcopy(list_tickers[left_range:right_range])
    m = X.index(min(X, key=lambda i: float(i[3])))
    return X[m]

def take_from_stability(money: float):
    sorted_info_by_total = read_csv('sort_by_stability_stock.csv')
    list_for_buy = []
    while money > float(min_cost_in_range(0, 23, sorted_info_by_total)[3]):
        slot = random.randint(0, 23)
        while money < float(sorted_info_by_total[slot][3]):
            slot = random.randint(0, 23)
        list_for_buy.append(sorted_info_by_total[slot])
        money = money - float(sorted_info_by_total[slot][3])

    return list_for_buy

def take_from_profit(money: float):
    sorted_info_by_total = read_csv('sort_by_profit_stock.csv')
    list_for_buy = []
    while money > float(min_cost_in_range(0, 15, sorted_info_by_total)[3]):
        slot = random.randint(0, 15)
        while money < float(sorted_info_by_total[slot][3]):
            slot = random.randint(0, 15)
        list_for_buy.append(sorted_info_by_total[slot])
        money = money - float(sorted_info_by_total[slot][3])

    return list_for_buy


def take_from_total(money: float):  # 0-30
    sorted_info_by_total = read_csv('sort_by_total.csv')
    list_for_buy = []
    while money > float(min_cost_in_range(0, 30, sorted_info_by_total)[3]):
        slot = random.randint(0, 30)
        while money < float(sorted_info_by_total[slot][3]):
            slot = random.randint(0, 30)
        list_for_buy.append(sorted_info_by_total[slot])
        money = money - float(sorted_info_by_total[slot][3])

    return list_for_buy

def create_time_manage(time, money):
    list_for_time = []
    if time == "6_months":
        timester = 6
    if time == "12_months":
        timester = 12
    if time == "3_years":
        timester = 36

        for i in range(timester):
            list_for_time.append()

def take_normal_names_from_ak(ob):
    return [ob[1], ob[2]]


# def del_tha_same(list_of_tickets, vremya):
#
#     end_spisok = []
#     spoe_time = date.today()
#     days = calendar.monthrange(spoe_time.year, spoe_time.month)[1]
#     # timing_plus = date(0,1,0)
#
#     if vremya == "6_months":
#         timester = 6
#     if vremya == "12_months":
#         timester = 12
#     if vremya == "3_years":
#         timester = 36
#     info = read_csv("sort_by_total.csv")
#
#     for _ in range(timester):
#         split_list = []
#         for i in list_of_tickets:
#             split_list.append(i[1])
#
#         coun = Counter(split_list)
#
#         some_list = []
#         for i in coun:
#             some_list.append([i, coun[i]])
#         print(some_list)
#
#         for i in some_list:
#             for j in list_of_tickets:
#                 if i[0] == j[1]:
#                     i.append(j[2])
#                     i.append(j[3])
#                     i.append(float(j[3]) * float(i[1]))
#
#         end_spisok.append([spoe_time.strftime("%d.%m.%Y"), some_list])
#         spoe_time = spoe_time + timedelta(days=days)
#         print(end_spisok)
#
#     return end_spisok


def react_akzi(money, vremya, profile):

    money = convert(float(money), "RUB")

    end_spisok = []
    spoe_time = date.today()
    days = calendar.monthrange(spoe_time.year, spoe_time.month)[1]
    # timing_plus = date(0,1,0)

    if vremya == "6_months":
        timester = 6
    if vremya == "12_months":
        timester = 12
    if vremya == "3_years":
        timester = 36
    info = read_csv("sort_by_total.csv")

    for _ in range(timester):
        if profile == "passive":
            list_of_tickets = copy.deepcopy(take_from_profit(money / 100 * 10)) + copy.deepcopy(take_from_total(money / 100 * 30)) \
                              + copy.deepcopy(take_from_stability(money / 100 * 60))

        if profile == "normal":
            list_of_tickets = copy.deepcopy(take_from_profit(money / 100 * 20)) + copy.deepcopy(take_from_total(money / 100 * 60)) \
                              + copy.deepcopy(take_from_stability(money / 100 * 20))

        if profile == "aggressive":
            list_of_tickets = copy.deepcopy(take_from_profit(money / 100 * 60)) + copy.deepcopy(take_from_total(money / 100 * 30)) \
                              + copy.deepcopy(take_from_stability(money / 100 * 10))
        split_list = []
        for i in list_of_tickets:
            split_list.append(i[1])

        coun = Counter(split_list)

        some_list = []
        for i in coun:
            some_list.append([i, coun[i]])
        # print(some_list)

        for i in some_list:
            for j in list_of_tickets:
                if i[0] == j[1]:
                    i.append(j[2])
                    i.append(convert(float(j[3]), "$"))
                    i.append(convert(float(j[3]) * float(i[1]), "$"))

        end_spisok.append([spoe_time.strftime("%d.%m.%y"), some_list])
        spoe_time = spoe_time + timedelta(days=days)
        # print(end_spisok)
    # ебаный костль  данные умножаются на кол-во акций
    for i , some in enumerate(end_spisok):
        for hof ,index in enumerate(some[1]):
            some[1][hof] = some[1][hof][:5]
    return end_spisok


# print(react_akzi(10000, "6_months", "passive"))


# x = take_from_total(300)
# good_print(x)

# ------------------------------ ---------------------------------------------------------------------------------------------------
# z = del_tha_same(100000,"6_months", "passive" )
# good_print(z)
# print("sdfsd")


def return_investing_plan(money_sum: int, time_for_investing: str, profile: str, currency: str="$") -> list[str, str, list[str, int, str, float]]:
    """0<money<100.000.000 time_for_investing=6_months, 12_months, 3_years profile=passive, normal, aggressive
    currency=$,RUB
    back = [ticker, full_name,[currency, number, dd.mm.yyyy, cost]]"""

    # if currency == "RUB":
    #     money_sum = money_sum * 110
    if time_for_investing == "6_months":
        timester = 6
    if time_for_investing == "12_months":
        timester = 12
    if time_for_investing == "3_years":
        timester = 36

    list_for_buy = []
    for i in range(timester):
        if profile == "passive":
            list_for_buy.append(take_from_stability(money_sum / 100 * 60))
            list_for_buy.append(take_from_total(money_sum / 100 * 30))
            list_for_buy.append(take_from_profit(money_sum / 100 * 10))
        if profile == "normal":
            list_for_buy.append(take_from_stability(money_sum / 100 * 20))
            list_for_buy.append(take_from_total(money_sum / 100 * 60))
            list_for_buy.append(take_from_profit(money_sum / 100 * 20))
        if profile == "aggressive":
            list_for_buy.append(take_from_stability(money_sum / 100 * 10))
            list_for_buy.append(take_from_total(money_sum / 100 * 30))
            list_for_buy.append(take_from_profit(money_sum / 100 * 60))

        #//// code


    return None


def liza_retern_2_lists(money_sum, vremya, profile):


    if vremya == "6_months":
        timester = 6
    if vremya == "12_months":
        timester = 12
    if vremya == "3_years":
        timester = 36


    if profile == "passive":
            liza_list = [react_akzi(money_sum / 100 * 20, vremya, profile), react_oblig(money_sum / 100 * 80, vremya, profile)]
    if profile == "normal":
            liza_list = [react_akzi(money_sum / 100 * 50, vremya, profile), react_oblig(money_sum / 100 * 50, vremya, profile)]
    if profile == "aggressive":
            liza_list = [react_akzi(money_sum / 100 * 80, vremya, profile), react_oblig(money_sum / 100 * 20, vremya, profile)]

    return liza_list

# print(liza_retern_2_lists(2000,"6_months", "normal"))

