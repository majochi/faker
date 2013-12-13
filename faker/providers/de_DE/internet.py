# coding=utf-8
from __future__ import unicode_literals
from ..internet import Provider as InternetProvider
import re

clean_company = re.compile('[,& .]+')

class Provider(InternetProvider):
    safe_email_tlds = ('com', 'net', 'de', 'de', 'de', 'de', 'de', 'de', 'info', 'biz', 'org')
    free_email_domains = (
        'arcor.de', 't-online.de', 'icloud.com', 'me.com', 'gmail.com', 'googlemail.com', 'hotmail.com', 'yahoo.com',
        'yahoo.de', 'web.de', 'gmx.de', 'gmx.net', 'mail.de', 'freenet.de', 'outlook.com'
    )
    tlds = ('com', 'net', 'de', 'de', 'de', 'de', 'de', 'de', 'info', 'biz', 'org')

    @staticmethod
    def _to_ascii(string):
        replacements = (
            ('é', 'e'), ('ä', 'ae'), ('ö', 'oe'), ('ü', 'ue'),
        )
        for search, replace in replacements:
            string = string.replace(search, replace)

        return string

    def user_name(self):
        pattern = self.random_element(self.user_name_formats)
        return self._to_ascii(self.bothify(self.generator.parse(pattern))).lower()

    def domain_word(self):
        company = clean_company.sub('-', self.generator.format('company'))
        return self._to_ascii(company).lower()
