from __future__ import annotations, with_statement
from typing import List, Optional
from generic_search import bfs, Node, node_to_path

MAX_NUM: int = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries
        self.wc: int = cannibals
        self.em: int = MAX_NUM - self.wm
        self.ec: int = MAX_NUM - self.wc
        self.boat: bool = boat
    
    def __str__(self) -> str:
        return ("On the west bank there are {} missionaries and {} cannibals.\n"
        "On the east bank there are {} missionaries and {} cannibals.\n"
        "The boat is on the {} bank.")\
            .format(self.wm, self.wc, self.em, self.ec)

    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.ec > 0:
            return False
        return True
    
    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM
    
    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        if self.boat:
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm -1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
            if (self.wc > 0) and (self.em > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else:
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.em > 0) and (self.ec > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in sucs if x.is_legal]