#   Copyright 2011 David Malcolm <dmalcolm@redhat.com>
#   Copyright 2011 Red Hat, Inc.
#
#   This is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see
#   <http://www.gnu.org/licenses/>.

# Verify that we can extract constants correctly back to python

import gcc
import gccutils

def on_finish_unit():
    vars = gccutils.get_variables_as_dict()
    for name in sorted(vars):
        var = vars[name]
        assert isinstance(var.decl.initial, gcc.IntegerCst)
        print '%s: %s' % (name, hex(var.decl.initial.constant))

gcc.register_callback(gcc.PLUGIN_FINISH_UNIT,
                      on_finish_unit)