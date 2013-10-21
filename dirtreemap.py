##Functions for building a directory tree in dot format, to be formatted with
##graphviz

from os import walk, path
import pygraphviz as gv

def dirTreeGraph(rootPath):
    gr=gv.AGraph(splines="ortho",url=path.dirname(path.abspath(rootPath)),rankdir="LR")
    gr.add_node(rootPath,label=path.basename(rootPath),url=path.basename(rootPath))
    for folder, subdirs, files in walk(rootPath):
        subdirs.sort()
        nsg=[folder] #newsubgraph
        for directory in subdirs:
            newnode=path.join(folder,directory)
            gr.add_node(newnode,label=directory,url=newnode)
            gr.add_edge(folder,newnode)
            nsg.append(newnode)
        if subdirs:
            gr.subgraph(nsg,folder,label="")
    return gr

def dirTreeGraph2(rootPath):
    gr=gv.AGraph(splines="ortho",url=path.dirname(path.abspath(rootPath)),rankdir="LR"):
    for folder, subdirs, files in walk(rootPath,topdown=False):
        gr.add_node(folder,label=path.basename(folder),url=folder)
        gr.subgraph([folder],folder)
