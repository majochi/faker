from __future__ import unicode_literals
from ..address import Provider as AddressProvider
from .city import names as city_names
import random
import re
with_space_or_dash_character = re.compile('\s|-')

class Provider(AddressProvider):
    city_prefixes = ('anna',)
    city_suffixes = ('bach', 'berg', 'kirchen', 'thal', 'tal')
    building_number_formats = ('#####', '####', '###')
    street_suffixes = ('Allee', 'Gasse', 'Höhe', 'Platz', 'Ring', 'Strasse', 'Straße', 'Weg')
    postcode_formats = ('#####',)
    states = (
        'Baden-Württemberg', 'Bayern', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hessen', 'Mecklenburg-Vorpommern',
        'Niedersachsen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Saarland', 'Sachsen', 'Sachsen-Anhalt',
        'Schleswig-Holstein', 'Thüringen',
    )

    states_abbr = ('BW', 'BY', 'BE', 'BB', 'HB', 'HH', 'HE', 'MV', 'NI', 'NW', 'RP', 'SL', 'SN', 'ST', 'SH', 'TH',)

    countries = (
        'Afghanistan', 'Ägypten', 'Albanien', 'Algerien', 'Andorra', 'Angola', 'Antigua', 'Äquatorialguinea',
        'Argentinien', 'Armenien', 'Aserbaidschan', 'Äthiopien', 'Australien', 'Bahamas', 'Bahrain', 'Bangladesch',
        'Barbados', 'Belarus', 'Belgien', 'Belize', 'Benin', 'Bhutan', 'Bolivien', 'Bosnien', 'Botsuana', 'Brasilien',
        'Brunei', 'Bulgarien', 'Burkina', 'Burundi', 'Chile', 'China', 'Cookinseln', 'Costa', 'Côte', 'Dänemark',
        'Deutschland', 'Dominica', 'Dominikanische', 'Dschibuti', 'Ecuador', 'El', 'Eritrea', 'Estland', 'Fidschi',
        'Finnland', 'Frankreich', 'Gabun', 'Gambia', 'Georgien', 'Ghana', 'Grenada', 'Griechenland', 'Großbritannien',
        'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Indien', 'Indonesien', 'Irak', 'Iran',
        'Irland', 'Island', 'Israel', 'Italien', 'Jamaika', 'Japan', 'Jemen', 'Jordanien', 'Kambodscha', 'Kamerun',
        'Kanada', 'Kap', 'Kasachstan', 'Katar', 'Kenia', 'Kirgisistan', 'Kiribati', 'Kolumbien', 'Komoren', 'Kongo',
        'Kongo,', 'Korea,', 'Korea,', 'Kosovo', 'Kroatien', 'Kuba', 'Kuwait', 'Laos', 'Lesotho', 'Lettland', 'Libanon',
        'Liberia', 'Libyen', 'Liechtenstein', 'Litauen', 'Luxemburg', 'Madagaskar', 'Malawi', 'Malaysia', 'Malediven',
        'Mali', 'Malta', 'Marokko', 'Marshallinseln', 'Mauretanien', 'Mauritius', 'Mazedonien', 'Mexiko', 'Mikronesien',
        'Moldau', 'Monaco', 'Mongolei', 'Montenegro', 'Mosambik', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Neuseeland',
        'Nicaragua', 'Niederlande', 'Niger', 'Nigeria', 'Norwegen', 'Oman', 'Österreich', 'Pakistan', 'Palau', 'Panama',
        'Papua-Neuguinea', 'Paraguay', 'Peru', 'Philippinen', 'Polen', 'Portugal', 'Ruanda', 'Rumänien', 'Russische',
        'Salomonen', 'Sambia', 'Samoa', 'San', 'São', 'Saudi-Arabien', 'Schweden', 'Schweiz', 'Senegal', 'Serbien',
        'Seychellen', 'Sierra', 'Simbabwe', 'Singapur', 'Slowakei', 'Slowenien', 'Somalia', 'Spanien', 'Sri', 'St.',
        'St.', 'St.', 'Südafrika', 'Sudan', 'Südsudan', 'Suriname', 'Swasiland', 'Syrien', 'Tadschikistan', 'Taiwan',
        'Tansania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad', 'Tschad', 'Tschechische', 'Tunesien',
        'Türkei', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'Ungarn', 'Uruguay', 'Usbekistan', 'Vanuatu',
        'Vatikanstadt', 'Venezuela', 'Vereinigte', 'Vereinigte', 'Vietnam', 'Zentralafrikanische', 'Zypern',
    )

    city_formats = (
        '{{city_prefix}}{{city_suffix}}',
    )
    street_name_formats = (
        '{{first_name}} {{street_suffix}}',
        '{{last_name}} {{street_suffix}}',
        '{{first_name}} {{last_name}} {{street_suffix}}',
        '{{first_name}} {{street_suffix}}',
        '{{first_name}}-{{last_name}}-{{street_suffix}}',
        '{{last_name}}-{{street_suffix}}',
        '{{first_name}}-{{street_suffix}}',
        '{{first_name}}{{street_suffix}}',
        '{{last_name}}{{street_suffix}}',
    )
    street_address_formats = (
        '{{street_name}}',
#        '{{street_name}} {{secondary_address}}',
    )
    address_formats = (
        "{{street_address}}\n{{postcode}} {{city}}",
    )
    secondary_address_formats = ('Whg. ###',)

    @classmethod
    def city_prefix(cls):
        return cls.random_element(cls.city_prefixes)

    @classmethod
    def city_suffix(cls):
        return cls.random_element(cls.city_suffixes)

    @classmethod
    def secondary_address(cls):
        return cls.numerify(cls.random_element(cls.secondary_address_formats))

    @classmethod
    def state(cls):
        return cls.random_element(cls.states)

    @classmethod
    def state_abbr(cls):
        return cls.random_element(cls.states_abbr)

    def city(self):
        r = random.randint(1, 20)
        if r > 1:
            return self.random_element(city_names)
        else:
            return super(Provider, self).city().capitalize()

    def street_name(self):
        name = super(Provider, self).street_name()
        if with_space_or_dash_character.search(name):
            return name
        else:
            return name.lower().capitalize()
