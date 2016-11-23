#!/usr/bin/python
# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter

from excel_reports import general_report



def WriteToExcel(data, request):

    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)

    date_format = workbook.add_format(
        {'num_format': 'dd-mmm-yyyy', 'border': 1})

    header_dict = {}
    # excel styles
    header_dict['title'] = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })

    header_dict['cell'] = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })

    # GENERAL REPORT
    report_header = "RESULTADOS"
    worksheet_s = workbook.add_worksheet("RESULTADOS")
    results = data.results.split(',')

    general_report(worksheet_s, data.users.all(),
                   header_dict, date_format, report_header, results)

    # close workbook
    workbook.close()
    xlsx_data = output.getvalue()
    return xlsx_data
