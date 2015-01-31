from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=200)

class Domain(models.Model):
    # will have a set of scenarios
    client = models.ForeignKey(Client)
    name = models.CharField(max_length=200)

class TestResult(models.Model):
    expectation = models.CharField(max_length=200)
    actual = models.CharField(max_length=200)
    success = models.BooleanField(default=False)

class TestBase(models.Model):
    start_time = models.DateTimeField(auto_now_add=True, blank=True)
    end_time = models.DateTimeField(auto_now_add=True, blank=True)

class TestRun(TestBase):
    # Has a set of testcases that have a foreign-key reference to TestRun
    # domains will be accessible via the testcase set's domain fk
    # testresults will be accessible via the testcase set's testresult
    scenarios_only = models.BooleanField(default=False)
    content_checks_only = models.BooleanField(default=False)

    def __unicode__(self):
        domain_str = ','.join(self.domains())
        if self.scenarios_only:
            scope_str = 'scenarios only'
        elif self.content_checks_only:
            scope_str = 'content checks only'
        else:
            scope_str = 'scenarios and content checks'
        return 'Test Run {}: Running {} against {}'.format(self.id, scope_str, domain_str)

    def domains(self):
        return [tc.domain for tc in self.testcase_set.all()]

class TestCase(TestBase):
    # Has a set of validations that have a foreign-key reference to TestCase
    testrun = models.ForeignKey(TestRun)
    testresult = models.ForeignKey(TestResult)
    domain = models.ForeignKey(Domain)

class Validation(TestResult):
    testcase = models.ForeignKey(TestCase)
