import logging
import sys
import unittest

import getcheddar_utils

class TestGetCheddarUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.utils = getcheddar_utils.GetCheddarUtils()
        cls.maxDiff = None

        logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', 
                            datefmt='%Y%m%d-%H:%M:%S',
                            stream=sys.stdout,
                            level=logging.DEBUG)

                        

    def test_decode_webhook_new_subscription(self):
        data = {'activityActor': 'luc.wastiaux@xsmail.com',
        'activityDatetime': '2021-06-01T01:10:14+00:00',
        'activityType': 'newSubscription',
        'customer': {'campaignContent': '',
                    'campaignMedium': '',
                    'campaignName': '',
                    'campaignSource': '',
                    'campaignTerm': '',
                    'code': 'no1@spam.com',
                    'company': '',
                    'createdDatetime': '2021-06-01T01:10:13+00:00',
                    'email': 'languagetools+customer1@mailc.net',
                    'firstContactDatetime': '',
                    'firstName': 'Luc',
                    'gatewayToken': 'SIMULATED',
                    'id': '1e39d01a-c276-11eb-bed7-0eff6b8b8fd3',
                    'isTaxExempt': '0',
                    'key': 'd868455a94',
                    'lastName': 'Customer1',
                    'notes': '',
                    'referer': '',
                    'taxNumber': ''},
        'product': {'code': 'LANGUAGE_TOOLS',
                    'id': '53def3f0-bceb-11eb-bed7-0eff6b8b8fd3',
                    'name': 'Language Tools',
                    'subdomain': 'languagetools'},
        'subscription': {'cancelReason': '',
                        'cancelType': '',
                        'canceledDatetime': '',
                        'ccAddress': '',
                        'ccCity': '',
                        'ccCompany': '',
                        'ccCountry': 'US',
                        'ccEmail': '',
                        'ccExpirationDate': '2028-01-31',
                        'ccFirstName': 'Luc',
                        'ccLastFour': '0002',
                        'ccLastName': 'Customer1',
                        'ccState': '',
                        'ccType': 'amex',
                        'ccZip': '',
                        'createdDatetime': '2021-06-01T01:10:13+00:00',
                        'gatewayToken': 'SIMULATED',
                        'id': '1e3ee8e5-c276-11eb-bed7-0eff6b8b8fd3',
                        'invoice': {'billingDatetime': '2021-06-01T01:10:13+00:00',
                                    'charges': [{'code': 'SMALL_RECURRING',
                                                'createdDatetime': '2021-06-01T01:10:13+00:00',
                                                'description': '',
                                                'eachAmount': '5.0000',
                                                'id': '1e850a52-c276-11eb-bed7-0eff6b8b8fd3',
                                                'quantity': '1.0000',
                                                'type': 'recurring'}],
                                    'createdDatetime': '2021-06-01T01:10:13+00:00',
                                    'id': '1e8333d1-c276-11eb-bed7-0eff6b8b8fd3',
                                    'invoiceNumber': '2',
                                    'isInitial': 1,
                                    'items': [{'code': 'thousand_chars',
                                                'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                'name': 'Thousand Chars',
                                                'quantity': 0}],
                                    'paidTransactionId': '1eae9c01-c276-11eb-bed7-0eff6b8b8fd3',
                                    'previousBillingDatetime': '',
                                    'taxRate': '',
                                    'transaction': {'amount': '5.00',
                                                    'gatewayToken': 'SIMULATED',
                                                    'id': '1eae9c01-c276-11eb-bed7-0eff6b8b8fd3',
                                                    'memo': '',
                                                    'parentId': '',
                                                    'paymentMethod': {'city': '',
                                                                        'company': '',
                                                                        'country': 'US',
                                                                        'createdDatetime': '2021-06-01T01:10:13+00:00',
                                                                        'creditCard': {'creditCardType': 'amex',
                                                                                    'firstSix': '370000',
                                                                                    'lastFour': '0002'},
                                                                        'email': '',
                                                                        'expirationDate': '2028-01-31',
                                                                        'firstName': 'Luc',
                                                                        'gatewayToken': 'SIMULATED',
                                                                        'gatewayTokenAux': '',
                                                                        'id': '11ebc276-1e3e-0e13-bed7-0eff6b8b8fd3',
                                                                        'lastName': 'Customer1',
                                                                        'method': 'cc',
                                                                        'postCode': '',
                                                                        'state': '',
                                                                        'street': '',
                                                                        'type': 'CreditCard'},
                                                    'response': 'approved',
                                                    'responseReason': 'SIMULATED '
                                                                        'approved '
                                                                        'payment',
                                                    'taxAmount': '',
                                                    'transactedDatetime': '2021-06-01T01:10:14+00:00'},
                                    'type': 'subscription'},
                        'method': 'cc',
                        'paymentMethod': {'city': '',
                                            'company': '',
                                            'country': 'US',
                                            'createdDatetime': '2021-06-01T01:10:13+00:00',
                                            'creditCard': {'creditCardType': 'amex',
                                                        'firstSix': '370000',
                                                        'lastFour': '0002'},
                                            'email': '',
                                            'expirationDate': '2028-01-31',
                                            'firstName': 'Luc',
                                            'gatewayToken': 'SIMULATED',
                                            'gatewayTokenAux': '',
                                            'id': '11ebc276-1e3e-0e13-bed7-0eff6b8b8fd3',
                                            'lastName': 'Customer1',
                                            'method': 'cc',
                                            'postCode': '',
                                            'state': '',
                                            'street': '',
                                            'type': 'CreditCard'},
                        'plan': {'billingFrequencyQuantity': '1',
                                'billingFrequencyUnit': 'months',
                                'code': 'SMALL',
                                'createdDatetime': '2021-06-01T00:57:28+00:00',
                                'description': '',
                                'id': '56561361-c274-11eb-bed7-0eff6b8b8fd3',
                                'isActive': '1',
                                'isFree': False,
                                'items': [{'code': 'thousand_chars',
                                            'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                            'isPeriodic': '1',
                                            'name': 'Thousand Chars',
                                            'overageAmount': '0.00',
                                            'quantityIncluded': 250}],
                                'name': 'Small',
                                'recurringChargeAmount': '5.00',
                                'recurringChargeCode': 'SMALL_RECURRING',
                                'setupChargeAmount': '0.00',
                                'setupChargeCode': 'SMALL_SETUP'}}}

        webhook_data = self.utils.decode_webhook(data)
        expected_data = {
            'type': 'newSubscription',
            'code': 'no1@spam.com',
            'email': 'languagetools+customer1@mailc.net',
            'status': 'active',
            'thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 0,
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=no1%40spam.com&key=d868455a94',
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=no1%40spam.com&key=d868455a94'
        }
        self.assertEqual(webhook_data, expected_data)

    def test_decode_webhook_update_subscription(self):
        data = {'activityActor': 'luc.wastiaux@xsmail.com',
            'activityDatetime': '2021-06-01T02:12:37+00:00',
            'activityType': 'subscriptionChanged',
            'customer': {'campaignContent': '',
                        'campaignMedium': '',
                        'campaignName': '',
                        'campaignSource': '',
                        'campaignTerm': '',
                        'code': 'languagetools+customer2@mailc.net',
                        'company': '',
                        'createdDatetime': '2021-06-01T02:11:06+00:00',
                        'email': 'languagetools+customer2@mailc.net',
                        'firstContactDatetime': '',
                        'firstName': 'Luc',
                        'gatewayToken': 'SIMULATED',
                        'id': '9f93a6ad-c27e-11eb-bed7-0eff6b8b8fd3',
                        'isTaxExempt': '0',
                        'key': 'f63826b48b',
                        'lastName': 'Customer2',
                        'notes': '',
                        'referer': '',
                        'taxNumber': ''},
            'previousSubscription': {'ccAddress': '',
                                    'ccCity': '',
                                    'ccCompany': '',
                                    'ccCountry': 'US',
                                    'ccEmail': '',
                                    'ccExpirationDate': '2031-07-31',
                                    'ccFirstName': 'Luc',
                                    'ccLastFour': '0002',
                                    'ccLastName': 'Customer2',
                                    'ccState': '',
                                    'ccType': 'amex',
                                    'ccZip': '',
                                    'createdDatetime': '2021-06-01T02:11:06+00:00',
                                    'gatewayToken': 'SIMULATED',
                                    'id': '9f966661-c27e-11eb-bed7-0eff6b8b8fd3',
                                    'plan': {'billingFrequencyQuantity': '1',
                                            'billingFrequencyUnit': 'months',
                                            'code': 'SMALL',
                                            'createdDatetime': '2021-06-01T00:57:28+00:00',
                                            'description': '',
                                            'id': '56561361-c274-11eb-bed7-0eff6b8b8fd3',
                                            'isActive': '1',
                                            'isFree': False,
                                            'items': [{'code': 'thousand_chars',
                                                        'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                        'isPeriodic': '1',
                                                        'name': 'Thousand Chars',
                                                        'overageAmount': '0.00',
                                                        'quantityIncluded': 250}],
                                            'name': 'Small',
                                            'recurringChargeAmount': '5.00',
                                            'recurringChargeCode': 'SMALL_RECURRING',
                                            'setupChargeAmount': '0.00',
                                            'setupChargeCode': 'SMALL_SETUP'}},
            'product': {'code': 'LANGUAGE_TOOLS',
                        'id': '53def3f0-bceb-11eb-bed7-0eff6b8b8fd3',
                        'name': 'Language Tools',
                        'subdomain': 'languagetools'},
            'subscription': {'cancelReason': '',
                            'cancelType': '',
                            'canceledDatetime': '',
                            'ccAddress': '',
                            'ccCity': '',
                            'ccCompany': '',
                            'ccCountry': 'US',
                            'ccEmail': '',
                            'ccExpirationDate': '2031-07-31',
                            'ccFirstName': 'Luc',
                            'ccLastFour': '0002',
                            'ccLastName': 'Customer2',
                            'ccState': '',
                            'ccType': 'amex',
                            'ccZip': '',
                            'createdDatetime': '2021-06-01T02:12:36+00:00',
                            'gatewayToken': 'SIMULATED',
                            'id': 'd592e749-c27e-11eb-bed7-0eff6b8b8fd3',
                            'invoice': {'billingDatetime': '2021-07-01T02:11:06+00:00',
                                        'createdDatetime': '2021-06-01T02:11:06+00:00',
                                        'id': '9fb4fd32-c27e-11eb-bed7-0eff6b8b8fd3',
                                        'invoiceNumber': '9',
                                        'isInitial': 0,
                                        'items': [{'code': 'thousand_chars',
                                                    'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                    'name': 'Thousand Chars',
                                                    'quantity': 0}],
                                        'paidTransactionId': '',
                                        'previousBillingDatetime': '2021-06-01T02:11:06+00:00',
                                        'taxRate': '',
                                        'type': 'subscription'},
                            'method': 'cc',
                            'paymentMethod': {'city': '',
                                                'company': '',
                                                'country': 'US',
                                                'createdDatetime': '2021-06-01T02:11:06+00:00',
                                                'creditCard': {'creditCardType': 'amex',
                                                            'firstSix': '370000',
                                                            'lastFour': '0002'},
                                                'email': '',
                                                'expirationDate': '2031-07-31',
                                                'firstName': 'Luc',
                                                'gatewayToken': 'SIMULATED',
                                                'gatewayTokenAux': '',
                                                'id': '11ebc27e-9f94-ed7b-bed7-0eff6b8b8fd3',
                                                'lastName': 'Customer2',
                                                'method': 'cc',
                                                'postCode': '',
                                                'state': '',
                                                'street': '',
                                                'type': 'CreditCard'},
                            'plan': {'billingFrequencyQuantity': '1',
                                    'billingFrequencyUnit': 'months',
                                    'code': 'MEDIUM',
                                    'createdDatetime': '2021-06-01T00:57:55+00:00',
                                    'description': '',
                                    'id': '66431ee6-c274-11eb-bed7-0eff6b8b8fd3',
                                    'isActive': '1',
                                    'isFree': False,
                                    'items': [{'code': 'thousand_chars',
                                                'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                'isPeriodic': '1',
                                                'name': 'Thousand Chars',
                                                'overageAmount': '0.00',
                                                'quantityIncluded': 500}],
                                    'name': 'Medium',
                                    'recurringChargeAmount': '10.00',
                                    'recurringChargeCode': 'MEDIUM_RECURRING',
                                    'setupChargeAmount': '0.00',
                                    'setupChargeCode': 'MEDIUM_SETUP'}}}

        webhook_data = self.utils.decode_webhook(data)
        expected_data = {
            'type': 'subscriptionChanged',
            'code': 'languagetools+customer2@mailc.net',
            'email': 'languagetools+customer2@mailc.net',
            'status': 'active',
            'thousand_char_quota': 500,
            'previous_thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 0,
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b',
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b'
        }
        self.assertEqual(webhook_data, expected_data)        

    def test_decode_webhook_update_subscription_with_usage(self):
        data = {'activityActor': 'luc.wastiaux@xsmail.com',
                'activityDatetime': '2021-06-06T01:20:42+00:00',
                'activityType': 'subscriptionChanged',
                'customer': {'campaignContent': '',
                            'campaignMedium': '',
                            'campaignName': '',
                            'campaignSource': '',
                            'campaignTerm': '',
                            'code': 'languagetools+customer2@mailc.net',
                            'company': '',
                            'createdDatetime': '2021-06-06T01:17:53+00:00',
                            'email': 'languagetools+customer1@mailc.net',
                            'firstContactDatetime': '',
                            'firstName': 'Luc',
                            'gatewayToken': 'SIMULATED',
                            'id': '048f67f4-c665-11eb-bed7-0eff6b8b8fd3',
                            'isTaxExempt': '0',
                            'key': 'f63826b48b',
                            'lastName': 'Customer1',
                            'notes': '',
                            'referer': '',
                            'taxNumber': ''},
                'previousSubscription': {'ccAddress': '',
                                        'ccCity': '',
                                        'ccCompany': '',
                                        'ccCountry': 'US',
                                        'ccEmail': '',
                                        'ccExpirationDate': '2025-06-30',
                                        'ccFirstName': 'Luc',
                                        'ccLastFour': '0002',
                                        'ccLastName': 'Customer1',
                                        'ccState': '',
                                        'ccType': 'amex',
                                        'ccZip': '',
                                        'createdDatetime': '2021-06-06T01:17:53+00:00',
                                        'gatewayToken': 'SIMULATED',
                                        'id': '049127e4-c665-11eb-bed7-0eff6b8b8fd3',
                                        'plan': {'billingFrequencyQuantity': '1',
                                                'billingFrequencyUnit': 'months',
                                                'code': 'SMALL',
                                                'createdDatetime': '2021-06-01T00:57:28+00:00',
                                                'description': '',
                                                'id': '56561361-c274-11eb-bed7-0eff6b8b8fd3',
                                                'isActive': '1',
                                                'isFree': False,
                                                'items': [{'code': 'thousand_chars',
                                                            'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                            'isPeriodic': '1',
                                                            'name': 'Thousand Chars',
                                                            'overageAmount': '0.00',
                                                            'quantityIncluded': 250}],
                                                'name': 'Small',
                                                'recurringChargeAmount': '5.00',
                                                'recurringChargeCode': 'SMALL_RECURRING',
                                                'setupChargeAmount': '0.00',
                                                'setupChargeCode': ''}},
                'product': {'code': 'LANGUAGE_TOOLS',
                            'id': '53def3f0-bceb-11eb-bed7-0eff6b8b8fd3',
                            'name': 'Language Tools',
                            'subdomain': 'languagetools'},
                'subscription': {'cancelReason': '',
                                'cancelType': '',
                                'canceledDatetime': '',
                                'ccAddress': '',
                                'ccCity': '',
                                'ccCompany': '',
                                'ccCountry': 'US',
                                'ccEmail': '',
                                'ccExpirationDate': '2025-06-30',
                                'ccFirstName': 'Luc',
                                'ccLastFour': '0002',
                                'ccLastName': 'Customer1',
                                'ccState': '',
                                'ccType': 'amex',
                                'ccZip': '',
                                'createdDatetime': '2021-06-06T01:20:42+00:00',
                                'gatewayToken': 'SIMULATED',
                                'id': '6918b996-c665-11eb-bed7-0eff6b8b8fd3',
                                'invoice': {'billingDatetime': '2021-06-06T01:20:42+00:00',
                                            'charges': [{'code': 'SMALL_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:20:42+00:00',
                                                        'description': 'Subscription change '
                                                                        'adjustment',
                                                        'eachAmount': '-5.0000',
                                                        'id': '69230a1f-c665-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'custom'},
                                                        {'code': 'MEDIUM_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:20:42+00:00',
                                                        'description': '',
                                                        'eachAmount': '10.0000',
                                                        'id': '69261b5e-c665-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'recurring'}],
                                            'createdDatetime': '2021-06-06T01:17:53+00:00',
                                            'id': '04aedf1d-c665-11eb-bed7-0eff6b8b8fd3',
                                            'invoiceNumber': '16',
                                            'isInitial': 0,
                                            'items': [{'code': 'thousand_chars',
                                                        'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                        'name': 'Thousand Chars',
                                                        'quantity': 123.45}],
                                            'paidTransactionId': '692cc6fb-c665-11eb-bed7-0eff6b8b8fd3',
                                            'previousBillingDatetime': '2021-06-06T01:17:53+00:00',
                                            'taxRate': '',
                                            'transaction': {'amount': '5.00',
                                                            'gatewayToken': 'SIMULATED',
                                                            'id': '692cc6fb-c665-11eb-bed7-0eff6b8b8fd3',
                                                            'memo': '',
                                                            'parentId': '',
                                                            'paymentMethod': {'city': '',
                                                                                'company': '',
                                                                                'country': 'US',
                                                                                'createdDatetime': '2021-06-06T01:17:53+00:00',
                                                                                'creditCard': {'creditCardType': 'amex',
                                                                                            'firstSix': '370000',
                                                                                            'lastFour': '0002'},
                                                                                'email': '',
                                                                                'expirationDate': '2025-06-30',
                                                                                'firstName': 'Luc',
                                                                                'gatewayToken': 'SIMULATED',
                                                                                'gatewayTokenAux': '',
                                                                                'id': '11ebc665-0490-4983-bed7-0eff6b8b8fd3',
                                                                                'lastName': 'Customer1',
                                                                                'method': 'cc',
                                                                                'postCode': '',
                                                                                'state': '',
                                                                                'street': '',
                                                                                'type': 'CreditCard'},
                                                            'response': 'approved',
                                                            'responseReason': 'SIMULATED '
                                                                                'approved '
                                                                                'payment',
                                                            'taxAmount': '',
                                                            'transactedDatetime': '2021-06-06T01:20:42+00:00'},
                                            'type': 'subscription'},
                                'method': 'cc',
                                'paymentMethod': {'city': '',
                                                    'company': '',
                                                    'country': 'US',
                                                    'createdDatetime': '2021-06-06T01:17:53+00:00',
                                                    'creditCard': {'creditCardType': 'amex',
                                                                'firstSix': '370000',
                                                                'lastFour': '0002'},
                                                    'email': '',
                                                    'expirationDate': '2025-06-30',
                                                    'firstName': 'Luc',
                                                    'gatewayToken': 'SIMULATED',
                                                    'gatewayTokenAux': '',
                                                    'id': '11ebc665-0490-4983-bed7-0eff6b8b8fd3',
                                                    'lastName': 'Customer1',
                                                    'method': 'cc',
                                                    'postCode': '',
                                                    'state': '',
                                                    'street': '',
                                                    'type': 'CreditCard'},
                                'plan': {'billingFrequencyQuantity': '1',
                                        'billingFrequencyUnit': 'months',
                                        'code': 'MEDIUM',
                                        'createdDatetime': '2021-06-01T00:57:55+00:00',
                                        'description': '',
                                        'id': '66431ee6-c274-11eb-bed7-0eff6b8b8fd3',
                                        'isActive': '1',
                                        'isFree': False,
                                        'items': [{'code': 'thousand_chars',
                                                    'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                    'isPeriodic': '1',
                                                    'name': 'Thousand Chars',
                                                    'overageAmount': '0.00',
                                                    'quantityIncluded': 500}],
                                        'name': 'Medium',
                                        'recurringChargeAmount': '10.00',
                                        'recurringChargeCode': 'MEDIUM_RECURRING',
                                        'setupChargeAmount': '0.00',
                                        'setupChargeCode': ''}}}

        webhook_data = self.utils.decode_webhook(data)
        expected_data = {
            'type': 'subscriptionChanged',
            'code': 'languagetools+customer2@mailc.net',
            'email': 'languagetools+customer1@mailc.net',
            'status': 'active',
            'thousand_char_quota': 500,
            'previous_thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 123.45,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b'
        }
        self.assertEqual(webhook_data, expected_data)

    def test_decode_webhook_update_subscription_large(self):
        data = {'activityActor': 'luc.wastiaux@xsmail.com',
                'activityDatetime': '2021-06-06T01:26:02+00:00',
                'activityType': 'subscriptionChanged',
                'customer': {'campaignContent': '',
                            'campaignMedium': '',
                            'campaignName': '',
                            'campaignSource': '',
                            'campaignTerm': '',
                            'code': 'languagetools+customer2@mailc.net',
                            'company': '',
                            'createdDatetime': '2021-06-06T01:17:53+00:00',
                            'email': 'languagetools+customer1@mailc.net',
                            'firstContactDatetime': '',
                            'firstName': 'Luc',
                            'gatewayToken': 'SIMULATED',
                            'id': '048f67f4-c665-11eb-bed7-0eff6b8b8fd3',
                            'isTaxExempt': '0',
                            'key': 'f63826b48b',
                            'lastName': 'Customer1',
                            'notes': '',
                            'referer': '',
                            'taxNumber': ''},
                'previousSubscription': {'ccAddress': '',
                                        'ccCity': '',
                                        'ccCompany': '',
                                        'ccCountry': 'US',
                                        'ccEmail': '',
                                        'ccExpirationDate': '2025-06-30',
                                        'ccFirstName': 'Luc',
                                        'ccLastFour': '0002',
                                        'ccLastName': 'Customer1',
                                        'ccState': '',
                                        'ccType': 'amex',
                                        'ccZip': '',
                                        'createdDatetime': '2021-06-06T01:20:42+00:00',
                                        'gatewayToken': 'SIMULATED',
                                        'id': '6918b996-c665-11eb-bed7-0eff6b8b8fd3',
                                        'plan': {'billingFrequencyQuantity': '1',
                                                'billingFrequencyUnit': 'months',
                                                'code': 'MEDIUM',
                                                'createdDatetime': '2021-06-01T00:57:55+00:00',
                                                'description': '',
                                                'id': '66431ee6-c274-11eb-bed7-0eff6b8b8fd3',
                                                'isActive': '1',
                                                'isFree': False,
                                                'items': [{'code': 'thousand_chars',
                                                            'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                            'isPeriodic': '1',
                                                            'name': 'Thousand Chars',
                                                            'overageAmount': '0.00',
                                                            'quantityIncluded': 500}],
                                                'name': 'Medium',
                                                'recurringChargeAmount': '10.00',
                                                'recurringChargeCode': 'MEDIUM_RECURRING',
                                                'setupChargeAmount': '0.00',
                                                'setupChargeCode': ''}},
                'product': {'code': 'LANGUAGE_TOOLS',
                            'id': '53def3f0-bceb-11eb-bed7-0eff6b8b8fd3',
                            'name': 'Language Tools',
                            'subdomain': 'languagetools'},
                'subscription': {'cancelReason': '',
                                'cancelType': '',
                                'canceledDatetime': '',
                                'ccAddress': '',
                                'ccCity': '',
                                'ccCompany': '',
                                'ccCountry': 'US',
                                'ccEmail': '',
                                'ccExpirationDate': '2025-06-30',
                                'ccFirstName': 'Luc',
                                'ccLastFour': '0002',
                                'ccLastName': 'Customer1',
                                'ccState': '',
                                'ccType': 'amex',
                                'ccZip': '',
                                'createdDatetime': '2021-06-06T01:26:01+00:00',
                                'gatewayToken': 'SIMULATED',
                                'id': '2793cbda-c666-11eb-bed7-0eff6b8b8fd3',
                                'invoice': {'billingDatetime': '2021-06-06T01:26:01+00:00',
                                            'charges': [{'code': 'MEDIUM_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:26:01+00:00',
                                                        'description': 'Subscription change '
                                                                        'adjustment',
                                                        'eachAmount': '-10.0000',
                                                        'id': '279c8876-c666-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'custom'},
                                                        {'code': 'LARGE_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:26:01+00:00',
                                                        'description': '',
                                                        'eachAmount': '20.0000',
                                                        'id': '279ff0d2-c666-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'recurring'}],
                                            'createdDatetime': '2021-06-06T01:20:42+00:00',
                                            'id': '6941336c-c665-11eb-bed7-0eff6b8b8fd3',
                                            'invoiceNumber': '17',
                                            'isInitial': 0,
                                            'items': [{'code': 'thousand_chars',
                                                        'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                        'name': 'Thousand Chars',
                                                        'quantity': 0}],
                                            'paidTransactionId': '27a92842-c666-11eb-bed7-0eff6b8b8fd3',
                                            'previousBillingDatetime': '2021-06-06T01:20:42+00:00',
                                            'taxRate': '',
                                            'transaction': {'amount': '10.00',
                                                            'gatewayToken': 'SIMULATED',
                                                            'id': '27a92842-c666-11eb-bed7-0eff6b8b8fd3',
                                                            'memo': '',
                                                            'parentId': '',
                                                            'paymentMethod': {'city': '',
                                                                                'company': '',
                                                                                'country': 'US',
                                                                                'createdDatetime': '2021-06-06T01:17:53+00:00',
                                                                                'creditCard': {'creditCardType': 'amex',
                                                                                            'firstSix': '370000',
                                                                                            'lastFour': '0002'},
                                                                                'email': '',
                                                                                'expirationDate': '2025-06-30',
                                                                                'firstName': 'Luc',
                                                                                'gatewayToken': 'SIMULATED',
                                                                                'gatewayTokenAux': '',
                                                                                'id': '11ebc665-0490-4983-bed7-0eff6b8b8fd3',
                                                                                'lastName': 'Customer1',
                                                                                'method': 'cc',
                                                                                'postCode': '',
                                                                                'state': '',
                                                                                'street': '',
                                                                                'type': 'CreditCard'},
                                                            'response': 'approved',
                                                            'responseReason': 'SIMULATED '
                                                                                'approved '
                                                                                'payment',
                                                            'taxAmount': '',
                                                            'transactedDatetime': '2021-06-06T01:26:01+00:00'},
                                            'type': 'subscription'},
                                'method': 'cc',
                                'paymentMethod': {'city': '',
                                                    'company': '',
                                                    'country': 'US',
                                                    'createdDatetime': '2021-06-06T01:17:53+00:00',
                                                    'creditCard': {'creditCardType': 'amex',
                                                                'firstSix': '370000',
                                                                'lastFour': '0002'},
                                                    'email': '',
                                                    'expirationDate': '2025-06-30',
                                                    'firstName': 'Luc',
                                                    'gatewayToken': 'SIMULATED',
                                                    'gatewayTokenAux': '',
                                                    'id': '11ebc665-0490-4983-bed7-0eff6b8b8fd3',
                                                    'lastName': 'Customer1',
                                                    'method': 'cc',
                                                    'postCode': '',
                                                    'state': '',
                                                    'street': '',
                                                    'type': 'CreditCard'},
                                'plan': {'billingFrequencyQuantity': '1',
                                        'billingFrequencyUnit': 'months',
                                        'code': 'LARGE',
                                        'createdDatetime': '2021-06-01T01:00:01+00:00',
                                        'description': '',
                                        'id': 'b1a293e7-c274-11eb-bed7-0eff6b8b8fd3',
                                        'isActive': '1',
                                        'isFree': False,
                                        'items': [{'code': 'thousand_chars',
                                                    'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                    'isPeriodic': '1',
                                                    'name': 'Thousand Chars',
                                                    'overageAmount': '0.03',
                                                    'quantityIncluded': 1000}],
                                        'name': 'Large',
                                        'recurringChargeAmount': '20.00',
                                        'recurringChargeCode': 'LARGE_RECURRING',
                                        'setupChargeAmount': '0.00',
                                        'setupChargeCode': ''}}}

        webhook_data = self.utils.decode_webhook(data)
        expected_data = {
            'type': 'subscriptionChanged',
            'code': 'languagetools+customer2@mailc.net',
            'email': 'languagetools+customer1@mailc.net',
            'status': 'active',
            'previous_thousand_char_quota': 500,
            'thousand_char_quota': 1000,
            'thousand_char_overage_allowed': 1,
            'thousand_char_used': 0.0,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b'
        }
        self.assertEqual(webhook_data, expected_data)        


    def test_decode_webhook_downgrade_small(self):
        data = {'activityActor': 'luc.wastiaux@xsmail.com',
                'activityDatetime': '2021-06-06T01:40:00+00:00',
                'activityType': 'subscriptionChanged',
                'customer': {'campaignContent': '',
                            'campaignMedium': '',
                            'campaignName': '',
                            'campaignSource': '',
                            'campaignTerm': '',
                            'code': 'languagetools+customer2@mailc.net',
                            'company': '',
                            'createdDatetime': '2021-06-06T01:17:53+00:00',
                            'email': 'languagetools+customer1@mailc.net',
                            'firstContactDatetime': '',
                            'firstName': 'Luc',
                            'gatewayToken': 'SIMULATED',
                            'id': '048f67f4-c665-11eb-bed7-0eff6b8b8fd3',
                            'isTaxExempt': '0',
                            'key': 'f63826b48b',
                            'lastName': 'Customer1',
                            'notes': '',
                            'referer': '',
                            'taxNumber': ''},
                'previousSubscription': {'ccAddress': '',
                                        'ccCity': '',
                                        'ccCompany': '',
                                        'ccCountry': 'US',
                                        'ccEmail': '',
                                        'ccExpirationDate': '2025-06-30',
                                        'ccFirstName': 'Luc',
                                        'ccLastFour': '0002',
                                        'ccLastName': 'Customer1',
                                        'ccState': '',
                                        'ccType': 'amex',
                                        'ccZip': '',
                                        'createdDatetime': '2021-06-06T01:26:01+00:00',
                                        'gatewayToken': 'SIMULATED',
                                        'id': '2793cbda-c666-11eb-bed7-0eff6b8b8fd3',
                                        'plan': {'billingFrequencyQuantity': '1',
                                                'billingFrequencyUnit': 'months',
                                                'code': 'LARGE',
                                                'createdDatetime': '2021-06-01T01:00:01+00:00',
                                                'description': '',
                                                'id': 'b1a293e7-c274-11eb-bed7-0eff6b8b8fd3',
                                                'isActive': '1',
                                                'isFree': False,
                                                'items': [{'code': 'thousand_chars',
                                                            'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                            'isPeriodic': '1',
                                                            'name': 'Thousand Chars',
                                                            'overageAmount': '0.03',
                                                            'quantityIncluded': 1000}],
                                                'name': 'Large',
                                                'recurringChargeAmount': '20.00',
                                                'recurringChargeCode': 'LARGE_RECURRING',
                                                'setupChargeAmount': '0.00',
                                                'setupChargeCode': ''}},
                'product': {'code': 'LANGUAGE_TOOLS',
                            'id': '53def3f0-bceb-11eb-bed7-0eff6b8b8fd3',
                            'name': 'Language Tools',
                            'subdomain': 'languagetools'},
                'subscription': {'cancelReason': '',
                                'cancelType': '',
                                'canceledDatetime': '',
                                'ccAddress': '',
                                'ccCity': '',
                                'ccCompany': '',
                                'ccCountry': 'US',
                                'ccEmail': '',
                                'ccExpirationDate': '2025-06-30',
                                'ccFirstName': 'Luc',
                                'ccLastFour': '0002',
                                'ccLastName': 'Customer1',
                                'ccState': '',
                                'ccType': 'amex',
                                'ccZip': '',
                                'createdDatetime': '2021-06-06T01:40:00+00:00',
                                'gatewayToken': 'SIMULATED',
                                'id': '1ba663b0-c668-11eb-bed7-0eff6b8b8fd3',
                                'invoice': {'billingDatetime': '2021-06-06T01:40:00+00:00',
                                            'charges': [{'code': 'LARGE_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:40:00+00:00',
                                                        'description': 'Subscription change '
                                                                        'adjustment',
                                                        'eachAmount': '-20.0000',
                                                        'id': '1bb0bb45-c668-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'custom'},
                                                        {'code': 'SMALL_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:40:00+00:00',
                                                        'description': '',
                                                        'eachAmount': '5.0000',
                                                        'id': '1bb4fa42-c668-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'recurring'}],
                                            'createdDatetime': '2021-06-06T01:26:02+00:00',
                                            'id': '27bcae65-c666-11eb-bed7-0eff6b8b8fd3',
                                            'invoiceNumber': '18',
                                            'isInitial': 0,
                                            'items': [{'code': 'thousand_chars',
                                                        'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                        'name': 'Thousand Chars',
                                                        'quantity': 42.789}],
                                            'paidTransactionId': '1bbc2b90-c668-11eb-bed7-0eff6b8b8fd3',
                                            'previousBillingDatetime': '2021-06-06T01:26:01+00:00',
                                            'taxRate': '',
                                            'transaction': {'amount': '0.00',
                                                            'gatewayToken': '',
                                                            'id': '1bbc2b90-c668-11eb-bed7-0eff6b8b8fd3',
                                                            'memo': '',
                                                            'parentId': '',
                                                            'paymentMethod': '',
                                                            'response': 'approved',
                                                            'responseReason': '',
                                                            'taxAmount': '',
                                                            'transactedDatetime': '2021-06-06T01:40:00+00:00'},
                                            'type': 'subscription'},
                                'method': 'cc',
                                'paymentMethod': {'city': '',
                                                    'company': '',
                                                    'country': 'US',
                                                    'createdDatetime': '2021-06-06T01:17:53+00:00',
                                                    'creditCard': {'creditCardType': 'amex',
                                                                'firstSix': '370000',
                                                                'lastFour': '0002'},
                                                    'email': '',
                                                    'expirationDate': '2025-06-30',
                                                    'firstName': 'Luc',
                                                    'gatewayToken': 'SIMULATED',
                                                    'gatewayTokenAux': '',
                                                    'id': '11ebc665-0490-4983-bed7-0eff6b8b8fd3',
                                                    'lastName': 'Customer1',
                                                    'method': 'cc',
                                                    'postCode': '',
                                                    'state': '',
                                                    'street': '',
                                                    'type': 'CreditCard'},
                                'plan': {'billingFrequencyQuantity': '1',
                                        'billingFrequencyUnit': 'months',
                                        'code': 'SMALL',
                                        'createdDatetime': '2021-06-01T00:57:28+00:00',
                                        'description': '',
                                        'id': '56561361-c274-11eb-bed7-0eff6b8b8fd3',
                                        'isActive': '1',
                                        'isFree': False,
                                        'items': [{'code': 'thousand_chars',
                                                    'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                    'isPeriodic': '1',
                                                    'name': 'Thousand Chars',
                                                    'overageAmount': '0.00',
                                                    'quantityIncluded': 250}],
                                        'name': 'Small',
                                        'recurringChargeAmount': '5.00',
                                        'recurringChargeCode': 'SMALL_RECURRING',
                                        'setupChargeAmount': '0.00',
                                        'setupChargeCode': ''}}}

        webhook_data = self.utils.decode_webhook(data)
        expected_data = {
            'type': 'subscriptionChanged',
            'code': 'languagetools+customer2@mailc.net',
            'email': 'languagetools+customer1@mailc.net',
            'status': 'active',
            'previous_thousand_char_quota': 1000,
            'thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 42.789,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b'
        }
        self.assertEqual(webhook_data, expected_data)                

    def test_decode_webhook_cancel_large(self):
        data = {'activityActor': 'luc.wastiaux@xsmail.com',
                'activityDatetime': '2021-06-06T01:44:42+00:00',
                'activityType': 'subscriptionCanceled',
                'customer': {'campaignContent': '',
                            'campaignMedium': '',
                            'campaignName': '',
                            'campaignSource': '',
                            'campaignTerm': '',
                            'code': 'languagetools+customer2@mailc.net',
                            'company': '',
                            'createdDatetime': '2021-06-06T01:17:53+00:00',
                            'email': 'languagetools+customer1@mailc.net',
                            'firstContactDatetime': '',
                            'firstName': 'Luc',
                            'gatewayToken': 'SIMULATED',
                            'id': '048f67f4-c665-11eb-bed7-0eff6b8b8fd3',
                            'isTaxExempt': '0',
                            'key': 'f63826b48b',
                            'lastName': 'Customer1',
                            'notes': '',
                            'referer': '',
                            'taxNumber': ''},
                'product': {'code': 'LANGUAGE_TOOLS',
                            'id': '53def3f0-bceb-11eb-bed7-0eff6b8b8fd3',
                            'name': 'Language Tools',
                            'subdomain': 'languagetools'},
                'subscription': {'cancelReason': '',
                                'cancelType': 'customer',
                                'canceledDatetime': '2021-06-06T01:44:42+00:00',
                                'ccAddress': '',
                                'ccCity': '',
                                'ccCompany': '',
                                'ccCountry': 'US',
                                'ccEmail': '',
                                'ccExpirationDate': '2025-06-30',
                                'ccFirstName': 'Luc',
                                'ccLastFour': '0002',
                                'ccLastName': 'Customer1',
                                'ccState': '',
                                'ccType': 'amex',
                                'ccZip': '',
                                'createdDatetime': '2021-06-06T01:43:57+00:00',
                                'gatewayToken': 'SIMULATED',
                                'id': 'a8794967-c668-11eb-bed7-0eff6b8b8fd3',
                                'invoice': {'billingDatetime': '2021-06-06T01:43:57+00:00',
                                            'charges': [{'code': 'CREDIT_FORWARD',
                                                        'createdDatetime': '2021-06-06T01:40:01+00:00',
                                                        'description': 'Credit carried '
                                                                        'forward from '
                                                                        'invoice #18',
                                                        'eachAmount': '-15.0000',
                                                        'id': '1bce8216-c668-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'custom'},
                                                        {'code': 'SMALL_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:43:57+00:00',
                                                        'description': 'Subscription change '
                                                                        'adjustment',
                                                        'eachAmount': '-5.0000',
                                                        'id': 'a87cd384-c668-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'custom'},
                                                        {'code': 'LARGE_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:43:57+00:00',
                                                        'description': '',
                                                        'eachAmount': '20.0000',
                                                        'id': 'a87e101c-c668-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'recurring'}],
                                            'createdDatetime': '2021-06-06T01:40:00+00:00',
                                            'id': '1bcc1c83-c668-11eb-bed7-0eff6b8b8fd3',
                                            'invoiceNumber': '19',
                                            'isInitial': 0,
                                            'items': [{'code': 'thousand_chars',
                                                        'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                        'name': 'Thousand Chars',
                                                        'quantity': 0}],
                                            'paidTransactionId': 'a880165d-c668-11eb-bed7-0eff6b8b8fd3',
                                            'previousBillingDatetime': '2021-06-06T01:40:00+00:00',
                                            'taxRate': '',
                                            'transaction': {'amount': '0.00',
                                                            'gatewayToken': '',
                                                            'id': 'a880165d-c668-11eb-bed7-0eff6b8b8fd3',
                                                            'memo': '',
                                                            'parentId': '',
                                                            'paymentMethod': '',
                                                            'response': 'approved',
                                                            'responseReason': '',
                                                            'taxAmount': '',
                                                            'transactedDatetime': '2021-06-06T01:43:57+00:00'},
                                            'type': 'subscription'},
                                'method': 'cc',
                                'paymentMethod': {'city': '',
                                                    'company': '',
                                                    'country': 'US',
                                                    'createdDatetime': '2021-06-06T01:17:53+00:00',
                                                    'creditCard': {'creditCardType': 'amex',
                                                                'firstSix': '370000',
                                                                'lastFour': '0002'},
                                                    'email': '',
                                                    'expirationDate': '2025-06-30',
                                                    'firstName': 'Luc',
                                                    'gatewayToken': 'SIMULATED',
                                                    'gatewayTokenAux': '',
                                                    'id': '11ebc665-0490-4983-bed7-0eff6b8b8fd3',
                                                    'lastName': 'Customer1',
                                                    'method': 'cc',
                                                    'postCode': '',
                                                    'state': '',
                                                    'street': '',
                                                    'type': 'CreditCard'},
                                'plan': {'billingFrequencyQuantity': '1',
                                        'billingFrequencyUnit': 'months',
                                        'code': 'LARGE',
                                        'createdDatetime': '2021-06-01T01:00:01+00:00',
                                        'description': '',
                                        'id': 'b1a293e7-c274-11eb-bed7-0eff6b8b8fd3',
                                        'isActive': '1',
                                        'isFree': False,
                                        'items': [{'code': 'thousand_chars',
                                                    'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                    'isPeriodic': '1',
                                                    'name': 'Thousand Chars',
                                                    'overageAmount': '0.03',
                                                    'quantityIncluded': 1000}],
                                        'name': 'Large',
                                        'recurringChargeAmount': '20.00',
                                        'recurringChargeCode': 'LARGE_RECURRING',
                                        'setupChargeAmount': '0.00',
                                        'setupChargeCode': ''}}}

        webhook_data = self.utils.decode_webhook(data)
        expected_data = {
            'type': 'subscriptionCanceled',
            'code': 'languagetools+customer2@mailc.net',
            'email': 'languagetools+customer1@mailc.net',
            'status': 'canceled',
            'thousand_char_quota': 1000,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 0.0,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b'
        }
        self.assertEqual(webhook_data, expected_data)


    def test_decode_webhook_cancel_small(self):
        data = {'activityActor': 'luc.wastiaux@xsmail.com',
                'activityDatetime': '2021-07-14T12:49:46+00:00',
                'activityType': 'subscriptionCanceled',
                'customer': {'campaignContent': '',
                            'campaignMedium': '',
                            'campaignName': '',
                            'campaignSource': '',
                            'campaignTerm': '',
                            'code': 'languagetools+development.language_tools.customer-1626266982@mailc.net',
                            'company': '',
                            'createdDatetime': '2021-07-14T12:49:44+00:00',
                            'email': 'languagetools+development.language_tools.customer-1626266982@mailc.net',
                            'firstContactDatetime': '',
                            'firstName': 'Test',
                            'gatewayToken': 'SIMULATED',
                            'id': 'f6a77aee-e4a1-11eb-bed7-0eff6b8b8fd3',
                            'isTaxExempt': '0',
                            'key': '4d5cb2fb95',
                            'lastName': 'Customer',
                            'notes': '',
                            'referer': '',
                            'taxNumber': ''},
                'product': {'code': 'LANGUAGE_TOOLS_LOCAL',
                            'id': '5c3f597a-ccbc-11eb-bed7-0eff6b8b8fd3',
                            'name': 'Language Tools Dev Local',
                            'subdomain': ''},
                'subscription': {'cancelReason': '',
                                'cancelType': 'customer',
                                'canceledDatetime': '2021-07-14T12:49:46+00:00',
                                'ccAddress': '',
                                'ccCity': '',
                                'ccCompany': '',
                                'ccCountry': '',
                                'ccEmail': '',
                                'ccExpirationDate': '2025-04-30',
                                'ccFirstName': 'Test',
                                'ccLastFour': '0002',
                                'ccLastName': 'Customer',
                                'ccState': '',
                                'ccType': 'amex',
                                'ccZip': '',
                                'createdDatetime': '2021-07-14T12:49:44+00:00',
                                'gatewayToken': 'SIMULATED',
                                'id': 'f6a9ac71-e4a1-11eb-bed7-0eff6b8b8fd3',
                                'invoice': {'billingDatetime': '2021-07-14T12:49:44+00:00',
                                            'charges': [{'code': 'SMALL_RECURRING',
                                                        'createdDatetime': '2021-07-14T12:49:44+00:00',
                                                        'description': '',
                                                        'eachAmount': '5.0000',
                                                        'id': 'f6afe99b-e4a1-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'recurring'}],
                                            'createdDatetime': '2021-07-14T12:49:44+00:00',
                                            'id': 'f6ae4607-e4a1-11eb-bed7-0eff6b8b8fd3',
                                            'invoiceNumber': '335',
                                            'isInitial': 1,
                                            'items': [{'code': 'thousand_chars',
                                                        'id': '7ef412ff-ccbc-11eb-bed7-0eff6b8b8fd3',
                                                        'name': 'Thousand Chars',
                                                        'quantity': 0}],
                                            'paidTransactionId': 'f6b8d8ec-e4a1-11eb-bed7-0eff6b8b8fd3',
                                            'previousBillingDatetime': '',
                                            'taxRate': '',
                                            'transaction': {'amount': '5.00',
                                                            'gatewayToken': 'SIMULATED',
                                                            'id': 'f6b8d8ec-e4a1-11eb-bed7-0eff6b8b8fd3',
                                                            'memo': '',
                                                            'parentId': '',
                                                            'paymentMethod': {'city': '',
                                                                                'company': '',
                                                                                'country': '',
                                                                                'createdDatetime': '2021-07-14T12:49:44+00:00',
                                                                                'creditCard': {'creditCardType': 'amex',
                                                                                            'firstSix': '370000',
                                                                                            'lastFour': '0002'},
                                                                                'email': '',
                                                                                'expirationDate': '2025-04-30',
                                                                                'firstName': 'Test',
                                                                                'gatewayToken': 'SIMULATED',
                                                                                'gatewayTokenAux': '',
                                                                                'id': '11ebe4a1-f6a8-9bea-bed7-0eff6b8b8fd3',
                                                                                'lastName': 'Customer',
                                                                                'method': 'cc',
                                                                                'postCode': '',
                                                                                'state': '',
                                                                                'street': '',
                                                                                'type': 'CreditCard'},
                                                            'response': 'approved',
                                                            'responseReason': 'SIMULATED '
                                                                                'approved '
                                                                                'payment',
                                                            'taxAmount': '',
                                                            'transactedDatetime': '2021-07-14T12:49:44+00:00'},
                                            'type': 'subscription'},
                                'method': 'cc',
                                'paymentMethod': {'city': '',
                                                    'company': '',
                                                    'country': '',
                                                    'createdDatetime': '2021-07-14T12:49:44+00:00',
                                                    'creditCard': {'creditCardType': 'amex',
                                                                'firstSix': '370000',
                                                                'lastFour': '0002'},
                                                    'email': '',
                                                    'expirationDate': '2025-04-30',
                                                    'firstName': 'Test',
                                                    'gatewayToken': 'SIMULATED',
                                                    'gatewayTokenAux': '',
                                                    'id': '11ebe4a1-f6a8-9bea-bed7-0eff6b8b8fd3',
                                                    'lastName': 'Customer',
                                                    'method': 'cc',
                                                    'postCode': '',
                                                    'state': '',
                                                    'street': '',
                                                    'type': 'CreditCard'},
                                'plan': {'billingFrequencyQuantity': '1',
                                        'billingFrequencyUnit': 'months',
                                        'code': 'SMALL',
                                        'createdDatetime': '2021-06-14T02:59:32+00:00',
                                        'description': '',
                                        'id': '8afad178-ccbc-11eb-bed7-0eff6b8b8fd3',
                                        'isActive': '1',
                                        'isFree': False,
                                        'items': [{'code': 'thousand_chars',
                                                    'id': '7ef412ff-ccbc-11eb-bed7-0eff6b8b8fd3',
                                                    'isPeriodic': '1',
                                                    'name': 'Thousand Chars',
                                                    'overageAmount': '0.00',
                                                    'quantityIncluded': 250}],
                                        'name': 'Small',
                                        'recurringChargeAmount': '5.00',
                                        'recurringChargeCode': 'SMALL_RECURRING',
                                        'setupChargeAmount': '0.00',
                                        'setupChargeCode': ''}}}

        webhook_data = self.utils.decode_webhook(data)
        expected_data = {
            'type': 'subscriptionCanceled',
            'code': 'languagetools+development.language_tools.customer-1626266982@mailc.net',
            'email': 'languagetools+development.language_tools.customer-1626266982@mailc.net',
            'status': 'canceled',
            'thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 0.0,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bdevelopment.language_tools.customer-1626266982%40mailc.net&key=4d5cb2fb95',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bdevelopment.language_tools.customer-1626266982%40mailc.net&key=4d5cb2fb95'
        }
        self.assertEqual(webhook_data, expected_data)                                        

    def test_decode_webhook_reactivate_large(self):
        data = {'activityActor': 'luc.wastiaux@xsmail.com',
                'activityDatetime': '2021-06-06T01:52:34+00:00',
                'activityType': 'subscriptionReactivated',
                'customer': {'campaignContent': '',
                            'campaignMedium': '',
                            'campaignName': '',
                            'campaignSource': '',
                            'campaignTerm': '',
                            'code': 'languagetools+customer2@mailc.net',
                            'company': '',
                            'createdDatetime': '2021-06-06T01:17:53+00:00',
                            'email': 'languagetools+customer1@mailc.net',
                            'firstContactDatetime': '',
                            'firstName': 'Luc',
                            'gatewayToken': 'SIMULATED',
                            'id': '048f67f4-c665-11eb-bed7-0eff6b8b8fd3',
                            'isTaxExempt': '0',
                            'key': 'f63826b48b',
                            'lastName': 'Customer1',
                            'notes': '',
                            'referer': '',
                            'taxNumber': ''},
                'product': {'code': 'LANGUAGE_TOOLS',
                            'id': '53def3f0-bceb-11eb-bed7-0eff6b8b8fd3',
                            'name': 'Language Tools',
                            'subdomain': 'languagetools'},
                'subscription': {'cancelReason': '',
                                'cancelType': '',
                                'canceledDatetime': '',
                                'ccAddress': '',
                                'ccCity': '',
                                'ccCompany': '',
                                'ccCountry': 'US',
                                'ccEmail': '',
                                'ccExpirationDate': '2029-01-31',
                                'ccFirstName': 'Luc',
                                'ccLastFour': '0002',
                                'ccLastName': 'Customer1',
                                'ccState': '',
                                'ccType': 'amex',
                                'ccZip': '',
                                'createdDatetime': '2021-06-06T01:43:57+00:00',
                                'gatewayToken': 'SIMULATED',
                                'id': 'a8794967-c668-11eb-bed7-0eff6b8b8fd3',
                                'invoice': {'billingDatetime': '2021-06-06T01:43:57+00:00',
                                            'charges': [{'code': 'CREDIT_FORWARD',
                                                        'createdDatetime': '2021-06-06T01:40:01+00:00',
                                                        'description': 'Credit carried '
                                                                        'forward from '
                                                                        'invoice #18',
                                                        'eachAmount': '-15.0000',
                                                        'id': '1bce8216-c668-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'custom'},
                                                        {'code': 'SMALL_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:43:57+00:00',
                                                        'description': 'Subscription change '
                                                                        'adjustment',
                                                        'eachAmount': '-5.0000',
                                                        'id': 'a87cd384-c668-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'custom'},
                                                        {'code': 'LARGE_RECURRING',
                                                        'createdDatetime': '2021-06-06T01:43:57+00:00',
                                                        'description': '',
                                                        'eachAmount': '20.0000',
                                                        'id': 'a87e101c-c668-11eb-bed7-0eff6b8b8fd3',
                                                        'quantity': '1.0000',
                                                        'type': 'recurring'}],
                                            'createdDatetime': '2021-06-06T01:40:00+00:00',
                                            'id': '1bcc1c83-c668-11eb-bed7-0eff6b8b8fd3',
                                            'invoiceNumber': '19',
                                            'isInitial': 0,
                                            'items': [{'code': 'thousand_chars',
                                                        'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                        'name': 'Thousand Chars',
                                                        'quantity': 0}],
                                            'paidTransactionId': 'a880165d-c668-11eb-bed7-0eff6b8b8fd3',
                                            'previousBillingDatetime': '2021-06-06T01:40:00+00:00',
                                            'taxRate': '',
                                            'transaction': {'amount': '0.00',
                                                            'gatewayToken': '',
                                                            'id': 'a880165d-c668-11eb-bed7-0eff6b8b8fd3',
                                                            'memo': '',
                                                            'parentId': '',
                                                            'paymentMethod': '',
                                                            'response': 'approved',
                                                            'responseReason': '',
                                                            'taxAmount': '',
                                                            'transactedDatetime': '2021-06-06T01:43:57+00:00'},
                                            'type': 'subscription'},
                                'method': 'cc',
                                'paymentMethod': {'city': '',
                                                    'company': '',
                                                    'country': 'US',
                                                    'createdDatetime': '2021-06-06T01:52:34+00:00',
                                                    'creditCard': {'creditCardType': 'amex',
                                                                'firstSix': '370000',
                                                                'lastFour': '0002'},
                                                    'email': '',
                                                    'expirationDate': '2029-01-31',
                                                    'firstName': 'Luc',
                                                    'gatewayToken': 'SIMULATED',
                                                    'gatewayTokenAux': '',
                                                    'id': '11ebc669-dccf-06cb-bed7-0eff6b8b8fd3',
                                                    'lastName': 'Customer1',
                                                    'method': 'cc',
                                                    'postCode': '',
                                                    'state': '',
                                                    'street': '',
                                                    'type': 'CreditCard'},
                                'plan': {'billingFrequencyQuantity': '1',
                                        'billingFrequencyUnit': 'months',
                                        'code': 'LARGE',
                                        'createdDatetime': '2021-06-01T01:00:01+00:00',
                                        'description': '',
                                        'id': 'b1a293e7-c274-11eb-bed7-0eff6b8b8fd3',
                                        'isActive': '1',
                                        'isFree': False,
                                        'items': [{'code': 'thousand_chars',
                                                    'id': '382ca6fd-c274-11eb-bed7-0eff6b8b8fd3',
                                                    'isPeriodic': '1',
                                                    'name': 'Thousand Chars',
                                                    'overageAmount': '0.03',
                                                    'quantityIncluded': 1000}],
                                        'name': 'Large',
                                        'recurringChargeAmount': '20.00',
                                        'recurringChargeCode': 'LARGE_RECURRING',
                                        'setupChargeAmount': '0.00',
                                        'setupChargeCode': ''}}}

        webhook_data = self.utils.decode_webhook(data)
        expected_data = {
            'type': 'subscriptionReactivated',
            'code': 'languagetools+customer2@mailc.net',
            'email': 'languagetools+customer1@mailc.net',
            'status': 'active',
            'thousand_char_quota': 1000,
            'thousand_char_overage_allowed': 1,
            'thousand_char_used': 0.0,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer2%40mailc.net&key=f63826b48b'
        }
        self.assertEqual(webhook_data, expected_data)        

    def test_decode_customer_xml_1(self):
        xml_str = """<?xml version="1.0" ?><customers>	
                    <customer id="0dc458e4-c66c-11eb-bed7-0eff6b8b8fd3" code="languagetools+customer3@mailc.net">		
                            <firstName>Luc</firstName>		
                            <lastName>Customer3</lastName>		
                            <company/>		
                            <email>languagetools+customer3@mailc.net</email>		
                            <notes/>		
                            <gatewayToken>SIMULATED</gatewayToken>		
                            <isTaxExempt>0</isTaxExempt>		
                            <isVatExempt>0</isVatExempt>		
                            <taxNumber/>		
                            <vatNumber/>		
                            <taxRate/>		
                            <firstContactDatetime/>		
                            <referer/>		
                            <refererHost/>		
                            <campaignSource/>		
                            <campaignMedium/>		
                            <campaignTerm/>		
                            <campaignContent/>		
                            <campaignName/>		
                            <key>31b4294939</key>		
                            <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>		
                            <modifiedDatetime>2021-06-06T02:08:15+00:00</modifiedDatetime>		
                            <metaData/>		
                            <subscriptions>			
                                <subscription id="0dca6c5f-c66c-11eb-bed7-0eff6b8b8fd3">				
                                        <plans>					
                                            <plan id="56561361-c274-11eb-bed7-0eff6b8b8fd3" code="SMALL">						
                                                    <name>Small</name>						
                                                    <displayName>Small • 5.00 / Month</displayName>						
                                                    <description/>						
                                                    <isActive>1</isActive>						
                                                    <isFree>0</isFree>						
                                                    <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                    <trialDays>0</trialDays>						
                                                    <initialBillCount>0</initialBillCount>						
                                                    <initialBillCountUnit>days</initialBillCountUnit>						
                                                    <initialInvoiceBillingDatetime>2021-06-06T02:09:21+00:00</initialInvoiceBillingDatetime>						
                                                    <billingFrequency>monthly</billingFrequency>						
                                                    <billingFrequencyPer>month</billingFrequencyPer>						
                                                    <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                    <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                    <nextInvoiceBillingDatetime>2021-07-06T02:09:21+00:00</nextInvoiceBillingDatetime>						
                                                    <setupChargeCode/>						
                                                    <setupChargeAmount>0.00</setupChargeAmount>						
                                                    <recurringChargeCode>SMALL_RECURRING</recurringChargeCode>						
                                                    <recurringChargeAmount>5.00</recurringChargeAmount>						
                                                    <onChangeInitialBillHandler>now</onChangeInitialBillHandler>						
                                                    <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                    <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                    <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>						
                                                    <items>							
                                                        <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                <name>Thousand Chars</name>								
                                                                <quantityIncluded>250</quantityIncluded>								
                                                                <isPeriodic>1</isPeriodic>								
                                                                <overageAmount>0.00</overageAmount>								
                                                                <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>								
                                                        </item>							
                                                    </items>						
                                            </plan>					
                                        </plans>				
                                        <gatewayToken>SIMULATED</gatewayToken>				
                                        <gatewayTokenAux/>				
                                        <gatewayAccount>					
                                            <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                            <gateway>Stripe_Simulator</gateway>					
                                            <type>cc</type>					
                                        </gatewayAccount>				
                                        <ccFirstName>Luc</ccFirstName>				
                                        <ccLastName>Customer3</ccLastName>				
                                        <ccCompany/>				
                                        <ccCountry>US</ccCountry>				
                                        <ccAddress/>				
                                        <ccCity/>				
                                        <ccState/>				
                                        <ccZip/>				
                                        <ccType>amex</ccType>				
                                        <ccLastFour>0002</ccLastFour>				
                                        <ccExpirationDate>2031-02-28</ccExpirationDate>				
                                        <ccEmail/>				
                                        <cancelType/>				
                                        <cancelReason/>				
                                        <canceledDatetime/>				
                                        <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>				
                                        <items>					
                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">						
                                                    <name>Thousand Chars</name>						
                                                    <quantity>42.789</quantity>						
                                                    <createdDatetime>2021-06-06T02:09:21+00:00</createdDatetime>						
                                                    <modifiedDatetime>2021-06-06T02:09:21+00:00</modifiedDatetime>						
                                            </item>					
                                        </items>				
                                        <invoices>					
                                            <invoice id="0df37017-c66c-11eb-bed7-0eff6b8b8fd3">						
                                                    <number>22</number>						
                                                    <type>subscription</type>						
                                                    <vatRate/>						
                                                    <taxRate/>						
                                                    <billingDatetime>2021-07-06T02:08:15+00:00</billingDatetime>						
                                                    <paidTransactionId/>						
                                                    <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>						
                                                    <charges>							
                                                        <charge id="" code="SMALL_RECURRING">								
                                                                <type>recurring</type>								
                                                                <quantity>1</quantity>								
                                                                <eachAmount>5.00</eachAmount>								
                                                                <description/>								
                                                                <createdDatetime>2021-07-06T02:08:15+00:00</createdDatetime>								
                                                        </charge>							
                                                    </charges>						
                                            </invoice>					
                                            <invoice id="0dd2c943-c66c-11eb-bed7-0eff6b8b8fd3">						
                                                    <number>21</number>						
                                                    <type>subscription</type>						
                                                    <vatRate/>						
                                                    <taxRate/>						
                                                    <billingDatetime>2021-06-06T02:08:15+00:00</billingDatetime>						
                                                    <paidTransactionId>0de3061e-c66c-11eb-bed7-0eff6b8b8fd3</paidTransactionId>						
                                                    <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>						
                                                    <charges>							
                                                        <charge id="0dd5db9e-c66c-11eb-bed7-0eff6b8b8fd3" code="SMALL_RECURRING">								
                                                                <type>recurring</type>								
                                                                <quantity>1</quantity>								
                                                                <eachAmount>5.00</eachAmount>								
                                                                <description/>								
                                                                <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>								
                                                        </charge>							
                                                    </charges>						
                                                    <transactions>							
                                                        <transaction id="0de3061e-c66c-11eb-bed7-0eff6b8b8fd3" code="">								
                                                                <parentId/>								
                                                                <gatewayToken>SIMULATED</gatewayToken>								
                                                                <gatewayAccount>									
                                                                    <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>									
                                                                    <gateway>Stripe_Simulator</gateway>									
                                                                    <type>cc</type>									
                                                                </gatewayAccount>								
                                                                <amount>5.00</amount>								
                                                                <memo/>								
                                                                <response>approved</response>								
                                                                <responseReason>SIMULATED approved payment</responseReason>								
                                                                <transactedDatetime>2021-06-06T02:08:15+00:00</transactedDatetime>								
                                                                <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>								
                                                        </transaction>							
                                                    </transactions>						
                                            </invoice>					
                                        </invoices>				
                                </subscription>			
                            </subscriptions>		
                    </customer>	
                </customers>"""

        actual_xml_data = self.utils.decode_customer_xml(xml_str)
        expected_xml_data = {
            'code': 'languagetools+customer3@mailc.net',
            'email': 'languagetools+customer3@mailc.net',
            'status': 'active',
            'thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 42.789,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer3%40mailc.net&key=31b4294939',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer3%40mailc.net&key=31b4294939'
        }
        self.assertEqual(actual_xml_data, expected_xml_data)


    def test_decode_customer_xml_empty_items(self):
        xml_str = """<?xml version="1.0" ?><customers>	
                    <customer id="0dc458e4-c66c-11eb-bed7-0eff6b8b8fd3" code="languagetools+customer3@mailc.net">		
                            <firstName>Luc</firstName>		
                            <lastName>Customer3</lastName>		
                            <company/>		
                            <email>languagetools+customer3@mailc.net</email>		
                            <notes/>		
                            <gatewayToken>SIMULATED</gatewayToken>		
                            <isTaxExempt>0</isTaxExempt>		
                            <isVatExempt>0</isVatExempt>		
                            <taxNumber/>		
                            <vatNumber/>		
                            <taxRate/>		
                            <firstContactDatetime/>		
                            <referer/>		
                            <refererHost/>		
                            <campaignSource/>		
                            <campaignMedium/>		
                            <campaignTerm/>		
                            <campaignContent/>		
                            <campaignName/>		
                            <key>31b4294939</key>		
                            <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>		
                            <modifiedDatetime>2021-06-06T02:08:15+00:00</modifiedDatetime>		
                            <metaData/>		
                            <subscriptions>			
                                <subscription id="0dca6c5f-c66c-11eb-bed7-0eff6b8b8fd3">				
                                        <plans>					
                                            <plan id="56561361-c274-11eb-bed7-0eff6b8b8fd3" code="SMALL">						
                                                    <name>Small</name>						
                                                    <displayName>Small • 5.00 / Month</displayName>						
                                                    <description/>						
                                                    <isActive>1</isActive>						
                                                    <isFree>0</isFree>						
                                                    <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                    <trialDays>0</trialDays>						
                                                    <initialBillCount>0</initialBillCount>						
                                                    <initialBillCountUnit>days</initialBillCountUnit>						
                                                    <initialInvoiceBillingDatetime>2021-06-06T02:09:21+00:00</initialInvoiceBillingDatetime>						
                                                    <billingFrequency>monthly</billingFrequency>						
                                                    <billingFrequencyPer>month</billingFrequencyPer>						
                                                    <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                    <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                    <nextInvoiceBillingDatetime>2021-07-06T02:09:21+00:00</nextInvoiceBillingDatetime>						
                                                    <setupChargeCode/>						
                                                    <setupChargeAmount>0.00</setupChargeAmount>						
                                                    <recurringChargeCode>SMALL_RECURRING</recurringChargeCode>						
                                                    <recurringChargeAmount>5.00</recurringChargeAmount>						
                                                    <onChangeInitialBillHandler>now</onChangeInitialBillHandler>						
                                                    <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                    <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                    <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>						
                                                    <items>							
                                                        <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                <name>Thousand Chars</name>								
                                                                <quantityIncluded>250</quantityIncluded>								
                                                                <isPeriodic>1</isPeriodic>								
                                                                <overageAmount>0.00</overageAmount>								
                                                                <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>								
                                                        </item>							
                                                    </items>						
                                            </plan>					
                                        </plans>				
                                        <gatewayToken>SIMULATED</gatewayToken>				
                                        <gatewayTokenAux/>				
                                        <gatewayAccount>					
                                            <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                            <gateway>Stripe_Simulator</gateway>					
                                            <type>cc</type>					
                                        </gatewayAccount>				
                                        <ccFirstName>Luc</ccFirstName>				
                                        <ccLastName>Customer3</ccLastName>				
                                        <ccCompany/>				
                                        <ccCountry>US</ccCountry>				
                                        <ccAddress/>				
                                        <ccCity/>				
                                        <ccState/>				
                                        <ccZip/>				
                                        <ccType>amex</ccType>				
                                        <ccLastFour>0002</ccLastFour>				
                                        <ccExpirationDate>2031-02-28</ccExpirationDate>				
                                        <ccEmail/>				
                                        <cancelType/>				
                                        <cancelReason/>				
                                        <canceledDatetime/>				
                                        <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>				
                                        <invoices>					
                                            <invoice id="0df37017-c66c-11eb-bed7-0eff6b8b8fd3">						
                                                    <number>22</number>						
                                                    <type>subscription</type>						
                                                    <vatRate/>						
                                                    <taxRate/>						
                                                    <billingDatetime>2021-07-06T02:08:15+00:00</billingDatetime>						
                                                    <paidTransactionId/>						
                                                    <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>						
                                                    <charges>							
                                                        <charge id="" code="SMALL_RECURRING">								
                                                                <type>recurring</type>								
                                                                <quantity>1</quantity>								
                                                                <eachAmount>5.00</eachAmount>								
                                                                <description/>								
                                                                <createdDatetime>2021-07-06T02:08:15+00:00</createdDatetime>								
                                                        </charge>							
                                                    </charges>						
                                            </invoice>					
                                            <invoice id="0dd2c943-c66c-11eb-bed7-0eff6b8b8fd3">						
                                                    <number>21</number>						
                                                    <type>subscription</type>						
                                                    <vatRate/>						
                                                    <taxRate/>						
                                                    <billingDatetime>2021-06-06T02:08:15+00:00</billingDatetime>						
                                                    <paidTransactionId>0de3061e-c66c-11eb-bed7-0eff6b8b8fd3</paidTransactionId>						
                                                    <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>						
                                                    <charges>							
                                                        <charge id="0dd5db9e-c66c-11eb-bed7-0eff6b8b8fd3" code="SMALL_RECURRING">								
                                                                <type>recurring</type>								
                                                                <quantity>1</quantity>								
                                                                <eachAmount>5.00</eachAmount>								
                                                                <description/>								
                                                                <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>								
                                                        </charge>							
                                                    </charges>						
                                                    <transactions>							
                                                        <transaction id="0de3061e-c66c-11eb-bed7-0eff6b8b8fd3" code="">								
                                                                <parentId/>								
                                                                <gatewayToken>SIMULATED</gatewayToken>								
                                                                <gatewayAccount>									
                                                                    <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>									
                                                                    <gateway>Stripe_Simulator</gateway>									
                                                                    <type>cc</type>									
                                                                </gatewayAccount>								
                                                                <amount>5.00</amount>								
                                                                <memo/>								
                                                                <response>approved</response>								
                                                                <responseReason>SIMULATED approved payment</responseReason>								
                                                                <transactedDatetime>2021-06-06T02:08:15+00:00</transactedDatetime>								
                                                                <createdDatetime>2021-06-06T02:08:15+00:00</createdDatetime>								
                                                        </transaction>							
                                                    </transactions>						
                                            </invoice>					
                                        </invoices>				
                                </subscription>			
                            </subscriptions>		
                    </customer>	
                </customers>"""

        actual_xml_data = self.utils.decode_customer_xml(xml_str)
        expected_xml_data = {
            'code': 'languagetools+customer3@mailc.net',
            'email': 'languagetools+customer3@mailc.net',
            'status': 'active',
            'thousand_char_quota': 250,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 0,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer3%40mailc.net&key=31b4294939',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer3%40mailc.net&key=31b4294939'
        }
        self.assertEqual(actual_xml_data, expected_xml_data)

    def test_decode_customer_xml_upgrades_and_usage(self):
        xml_str = """<?xml version="1.0" ?><customers>	
                        <customer id="e72f0991-c68c-11eb-bed7-0eff6b8b8fd3" code="languagetools+customer4@mailc.net">		
                                <firstName>Luc</firstName>		
                                <lastName>Customer4</lastName>		
                                <company/>		
                                <email>languagetools+customer4@mailc.net</email>		
                                <notes/>		
                                <gatewayToken>SIMULATED</gatewayToken>		
                                <isTaxExempt>0</isTaxExempt>		
                                <isVatExempt>0</isVatExempt>		
                                <taxNumber/>		
                                <vatNumber/>		
                                <taxRate/>		
                                <firstContactDatetime/>		
                                <referer/>		
                                <refererHost/>		
                                <campaignSource/>		
                                <campaignMedium/>		
                                <campaignTerm/>		
                                <campaignContent/>		
                                <campaignName/>		
                                <key>03ff591107</key>		
                                <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>		
                                <modifiedDatetime>2021-06-06T06:03:24+00:00</modifiedDatetime>		
                                <metaData/>		
                                <subscriptions>			
                                    <subscription id="f0ad4f2c-c68d-11eb-bed7-0eff6b8b8fd3">				
                                            <plans>					
                                                <plan id="b1a293e7-c274-11eb-bed7-0eff6b8b8fd3" code="LARGE">						
                                                        <name>Large</name>						
                                                        <displayName>Large • 20.00 / Month</displayName>						
                                                        <description/>						
                                                        <isActive>1</isActive>						
                                                        <isFree>0</isFree>						
                                                        <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                        <trialDays>0</trialDays>						
                                                        <initialBillCount>0</initialBillCount>						
                                                        <initialBillCountUnit>days</initialBillCountUnit>						
                                                        <initialInvoiceBillingDatetime>2021-06-06T06:11:16+00:00</initialInvoiceBillingDatetime>						
                                                        <billingFrequency>monthly</billingFrequency>						
                                                        <billingFrequencyPer>month</billingFrequencyPer>						
                                                        <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                        <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                        <nextInvoiceBillingDatetime>2021-07-06T06:11:16+00:00</nextInvoiceBillingDatetime>						
                                                        <setupChargeCode/>						
                                                        <setupChargeAmount>0.00</setupChargeAmount>						
                                                        <recurringChargeCode>LARGE_RECURRING</recurringChargeCode>						
                                                        <recurringChargeAmount>20.00</recurringChargeAmount>						
                                                        <onChangeInitialBillHandler>next</onChangeInitialBillHandler>						
                                                        <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                        <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                        <createdDatetime>2021-06-01T01:00:01+00:00</createdDatetime>						
                                                        <items>							
                                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                    <name>Thousand Chars</name>								
                                                                    <quantityIncluded>1000</quantityIncluded>								
                                                                    <isPeriodic>1</isPeriodic>								
                                                                    <overageAmount>0.03</overageAmount>								
                                                                    <createdDatetime>2021-06-01T01:00:01+00:00</createdDatetime>								
                                                            </item>							
                                                        </items>						
                                                </plan>					
                                            </plans>				
                                            <gatewayToken>SIMULATED</gatewayToken>				
                                            <gatewayTokenAux/>				
                                            <gatewayAccount>					
                                                <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                                <gateway>Stripe_Simulator</gateway>					
                                                <type>cc</type>					
                                            </gatewayAccount>				
                                            <ccFirstName>Luc</ccFirstName>				
                                            <ccLastName>Customer4</ccLastName>				
                                            <ccCompany/>				
                                            <ccCountry>US</ccCountry>				
                                            <ccAddress/>				
                                            <ccCity/>				
                                            <ccState/>				
                                            <ccZip/>				
                                            <ccType>amex</ccType>				
                                            <ccLastFour>0002</ccLastFour>				
                                            <ccExpirationDate>2029-04-30</ccExpirationDate>				
                                            <ccEmail/>				
                                            <cancelType/>				
                                            <cancelReason/>				
                                            <canceledDatetime/>				
                                            <createdDatetime>2021-06-06T06:10:49+00:00</createdDatetime>				
                                            <items>					
                                                <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">						
                                                        <name>Thousand Chars</name>						
                                                        <quantity>45.87</quantity>						
                                                        <createdDatetime>2021-06-06T06:04:58+00:00</createdDatetime>						
                                                        <modifiedDatetime>2021-06-06T06:11:16+00:00</modifiedDatetime>						
                                                </item>					
                                            </items>				
                                            <invoices>					
                                                <invoice id="e76cb85b-c68c-11eb-bed7-0eff6b8b8fd3">						
                                                        <number>25</number>						
                                                        <type>subscription</type>						
                                                        <vatRate/>						
                                                        <taxRate/>						
                                                        <billingDatetime>2021-07-06T06:03:24+00:00</billingDatetime>						
                                                        <paidTransactionId/>						
                                                        <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>						
                                                        <charges>							
                                                            <charge id="" code="LARGE_RECURRING">								
                                                                    <type>recurring</type>								
                                                                    <quantity>1</quantity>								
                                                                    <eachAmount>20.00</eachAmount>								
                                                                    <description/>								
                                                                    <createdDatetime>2021-07-06T06:03:24+00:00</createdDatetime>								
                                                            </charge>							
                                                            <charge id="" code="thousand_chars">								
                                                                    <type>item</type>								
                                                                    <quantity>0</quantity>								
                                                                    <eachAmount>0.03</eachAmount>								
                                                                    <description/>								
                                                                    <createdDatetime>2021-06-06T06:11:16+00:00</createdDatetime>								
                                                            </charge>							
                                                        </charges>						
                                                </invoice>					
                                            </invoices>				
                                    </subscription>			
                                    <subscription id="3bb583d8-c68d-11eb-bed7-0eff6b8b8fd3">				
                                            <plans>					
                                                <plan id="66431ee6-c274-11eb-bed7-0eff6b8b8fd3" code="MEDIUM">						
                                                        <name>Medium</name>						
                                                        <displayName>Medium • 10.00 / Month</displayName>						
                                                        <description/>						
                                                        <isActive>1</isActive>						
                                                        <isFree>0</isFree>						
                                                        <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                        <trialDays>0</trialDays>						
                                                        <initialBillCount>0</initialBillCount>						
                                                        <initialBillCountUnit>days</initialBillCountUnit>						
                                                        <initialInvoiceBillingDatetime>2021-06-06T06:11:16+00:00</initialInvoiceBillingDatetime>						
                                                        <billingFrequency>monthly</billingFrequency>						
                                                        <billingFrequencyPer>month</billingFrequencyPer>						
                                                        <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                        <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                        <nextInvoiceBillingDatetime>2021-07-06T06:11:16+00:00</nextInvoiceBillingDatetime>						
                                                        <setupChargeCode/>						
                                                        <setupChargeAmount>0.00</setupChargeAmount>						
                                                        <recurringChargeCode>MEDIUM_RECURRING</recurringChargeCode>						
                                                        <recurringChargeAmount>10.00</recurringChargeAmount>						
                                                        <onChangeInitialBillHandler>next</onChangeInitialBillHandler>						
                                                        <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                        <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                        <createdDatetime>2021-06-01T00:57:55+00:00</createdDatetime>						
                                                        <items>							
                                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                    <name>Thousand Chars</name>								
                                                                    <quantityIncluded>500</quantityIncluded>								
                                                                    <isPeriodic>1</isPeriodic>								
                                                                    <overageAmount>0.00</overageAmount>								
                                                                    <createdDatetime>2021-06-01T00:57:55+00:00</createdDatetime>								
                                                            </item>							
                                                        </items>						
                                                </plan>					
                                            </plans>				
                                            <gatewayToken>SIMULATED</gatewayToken>				
                                            <gatewayTokenAux/>				
                                            <gatewayAccount>					
                                                <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                                <gateway>Stripe_Simulator</gateway>					
                                                <type>cc</type>					
                                            </gatewayAccount>				
                                            <ccFirstName>Luc</ccFirstName>				
                                            <ccLastName>Customer4</ccLastName>				
                                            <ccCompany/>				
                                            <ccCountry>US</ccCountry>				
                                            <ccAddress/>				
                                            <ccCity/>				
                                            <ccState/>				
                                            <ccZip/>				
                                            <ccType>amex</ccType>				
                                            <ccLastFour>0002</ccLastFour>				
                                            <ccExpirationDate>2029-04-30</ccExpirationDate>				
                                            <ccEmail/>				
                                            <cancelType/>				
                                            <cancelReason/>				
                                            <canceledDatetime/>				
                                            <createdDatetime>2021-06-06T06:05:45+00:00</createdDatetime>				
                                    </subscription>			
                                    <subscription id="e736c1ca-c68c-11eb-bed7-0eff6b8b8fd3">				
                                            <plans>					
                                                <plan id="56561361-c274-11eb-bed7-0eff6b8b8fd3" code="SMALL">						
                                                        <name>Small</name>						
                                                        <displayName>Small • 5.00 / Month</displayName>						
                                                        <description/>						
                                                        <isActive>1</isActive>						
                                                        <isFree>0</isFree>						
                                                        <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                        <trialDays>0</trialDays>						
                                                        <initialBillCount>0</initialBillCount>						
                                                        <initialBillCountUnit>days</initialBillCountUnit>						
                                                        <initialInvoiceBillingDatetime>2021-06-06T06:11:16+00:00</initialInvoiceBillingDatetime>						
                                                        <billingFrequency>monthly</billingFrequency>						
                                                        <billingFrequencyPer>month</billingFrequencyPer>						
                                                        <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                        <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                        <nextInvoiceBillingDatetime>2021-07-06T06:11:16+00:00</nextInvoiceBillingDatetime>						
                                                        <setupChargeCode/>						
                                                        <setupChargeAmount>0.00</setupChargeAmount>						
                                                        <recurringChargeCode>SMALL_RECURRING</recurringChargeCode>						
                                                        <recurringChargeAmount>5.00</recurringChargeAmount>						
                                                        <onChangeInitialBillHandler>next</onChangeInitialBillHandler>						
                                                        <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                        <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                        <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>						
                                                        <items>							
                                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                    <name>Thousand Chars</name>								
                                                                    <quantityIncluded>250</quantityIncluded>								
                                                                    <isPeriodic>1</isPeriodic>								
                                                                    <overageAmount>0.00</overageAmount>								
                                                                    <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>								
                                                            </item>							
                                                        </items>						
                                                </plan>					
                                            </plans>				
                                            <gatewayToken>SIMULATED</gatewayToken>				
                                            <gatewayTokenAux/>				
                                            <gatewayAccount>					
                                                <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                                <gateway>Stripe_Simulator</gateway>					
                                                <type>cc</type>					
                                            </gatewayAccount>				
                                            <ccFirstName>Luc</ccFirstName>				
                                            <ccLastName>Customer4</ccLastName>				
                                            <ccCompany/>				
                                            <ccCountry>US</ccCountry>				
                                            <ccAddress/>				
                                            <ccCity/>				
                                            <ccState/>				
                                            <ccZip/>				
                                            <ccType>amex</ccType>				
                                            <ccLastFour>0002</ccLastFour>				
                                            <ccExpirationDate>2029-04-30</ccExpirationDate>				
                                            <ccEmail/>				
                                            <cancelType/>				
                                            <cancelReason/>				
                                            <canceledDatetime/>				
                                            <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>				
                                            <invoices>					
                                                <invoice id="e7416930-c68c-11eb-bed7-0eff6b8b8fd3">						
                                                        <number>24</number>						
                                                        <type>subscription</type>						
                                                        <vatRate/>						
                                                        <taxRate/>						
                                                        <billingDatetime>2021-06-06T06:03:24+00:00</billingDatetime>						
                                                        <paidTransactionId>e753cc7c-c68c-11eb-bed7-0eff6b8b8fd3</paidTransactionId>						
                                                        <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>						
                                                        <charges>							
                                                            <charge id="e74509e1-c68c-11eb-bed7-0eff6b8b8fd3" code="SMALL_RECURRING">								
                                                                    <type>recurring</type>								
                                                                    <quantity>1</quantity>								
                                                                    <eachAmount>5.00</eachAmount>								
                                                                    <description/>								
                                                                    <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>								
                                                            </charge>							
                                                        </charges>						
                                                        <transactions>							
                                                            <transaction id="e753cc7c-c68c-11eb-bed7-0eff6b8b8fd3" code="">								
                                                                    <parentId/>								
                                                                    <gatewayToken>SIMULATED</gatewayToken>								
                                                                    <gatewayAccount>									
                                                                        <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>									
                                                                        <gateway>Stripe_Simulator</gateway>									
                                                                        <type>cc</type>									
                                                                    </gatewayAccount>								
                                                                    <amount>5.00</amount>								
                                                                    <memo/>								
                                                                    <response>approved</response>								
                                                                    <responseReason>SIMULATED approved payment</responseReason>								
                                                                    <transactedDatetime>2021-06-06T06:03:24+00:00</transactedDatetime>								
                                                                    <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>								
                                                            </transaction>							
                                                        </transactions>						
                                                </invoice>					
                                            </invoices>				
                                    </subscription>			
                                </subscriptions>		
                        </customer>	
                    </customers>"""

        actual_xml_data = self.utils.decode_customer_xml(xml_str)
        expected_xml_data = {
            'code': 'languagetools+customer4@mailc.net',
            'email': 'languagetools+customer4@mailc.net',
            'status': 'active',
            'thousand_char_quota': 1000,
            'thousand_char_overage_allowed': 1,
            'thousand_char_used': 45.87,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer4%40mailc.net&key=03ff591107',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer4%40mailc.net&key=03ff591107'
        }
        self.assertEqual(actual_xml_data, expected_xml_data)

    def test_decode_customer_xml_large_canceled_no_overage(self):
        xml_str = """<?xml version="1.0" ?><customers>	
                        <customer id="e72f0991-c68c-11eb-bed7-0eff6b8b8fd3" code="languagetools+customer4@mailc.net">		
                                <firstName>Luc</firstName>		
                                <lastName>Customer4</lastName>		
                                <company/>		
                                <email>languagetools+customer4@mailc.net</email>		
                                <notes/>		
                                <gatewayToken>SIMULATED</gatewayToken>		
                                <isTaxExempt>0</isTaxExempt>		
                                <isVatExempt>0</isVatExempt>		
                                <taxNumber/>		
                                <vatNumber/>		
                                <taxRate/>		
                                <firstContactDatetime/>		
                                <referer/>		
                                <refererHost/>		
                                <campaignSource/>		
                                <campaignMedium/>		
                                <campaignTerm/>		
                                <campaignContent/>		
                                <campaignName/>		
                                <key>03ff591107</key>		
                                <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>		
                                <modifiedDatetime>2021-06-06T06:03:24+00:00</modifiedDatetime>		
                                <metaData/>		
                                <subscriptions>			
                                    <subscription id="ee0849c9-c693-11eb-bed7-0eff6b8b8fd3">				
                                            <plans>					
                                                <plan id="b1a293e7-c274-11eb-bed7-0eff6b8b8fd3" code="LARGE">						
                                                        <name>Large</name>						
                                                        <displayName>Large • 20.00 / Month</displayName>						
                                                        <description/>						
                                                        <isActive>1</isActive>						
                                                        <isFree>0</isFree>						
                                                        <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                        <trialDays>0</trialDays>						
                                                        <initialBillCount>0</initialBillCount>						
                                                        <initialBillCountUnit>days</initialBillCountUnit>						
                                                        <initialInvoiceBillingDatetime>2021-06-06T06:55:48+00:00</initialInvoiceBillingDatetime>						
                                                        <billingFrequency>monthly</billingFrequency>						
                                                        <billingFrequencyPer>month</billingFrequencyPer>						
                                                        <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                        <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                        <nextInvoiceBillingDatetime>2021-07-06T06:55:48+00:00</nextInvoiceBillingDatetime>						
                                                        <setupChargeCode/>						
                                                        <setupChargeAmount>0.00</setupChargeAmount>						
                                                        <recurringChargeCode>LARGE_RECURRING</recurringChargeCode>						
                                                        <recurringChargeAmount>20.00</recurringChargeAmount>						
                                                        <onChangeInitialBillHandler>next</onChangeInitialBillHandler>						
                                                        <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                        <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                        <createdDatetime>2021-06-01T01:00:01+00:00</createdDatetime>						
                                                        <items>							
                                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                    <name>Thousand Chars</name>								
                                                                    <quantityIncluded>1000</quantityIncluded>								
                                                                    <isPeriodic>1</isPeriodic>								
                                                                    <overageAmount>0.03</overageAmount>								
                                                                    <createdDatetime>2021-06-01T01:00:01+00:00</createdDatetime>								
                                                            </item>							
                                                        </items>						
                                                </plan>					
                                            </plans>				
                                            <gatewayToken>SIMULATED</gatewayToken>				
                                            <gatewayTokenAux/>				
                                            <gatewayAccount>					
                                                <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                                <gateway>Stripe_Simulator</gateway>					
                                                <type>cc</type>					
                                            </gatewayAccount>				
                                            <ccFirstName>Luc</ccFirstName>				
                                            <ccLastName>Customer4</ccLastName>				
                                            <ccCompany/>				
                                            <ccCountry>US</ccCountry>				
                                            <ccAddress/>				
                                            <ccCity/>				
                                            <ccState/>				
                                            <ccZip/>				
                                            <ccType>amex</ccType>				
                                            <ccLastFour>0002</ccLastFour>				
                                            <ccExpirationDate>2024-01-31</ccExpirationDate>				
                                            <ccEmail/>				
                                            <cancelType>customer</cancelType>				
                                            <cancelReason/>				
                                            <canceledDatetime>2021-06-06T06:54:35+00:00</canceledDatetime>				
                                            <createdDatetime>2021-06-06T06:53:42+00:00</createdDatetime>				
                                            <items>					
                                                <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">						
                                                        <name>Thousand Chars</name>						
                                                        <quantity>45.87</quantity>						
                                                        <createdDatetime>2021-06-06T06:04:58+00:00</createdDatetime>						
                                                        <modifiedDatetime>2021-06-06T06:53:42+00:00</modifiedDatetime>						
                                                </item>					
                                            </items>				
                                            <invoices>					
                                                <invoice id="e76cb85b-c68c-11eb-bed7-0eff6b8b8fd3">						
                                                        <number>25</number>						
                                                        <type>subscription</type>						
                                                        <vatRate/>						
                                                        <taxRate/>						
                                                        <billingDatetime>2021-07-06T06:03:24+00:00</billingDatetime>						
                                                        <paidTransactionId/>						
                                                        <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>						
                                                        <charges>							
                                                            <charge id="" code="LARGE_RECURRING">								
                                                                    <type>recurring</type>								
                                                                    <quantity>1</quantity>								
                                                                    <eachAmount>20.00</eachAmount>								
                                                                    <description/>								
                                                                    <createdDatetime>2021-07-06T06:03:24+00:00</createdDatetime>								
                                                            </charge>							
                                                            <charge id="" code="thousand_chars">								
                                                                    <type>item</type>								
                                                                    <quantity>0</quantity>								
                                                                    <eachAmount>0.03</eachAmount>								
                                                                    <description/>								
                                                                    <createdDatetime>2021-06-06T06:53:42+00:00</createdDatetime>								
                                                            </charge>							
                                                        </charges>						
                                                </invoice>					
                                            </invoices>				
                                    </subscription>			
                                    <subscription id="44928d8f-c68f-11eb-bed7-0eff6b8b8fd3">				
                                            <plans>					
                                                <plan id="56561361-c274-11eb-bed7-0eff6b8b8fd3" code="SMALL">						
                                                        <name>Small</name>						
                                                        <displayName>Small • 5.00 / Month</displayName>						
                                                        <description/>						
                                                        <isActive>1</isActive>						
                                                        <isFree>0</isFree>						
                                                        <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                        <trialDays>0</trialDays>						
                                                        <initialBillCount>0</initialBillCount>						
                                                        <initialBillCountUnit>days</initialBillCountUnit>						
                                                        <initialInvoiceBillingDatetime>2021-06-06T06:55:48+00:00</initialInvoiceBillingDatetime>						
                                                        <billingFrequency>monthly</billingFrequency>						
                                                        <billingFrequencyPer>month</billingFrequencyPer>						
                                                        <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                        <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                        <nextInvoiceBillingDatetime>2021-07-06T06:55:48+00:00</nextInvoiceBillingDatetime>						
                                                        <setupChargeCode/>						
                                                        <setupChargeAmount>0.00</setupChargeAmount>						
                                                        <recurringChargeCode>SMALL_RECURRING</recurringChargeCode>						
                                                        <recurringChargeAmount>5.00</recurringChargeAmount>						
                                                        <onChangeInitialBillHandler>next</onChangeInitialBillHandler>						
                                                        <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                        <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                        <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>						
                                                        <items>							
                                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                    <name>Thousand Chars</name>								
                                                                    <quantityIncluded>250</quantityIncluded>								
                                                                    <isPeriodic>1</isPeriodic>								
                                                                    <overageAmount>0.00</overageAmount>								
                                                                    <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>								
                                                            </item>							
                                                        </items>						
                                                </plan>					
                                            </plans>				
                                            <gatewayToken>SIMULATED</gatewayToken>				
                                            <gatewayTokenAux/>				
                                            <gatewayAccount>					
                                                <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                                <gateway>Stripe_Simulator</gateway>					
                                                <type>cc</type>					
                                            </gatewayAccount>				
                                            <ccFirstName>Luc</ccFirstName>				
                                            <ccLastName>Customer4</ccLastName>				
                                            <ccCompany/>				
                                            <ccCountry>US</ccCountry>				
                                            <ccAddress/>				
                                            <ccCity/>				
                                            <ccState/>				
                                            <ccZip/>				
                                            <ccType>amex</ccType>				
                                            <ccLastFour>0002</ccLastFour>				
                                            <ccExpirationDate>2024-01-31</ccExpirationDate>				
                                            <ccEmail/>				
                                            <cancelType/>				
                                            <cancelReason/>				
                                            <canceledDatetime/>				
                                            <createdDatetime>2021-06-06T06:20:19+00:00</createdDatetime>				
                                    </subscription>			
                                    <subscription id="f0ad4f2c-c68d-11eb-bed7-0eff6b8b8fd3">				
                                            <plans>					
                                                <plan id="b1a293e7-c274-11eb-bed7-0eff6b8b8fd3" code="LARGE">						
                                                        <name>Large</name>						
                                                        <displayName>Large • 20.00 / Month</displayName>						
                                                        <description/>						
                                                        <isActive>1</isActive>						
                                                        <isFree>0</isFree>						
                                                        <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                        <trialDays>0</trialDays>						
                                                        <initialBillCount>0</initialBillCount>						
                                                        <initialBillCountUnit>days</initialBillCountUnit>						
                                                        <initialInvoiceBillingDatetime>2021-06-06T06:55:48+00:00</initialInvoiceBillingDatetime>						
                                                        <billingFrequency>monthly</billingFrequency>						
                                                        <billingFrequencyPer>month</billingFrequencyPer>						
                                                        <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                        <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                        <nextInvoiceBillingDatetime>2021-07-06T06:55:48+00:00</nextInvoiceBillingDatetime>						
                                                        <setupChargeCode/>						
                                                        <setupChargeAmount>0.00</setupChargeAmount>						
                                                        <recurringChargeCode>LARGE_RECURRING</recurringChargeCode>						
                                                        <recurringChargeAmount>20.00</recurringChargeAmount>						
                                                        <onChangeInitialBillHandler>next</onChangeInitialBillHandler>						
                                                        <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                        <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                        <createdDatetime>2021-06-01T01:00:01+00:00</createdDatetime>						
                                                        <items>							
                                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                    <name>Thousand Chars</name>								
                                                                    <quantityIncluded>1000</quantityIncluded>								
                                                                    <isPeriodic>1</isPeriodic>								
                                                                    <overageAmount>0.03</overageAmount>								
                                                                    <createdDatetime>2021-06-01T01:00:01+00:00</createdDatetime>								
                                                            </item>							
                                                        </items>						
                                                </plan>					
                                            </plans>				
                                            <gatewayToken>SIMULATED</gatewayToken>				
                                            <gatewayTokenAux/>				
                                            <gatewayAccount>					
                                                <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                                <gateway>Stripe_Simulator</gateway>					
                                                <type>cc</type>					
                                            </gatewayAccount>				
                                            <ccFirstName>Luc</ccFirstName>				
                                            <ccLastName>Customer4</ccLastName>				
                                            <ccCompany/>				
                                            <ccCountry>US</ccCountry>				
                                            <ccAddress/>				
                                            <ccCity/>				
                                            <ccState/>				
                                            <ccZip/>				
                                            <ccType>amex</ccType>				
                                            <ccLastFour>0002</ccLastFour>				
                                            <ccExpirationDate>2029-04-30</ccExpirationDate>				
                                            <ccEmail/>				
                                            <cancelType/>				
                                            <cancelReason/>				
                                            <canceledDatetime/>				
                                            <createdDatetime>2021-06-06T06:10:49+00:00</createdDatetime>				
                                    </subscription>			
                                    <subscription id="3bb583d8-c68d-11eb-bed7-0eff6b8b8fd3">				
                                            <plans>					
                                                <plan id="66431ee6-c274-11eb-bed7-0eff6b8b8fd3" code="MEDIUM">						
                                                        <name>Medium</name>						
                                                        <displayName>Medium • 10.00 / Month</displayName>						
                                                        <description/>						
                                                        <isActive>1</isActive>						
                                                        <isFree>0</isFree>						
                                                        <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                        <trialDays>0</trialDays>						
                                                        <initialBillCount>0</initialBillCount>						
                                                        <initialBillCountUnit>days</initialBillCountUnit>						
                                                        <initialInvoiceBillingDatetime>2021-06-06T06:55:48+00:00</initialInvoiceBillingDatetime>						
                                                        <billingFrequency>monthly</billingFrequency>						
                                                        <billingFrequencyPer>month</billingFrequencyPer>						
                                                        <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                        <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                        <nextInvoiceBillingDatetime>2021-07-06T06:55:48+00:00</nextInvoiceBillingDatetime>						
                                                        <setupChargeCode/>						
                                                        <setupChargeAmount>0.00</setupChargeAmount>						
                                                        <recurringChargeCode>MEDIUM_RECURRING</recurringChargeCode>						
                                                        <recurringChargeAmount>10.00</recurringChargeAmount>						
                                                        <onChangeInitialBillHandler>next</onChangeInitialBillHandler>						
                                                        <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                        <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                        <createdDatetime>2021-06-01T00:57:55+00:00</createdDatetime>						
                                                        <items>							
                                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                    <name>Thousand Chars</name>								
                                                                    <quantityIncluded>500</quantityIncluded>								
                                                                    <isPeriodic>1</isPeriodic>								
                                                                    <overageAmount>0.00</overageAmount>								
                                                                    <createdDatetime>2021-06-01T00:57:55+00:00</createdDatetime>								
                                                            </item>							
                                                        </items>						
                                                </plan>					
                                            </plans>				
                                            <gatewayToken>SIMULATED</gatewayToken>				
                                            <gatewayTokenAux/>				
                                            <gatewayAccount>					
                                                <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                                <gateway>Stripe_Simulator</gateway>					
                                                <type>cc</type>					
                                            </gatewayAccount>				
                                            <ccFirstName>Luc</ccFirstName>				
                                            <ccLastName>Customer4</ccLastName>				
                                            <ccCompany/>				
                                            <ccCountry>US</ccCountry>				
                                            <ccAddress/>				
                                            <ccCity/>				
                                            <ccState/>				
                                            <ccZip/>				
                                            <ccType>amex</ccType>				
                                            <ccLastFour>0002</ccLastFour>				
                                            <ccExpirationDate>2029-04-30</ccExpirationDate>				
                                            <ccEmail/>				
                                            <cancelType/>				
                                            <cancelReason/>				
                                            <canceledDatetime/>				
                                            <createdDatetime>2021-06-06T06:05:45+00:00</createdDatetime>				
                                    </subscription>			
                                    <subscription id="e736c1ca-c68c-11eb-bed7-0eff6b8b8fd3">				
                                            <plans>					
                                                <plan id="56561361-c274-11eb-bed7-0eff6b8b8fd3" code="SMALL">						
                                                        <name>Small</name>						
                                                        <displayName>Small • 5.00 / Month</displayName>						
                                                        <description/>						
                                                        <isActive>1</isActive>						
                                                        <isFree>0</isFree>						
                                                        <paymentMethodIsRequired>1</paymentMethodIsRequired>						
                                                        <trialDays>0</trialDays>						
                                                        <initialBillCount>0</initialBillCount>						
                                                        <initialBillCountUnit>days</initialBillCountUnit>						
                                                        <initialInvoiceBillingDatetime>2021-06-06T06:55:48+00:00</initialInvoiceBillingDatetime>						
                                                        <billingFrequency>monthly</billingFrequency>						
                                                        <billingFrequencyPer>month</billingFrequencyPer>						
                                                        <billingFrequencyUnit>months</billingFrequencyUnit>						
                                                        <billingFrequencyQuantity>1</billingFrequencyQuantity>						
                                                        <nextInvoiceBillingDatetime>2021-07-06T06:55:48+00:00</nextInvoiceBillingDatetime>						
                                                        <setupChargeCode/>						
                                                        <setupChargeAmount>0.00</setupChargeAmount>						
                                                        <recurringChargeCode>SMALL_RECURRING</recurringChargeCode>						
                                                        <recurringChargeAmount>5.00</recurringChargeAmount>						
                                                        <onChangeInitialBillHandler>next</onChangeInitialBillHandler>						
                                                        <setupChargeBillHandler>now</setupChargeBillHandler>						
                                                        <onChangeSetupChargeBillHandler>no</onChangeSetupChargeBillHandler>						
                                                        <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>						
                                                        <items>							
                                                            <item id="382ca6fd-c274-11eb-bed7-0eff6b8b8fd3" code="thousand_chars">								
                                                                    <name>Thousand Chars</name>								
                                                                    <quantityIncluded>250</quantityIncluded>								
                                                                    <isPeriodic>1</isPeriodic>								
                                                                    <overageAmount>0.00</overageAmount>								
                                                                    <createdDatetime>2021-06-01T00:57:28+00:00</createdDatetime>								
                                                            </item>							
                                                        </items>						
                                                </plan>					
                                            </plans>				
                                            <gatewayToken>SIMULATED</gatewayToken>				
                                            <gatewayTokenAux/>				
                                            <gatewayAccount>					
                                                <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>					
                                                <gateway>Stripe_Simulator</gateway>					
                                                <type>cc</type>					
                                            </gatewayAccount>				
                                            <ccFirstName>Luc</ccFirstName>				
                                            <ccLastName>Customer4</ccLastName>				
                                            <ccCompany/>				
                                            <ccCountry>US</ccCountry>				
                                            <ccAddress/>				
                                            <ccCity/>				
                                            <ccState/>				
                                            <ccZip/>				
                                            <ccType>amex</ccType>				
                                            <ccLastFour>0002</ccLastFour>				
                                            <ccExpirationDate>2029-04-30</ccExpirationDate>				
                                            <ccEmail/>				
                                            <cancelType/>				
                                            <cancelReason/>				
                                            <canceledDatetime/>				
                                            <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>				
                                            <invoices>					
                                                <invoice id="e7416930-c68c-11eb-bed7-0eff6b8b8fd3">						
                                                        <number>24</number>						
                                                        <type>subscription</type>						
                                                        <vatRate/>						
                                                        <taxRate/>						
                                                        <billingDatetime>2021-06-06T06:03:24+00:00</billingDatetime>						
                                                        <paidTransactionId>e753cc7c-c68c-11eb-bed7-0eff6b8b8fd3</paidTransactionId>						
                                                        <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>						
                                                        <charges>							
                                                            <charge id="e74509e1-c68c-11eb-bed7-0eff6b8b8fd3" code="SMALL_RECURRING">								
                                                                    <type>recurring</type>								
                                                                    <quantity>1</quantity>								
                                                                    <eachAmount>5.00</eachAmount>								
                                                                    <description/>								
                                                                    <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>								
                                                            </charge>							
                                                        </charges>						
                                                        <transactions>							
                                                            <transaction id="e753cc7c-c68c-11eb-bed7-0eff6b8b8fd3" code="">								
                                                                    <parentId/>								
                                                                    <gatewayToken>SIMULATED</gatewayToken>								
                                                                    <gatewayAccount>									
                                                                        <id>71e29c22-bceb-11eb-bed7-0eff6b8b8fd3</id>									
                                                                        <gateway>Stripe_Simulator</gateway>									
                                                                        <type>cc</type>									
                                                                    </gatewayAccount>								
                                                                    <amount>5.00</amount>								
                                                                    <memo/>								
                                                                    <response>approved</response>								
                                                                    <responseReason>SIMULATED approved payment</responseReason>								
                                                                    <transactedDatetime>2021-06-06T06:03:24+00:00</transactedDatetime>								
                                                                    <createdDatetime>2021-06-06T06:03:24+00:00</createdDatetime>								
                                                            </transaction>							
                                                        </transactions>						
                                                </invoice>					
                                            </invoices>				
                                    </subscription>			
                                </subscriptions>		
                        </customer>	
                    </customers>"""

        actual_xml_data = self.utils.decode_customer_xml(xml_str)
        expected_xml_data = {
            'code': 'languagetools+customer4@mailc.net',
            'email': 'languagetools+customer4@mailc.net',
            'status': 'canceled',
            'thousand_char_quota': 1000,
            'thousand_char_overage_allowed': 0,
            'thousand_char_used': 45.87,
            'cancel_url': 'https://languagetools-dev-local.chargevault.com/cancel?code=languagetools%2Bcustomer4%40mailc.net&key=03ff591107',
            'update_url': 'https://languagetools-dev-local.chargevault.com/update?code=languagetools%2Bcustomer4%40mailc.net&key=03ff591107'
        }
        self.assertEqual(actual_xml_data, expected_xml_data)        