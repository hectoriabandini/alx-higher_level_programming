#!/usr/bin/python3

def element_at(my_list, idx):
    """Element retrieval"""
    if idx < 0 or idx >= len(my_list):
        return(my_list[idx])
    return my_list[idx]
