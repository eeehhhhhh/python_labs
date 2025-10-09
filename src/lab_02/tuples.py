def format_record(rec):
    fio = rec[0]
    group = rec[1]
    gpa = rec[2]
    
    if fio == "" or group == "":
        return 'ValueError'
    
    if not isinstance(gpa, (int, float)):
        return 'TypeError'
    
    fio_parts = fio.split()
    clean_parts = []
    for p in fio_parts:
        if p != "":
            clean_parts.append(p.strip())
    
    if len(clean_parts) == 3:
        initials = clean_parts[1][0].upper() + "." + clean_parts[2][0].upper() + "."
    elif len(clean_parts) == 2:
        initials = clean_parts[1][0].upper() + "."
    else:
        return 'ValueError'
    
    gpa_str = str(round(gpa, 2))
    if "." in gpa_str:
        parts = gpa_str.split(".")
        if len(parts[1]) == 1:
            gpa_str = gpa_str + "0"
    else:
        gpa_str = gpa_str + ".00"

    surname = clean_parts[0].capitalize()
    
    result = surname + " " + initials + ", гр. " + group + ", GPA " + gpa_str
    return result

print('format_record')
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("", "BIVT-25", 4.0)))  # пустое фио
