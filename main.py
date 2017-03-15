import csv, vobject

filename = "contacts.CSV"
delimiter=","


def convert_to_vcard(csv_filename):

    rows = []
    with open(csv_filename, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter, quotechar="|")
        row_index = 0
        for row in reader:
            column_index = 0
            if row_index == 0:
                for name in row:
                    print name
                    rows.append(name.replace("\"", ""))

            else:
                print
                print "NEW CONTACT: ---------"
                # see https://en.wikipedia.org/wiki/VCard and https://github.com/eventable/vobject

                contact = {
                    "title": "", "first": "", "middle": "", "last": "",
                    "address":  "", "email": ""
                }

                for column in row:
                    j = vobject.vCard()

                    if len(column) > 2:
                        col_no_qt = column.replace("\"", "")
                        print ( rows[column_index] + ": " + col_no_qt)
                        if rows[column_index] == 'Title':
                            contact['title'] == col_no_qt
                        if rows[column_index] == 'First Name':
                            contact['first'] = col_no_qt
                        elif rows[column_index] == "Middle Name":
                            contact['middle'] = col_no_qt
                        elif rows[column_index] == "Last Name":
                            contact['last'] = col_no_qt
                    if len(name) > 0:
                        print "Name"
                        print(name)
                    column_index += 1
                print "END NEW CONTACT"
            row_index += 1
    pass

if __name__ == "__main__":
    convert_to_vcard(filename)