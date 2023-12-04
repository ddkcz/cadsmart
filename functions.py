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


def BaseValueImperial(UnitImperial_mi, ValueImperial_mi):
    match UnitImperial_mi:
        case "in":
            valueMILE = ValueImperial_mi / 63360
        case "ft":
            valueMILE = ValueImperial_mi / 5280
        case "yd":
            valueMILE = ValueImperial_mi / 1760
        case "fur":
            valueMILE = ValueImperial_mi / 5280
        case "mi":
            valueMILE = ValueImperial_mi
    
    return valueMILE

def UnitMetricConversion(valueConvMetric, unitConvMetric):  

    match unitConvMetric:
        case "mm":
            valueMet = valueConvMetric * 1000
        case "cm":
            valueMet = valueConvMetric * 100
        case "dm":
            valueMet = valueConvMetric * 10
        case "m":
            pass
        case "km":
            valueMet = valueConvMetric / 1000 

    return valueMet
    
def UnitImperialConversion(valueConvImperial, unitConvImperial):    
     
    match unitConvImperial:
        case "in":
            valueImp = valueConvImperial * 63360
        case "ft":
            valueImp = valueConvImperial * 5280
        case "yd":
            valueImp = valueConvImperial * 1760
        case "fur":
            valueImp = valueConvImperial * 0.000189393939
        case "mi":
            valueImp = valueConvImperial

    return valueImp

def InImperial_OutMetric(in_imperial):
    out_metric = in_imperial / 0.000621371
    return out_metric

def InMetric_OutImperial(in_metric):
    out_imperial = in_metric / 1609.344
    return out_imperial

###########################################################
#####                            input_area

def data_gathering():
    com = "Podaj długość wraz z jednostką w formacie \n metrycznym:\n mm, cm, dm, m, km:\n lub imperialnym:\n in, ft, yd, fur, mi \n >>"
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
    

    if Unit_in in ["mm", "cm", "m", "dm", "km"]:
        system_in = "metric"
        valueMID = BaseValueMetric(ValueMetric_m = Value_in, UnitMetric_m = Unit_in)
        
    elif Unit_in in ["in", "ft", "yd", "mi"]:
        system_in = "imperial"
        valueMID = BaseValueImperial(ValueImperial_mi = Value_in, UnitImperial_mi = Unit_in)
        
    if Unit_out in ["mm", "cm", "m", "dm", "km"]:
        system_out = "metric"

    elif Unit_out in ["in", "ft", "yd", "mi"]:
        system_out = "imperial"

    return valueMID, system_in, system_out

def converter_strategy(Value_in, Unit_out, system_in, system_out):
    if system_in == "metric" and system_out == "metric":
        valueOUT = UnitMetricConversion(valueConvMetric = Value_in, unitConvMetric = Unit_out)

    elif system_in == "imperial" and system_out == "imperial":
        valueOUT = UnitImperialConversion(valueConvImperial = Value_in, unitConvImperial = Unit_out)
    
    elif system_in == "metric" and system_out == "imperial":
        valueALMOST = InMetric_OutImperial(in_metric = Value_in)
        valueOUT = UnitImperialConversion(valueConvImperial = valueALMOST, unitConvImperial = Unit_out)

    elif system_in == "imperial" and system_out == "metric":
        valueALMOST = InImperial_OutMetric(in_imperial = Value_in)
        valueOUT = UnitMetricConversion(valueConvMetric = valueALMOST, unitConvMetric = Unit_out)

    return valueOUT


valueMID, systemIN, systemOUT = system_determining(Value_in = valueIN, Unit_in = unitIN, Unit_out = unitOUT)
print(systemIN, systemOUT)
valueFINAL = converter_strategy(Value_in = valueMID, Unit_out = unitOUT, system_in = systemIN, system_out = systemOUT)


###########################################################
#####                            output_area

print(valueFINAL, unitOUT)
