# coding=utf8
from __future__ import unicode_literals
from ..person import Provider as PersonProvider
from .male import names as male_names
from.female import names as female_names
from .last import names as last_names

class Provider(PersonProvider):
    formats = (
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}}',
        '{{first_name}} {{last_name}} {{suffix}}',
        '{{prefix}} {{first_name}} {{last_name}}',
        '{{prefix}} {{first_name}} {{last_name}}',
        '{{prefix}} {{first_name}} {{last_name}} {{suffix}}',
    )

    first_names = male_names + female_names

    last_names = last_names

    prefixes = (
        'Prof.', 'Dr. med.', 'Dr. med.', 'Dr.', 'Dr.', 'Dr.', 'Dipl.-Ing.', 'Dipl.-Ing.', 'Dipl.-Ing.',
        'Dr. hc.', 'PD',
    )

    suffixes = (
        'MdB', 'MdL', 'MdEP', 'MdA', 'MdHB', 'StB', 'WP', 'RA', 'FA',
    )

    @classmethod
    def prefix(cls):
        return cls.random_element(cls.prefixes)

    @classmethod
    def suffix(cls):
        return cls.random_element(cls.suffixes)
