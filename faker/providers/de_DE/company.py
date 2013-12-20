# coding=utf8
from __future__ import unicode_literals
from ..company import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{last_name}} {{company_suffix}}', '{{last_name}} {{company_suffix}}', '{{last_name}} {{company_suffix}}',
        '{{last_name}} & {{last_name}}',
        '{{last_name}}, {{last_name}} {{company_suffix}}',
        '{{last_name}}, {{last_name}}, {{last_name}}'
    )

    catch_phrase_words = (
        (
            'Große', 'Schöne', 'Schwarze', 'Weiße', 'Bunte',
        ),
        (
            'Dinge', 'Teile', 'Fenster', 'Autos', 'Computer', 'IT-Systeme',
        ),
        (
            'einfach', 'schnell',
        )
    )

    bsWords = (
        (
            'implement', 'utilize', 'integrate', 'streamline', 'optimize', 'evolve', 'transform', 'embrace', 'enable',
            'orchestrate', 'leverage', 'reinvent', 'aggregate', 'architect', 'enhance', 'incentivize', 'morph',
            'empower', 'envisioneer', 'monetize', 'harness', 'facilitate', 'seize', 'disintermediate', 'synergize',
            'strategize', 'deploy', 'brand', 'grow', 'target', 'syndicate', 'synthesize', 'deliver', 'mesh', 'incubate',
            'engage', 'maximize', 'benchmark', 'expedite', 'reintermediate', 'whiteboard', 'visualize', 'repurpose',
            'innovate', 'scale', 'unleash', 'drive', 'extend', 'engineer', 'revolutionize', 'generate', 'exploit',
            'transition', 'e-enable', 'iterate', 'cultivate', 'matrix', 'productize', 'redefine', 'recontextualize'
        ),
        (
            'clicks-and-mortar', 'value-added', 'vertical', 'proactive', 'robust', 'revolutionary', 'scalable',
            'leading-edge', 'innovative', 'intuitive', 'strategic', 'e-business', 'mission-critical', 'sticky',
            'one-to-one', '24/7', 'end-to-end', 'global', 'B2B', 'B2C', 'granular', 'frictionless', 'virtual', 'viral',
            'dynamic', '24/365', 'best-of-breed', 'killer', 'magnetic', 'bleeding-edge', 'web-enabled', 'interactive',
            'dot-com', 'sexy', 'back-end', 'real-time', 'efficient', 'front-end', 'distributed', 'seamless',
            'extensible', 'turn-key', 'world-class', 'open-source', 'cross-platform', 'cross-media', 'synergistic',
            'bricks-and-clicks', 'out-of-the-box', 'enterprise', 'integrated', 'impactful', 'wireless', 'transparent',
            'next-generation', 'cutting-edge', 'user-centric', 'visionary', 'customized', 'ubiquitous', 'plug-and-play',
            'collaborative', 'compelling', 'holistic', 'rich'
        ),
        (
            'synergies', 'web-readiness', 'paradigms', 'markets', 'partnerships', 'infrastructures', 'platforms',
            'initiatives', 'channels', 'eyeballs', 'communities', 'ROI', 'solutions', 'e-tailers', 'e-services',
            'action-items', 'portals', 'niches', 'technologies', 'content', 'vortals', 'supply-chains', 'convergence',
            'relationships', 'architectures', 'interfaces', 'e-markets', 'e-commerce', 'systems', 'bandwidth',
            'infomediaries', 'models', 'mindshare', 'deliverables', 'users', 'schemas', 'networks', 'applications',
            'metrics', 'e-business', 'functionalities', 'experiences', 'webservices', 'methodologies'
        )
    )

    company_suffixes = (
        'AG', 'gAG', 'AG & Co. KG', 'AG & Co. KGaA', 'eG', 'e.K.', 'e.V.', 'GbR', 'GbRmbH', 'GmbH', 'gGmbH',
        'GmbH & Co. KG', 'GmbH Co. KGaA', 'GmbH Co. OHG', 'InvAG', 'KG', 'KGaA', 'Limited & Co. KG', 'OHG',
        'Partenreederei', 'PartG', 'PartG mbB', 'G-REIT', 'Stiftung', 'Stiftung & Co. KG', 'Stiftung & Co. KGaA',
        'Stiftung GmbH & Co. KG', 'Stille Gesellschaft', 'UG (haftungsbeschränkt)', 'UG (haftungsbeschränkt) & Co. KG',
        'VVaG', 'EWIV', 'SCE', 'SE', 'SPE', '& Söhne', '& Sohn', '& Partner',
    )

    def catch_phrase(self):
        """
        :example 'Robust full-range hub'
        """
        result = []
        for word_list in self.catch_phrase_words:
            result.append(self.random_element(word_list))

        return " ".join(result)

    def bs(self):
        """
        :example 'integrate extensible convergence'
        """
        result = []
        for word_list in self.bsWords:
            result.append(self.random_element(word_list))

        return " ".join(result)
