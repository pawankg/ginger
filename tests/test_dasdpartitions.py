#
# Project Ginger
#
# Copyright IBM, Corp. 2015
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA

import mock
import re
import unittest

from wok import config
from wok.objectstore import ObjectStore

import wok.plugins.ginger.models.dasdpartitions as partitions


class DASDPartitionsTests(unittest.TestCase):
    def setUp(self):
        objstore_loc = config.get_object_store() + '_ginger'
        self._objstore = ObjectStore(objstore_loc)

    def test_get_list(self):
        dasd_partitions = partitions.DASDPartitionsModel()
        dasd_part_list = dasd_partitions.get_list()
        self.assertGreaterEqual(len(dasd_part_list), 0)

    @mock.patch('wok.plugins.ginger.models.dasd_utils._create_dasd_part', autospec=True)
    def test_create_part(self, mock_create_part):
        parts = partitions.DASDPartitionsModel()
        dev = 'dasdb'
        size = '10'
        params = {'dev_name': dev, 'size': size}
        parts.create(params)
        mock_create_part.return_value = 'dasdb'
        mock_create_part.assert_called_with(dev, size)

    @mock.patch('wok.plugins.ginger.models.dasd_utils._delete_dasd_part', autospec=True)
    def test_delete_part(self, mock_delete_part):
        part = partitions.DASDPartitionModel()
        part_name = 'dasdb2'
        name_split = re.split('(\D+)', part_name, flags=re.IGNORECASE)
        dev_name = name_split[1]
        part_num = name_split[2]
        part.delete(part_name)
        mock_delete_part.assert_called_with(dev_name, part_num)
