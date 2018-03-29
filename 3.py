#My short trip
def trans(city):
    if city == "London":
        return 5000
    elif city == "Surat":
        return 2000
    elif city== "Diu":
        return 3000
    else:
        print ("Enter a valid input")

def tour(dist):
    fare = dist * 120
    if dist >= 10 and dist<=15:
        return fare - 50
    elif dist > 15 :
        return fare - 100
    return fare

def stay(days):
    if days <= 2 :
        return 1000 * days
    elif days >= 2 :
        return 1000 * days - 500

def total(city,dist,days):
    tot = trans(city) + tour(dist) + stay(days)
    print ("So your total expenditure for %s city , for %d km and %d days will be Rs %d") % (city,dist,days,tot)

total("London",1500,30)





