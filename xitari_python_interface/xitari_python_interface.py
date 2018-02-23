# ale_python_interface.py
# Author: Ben Goodrich
# This directly implements a python version of the arcade learning
# environment interface.
__all__ = ['ALEInterface']

from ctypes import *
import numpy as np
from numpy.ctypeslib import as_ctypes
import os

xitari_lib = cdll.LoadLibrary(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'libxitari_c.so'))

# Specify the argument and return types of functions
xitari_lib.ale_fillRgbFromPalette.argtypes = [POINTER(c_ubyte), POINTER(c_ubyte), c_size_t, c_size_t]
xitari_lib.ale_fillRgbFromPalette.restype = c_void_p
xitari_lib.ale_new.argtypes = [c_char_p]
xitari_lib.ale_new.restype = c_void_p
xitari_lib.ale_gc.argtypes = [c_void_p]
xitari_lib.ale_gc.restype = None
xitari_lib.ale_act.argtypes = [c_void_p, c_int]
xitari_lib.ale_act.restype = c_double
xitari_lib.ale_act2.argtypes = [c_void_p, c_int, c_int]
xitari_lib.ale_act2.restype = None
xitari_lib.ale_getRewardA.argtypes = [c_void_p]
xitari_lib.ale_getRewardA.restype = c_double
xitari_lib.ale_getRewardB.argtypes = [c_void_p]
xitari_lib.ale_getRewardB.restype = c_double
xitari_lib.ale_getSideBouncing.argtypes = [c_void_p]
xitari_lib.ale_getSideBouncing.restype = c_double
xitari_lib.ale_getWallBouncing.argtypes = [c_void_p]
xitari_lib.ale_getWallBouncing.restype = c_bool
xitari_lib.ale_getCrash.argtypes = [c_void_p]
xitari_lib.ale_getCrash.restype = c_bool
xitari_lib.ale_getServing.argtypes = [c_void_p]
xitari_lib.ale_getServing.restype = c_bool
xitari_lib.ale_getPoints.argtypes = [c_void_p]
xitari_lib.ale_getPoints.restype = c_int
xitari_lib.ale_getScreenWidth.argtypes = [c_void_p]
xitari_lib.ale_getScreenWidth.restype = c_int
xitari_lib.ale_getScreenHeight.argtypes = [c_void_p]
xitari_lib.ale_getScreenHeight.restype = c_int
xitari_lib.ale_isGameOver.argtypes = [c_void_p]
xitari_lib.ale_isGameOver.restype = c_bool
xitari_lib.ale_resetGame.argtypes = [c_void_p]
xitari_lib.ale_resetGame.restype = None
xitari_lib.ale_saveState.argtypes = [c_void_p]
xitari_lib.ale_saveState.restype = None
xitari_lib.ale_loadState.argtypes = [c_void_p]
xitari_lib.ale_loadState.restype = None
xitari_lib.ale_fillObs.argtypes = [c_void_p, POINTER(c_ubyte), c_size_t]
xitari_lib.ale_fillObs.restype = None
xitari_lib.ale_fillRamObs.argtypes = [c_void_p, POINTER(c_ubyte), c_size_t]
xitari_lib.ale_fillRamObs.restype = None
xitari_lib.ale_numLegalActions.argtypes = [c_void_p]
xitari_lib.ale_numLegalActions.restype = c_int
xitari_lib.ale_legalActions.argtypes = [c_void_p, POINTER(c_int), c_size_t]
xitari_lib.ale_legalActions.restype = None
xitari_lib.ale_legalActionsB.argtypes = [c_void_p, POINTER(c_int), c_size_t]
xitari_lib.ale_legalActionsB.restype = None
xitari_lib.ale_livesRemained.argtypes = [c_void_p]
xitari_lib.ale_livesRemained.restype = c_int
xitari_lib.ale_livesRemainedB.argtypes = [c_void_p]
xitari_lib.ale_livesRemainedB.restype = c_int
xitari_lib.ale_getSnapshotLength.argtypes = [c_void_p]
xitari_lib.ale_getSnapshotLength.restype = c_int
xitari_lib.ale_saveSnapshot.argtypes = [c_void_p, POINTER(c_ubyte), c_size_t]
xitari_lib.ale_saveSnapshot.restype = None
xitari_lib.ale_restoreSnapshot.argtypes = [c_void_p, POINTER(c_ubyte), c_size_t]
xitari_lib.ale_restoreSnapshot.restype = None

def ale_fillRgbFromPalette(rgb, obs, rgb_size, obs_size):
	return xitari_lib.ale_fillRgbFromPalette(rgb, obs, rgb_size, obs_size)

class ALEInterface(object):
	def __init__(self, rom_file):
		self.obj = xitari_lib.ale_new(rom_file)

	def ale_act(self, action):
		return xitari_lib.ale_act(self.obj, action)

	def ale_act2(self, actionA, actionB):
		return xitari_lib.ale_act2(self.obj, actionA, actionB)

	def ale_getRewardA(self):
		return xitari_lib.ale_getRewardA(self.obj)

	def ale_getRewardB(self):
		return xitari_lib.ale_getRewardB(self.obj)

	def ale_getSideBouncing(self):
		return xitari_lib.ale_getSideBouncing(self.obj)

	def ale_getWallBouncing(self):
		return xitari_lib.ale_getWallBouncing(self.obj)

	def ale_getCrash(self):
		return xitari_lib.ale_getCrash(self.obj)

	def ale_getServing(self):
		return xitari_lib.ale_getServing(self.obj)

	def ale_getPoints(self):
		return xitari_lib.ale_getPoints(self.obj)

	def ale_getScreenWidth(self):
		return xitari_lib.ale_getScreenWidth(self.obj)

	def ale_getScreenHeight(self):
		return xitari_lib.ale_getScreenHeight(self.obj)

	def ale_isGameOver(self):
		return xitari_lib.ale_isGameOver(self.obj)

	def ale_resetGame(self):
		return xitari_lib.ale_resetGame(self.obj)

	def ale_saveState(self):
		return xitari_lib.ale_saveState(self.obj)

	def ale_loadState(self):
		return xitari_lib.ale_loadState(self.obj)

	def ale_fillObs(self, obs, obs_size):
		return xitari_lib.ale_fillObs(self.obj, obs, obs_size)

	def ale_fillRamObs(self, obs, obs_size):
		return xitari_lib.ale_fillRamObs(self.obj, obs, obs_size)

	def ale_numLegalActions(self):
		return xitari_lib.ale_numLegalActions(self.obj)

	def ale_legalActions(self, actions, size):
		return xitari_lib.ale_legalActions(self.obj, actions, size)

	def ale_legalActionsB(self, actions, size):
		return xitari_lib.ale_legalActionsB(self.obj, actions, size)

	def ale_livesRemained(self):
		return xitari_lib.ale_livesRemained(self.obj)

	def ale_livesRemainedB(self):
		return xitari_lib.ale_livesRemainedB(self.obj)

	def ale_getSnapshotLength(self):
		return xitari_lib.ale_getSnapshotLength(self.obj)

	def ale_saveSnapshot(self, data, length):
		return xitari_lib.ale_saveSnapshot(self.obj, data, length)

	def ale_restoreSnapshot(self, snapshot, size):
		return xitari_lib.ale_restoreSnapshot(self.obj, snapshot, size)

	def __del__(self):
		xitari_lib.ale_gc(self.obj)