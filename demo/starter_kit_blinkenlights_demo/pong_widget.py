# -*- coding: utf-8 -*-
"""
Starter Kit: Blinkenlights Demo Application
Copyright (C) 2013 Olaf Lüke <olaf@tinkerforge.com>
Copyright (C) 2013-2015 Matthias Bolte <matthias@tinkerforge.com>

pong_widget.py: Widget for Pong example

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

from threading import Thread

from PyQt5.QtWidgets import QWidget

import starter_kit_blinkenlights_demo.config as config
from starter_kit_blinkenlights_demo.ui_pong import Ui_Pong
from starter_kit_blinkenlights_demo.pong import Pong


class PongWidget(QWidget, Ui_Pong):
    pong = None
    thread = None

    def __init__(self, parent, app):
        super().__init__()
        self.app = app

        self.setupUi(self)

        self.button_a.pressed.connect(lambda: self.button_press('a'))
        self.button_s.pressed.connect(lambda: self.button_press('s'))
        self.button_k.pressed.connect(lambda: self.button_press('k'))
        self.button_l.pressed.connect(lambda: self.button_press('l'))
        self.button_r.pressed.connect(lambda: self.button_press('r'))

    def start_pong(self):
        self.pong = Pong(self.app.ipcon)

        if self.pong.okay:
            self.pong.run_game_loop()

        self.pong = None

    def button_press(self, button):
        if self.pong:
            self.pong.kp.key_queue.put(button)

    def start(self):
        self.thread = Thread(target=self.start_pong)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        if self.pong:
            self.pong.loop = False
            self.pong.kp.key_queue.put('q')
