## A9.9 Device memory access

## A9.9.1 Device access to a Protected IPA

- Access from a VDEV to an IPA is subject to the same stage 2 address translation used for PE accesses.
- A VDEV whose DMA state is VDEV\_DMA\_ENABLED is associated with a specified Plane within the Realm.
- Access from a VDEV to a Protected IPA follows the same rules, regarding stage 2 access permissions and stage 2 fault handling, as for a PE access from the associated Plane to the same IPA.
- A device may implement an Address Translation Cache (ATC), which it uses to store the result of Address Translation Service (ATS) requests issued to the SMMU.
- A device which implements an ATC may issue translated requests. In order to enforce isolation between Realms, translated requests are subject to checking by the SMMU against a Device Permission Table (DPT). The DPT is indexed by physical address, and stores the VMID which is permitted to access the corresponding physical location.
- The attributes of a Realm include the following which relate to device translated requests:
- An 'ATS enable' flag which specifies whether the platform is permitted to respond to ATS requests which target the Realm's address space.
- An 'ATS Plane' value. If ATS is enabled for the Realm, this value is used by the RMM to determine which VMID to write into DPT entries corresponding to Granules which are owned by the Realm.
- The Realm can discover the values of the 'ATS enable' and 'ATS Plane' attributes via the RSI\_REALM\_CONFIG command.
- When executing the RSI\_VDEV\_DMA\_ENABLE command, the Realm provides two parameters:
- An 'ATS enable' flag.
- A 'non-ATS Plane' index.
- If both the Realm 'ATS enable' flag and the VDEV 'ATS enable' flags are set then the device uses the stage 2 translation associated with the Realm 'ATS Plane'.

Otherwise, the device uses the stage 2 translation associated with the 'non-ATS Plane'.


- The STE.EATS flag is set on an SMMU stream if all of the following are true:
- The Realm 'ATS enable' flag is true.
- The VDEV 'ATS enable' flag is true.
- The SMMU implementation supports ATS.
- The PSMMU 'ATS enable' flag is true.

See also:

- PCI Express 6.0 specification [16]
- Arm System Memory Management Unit Architecture Specification [22]
- A2.2.3 Realm attributes
- A5.2.3 Realm access to a Protected IPA
- A9.4 Virtual device object
- A9.7 Physical SMMU
- Chapter A10 Planes
- B5.4.16 RSI\_REALM\_CONFIG command
- B5.4.18 RSI\_VDEV\_DMA\_ENABLE command