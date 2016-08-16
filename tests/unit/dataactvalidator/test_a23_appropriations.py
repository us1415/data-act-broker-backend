from dataactcore.models.stagingModels import Appropriation
from dataactcore.models.jobModels import Submission
from dataactcore.models.domainModels import SF133
from tests.unit.dataactvalidator.utils import insert_submission, run_sql_rule


_FILE = 'a23_appropriations'
_TAS = 'a23_appropriations_tas'


def test_success(database):
    """ Tests that SF 133 amount sum for line 2500 matches Appropriation status_of_budgetary_resour_cpe
        for the specified fiscal year and period """
    tas = "".join([_TAS, "_success"])

    sf = SF133(line=2500, tas=tas, period=1, fiscal_year=2016, amount=1, agency_identifier="sys",
               main_account_code="000", sub_account_code="000")
    ap = Appropriation(job_id=1, row_number=1, tas=tas, status_of_budgetary_resour_cpe=1)

    assert run_sql_rule(_FILE, database.stagingDb, models=[sf, ap]) == 0


def test_failure(database):
    """ Tests that SF 133 amount sum for line 2500 does not match Appropriation status_of_budgetary_resour_cpe
        for the specified fiscal year and period """
    tas = "".join([_TAS, "_failure"])

    sf = SF133(line=2500, tas=tas, period=1, fiscal_year=2016, amount=1, agency_identifier="sys",
               main_account_code="000", sub_account_code="000")
    ap = Appropriation(job_id=1, row_number=1, tas=tas, status_of_budgetary_resour_cpe=0)

    assert run_sql_rule(_FILE, database.stagingDb, models=[sf, ap]) == 1

