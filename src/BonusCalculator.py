class BonusCalculator(object):
    @staticmethod
    def calculate_bonus(sales, quota, commission_pct, tax_pct):
        if tax_pct > 100 or tax_pct < 0:
            raise InvalidTaxException()
        if commission_pct > 100 or commission_pct < 0:
            raise InvalidCommissionException()
        if sales > quota:
            return (sales-quota) * commission_pct / 100 * (100 - tax_pct) / 100
        return 0

    @staticmethod
    def calculate_team_bonus(sales, quota, commission_pct, team_members):
        if commission_pct > 100 or commission_pct < 0:
            raise InvalidCommissionException
        if team_members <= 0:
            raise NoTeamMembersException()
        if sales > quota:
            return (sales - quota)*commission_pct/100/team_members
        return 0


class InvalidTaxException(Exception):
    pass


class InvalidCommissionException(Exception):
    pass


class NoTeamMembersException(Exception):
    pass