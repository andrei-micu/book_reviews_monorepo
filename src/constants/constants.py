from collections import namedtuple

Polarity = namedtuple('Polarity', ["NEGATIVE", "NEUTRAL", "POSITIVE"])
polarity = Polarity(NEGATIVE="NEGATIVE", NEUTRAL="NEUTRAL", POSITIVE="POSITIVE")