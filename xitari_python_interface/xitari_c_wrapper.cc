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

#include "xitari_c_wrapper.h"
//#include "lua.h"
//#include "lualib.h"
//#include "lauxlib.h"
#include <stdexcept>
#include <cassert>
#include <algorithm>
#include <iostream>

double rewardA,rewardB,sideBouncing;
bool wallBouncing,crash,serving;
int points;
void ale_fillRgbFromPalette(uint8_t *rgb, const uint8_t *obs, size_t rgb_size,
                            size_t obs_size) {
  assert(obs_size >= 0);
  assert(rgb_size == 3 * obs_size);

  const int r_offset = 0ul;
  const int g_offset = obs_size;
  const int b_offset = 2ul * obs_size;

  for (int index = 0ul; index < obs_size; ++index) {
    uint8_t r, g, b;
    ALEInterface::getRGB(obs[index], r, g, b);

    rgb[r_offset + index] = r;
    rgb[g_offset + index] = g;
    rgb[b_offset + index] = b;
  }
}

ALEInterface *ale_new(const char *rom_file) {
  return new ALEInterface(rom_file);
}

void ale_gc(ALEInterface *ale) { delete ale; }

double ale_act(ALEInterface *ale, int action) {
  assert(action >= static_cast<int>(ale::PLAYER_A_NOOP) &&
         action <= static_cast<int>(ale::PLAYER_A_DOWNLEFTFIRE));
  return ale->act(static_cast<ale::Action>(action));
}

void ale_act2(ALEInterface *ale, int actionA, int actionB){

assert(actionA >= static_cast<int>(ale::PLAYER_A_NOOP) &&
         actionA <= static_cast<int>(ale::PLAYER_A_DOWNLEFTFIRE));
assert(actionB >= static_cast<int>(ale::PLAYER_B_NOOP) &&
         actionB <= static_cast<int>(ale::PLAYER_B_DOWNLEFTFIRE)); 
double *pRewardA = &rewardA;
double *pRewardB = &rewardB;
double *pSideBouncing = &sideBouncing;
bool *pWallBouncing = &wallBouncing;
bool *pCrash = &crash;
bool *pServing= &serving;
int *pPoints = &points;



  ale->act2(static_cast<ale::Action>(actionA),static_cast<ale::Action>(actionB),pRewardA, pRewardB,pSideBouncing,pWallBouncing,pPoints,pCrash,pServing);


}

double ale_getRewardA(const ALEInterface *ale){return rewardA;}
double ale_getRewardB(const ALEInterface *ale){return rewardB;}

double ale_getSideBouncing(const ALEInterface *ale){return sideBouncing;}
bool ale_getWallBouncing(const ALEInterface *ale){return wallBouncing;}
bool ale_getCrash(const ALEInterface *ale){return crash;}
int ale_getPoints(const ALEInterface *ale){return points;}
bool ale_getServing(const ALEInterface *ale){return serving;}
int ale_getScreenWidth(const ALEInterface *ale) {
  return ale->getScreen().width();
}

int ale_getScreenHeight(const ALEInterface *ale) {
  return ale->getScreen().height();
}

bool ale_isGameOver(const ALEInterface *ale) { return ale->gameOver(); }

void ale_resetGame(ALEInterface *ale) {
  ale->resetGame();
  assert(!ale->gameOver());
}

bool ale_loadState(ALEInterface *ale) { return ale->loadState(); }

void ale_saveState(ALEInterface *ale) { ale->saveState(); }

void ale_fillObs(const ALEInterface *ale, uint8_t *obs, size_t obs_size) {
  const ale::ALEScreen& screen = ale->getScreen();
  size_t h = screen.height();
  size_t w = screen.width();
  assert(obs_size == h * w);

  std::copy(screen.getArray().begin(), screen.getArray().end(), obs);
}

void ale_fillRamObs(const ALEInterface *ale, uint8_t *ram,
                    size_t ram_size) {
  const ale::ALERAM& ale_ram = ale->getRAM();
  assert(ram_size == ale_ram.size());

  const unsigned char* ram_content = ale_ram.array();
  std::copy(ram_content, ram_content + ram_size, ram);
}

int ale_numLegalActions(ALEInterface *ale) {
  return static_cast<int>(ale->getMinimalActionSet().size());
}

void ale_legalActions(ALEInterface *ale, int *actions,
                      size_t actions_size) {
  const std::vector<enum ale::Action>& legal_actions = ale->getMinimalActionSet();
  assert(actions_size == legal_actions.size());
  std::copy(legal_actions.begin(), legal_actions.end(), actions);
}
void ale_legalActionsB(ALEInterface *ale, int *actions,
                      size_t actions_size) {
  const std::vector<enum ale::Action>& legal_actions = ale->getMinimalActionSetB();
  assert(actions_size == legal_actions.size());
  std::copy(legal_actions.begin(), legal_actions.end(), actions);
}

int ale_livesRemained(const ALEInterface *ale) { return ale->lives(); }
int ale_livesRemainedB(const ALEInterface *ale) { return ale->livesB(); }

int ale_getSnapshotLength(const ALEInterface *ale) {
  return static_cast<int>(ale->getSnapshot().size());
}

void ale_saveSnapshot(const ALEInterface *ale, uint8_t *data,
                      size_t length) {
  std::string result = ale->getSnapshot();

  assert(length >= result.size() && length > 0);

  if (length < result.size())
    data = NULL;
  else
    result.copy(reinterpret_cast<char *>(data), length);
}

void ale_restoreSnapshot(ALEInterface *ale, const uint8_t *snapshot,
                         size_t size) {
  assert(size > 0);

  std::string snapshotStr(reinterpret_cast<char const *>(snapshot), size);
  ale->restoreSnapshot(snapshotStr);
}
