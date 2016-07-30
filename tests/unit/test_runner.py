# Copyright 2016 Rackspace
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import testtools

import syntribos.config
from syntribos.runner import Runner
import syntribos.tests

syntribos.config.register_opts()


class RunnerUnittest(testtools.TestCase):

    r = Runner()
    common_endings = ["BODY", "HEADERS", "PARAMS", "URL"]

    def _compare_tests(self, expected, loaded):
        """Compare list of expected test names with those that were loaded."""
        loaded_test_names = []
        for name, test in loaded:
            self.assertIn(name, expected)
            loaded_test_names.append(name)
        self.assertEqual(expected, loaded_test_names)

    def test_get_LDAP_tests(self):
        """Check that we get the proper LDAP tests."""
        expected = ["LDAP_INJECTION_" + x for x in self.common_endings]
        loaded_tests = self.r.get_tests(["LDAP"])
        self._compare_tests(expected, loaded_tests)

    def test_get_SQL_tests(self):
        """Check that we get the proper SQLi tests."""
        expected = ["SQL_INJECTION_" + x for x in self.common_endings]
        loaded_tests = self.r.get_tests(["SQL"])
        self._compare_tests(expected, loaded_tests)

    def test_get_XXE_tests(self):
        """Check that we get the proper XXE tests."""
        expected = ["XML_EXTERNAL_ENTITY_BODY"]
        loaded_tests = self.r.get_tests(["XML"])
        self._compare_tests(expected, loaded_tests)

    def test_get_int_overflow_tests(self):
        """Check that we get the proper integer overflow tests."""
        expected = ["INT_OVERFLOW_" + x for x in self.common_endings]
        loaded_tests = self.r.get_tests(["INT_OVERFLOW"])
        self._compare_tests(expected, loaded_tests)

    def test_get_buffer_overflow_tests(self):
        """Check that we get the proper buffer overflow tests."""
        expected = ["BUFFER_OVERFLOW_" + x for x in self.common_endings]
        loaded_tests = self.r.get_tests(["BUFFER_OVERFLOW"])
        self._compare_tests(expected, loaded_tests)

    def test_get_command_injection_tests(self):
        """Check that we get the proper command injection tests."""
        expected = ["COMMAND_INJECTION_" + x for x in self.common_endings]
        loaded_tests = self.r.get_tests(["COMMAND_INJECTION"])
        self._compare_tests(expected, loaded_tests)

    def test_get_string_validation_tests(self):
        """Check that we get the proper string validation tests."""
        expected = [
            "STRING_VALIDATION_VULNERABILITY_" + x for x in self.common_endings
        ]
        loaded_tests = self.r.get_tests(["STRING_VALIDATION"])
        self._compare_tests(expected, loaded_tests)

    def test_get_xss_test(self):
        """Check that we get only the XSS_BODY test from get_tests."""
        expected = ["XSS_BODY"]
        loaded_tests = self.r.get_tests(["XSS"])
        self._compare_tests(expected, loaded_tests)

    def test_get_ssl_test(self):
        """Check that we get only the SSL test from get_tests."""
        expected = ["SSL"]
        loaded_tests = self.r.get_tests(["SSL"])
        self._compare_tests(expected, loaded_tests)

    def test_get_cors_test(self):
        """Check that we get only the CORS_HEADER test from get_tests."""
        expected = ["CORS_HEADER"]
        loaded_tests = self.r.get_tests(["CORS_HEADER"])
        self._compare_tests(expected, loaded_tests)

    def test_log_path_caching(self):
        """Check that we get the same log file name every time."""
        res1 = self.r.get_log_file_name()
        res2 = self.r.get_log_file_name()
        self.assertEqual(res1, res2)