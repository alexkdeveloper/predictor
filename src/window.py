# window.py
#
# Copyright 2023 Alex
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import random

from gi.repository import Adw
from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import Gio


@Gtk.Template(resource_path='/io/github/alexkdeveloper/predictor/window.ui')
class PredictorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'PredictorWindow'

    label = Gtk.Template.Child()
    button = Gtk.Template.Child()
    revealer = Gtk.Template.Child()

    arr_str = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.button.connect('clicked', self.on_button_clicked)

        settings = Gio.Settings(schema_id="io.github.alexkdeveloper.predictor")

        settings.bind("width", self, "default-width", Gio.SettingsBindFlags.DEFAULT)
        settings.bind("height", self, "default-height", Gio.SettingsBindFlags.DEFAULT)
        settings.bind("is-maximized", self, "maximized", Gio.SettingsBindFlags.DEFAULT)
        settings.bind("is-fullscreen", self, "fullscreened", Gio.SettingsBindFlags.DEFAULT)

        self.arr_str.append(_("It is certain."))
        self.arr_str.append(_("It is decidedly so."))
        self.arr_str.append(_("Without a doubt."))
        self.arr_str.append(_("Yes—definitely."))
        self.arr_str.append(_("You may rely on it."))
        self.arr_str.append(_("As I see it, yes."))
        self.arr_str.append(_("Most likely."))
        self.arr_str.append(_("Outlook good."))
        self.arr_str.append(_("Yes."))
        self.arr_str.append(_("Signs point to yes."))
        self.arr_str.append(_("Yep!"))
        self.arr_str.append(_("Absolutely!"))
        self.arr_str.append(_("You bet!"))
        self.arr_str.append(_("Confirmed."))
        self.arr_str.append(_("Don’t count on it."))
        self.arr_str.append(_("My reply is no."))
        self.arr_str.append(_("My sources say no."))
        self.arr_str.append(_("Outlook not so good."))
        self.arr_str.append(_("Very doubtful."))
        self.arr_str.append(_("Naw."))
        self.arr_str.append(_("I’ve got a bad feeling about this…"))
        self.arr_str.append(_("Reply hazy, try again."))
        self.arr_str.append(_("Ask again later."))
        self.arr_str.append(_("Better not tell you now."))
        self.arr_str.append(_("Cannot predict now."))
        self.arr_str.append(_("Concentrate and ask again."))
        self.arr_str.append(_("Impossible to see, the future is."))
        self.arr_str.append(_("404 Answer Not Found"))

        GLib.timeout_add(1000, self.after_timeout)


    def on_button_clicked(self, widget):

        self.revealer.set_reveal_child(not self.revealer.get_child_revealed)

        GLib.timeout_add(6000, self.after_timeout)

        self.button.set_sensitive(False)


    def after_timeout(self):

        self.revealer.set_reveal_child(self.revealer.get_child_revealed)

        rand = random.randint(0, 27)

        self.label.set_text(self.arr_str[rand])

        self.label.remove_css_class('success')
        self.label.remove_css_class('error')
        self.label.remove_css_class('warning')

        if rand < 14:
           self.label.add_css_class('success')
        elif rand > 13 and rand < 21:
           self.label.add_css_class('error')
        else:
           self.label.add_css_class('warning')

        if self.revealer.get_child_revealed:
           self.button.set_sensitive(True)
           self.button.grab_focus()

