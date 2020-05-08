"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = ""
        self.tax = 0


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        # Adjust price if christmas melon, which is 1.5 times other melons
        if self.species == "christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact that an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize domestic melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize international melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17


    def get_total(self):
        """Calculate price, including tax and fees."""

        # Get the total of the order without the fees
        total = super().get_total()

        # Check if order quantity is under 10 melons. If so, add flat fee.
        if self.qty < 10:
            total = total + 3

        return total


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the government."""

    def __init__(self, species, qty):
        """Initialize government melon order attributes."""

        super().__init__(species, qty)
        self.order_type = "government"
        self.passed_inspection = False
        # Explicit setting of tax to 0, in case it may change in future
        self.tax = 0


    def mark_inspection(self, passed):
        """Update the order inspection status based on the argument."""

        self.passed_inspection = passed