import re


class Phone:
    @staticmethod
    def is_valid(phone: str):
        """Returns true if the phone number is valid"""

        expretion = r"/^(?:(\+244|00244))?(9)(1|2|3|4|9)([\d]{7,7})$/ix"

        return True if re.search(expretion, phone) is not None else False
