# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2018-2021 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Provide a report on why a step is outdated."""

from craft_parts.steps import Step
from craft_parts.utils import formatting_utils


class OutdatedReport:
    """The OutdatedReport class explains why a given step is outdated.

    An outdated step is defined to be a step that has run, but since doing so
    one of the following things have happened:

    - A step earlier in the lifecycle has run again.
    - The source on disk has been updated.
    """

    def __init__(
        self, *, previous_step_modified: Step = None, source_modified: bool = False
    ) -> None:
        """Create a new OutdatedReport.

        :param previous_step_modified: Step earlier in the lifecycle that has changed.
        :param source_modified: Whether the source changed on disk.
        """
        self.previous_step_modified = previous_step_modified
        self.source_modified = source_modified

    def reason(self) -> str:
        """Get summarized report.

        :return: Short summary of why the step is outdated.
        """
        reasons = []

        if self.previous_step_modified:
            reasons.append("{!r} step".format(self.previous_step_modified.name))

        if self.source_modified:
            reasons.append("source")

        if not reasons:
            return ""

        return "{} changed".format(formatting_utils.humanize_list(reasons, "and", "{}"))