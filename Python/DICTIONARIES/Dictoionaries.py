# Key : Value pairs

month_conversions_dict = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"

}

print(month_conversions_dict["Feb"])
print(month_conversions_dict.get("Jan"))
print(month_conversions_dict.get("Apr", "Not a valid entry"))


print(len(month_conversions_dict))