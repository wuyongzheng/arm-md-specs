## A9.11 Coherent memory devices

## A9.11.1 Coherent memory device overview

- D0043 A coherent memory device (CMEM device) is a device which allows expansion of the pool of conventional memory available to a system.
- R0044 In this version of the specification, the only supported type of CMEM is CXL type-3 with the following properties:
- Volatile memory
- Host-only Coherent HDM (HDM-H)
- Single Logical Device, or Multiple Logical Devices with fixed capacity
- CXL transport security
- Support for CXL Trusted Execution Environment Security Protocol (CXL TSP)
- I0045 A CMEM object represents an Interleave Set of devices, with each Interleave Way being represented by a PDEV object.

## See also:

- Compute eXpress Link specification [18]
- A9.2 Physical device object

## A9.11.2 Coherent memory device attributes

D0046 The attributes of a CMEM are summarized in the following table.

| Name                                                         | Type                                                                | Description                                                                                                                                                                                                           |
|--------------------------------------------------------------|---------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| chbcr_addr hb_hdm_id addr_range ilv_gran ilv_ways state pdev | Bits64 Bits8 RmmAddrRange UInt64 UInt64 RmmCmemState RmmCmemPdev[8] | Address of CHBCR register in the Host Bridge Host Bridge HDMdecider identifier CMEMwindow. Base and size are aligned to 256MB. Interleave granularity in bytes Number of interleave ways CMEMstate Bound PDEV objects |


## A9.11.3 Coherent memory device invariants

This section lists invariants which are enforced via checks performed by the RMM.

R0047 cmem.addr\_range does not overlap with address range of any other CMEM.

R0048 cmem.addr\_range does not overlap with coherent address range of any PDEV which is not associated with this CMEM.

R0049

IDE is enabled for a CMEM device.

I0050 IDE is optional in the CXL specification, but the RMM currently takes a stricter approach by requiring IDE link protection.

R0051 cmem.addr\_range is within the physical address region(s) of the system memory map which are reserved for coherent device memory.

- R0052

cmem.ilv\_gran is permitted by CXL specification.

R0053

cmem.ilv\_ways is permitted by CXL specification.

R0054

If the platform requires Target-Side Encryption in coherent memory devices then a PDEV is allowed to be added to a CMEM Interleave Set only if it supports Target-Side Encryption.

## See also:

- A2.3.2 Views of physical memory
- A3.11 Support for coherent memory devices
- A9.2 Physical device object

## A9.11.4 Coherent memory device lifecycle

## A9.11.4.1 States

D0055

The states of a CMEM are listed below.

| State        | Description                                                   |
|--------------|---------------------------------------------------------------|
| CMEM_STOPPED | Device is not ready to provide coherent memory to the system. |
| CMEM_STARTED | Device is ready to provide coherent memory to the system.     |

## A9.11.4.2 State transitions

R0056 On creation of a CMEM object, no Realms exist in the system.

- I0057 Permitted CMEM state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a CMEM object. A transition to the pseudo-state NULL represents destruction of a CMEM object.

| From state   | To state     | Events           |
|--------------|--------------|------------------|
| NULL         | CMEM_STOPPED | RMI_CMEM_CREATE  |
| CMEM_STOPPED | CMEM_STARTED | RMI_CMEM_START   |
| CMEM_STARTED | CMEM_STOPPED | RMI_CMEM_STOP    |
| CMEM_STOPPED | NULL         | RMI_CMEM_DESTROY |

## See also:

- B4.5.3 RMI\_CMEM\_CREATE command
- B4.5.4 RMI\_CMEM\_DESTROY command
- B4.5.7 RMI\_CMEM\_START command
- B4.5.8 RMI\_CMEM\_STOP command

## A9.11.5 Coherent memory device flows

## A9.11.5.1 Coherent memory device setup flow


I0058

Setup of a CMEM is illustrated in the following sequence diagram.

Figure A9.25: CMEM setup (part 1 of 2)

<!-- image -->

Figure A9.26: CMEM setup (part 2 of 2)

<!-- image -->

I0059 Setup of a CMEM is summarised below.

## Interleave Way setup phase

For each PDEV in the Interleave Set, the Host initiates Secure SPDM session establishment and configuration of IDE link protection, by execution of RMI\_PDEV\_CREATE. This causes a device transaction to be initiated for the PDEV.

On subsequent execution of RMI\_PDEV\_COMMUNICATE, the RMM retrieves each of the following objects from the device. For each object, the RMM stores a digest and requests the Host to cache the object blob:

- An SPDM VCA object.
- A device certificate chain.

On subsequent execution of RMI\_PDEV\_COMMUNICATE, the RMM performs TSP locking, retrieves the device Target Report and retrieves device measurement data. If the device supports signed measurements, the RMM requests signed measurement data using an RMM generated nonce. The RMM's requesting and processing of attestation evidence from CMEM devices must not use any CMEM resources, including for nonce generation. For both the Target Report and the device measurement data, the RMM stores a digest and requests the Host to cache the object blob.

## Interleave Set creation phase

The Host initiates creation of an Interleave Set by execution of RMI\_CMEM\_CREATE. This causes the RMM to check that the configuration of the Host Bridge decoder is consistent with the parameters provided by the Host.

For each PDEV in the Interleave Set, the Host establishes a binding between the CMEM and the PDEV by execution of RMI\_CMEM\_ADD\_PDEV. This causes the RMM to check consistency between the CMEM attributes and the PDEV attributes.

The Host completes creation of an Interleave Set by execution of RMI\_CMEM\_START. This causes the RMM to check that the number of Interleave Ways specified at RMI\_CMEM\_CREATE have been added. The CMEM transitions to CMEM\_STARTED state.

## Mark CMEM PA range as populated

To mark a PA range within the address range of a CMEM as populated, the Host executes RMI\_CMEM\_POPULATE. On successful execution of this command, the target PA range becomes delegable.

## See also:

- A2.3.3 Populated physical memory
- A2.3.4 Granule tracking region
- A2.3.5 Delegable physical memory
- A9.5 Communication between RMM and a device
- Chapter A11 Realm memory encryption
- B4.5.2 RMI\_CMEM\_ADD\_PDEV command
- B4.5.3 RMI\_CMEM\_CREATE command
- B4.5.5 RMI\_CMEM\_POPULATE command


- B4.5.26 RMI\_PDEV\_COMMUNICATE command
- B4.5.27 RMI\_PDEV\_CREATE command

## A9.11.6 Coherent memory device encryption

- I0060 When the encryption context of delegable memory is updated, a corresponding update must be performed by all CMEMdevices.
- A11.1.2 MEC and CMEM devices

## A9.11.7 Coherent memory device attestation

- I0061 On successful execution of RMI\_CMEM\_START, the RMM records that the CCA platform token is invalid.
- I0062 On successful execution of RMI\_CMEM\_STOP, the RMM records that the CCA platform token is invalid.
- I0063 RMI\_REALM\_CREATE fails if the CCA platform token is invalid.
- I0064 On execution of RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH, if refresh of the CCA platform token is not complete, the command returns RMI\_BUSY. The caller is expected to wait for an IMPLEMENTATION DEFINED period before calling RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH again.
- I0065 On successful execution of RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH, the CCA platform token is marked as valid.

I0066

The set of CMEM devices attached to the platform is presented in the CCA platform extension claim.

I0067 Refresh of the CCA platform token following initialization of CMEM devices is illustrated in the following sequence diagram.

Figure A9.27: CMEM PAT refresh

<!-- image -->


For details of extending PAT with CMEM devices, refer to Firmware Interfaces for RME (FIRME) specification [19].

## See also:

- A2.1.2 RMMlifecycle
- A7.2.3.3.12 CCA platform extension
- B4.5.1 RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH command
- B4.5.7 RMI\_CMEM\_START command
- B4.5.8 RMI\_CMEM\_STOP command
- B4.5.46 RMI\_REALM\_CREATE command

I0068

## Chapter A10 Planes

This section describes how a Realm can be divided into multiple mutually isolated execution environments, called Planes.

