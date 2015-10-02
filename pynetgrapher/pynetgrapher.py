import click
import pynetlib
from pynetlib.namespace import Namespace
from pynetlib.device import Device
from graphviz import Digraph


@click.command()
@click.option('--debug', '-d', is_flag=True, help='Output processing informations')
@click.option('--output', '-o', default='netgraph.dot', help='Output file in DOT format')
def pynetgrapher(debug, output):
    g = Digraph('Topology', filename=output)
    for namespace in Namespace.discover():
        ns_name = 'default' if namespace.is_default() else namespace.name.replace(':', '-')
        ns_graph = Digraph(ns_name)
        ns_graph.body.append('style=filled')
        ns_graph.body.append('color=lightgrey')
        ns_graph.body.append('label = "%s"' % ns_name)
        devices = Device.discover(namespace=namespace)
        for device in devices:
            dev_name = '%s-%s' % (device.id, device.name)
            ns_graph.node(dev_name)
            
        g.subgraph(ns_graph)
    g.view()

def main():
    pynetgrapher()

if __name__ == '__main__':
    main()
