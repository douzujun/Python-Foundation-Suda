# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:27:00 2020

@author: douzi
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')