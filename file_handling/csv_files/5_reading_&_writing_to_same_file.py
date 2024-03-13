"""
In the below program we are interacting with the invoices.csv file. The file contains 3
columns of data each row. The invoice number, company and amount. The invoice number has 8
digits separated by a '-' character. The first four digits correspond to the year and the
next four digits correspond to the invoice number. While adding an invoice details to the file
we first need to check the last invoice number(i.e the year and the number) and then
generate the next invoice number in sequence. The below code precisely does that. Please
refer to the below code. We will cover descriptions of different code fragments as we go.
"""

import datetime
from os import SEEK_SET
from typing import TextIO


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


"""
The above function uses the methods in the datetime module of python. It gives use the 
current year details. In the context of our program this will be useful to autogenerate the 
invoice number whose first 4 digits is the year.
"""


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year, number = invoice_number.split('-')
    return int(year), int(number)


"""
The above function parse_invoice_number receives an invoice number as a parameter argument 
and extracts the year and number using the split method. Then it returns both values. In the
context of the program this function will be used to extract the year and the number which 
will then be used to generate the next invoice number.
"""


def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    invoice_year, number = parse_invoice_number(invoice_number)
    year = get_year()
    if year == invoice_year:
        number += 1
    else:
        invoice_year = year
        number = 1
    new_invoice_number = f"{invoice_year}-{number:04d}"
    return new_invoice_number


"""
The above function takes an invoice number and generates the next invoice number in the series.
If the last invoice number in the csv file was generated in the same year, then it only 
increments the number and not the year. If the year in the last invoice number does not 
match the current year then the new invoice number should start from the current year. Also 
the number on the  last 4 digits should be set to 0001.
"""


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,
                   last_line_ptr: int = 0) -> int:
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    :param last_line_ptr: The position of the start of the last line
        in the file. This will be obtained from the previous call to
        record_invoice.
    :return: The position of the  start of the last line of the file.
        This can be used in the subsequent calls to record_invoice.
    """
    invoice_file.seek(last_line_ptr, SEEK_SET)
    last_row = ""
    for line in invoice_file:
        last_row = line
    if last_row:
        invoice_number = last_row.split("\t")[0]
        new_invoice_number = next_invoice_number(invoice_number)
    else:
        # if the file is empty we will start numbering from 1.
        year = get_year()
        new_invoice_number = f"{year}-{1:04d}"

    last_line_ptr = invoice_file.tell()
    print(f"{new_invoice_number}\t{company}\t{amount}", file=invoice_file)
    return last_line_ptr


"""
The above function accepts values that are to be added to the csv file and writes the 
corresponding data to the csv file. Of all the arguments in this function 2 are important.
First the invoice_file argument takes a file parameter. The file should already be open in 
both read and write mode.
Second is the last_line_ptr argument which is set to 0 by default. This argument keeps track
of the position of the last line in the file. It is important because subsequent calls to the
function can lead to generating incorrect invoice numbers that will then be added to the file.
It is important that the invoice number in the last line of the file is referred in order to
generate a new one.
This can be done using the seek() and tell() methods. In line 110 we use the tell() method. 
It is important to note that the tell() method in the context of this program is being used 
only after the preceding code moves the pointer to the last line of the file. Hence, 
the tell() method at line 110 will give us the last line pointer value.
In the line 98 we are using the seek() method which we have previously used. However, 
here we are sending a second argument SEEK_SET. The first argument is the last_line_ptr. 
What our code basically tells python is to set the pointer at the last_line_ptr value from 
the beginning of the file. SEEK_SET refers to the beginning of the file. There are also 
SEEK_CUR and SEEK_END which refer to the current position and the end of the file.
"""


data_file = "invoices.csv"
with open(data_file, "r+", encoding="utf-8") as invoices:
    last_line = record_invoice(invoices, "ACME RoadRunner", 18.40)
    last_line = record_invoice(invoices, "Squirrel Storage", 320.55, last_line)


"""
The above code fragment is easy to understand. We are opening a csv file like we normally 
do. The only difference is the file mode specified in the argument of open() function is "r+".
We know that "r" refers to read mode and "w" refers to write mode. When we specify the file 
mode as "r+" or "w+" it means that we want the file opened in both read and write mode. In 
the context of this program we use "r+" as the file mode. The reason being that when we open
file with "w+" mode, although the file is opened in both read and write mode, still it gets 
truncated everytime it get opened. This is just like "w" mode. In order to avoid that we use
the "r+" mode.
"""