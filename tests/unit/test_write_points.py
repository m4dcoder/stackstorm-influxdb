# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from st2forge.packs import tests as forge_tests
from actions import write_points


class WritePointsActionTest(forge_tests.BaseActionTest):

    def test_logging(self):
        write_points.WritePointsAction(dict(), logger=self.logger)

        self.assertIn(
            'Instantiating WritePointsAction...',
            self.log_stream.getvalue()
        )  

    def test_instance_default(self):
        action = write_points.WritePointsAction(dict(), logger=self.logger)

        self.assertEqual(['localhost'], action.hosts)
        self.assertEqual(8086, action.port)
        self.assertIsNone(action.username)
        self.assertIsNone(action.password)

    def test_instance_with_config(self):
        config = {
            'hosts': ['gotham'],
            'port': 8987,
            'username': 'alfred',
            'password': 'butler'
        }

        action = write_points.WritePointsAction(config, logger=self.logger)

        self.assertEqual(config['hosts'], action.hosts)
        self.assertEqual(config['port'], action.port)
        self.assertEqual(config['username'], action.username)
        self.assertEqual(config['password'], action.password)

    def test_instance_bad_hosts_value(self):
        config = {
            'hosts': 'gotham'
        }

        self.assertRaises(
            ValueError,
            write_points.WritePointsAction,
            config,
            logger=self.logger
        )

    def test_instance_bad_port_value(self):
        config = {
            'port': 'abcdef'
        }

        self.assertRaises(
            ValueError,
            write_points.WritePointsAction,
            config,
            logger=self.logger
        )
