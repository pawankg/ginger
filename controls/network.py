#
# Project Ginger
#
# Copyright IBM, Corp. 2014
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

from cfginterfaces import Cfginterfaces
from interfaces import Interfaces
from wok.control.base import Resource


class Network(Resource):

    def __init__(self, model):
        super(Network, self).__init__(model, None)
        self.role_key = "administration"
        self.admin_methods = ['PUT']
        self.interfaces = Interfaces(model)
        self.cfginterfaces = Cfginterfaces(model)
        self.uri_fmt = '/network/%s'
        self.update_params = ['nameservers', 'gateway']
        self.confirm_change = self.generate_action_handler('confirm_change')

    @property
    def data(self):
        return self.info
