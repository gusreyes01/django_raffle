from django.utils.translation import ugettext


def general_report(worksheet_s, users, header_dict, date_format,report_header, results):

    # REPORTE
    ##########################################################################
    ##########################################################################
    ##########################################################################

    # write title
    title_text = u"{0} {1}".format(report_header, "")
    # merge header_dict['cell']s
    worksheet_s.merge_range('B2:I2', title_text, header_dict['title'])

    # column widths
    town_col_width = 10
    description_col_width = 10
    observations_col_width = 25

    # change column widths
    worksheet_s.set_column('A:A', 20)  # column
    worksheet_s.set_column('B:B', 20)  # column
    idx = 1

    for user, result in zip(users, results):
        row = 5 + idx
        worksheet_s.write(row, 0, user.first_name, header_dict['cell'])
        worksheet_s.write(row, 1, result, header_dict['cell'])
        idx += 1
