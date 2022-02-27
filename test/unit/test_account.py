from unittest import TestCase

from packages.server.easepayment.src.domain import Account
from packages.server.easepayment.src.domain.entityprops.AccountProps import AccountProps

class TestAccount(TestCase):

    def test_account(self):

        account = Account.create(AccountProps(
            password="1234",
            username="Ag"
        ))

        print(str(account.props.password))
        current_hash = str(b'abe3999258cb47216e21538556655a3e8c5cbcb3')
        comparision_result = Account.compare(current_hash, account.props.password)
        print(comparision_result)

        self.assertTrue(comparision_result)