import xlrd
import xlwt

plik_tnt = xlrd.open_workbook("01.xls")
strona_tnt = plik_tnt.sheet_by_index(0)
total_rows_tnt = strona_tnt.nrows

plik_klienci = xlrd.open_workbook("02.xls")
strona_klienci = plik_klienci.sheet_by_index(0)
total_rows_klienci = strona_klienci.nrows

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('Arkusz 1')


pozycja = 1

klienci = [strona_klienci.cell(licznik,0).value for licznik in range(total_rows_klienci)]

for klient in klienci:
    t = 0

    while t < total_rows_tnt:

        if klient >= strona_tnt.cell(t,0).value and klient <= strona_tnt.cell(t,1).value:
            sheet.write(pozycja,0,klient)
            workbook.save("rabat.xls")
            pozycja += 1
            t = total_rows_tnt
            
        else:
            t += 1
