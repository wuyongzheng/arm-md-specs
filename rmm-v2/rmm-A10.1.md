## A10.1 Planes overview

- A Realm contains:
- a single primary Plane
- zero or more auxiliary Planes .

A Realm with a non-zero number of auxiliary Planes is said to contain multiple Planes .

- The number of auxiliary Planes is specified by the Host at Realm creation.
- Planes within a Realm are identified using a zero-based Plane index .

The Plane index of the primary Plane is zero.

- When referring to the primary Plane of a Realm, this specification uses the term Plane 0 , or P0 .

When referring to any auxiliary Plane, this specification uses the term Pn .

- All Planes within a Realm share a single IPA space.

Stage 2 memory access permissions for a given IPA can differ between Planes.

Each Plane has a VMID which is unique both within the owning Realm and among all Realms.

- A Realm with multiple Planes may either have:
- An RTT tree per Plane, or
- A single RTT tree, with per-Plane access permissions being managed indirectly.
- On REC exit due to Data Abort or Instruction Abort, the index of the RTT tree used by the exited Plane is provided to the Host.

This allows the Host to know which RTT tree must be modified in order to service a fault.

- A given VPE executes in one Plane at a time.

This is referred to as the active Plane of the VPE.

- The following capabilities are available only to P0:
- Change the active Plane of the current VPE
- Read and write register state of other Planes in the current VPE


- Configure and take traps from other Planes in the current VPE
- Control delivery of virtual interrupts to other Planes in the current VPE
- Control memory access permissions observed by other Planes in all VPEs

## See also:

- [A3.12 Support for auxiliary Planes](rmm-A3.md#a312-support-for-auxiliary-planes)
- [A10.2 Planes exception model](rmm-A10.2.md)
- [A10.3 Planes memory management](rmm-A10.3.md)
- [A10.4 Planes interrupts](rmm-A10.4.md)