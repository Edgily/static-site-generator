import unittest


class CustomTestResult(unittest.TextTestResult):
    def __init__(self, stream, descriptions, verbosity):
        super().__init__(stream, descriptions, verbosity)
        self.successes = []
        self.failures = []
        self.errors = []

    def addSuccess(self, test):
        self.stream.write(
            f"{test.__class__.__name__}: ({test._testMethodName}) ... ok\n"
        )
        self.successes.append(test)

    def addFailure(self, test, err):
        self.stream.write(
            f"{test.__class__.__name__}: ({test._testMethodName}) ... FAIL\n"
        )
        self.failures.append((test, self._exc_info_to_string(err, test)))

    def addError(self, test, err):
        self.stream.write(
            f"{test.__class__.__name__}: ({test._testMethodName}) ... ERROR\n"
        )
        self.errors.append((test, self._exc_info_to_string(err, test)))


class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.discover(
        start_dir="src", pattern="test_*.py"
    )  # Adjust pattern if needed
    runner = CustomTestRunner()
    runner.run(suite)
