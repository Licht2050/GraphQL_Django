# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['AuthorTestCase::testAllAuthors 1'] = {
    'data': {
        'allAuthors': [
            {
                'id': '1',
                'name': 'Max',
                'vorname': 'Muster'
            },
            {
                'id': '2',
                'name': 'Mueller',
                'vorname': 'Rabin'
            }
        ]
    }
}

snapshots['AuthorTestCase::testBookById 1'] = {
    'data': {
        'bookById': {
            'id': '1',
            'titel': 'C++ New Release'
        }
    }
}
