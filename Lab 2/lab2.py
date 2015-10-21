q = float(input("Enter the quantity: "))
start_unit = input("Enter the starting unit: ")
final_unit = input("Enter the final unit: ")

if start_unit == "tera":
	q = q * 1000000000000
elif start_unit == "giga":
	q = q * 1000000000
elif start_unit == "mega":
	q = q * 1000000
elif start_unit == "kilo":
	q = q * 1000
elif start_unit == "hecto":
	q = q * 100
elif start_unit == "none":
	q = q
elif start_unit == "deci":
	q = q * 0.1
elif start_unit == "centi":
	q = q * 0.01
elif start_unit == "milli":
	q = q * 0.001
elif start_unit == "micro":
	q = q * 0.000001
elif start_unit == "nano":
	q = q * 0.000000001
elif start_unit == "pico":
	q = q * 0.000000000001

#at this point we have converted q values

if final_unit == "tera":
	q = q / 1000000000000
elif final_unit == "giga":
	q = q / 1000000000
elif final_unit == "mega":
	q = q / 1000000
elif final_unit == "kilo":
	q = q / 1000
elif final_unit == "hecto":
	q = q / 100
elif final_unit == "none":
	q = q
elif final_unit == "deci":
	q = q / 0.1
elif final_unit == "centi":
	q = q / 0.01
elif final_unit == "milli":
	q = q / 0.001
elif final_unit == "micro":
	q = q / 0.000001
elif final_unit == "nano":
	q = q / 0.000000001
elif final_unit == "pico":
	q = q / 0.000000000001


print(q)