def format_record(rec):
    try:
        fio = rec[0]
        group = rec[1]
        gpa = rec[2]
        
        if fio == "" or group == "":
            raise(ValueError)
        
        if not isinstance(gpa, (int, float)):
            raise(TypeError)
        
        fio_parts = fio.split()
        fio_parts = [p.strip() for p in fio_parts]
        
        if len(fio_parts) == 3:
            initials = fio_parts[1][0].upper() + "." + fio_parts[2][0].upper() + "."
        elif len(fio_parts) == 2:
            initials = fio_parts[1][0].upper() + "."
        else:
            raise(ValueError)
        
        gpa_str = str(round(gpa, 2))
        if "." in gpa_str:
            parts = gpa_str.split(".")
            if len(parts[1]) == 1:
                gpa_str = gpa_str + "0" 
        else:
            gpa_str = gpa_str + ".00"
        
        surname = fio_parts[0].capitalize() 
        
        result = surname + " " + initials + ", гр. " + group + ", GPA " + gpa_str
        return result
    except Exception as err:
        return repr(err)

print('format_record')
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("", "BIVT-25", 4.0)))  # пустое фио
