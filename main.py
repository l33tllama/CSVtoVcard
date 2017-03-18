import csv, vobject

filename = "contacts.CSV"
delimiter=","

# array get - return empty string if None
def ag(a, i):
    if a[i] == None:
        return ""
    else:
        return a[i]

def create_vcard(c):
    print c

    # field index
    fi = 0

    # Name ( Title, First, Middle, Last, Suffix)
    name = [None] * 5
    for i in range(0, 5):
        if c[fi + i] is not None and len(c[fi + i]) > 0:
            name[i] = c[i + fi]

    # Organisaion/business ( company, department, job title)
    fi += 5 # fi = 5
    org = [None] * 4
    for i in range(0, 3):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            org[i] = c[i + fi]

    # Work address (street, street2, street3, city, state, postcode, country)
    fi += 3 # fi = 8
    work_addr = [None] * 7
    for i in range(0, 7):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            work_addr[i] = c[i + fi]

    # Home address (street, street2, street3, city, state, postcode, country)
    fi += 7 # fi = 15
    home_addr = [None] * 7
    for i in range(0, 7):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            home_addr[i] = c[i + fi]

    # Other address
    fi += 7 # fi = 22
    other_addr = [None] * 7
    for i in range(0, 7):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            other_addr[i] = c[i + fi]

    fi += 7 # fi = 29

    # Assistant's phone (ignore)
    fi += 1 # fi = 30

    # Business fax, phone, phone 2
    work_ph = [None] * 3
    for i in range(0, 3):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            work_ph[i] = c[i + fi]
    fi += 3 # fi = 33

    # Callback, car phone, company main phone (ignore)
    fi += 3 # fi = 36

    # Home fax, phone, phone 2
    home_ph = [None] * 3
    for i in range(0, 3):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            home_ph[i] = c[i + fi]
    fi += 3 # fi = 39

    # ISDN? skip
    fi +=1 # fi = 40

    # Mobile phone (one index)
    mobile = [None]
    if c[fi] is not None and len(c[fi]) > 0:
        mobile  = c[fi]
    fi += 1 # fi = 41

    #Other fax*2, pager (skip)
    fi += 2 # fi = 44

    # Primary phone
    primary_ph = [None]
    if c[fi] is not None and len(c[fi]) > 0:
        primary_ph  = c[fi]
    fi += 1 # fi = 45

    # radio phone, TTY/TDD, Telex, Account, Anniversary, Assistant's name, billing info (skip)
    fi += 7 # fi = 52

    # Birthday
    birthday = [None]
    if c[fi] is not None and len(c[fi]) > 0:
        birthday = c[fi]
    fi += 1 # fi = 53

    #Business PO box, categories, children, directory server (skip)
    fi += 4 # fi = 57

    #Email address, type, display name
    email1 = [None] * 3
    for i in range(0, 3):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            email1[i] = c[i + fi]
    fi += 3 # fi = 60

    #Email 2
    email2 = [None] * 3
    for i in range(0, 3):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            email2[i] = c[i + fi]
    fi += 3  # fi = 63

    # Email 3
    email3 = [None] * 3
    for i in range(0, 3):
        if c[i + fi] is not None and len(c[i + fi]) > 0:
            email3[i] = c[i + fi]
    fi += 3  # fi = 66

    # Gender
    gender = [None]
    if c[fi] is not None and len(c[fi]) > 0:
        gender = c[fi]
    fi += 1 # fi = 67

    # gov ID number, hobby (skip)
    fi += 2 # fi = 69

    # Home PO box
    home_pobox = [None]
    if c[fi] is not None and len(c[fi]) > 0:
        home_pobox = c[fi]
    fi += 1 # fi = 70

    # Initials
    initials = [None]
    if c[fi] is not None and len(c[fi]) > 0:
        initials = c[fi]
    fi += 1 # fi = 71

    # Internet free busy, keywords, language, location, managers name, mileage (skip)
    fi += 6 # fi = 77

    # Notes
    notes = [None]
    if c[fi] is not None and len(c[fi]) > 0:
        notes = c[fi]
    fi += 1 # fi = 78

    # Office loc, org ID number, other pO box, priority, private, referred by, sensetivity, spouse, user 1, user 2, user 3, user 4 (skip)
    fi += 12 # fi = 80

    # Web page
    webpage = [None]
    if c[fi] is not None and len(c[fi]) > 0:
        webpage = c[fi]

    all_info = [name, org, work_addr, home_addr,
                    other_addr, work_ph, home_ph, mobile, primary_ph, birthday,
                    email1, email2, email3, gender, home_pobox, initials, notes, webpage]

    print(all_info)



    #print(name)


def convert_to_vcard(csv_filename):

    rows = []
    with open(csv_filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
        row_index = 0
        # Each row
        for row in reader:

            # Get the column names
            column_index = 0
            if row_index == 0:
                name_index = 0
                for name in row:
                    print str(name_index) + " " + name
                    rows.append(name.replace("\"", ""))
                    name_index += 1

            # Start reading contacts per row
            else:
                #print
                #print "NEW CONTACT: ---------"
                # see https://en.wikipedia.org/wiki/VCard and https://github.com/eventable/vobject

                contact_details = [None] * len(rows)
                contact_col_i = 0

                # For each contact's detail column values
                for column in row:
                    j = vobject.vCard()
                    col_no_qt = column.replace("\"", "")
                    #print ( rows[contact_col_i] + ": " + col_no_qt)

                    # Add to contacts array
                    contact_details[contact_col_i] = col_no_qt

                    contact_col_i += 1
                #print "END NEW CONTACT"

                create_vcard(contact_details)
            row_index += 1
    pass

if __name__ == "__main__":
    convert_to_vcard(filename)