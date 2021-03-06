/* Copyright 2014 Google Inc.
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
*/

/*
This file is taken from https://github.com/NeuroCSUT/Alewrap2Player, 
a lua wrapper for the Xitari environment
*/

#ifndef XITARI_C_WRAPPER_H
#define XITARI_C_WRAPPER_H

#include <ale_interface.hpp>

typedef ale::ALEInterface ALEInterface;

extern "C" {
#include "xitari_c_wrapper.inl"
}

#endif  // XITARI_C_WRAPPER_H