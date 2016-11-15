#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import string

import xlrd
from django.contrib.auth.models import User


def random_string(length):
    pool = string.letters + string.digits
    return ''.join(random.choice(pool) for i in xrange(length))


def handle_uploaded_file(request, f, raffle):
    book = xlrd.open_workbook(file_contents=f.read())
    for sheet in book.sheets():
        number_of_rows = sheet.nrows

        for row in range(1, number_of_rows):
            # do something with your rows
            first_name = sheet.cell(row, 0).value

            user = User(first_name=first_name, username=random_string(20))
            user.save()
            raffle.users.add(user)
            raffle.save()
