# SDN Static Routing Project

This project demonstrates static routing using Software Defined Networking (SDN).

## Tools Used
- Mininet
- Ryu Controller
- OpenFlow 1.3

## Topology
h1 → s1 → s2 → h2

## Description
The controller installs static flow rules in switches to control packet forwarding. Connectivity is verified using pingall.

## Output
0% packet loss

## How to Run

1. Start controller:
   python -m ryu.cmd.manager controller.py

2. Run Mininet:
   sudo mn --custom topo.py --topo static_topo --controller remote --switch ovsk,protocols=OpenFlow13

3. Test:
   pingall

## Output
0% packet loss

Packet delivery verified using pingall command.
