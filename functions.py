###########################################################
#####                            def_area

#variables
def variables_definition():
    #   mm = milimeter
    #   cm = centimeter
    #   dm = decyieter
    #   m = meter
    #   km = kilometer
    #
    #   in = inch
    #   ft = foot
    #   yd = yard
    #   fur = furlong
    #   mi = #mil
    pass
    
def BaseValueMetric(ValueMetric_m, UnitMetric_m):
    match UnitMetric_m:
        case "mm":
            valueMETER = ValueMetric_m / 1000
        case "cm":
            valueMETER = ValueMetric_m / 100
        case "dm":
            valueMETER = ValueMetric_m / 10
        case "m":
            valueMETER = ValueMetric_m
        case "km":
            valueMETER = ValueMetric_m * 1000 
    return valueMETER


def BaseValueImperial(Unit_Imperial_mi, ValueImperial_mi):
    match Unit_Imperial_mi:
        case "in":
            valueMILE = ValueImperial_mi * 63360
        case "ft":
            valueMILE = ValueImperial_mi * 5.280
        case "yd":
            valueMILE = ValueImperial_mi * 1.760
        case "fur":
            valueMILE = ValueImperial_mi * 5.280
        case "mi":
            valueMILE = ValueImperial_mi
    
    return valueMILE

def UnitMetricConversion(future_Unit_Metric_mic, future_Unit_Metric_mic_value):  

    match future_Unit_Metric_mic_value:
        case "mm":
            future_Unit_Metric_mic = future_Unit_Metric_mic / 1000
        case "cm":
            future_Unit_Metric_mic = future_Unit_Metric_mic / 100
        case "dm":
            future_Unit_Metric_mic = future_Unit_Metric_mic / 10
        case "m":
            future_Unit_Metric_mic = future_Unit_Metric_mic
        case "km":
            future_Unit_Metric_micr = future_Unit_Metric_mic * 1000 

    return future_Unit_Metric_mic_value
    
def UnitImperialConversion(future_imperial, future_imperial_value):
     
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

def InImperial_OutMetric(in_imperial):
    out_Unit_Metric_mic = in_imperial * 0.000621371
    return out_Unit_Metric_mic

def InMetric_OutImperial(in_Unit_Metric_mic):
    out_imperial = in_Unit_Metric_mic / 1609.344
    return out_imperial

###########################################################
#####                            input_area

def data_gathering():
    com = "Podaj długość wraz z jednostką w formacie \n metrycznym:\n mm, cm, m, km:\n lub imperialnym:\n in, ft, yd, fur, mi \n >>"
    x = input(com)
    x = x.split(" ")
    return x
    
def inputdata(x):
    Value_in = x[0]
    Value_in = float(Value_in)
    Unit_in = x[1]
    Unit_out = input("Na co zamienić tą długość?\n Format metryczny??:\n mm, cm, m, km:\n Format imperialny??:\n in, ft, yd, fur, mi \n >>")
    return Value_in, Unit_in, Unit_out
    
def datacleaning():
    #CREATE DATA CLEANING
    pass

def try_except():
    #CREATE TRY EXCEPTS
    pass

clientANS = data_gathering()
valueIN, unitIN, unitOUT = inputdata(x = clientANS)
datacleaning()
try_except()

#OUT: valueIN, unitIN, unitOUT


###########################################################
#####                            execution_area

#determining the type of conversion, and creating stratefy for converter

def system_determining(Value_in, Unit_in, Unit_out):
    
    if Unit_in == "mm" or "cm" or "m" or "dm" or "km":
        system_in = "metric"
        valueMID = BaseValueMetric(ValueMetric_m = Value_in, UnitMetric_m = Unit_in)
    elif Unit_in == "in" or "ft" or "yd" or "mi":
        system_in = "imperial"
        valueMID = BaseValueImperial(ValueImperial_mi = Value_in, UnitImperial_mi = Unit_in)
        
    if Unit_out == "mm" or "cm" or "m" or "km":
        system_out = "metric"
    elif Unit_out == "in" or "ft" or "yd" or "mi":
        system_out = "imperial"

    return valueMID, system_in, system_out

def converter_strategy(system_in, system_out):
    if system_in == system_out == "metric":
        valueOUT = UnitMetricConversion(future_Unit_Metric_mic = value_m, future_Unit_Metric_mic_value= unitOUT)

    elif system_in == system_out == "imperial":
        valueOUT = UnitImperialConversion(future_imperial_value = valueOUT, future_imperial = unitOUT)
    
    elif system_in == "metric" and system_out == "imperial":
        pass

    elif system_in == "imperial" and system_out == "metric":
        pass

    return valueOUT

valueMID, systemIN, systemOUT = system_determining(Value_in = valueIN, Unit_in = unitIN, Unit_out = unitOUT)
valueFINAL = converter_strategy(system_in = systemIN, system_out = systemOUT)

###########################################################
#####                            output_area

print(valueFINAL, unitOUT)