#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import xlrd

from raffle.models import Raffle


def handle_uploaded_file(request, f):

    raffle = Raffle()


    book = xlrd.open_workbook(file_contents=f.read())
    for sheet in book.sheets():
        number_of_rows = sheet.nrows

        for row in range(1, number_of_rows):
            # do something with your rows
            pass