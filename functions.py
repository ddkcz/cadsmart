#jednostki metryczne na metr
def metric(metr, na_metr):
    match metr:
        case "mm":
            na_metr = na_metr / 1000
        case "cm":
            na_metr = na_metr / 100
        case "dm":
            na_metr = na_metr / 10
        case "m":
            na_metr = na_metr
        case "km":
            na_metr = na_metr * 1000 

    return na_metr




#jednostki imperialne na milę
def imperial(mila, na_mile):
    match mila:
        case "in":
            na_mile = na_mile * 63360
        case "ft":
            na_mile = na_mile * 5.280
        case "yd":
            na_mile = na_mile * 1.760
        case "fur":
            na_mile = na_mile * 5.280
        case "mi":
            na_mile = na_mile
    
    return na_mile




#metry na jednostki metryczne
def metr_conversion(future_metric, future_metric_value):  

    match future_metric_value:
        case "mm":
            future_metric = future_metric / 1000
        case "cm":
            future_metric = future_metric / 100
        case "dm":
            future_metric = future_metric / 10
        case "m":
            future_metric = future_metric
        case "km":
            future_metricr = future_metric * 1000 

    return future_metric_value
    



#mile na jednostki imprerialne
def imperial_conversion(future_imperial, future_imperial_value):
     
    match future_imperial:
        case "in":
            future_imperial_value = future_imperial_value / 63360
        case "ft":
            future_imperial_value = future_imperial_value / 5280
        case "yd":
            future_imperial_value = future_imperial_value / 1760
        case "fur":
            future_imperial_value = future_imperial_value / 0.000189393939
        case "mi":
            future_imperial_value = future_imperial_value

    return future_imperial_value



#mile na metry
def imperial_to_metric(in_imperial):
    out_metric = in_imperial * 0.000621371
    return out_metric

#metry na mile
def metric_to_imperial(in_metric):
    out_imperial = in_metric / 1609.344
    return out_imperial


x = input("Podaj długość wraz z jednostką w formacie: mm, cm, m, km: ")
        #if mm,m,dm,cm to wykonać dla metrycznych itp
x = x.split(" ")
    

# dodać funkcję, która pozwoli na przypisanie zawsze mm cm dm m km dla jednostki w tym miejscu listy, 
# bez względu na formę wkładu przez klienta
wartosc_in = x[0]
wartosc_in = float(wartosc_in)
jednostka_in = x[1]
jednostka_out = input("Na co zamienić tą długość? ")

#określenie systemu in, przeliczenie na bazową jednostkę
if jednostka_in == "mm" or "cm" or "m" or "dm" or "km":
    system_in = "metric"
    wartosc_metr = metric(na_metr = wartosc_in, metr = jednostka_in)
    
    
elif jednostka_in == "in" or "ft" or "yd" or "mi":
    system_in = "imperial"
    wartosc_mila = imperial(na_mile = wartosc_in, mila = jednostka_in)


#określenie systemu out
if jednostka_out == "mm" or "cm" or "m" or "km":
    system_out = "metric"
    
elif jednostka_out == "in" or "ft" or "yd" or "mi":
    system_out = "imperial"


#porównanie systemów, wybór straregii konwersji
if system_in == system_out == "metric":
    wynik = metr_conversion(future_metric = jednostka_in, future_metric_value = wartosc_metr)




elif system_in == system_out == "imperial":
    wynik = imperial_conversion(future_imperial = jednostka_in, future_imperial_value = wartosc_mila)




elif system_in == "metric" and system_out == "imperial":
    wartosc_imperial = metric_to_imperial(in_metric = wartosc_metr)
    wynik = imperial(mila = "mi", na_mile = wartosc_imperial)





elif system_in == "imperial" and system_out == "metric":
    out_metric = imperial_to_metric(in_imperial = wartosc_mila)
    wynik = metr_conversion(future_metric = "m", future_metric_value = out_metric)




    
print(wynik, jednostka_out)