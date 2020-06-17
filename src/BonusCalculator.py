class BonusCalculator(object):
    def calulate_bonus(self, sales, quota, commision_pct, tax_pct):
        if tax_pct > 100 or tax_pct < 0:
            raise InvalidTaxException()
        if commision_pct > 100 or commision_pct < 0:
            raise InvalidCommissionException()
        if sales > quota:
            return (sales-quota)*commision_pct/100*(100 - tax_pct)/100
        return 0


class InvalidTaxException(Exception):
    pass


class InvalidCommissionException(Exception):
    pass