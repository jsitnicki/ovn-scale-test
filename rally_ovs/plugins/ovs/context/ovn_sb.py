# Copyright 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import six
from rally.common.i18n import _
from rally.common import logging
from rally import consts
from rally.task import context
import rally_ovs.plugins.ovs as ovs

LOG = logging.getLogger(__name__)


@context.configure(name="ovn_sb", order=120)
class OvnSouthboundContext(context.Context):
    CONFIG_SCHEMA = {
        "type": "object",
        "$schema": consts.JSON_SCHEMA,
        "properties": {
        },
        "additionalProperties": True
    }

    DEFAULT_CONFIG = {
    }

    @logging.log_task_wrapper(LOG.info, _("Enter context: `ovn_sb`"))
    def setup(self):

        controller = self.context["ovn_multihost"]["controller"]
        info = six.next(six.itervalues(controller))
        ovn_sbctl = getattr(ovs.ovsclients.Clients(info["credential"]), "ovn-sbctl")()
        ovn_sbctl.set_sandbox("controller-sandbox")
        chassis = ovn_sbctl.chassis_list()

        self.context["ovn-sb"] = chassis

    @logging.log_task_wrapper(LOG.info, _("Exit context: `ovn_sb`"))
    def cleanup(self):
        pass
