from __future__ import unicode_literals
from ..phone_number import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        '+49 (%##) %########',
        '+49 (%##) %#####-###',
        '+49 (%###) %#########',
        '+49 (%###) %######-###',
        '+49 (%####) %#########',
        '+49 (%####) %#####-####',
        '+49 %## %########',
        '+49 %## %#####-###',
        '+49 %### %#######',
        '+49 %### %####-###',
        '+49 %#### %#####',
        '+49 %#### %###-##',
        '0049 %## %#########',
        '0049 %## %######-###',
        '0049 %### %#########',
        '0049 %### %#####-####',
        '0049 %#### %#########',
        '0049 %#### %#####-####',
        '0%# %########',
        '0%# %#####-###',
        '0%## %#######',
        '0%## %####-###',
        '0%### %######',
        '0%### %####-##',
        '0%##########',
    )
