from ehr_functions.features import codes
import unittest
import pandas as pd


class CodesTest(unittest.TestCase):

    @staticmethod
    def test_convert_to_icd10():
        df = pd.DataFrame({
            'PatientID': [1, 2, 3, 4],
            'Diagnosis1': ['0011', 'A009', '0053', '0065'],
            'Diagnosis2': ['A014', '00844', None, None],
            'Diagnosis3': [None, None, '0011', None],
        })

        result = codes.convert_to_icd10(df)

        pd.testing.assert_frame_equal(result, pd.DataFrame({
            'PatientID': [1, 2, 3, 4],
            'Diagnosis1': ['A001', 'A009', 'A058', 'A066'],
            'Diagnosis2': ['A014', 'A046', None, None],
            'Diagnosis3': [None, None, 'A001', None],
        }))

    @staticmethod
    def test_convert_to_icd9():
        df = pd.DataFrame({
            'PatientID': [1, 2, 3, 4],
            'Diagnosis1': ['0011', 'A009', '0053', '0065'],
            'Diagnosis2': ['A014', '00844', None, None],
            'Diagnosis3': [None, None, '0011', None],
        })

        result = codes.convert_to_icd9(df)

        pd.testing.assert_frame_equal(result, pd.DataFrame({
            'PatientID': [1, 2, 3, 4],
            'Diagnosis1': ['0011', '0019', '0053', '0065'],
            'Diagnosis2': ['0029', '00844', None, None],
            'Diagnosis3': [None, None, '0011', None],
        }))

    @staticmethod
    def test_clean():
        df = pd.DataFrame({
            'PatientID': [1, 2, 3, 4],
            'Diagnosis1': ['0011 ', 'A00912  ', ' 0053', ' 0065 '],
            'Diagnosis2': ['A014 1', '008.44', None, None],
            'Diagnosis3': [None, None, '0011', None],
        })

        result = codes.clean(df)

        pd.testing.assert_frame_equal(result, pd.DataFrame({
            'PatientID': [1, 2, 3, 4],
            'Diagnosis1': ['0011', 'A00912', '0053', '0065'],
            'Diagnosis2': ['A014', '00844', None, None],
            'Diagnosis3': [None, None, '0011', None],
        }))

    @staticmethod
    def test_simplify():
        df = pd.DataFrame({
            'PatientID': [1, 2, 3, 4],
            'Diagnosis1': ['0011', 'A00912', '0053', '0065'],
            'Diagnosis2': ['A014', '00844', None, None],
            'Diagnosis3': [None, None, '0011', None],
        })

        result = codes.simplify(df)

        pd.testing.assert_frame_equal(result, pd.DataFrame({
            'PatientID': [1, 2, 3, 4],
            'Diagnosis1': ['001', 'A00', '005', '006'],
            'Diagnosis2': ['A01', '008', None, None],
            'Diagnosis3': [None, None, '001', None],
        }))

    def test_get_ccs_mapping(self):
        with self.assertRaises(ValueError):
            codes.get_ccs_mapping('2', level=5)

    @staticmethod
    def test_get_ccs_mapping_10():
        assert codes.get_ccs_mapping('2') == ['A021', 'A207', 'A227', 'A267', 'A327', 'A392', 'A393', 'A394', 'A400',
                                              'A401', 'A403', 'A408', 'A409', 'A4101', 'A4102', 'A411', 'A412', 'A413',
                                              'A414', 'A4150', 'A4151', 'A4152', 'A4153', 'A4159', 'A4181', 'A4189',
                                              'A419',
                                              'A427', 'A5486', 'B007', 'B377', 'I76', 'P360', 'P3610', 'P3619', 'P362',
                                              'P3630', 'P3639', 'P364', 'P365', 'P368', 'P369', 'R6520']

        assert codes.get_ccs_mapping('4', level=1) == ['D500', 'D501', 'D508', 'D509', 'D510', 'D511', 'D512', 'D513',
                                                       'D518', 'D519', 'D520', 'D521', 'D528', 'D529', 'D530', 'D531',
                                                       'D532', 'D538', 'D539', 'D550', 'D551', 'D552', 'D553', 'D558',
                                                       'D559', 'D560', 'D561', 'D562', 'D563', 'D564', 'D565', 'D568',
                                                       'D569', 'D580', 'D581', 'D582', 'D588', 'D589', 'D590', 'D591',
                                                       'D592', 'D593', 'D594', 'D595', 'D596', 'D598', 'D599', 'D600',
                                                       'D601', 'D608', 'D609', 'D6101', 'D6109', 'D611', 'D612', 'D613',
                                                       'D61810', 'D61811', 'D61818', 'D6182', 'D6189', 'D619', 'D630',
                                                       'D631', 'D638', 'D640', 'D641', 'D642', 'D643', 'D644', 'D6489',
                                                       'D649', 'Z8631', 'D62', 'D5700', 'D5701', 'D5702', 'D571',
                                                       'D5720',
                                                       'D57211', 'D57212', 'D57219', 'D573', 'D5740', 'D57411',
                                                       'D57412',
                                                       'D57419', 'D5780', 'D57811', 'D57812', 'D57819', 'D65', 'D66',
                                                       'D67',
                                                       'D680', 'D681', 'D682', 'D68311', 'D68312', 'D68318', 'D6832',
                                                       'D684', 'D6851', 'D6852', 'D6859', 'D6861', 'D6862', 'D6869',
                                                       'D688',
                                                       'D689', 'D690', 'D691', 'D692', 'D693', 'D6941', 'D6942',
                                                       'D6949',
                                                       'D6959', 'D696', 'D698', 'D699', 'D7582', 'R233', 'D700', 'D701',
                                                       'D702', 'D703', 'D704', 'D708', 'D709', 'D71', 'D720', 'D721',
                                                       'D72810', 'D72818', 'D72819', 'D72820', 'D72821', 'D72822',
                                                       'D72823',
                                                       'D72824', 'D72825', 'D72828', 'D72829', 'D7289', 'D729', 'D7381',
                                                       'D761', 'D762', 'D763', 'D730', 'D731', 'D732', 'D733', 'D734',
                                                       'D735', 'D7389', 'D739', 'D740', 'D748', 'D749', 'D750', 'D751',
                                                       'D7581', 'D7589', 'D759', 'D77', 'R700', 'R701', 'R710', 'R718',
                                                       'R770', 'R771', 'R772', 'R778', 'R779', 'Z862']

        assert codes.get_ccs_mapping('4.3', level=2) == ['D700', 'D701', 'D702', 'D703', 'D704', 'D708', 'D709', 'D71',
                                                         'D720', 'D721', 'D72810', 'D72818', 'D72819', 'D72820',
                                                         'D72821',
                                                         'D72822', 'D72823', 'D72824', 'D72825', 'D72828', 'D72829',
                                                         'D7289', 'D729', 'D7381', 'D761', 'D762', 'D763']

        part_2_3 = ['C3400', 'C3401', 'C3402', 'C3410', 'C3411', 'C3412', 'C342', 'C3430', 'C3431', 'C3432', 'C3480',
                    'C3481', 'C3482', 'C3490', 'C3491', 'C3492', 'C7A090', 'D0220', 'D0221', 'D0222', 'Z85118']
        part_4_3 = ['D700', 'D701', 'D702', 'D703', 'D704', 'D708', 'D709', 'D71', 'D720', 'D721', 'D72810', 'D72818',
                    'D72819', 'D72820', 'D72821', 'D72822', 'D72823', 'D72824', 'D72825', 'D72828', 'D72829', 'D7289',
                    'D729', 'D7381', 'D761', 'D762', 'D763']
        result = {}
        for code in part_2_3:
            result[code] = '2.3'
        for code in part_4_3:
            result[code] = '4.3'
        assert codes.get_ccs_mapping(['2.3', '4.3'], level=2) == result

    @staticmethod
    def test_get_ccs_mapping_9():
        assert codes.get_ccs_mapping('2', code_type=9) == ['0031', '0202', '0223', '0362', '0380', '0381', '03810',
                                                           '03811',
                                                           '03812', '03819', '0382', '0383', '03840', '03841', '03842',
                                                           '03843', '03844', '03849', '0388', '0389', '0545', '449',
                                                           '77181', '7907', '99591', '99592']

        assert codes.get_ccs_mapping('2.1.1', level=3, code_type=9) == ['1530', '1531', '1532', '1533', '1534', '1535',
                                                                        '1536', '1537', '1538', '1539', '1590', '20910',
                                                                        '20911', '20912', '20913', '20914', '20915',
                                                                        '20916', '2303', 'V1005']

        part_11_6_4 = ['65610', '65611', '65613']
        part_11_6_5 = ['65640', '65641', '65643']
        result = {}
        for code in part_11_6_4:
            result[code] = '11.6.4'
        for code in part_11_6_5:
            result[code] = '11.6.5'
        assert codes.get_ccs_mapping(['11.6.4', '11.6.5'], level=3, code_type=9) == result
