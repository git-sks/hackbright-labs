############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 1988, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')

    cas = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    cas.add_pairing('strawberries')
    cas.add_pairing('mint')

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('prosciutto')

    yw = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yw.add_pairing('ice cream')

    all_melon_types.extend([musk, cas, cren, yw])

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon_type in melon_types:
        # Print header part of pairing for one melon type
        print(f"{melon_type.name} pairs with")

        # Go through all the pairings the melon type has and print one per line
        for pairing in melon_type.pairings:
            print(f"- {pairing}")

        # Add a line break between different melon types
        print()


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_type_lookup = {}

    for melon_type in melon_types:
        melon_type_lookup[melon_type.code] = melon_type

    return melon_type_lookup


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

    def __init__(self, melon_type, shape_rating, color_rating,
                harvest_location, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_location = harvest_location
        self.harvested_by = harvested_by

    def is_sellable(self):
        """Check whether melon meets conditions and return True or False
        based on the check.

        Current conditions are:
        - shape rating greater than 5
        - color rating greater than 5
        - harvest location NOT from field 3"""

        good_shape = self.shape_rating > 5
        good_color = self.color_rating > 5
        unpoisoned = not self.harvest_location == 3

        if good_shape and good_color and unpoisoned:
            return True
        
        return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    melons.extend([melon_1, melon_2, melon_3, melon_4, melon_5,
        melon_6, melon_7, melon_8, melon_9])

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
    # Go through each melon
    for melon in melons:
        harvester = melon.harvested_by
        field = f"Field {str(melon.harvest_location)}"

        # By default, assume not sellable
        sellability = "NOT SELLABLE"

        # If melon is in fact sellable, update sellability message
        if melon.is_sellable():
            sellability = "CAN BE SOLD"

        # Put together the sellability report for a single melon
        print(f"Harvested by {harvester} from {field} ({sellability})")



