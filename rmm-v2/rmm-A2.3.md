## A2.3 Physical memory

This section describes how the RMM manages the usage within Realm PAS of physically memory-mapped resources.


Physically memory-mapped resources may be used within Realm PAS for the following purposes:

- To store code or data used by a Realm
- As device memory used by a Realm
- To store data used by the RMM to manage a Realm

## A2.3.1 Granule size

This section describes the granularities at which physical memory may be addressed by the RMM, and via RMM interfaces.

- Physical Granule size is the smallest unit of physical memory which can be described in a Granule Protection Table (GPT) entry.
- RMI Granule size is the smallest unit of physical memory for which the RMM manages usage within Realm PAS.
- At platform boot, RMI Granule size is equal to Physical Granule size.
- The current RMI Granule size can be discovered by execution of RMI\_RMM\_CONFIG\_GET.
- The set of supported RMI Granule sizes can be discovered by execution of RMI\_FEATURES.
- The set of supported RMI Granule sizes does not include any value which is not a supported translation granule size.
- The set of supported RMI Granule sizes does not include any value which is smaller than the Physical Granule size.
- RMI Granule size can be modified by execution of RMI\_RMM\_CONFIG\_SET.
- Modification of RMI Granule size fails if any tracking region has been transitioned from untracked to tracked.
- RSI Granule size is the smallest unit of physical memory which can be referred to by the input values of an RSI command.
- RSI Granule size is equal to 4KB.

See also:

- A2.3.2 Views of physical memory
- A2.3.4 Granule tracking region
- B4.5.14 RMI\_FEATURES command
- B4.5.53 RMI\_RMM\_CONFIG\_GET command
- B4.5.54 RMI\_RMM\_CONFIG\_SET command

## A2.3.2 Views of physical memory

- The RMM manages the usage within Realm PAS of physically memory-mapped resources by combining the following views:
- The memory layout view , which is a static description of how regions of physical address space are reserved for specific purposes.
- The memory population view , which is a dynamic record of the regions of physical address space which are backed by resources which have been verified by the RMM.
- The memory tracking view , which is a dynamic record of the regions of physical address space for which the RMMis tracking usage within Realm PAS.

The memory layout view consists of information about the system memory map which is known to the RMM at platform boot:




- The physical address size
- Configuration of the Granule Protection Table (GPT)
- -The Level 0 GPT Size (L0GPTSZ)
- -The Physical Granule Size (PGS)
- The physical address region(s) which are reserved for DRAM
- The physical address region(s) which are reserved for coherent device memory
- The physical address region(s) which are reserved for non-coherent device memory

The following diagram shows an example of the system memory map information held by the RMM.

Figure A2.3: Example memory layout view

At runtime, the Host can inform the RMM of the existence of a device which is to be made accessible via Realm PAS.

For each such device, the memory population view records the following information:

- The physical address regions which are associated with the device. The RMM checks that these lie within the appropriate regions of the system memory map, and that they do not overlap with those associated with any other device.
- Arm Architecture Reference Manual for A-Profile architecture [3]

· Whether the RMM has verified the identity and configuration of the device. In order to track the usage within Realm PAS of physically memory-mapped resources, the RMM requires memory for storage of Granule metadata. This metadata includes Granule state, and may also include additional IMPLEMENTATION DEFINED information. To enable tracking for a given region of physical address space, the Host specifies the granularity at which Granule state should be tracked for that region, and provides sufficient memory to the RMM for storage of the metadata. For each region of physical address space, the memory tracking view records whether tracking has been enabled, and if so at which granularity. See also:

- A2.3.3 Populated physical memory
- A2.3.4 Granule tracking region
- Chapter A9 Realm device assignment
- B3.57 PaIsCohDevMem function
- B3.64 PaIsDram function
- B3.65 PaIsNonCohDevMem function
- B3.66 PaIsPopulated function

## A2.3.3 Populated physical memory

- A physical address is populated if it is backed by a resource which has been verified by the RMM.
- An address which is within a region of the system memory map that is reserved for DRAM is populated . DRAM hot-plug is not supported.
- Device memory is populated if the state of the corresponding PDEV is PDEV\_READY.
- The following diagram shows an example of how the memory population view is updated following attestation of the identity and configuration of devices.

<!-- image -->


Figure A2.4: Example memory population view

<!-- image -->

## See also:

- A2.3.2 Views of physical memory
- Chapter A9 Realm device assignment

## A2.3.4 Granule tracking region

- A Granule tracking region is a naturally-aligned region of physical address space.
- The Granule tracking region size can be discovered by execution of RMI\_RMM\_CONFIG\_GET.
- The Granule tracking region size can be modified by execution of RMI\_RMM\_CONFIG\_SET.
- The valid combinations of RMI Granule size and Granule tracking region size are listed in the following table.

| RMI Granule size   | Granule tracking region sizes   |
|--------------------|---------------------------------|
| 4KB                | 1GB                             |
| 16KB               | 32MB, 64GB                      |
| 64KB               | 512MB, 4TB                      |

The attributes of a Granule tracking region are summarized in the following table.


| Name     | Type                   | Description            |
|----------|------------------------|------------------------|
| state    | RmmTrackingRegionState | Tracking region state. |
| category | RmmMemCategory         | Memory category.       |

The states of a Granule tracking region are listed below.

| Name              | Description                                                       |
|-------------------|-------------------------------------------------------------------|
| TRACKING_COARSE   | Region is tracked at the granularity of the Tracking Region size. |
| TRACKING_FINE     | Region is tracked at the granularity of the RMI Granule size.     |
| TRACKING_NONE     | Region is not tracked.                                            |
| TRACKING_RESERVED | Region is reserved for use by the platform.                       |

At platform boot, the state of all tracking regions within the physical address range(s) which are reserved for DRAM is either TRACKING\_READY or TRACKING\_NOT\_READY.

At platform boot, the state of all tracking regions within the physical address range(s) which are reserved for coherent device memory is either TRACKING\_READY or TRACKING\_NOT\_READY.

At platform boot, the state of all tracking regions within the physical address range(s) which are reserved for device memory is either TRACKING\_READY or TRACKING\_NOT\_READY.

A physical address is tracked if it is within a tracking region whose state is TRACKING\_READY.

Attributes of a Granule tracking region can be read by execution of RMI\_GRANULE\_TRACKING\_GET.

Attributes of a Granule tracking region can be modified by execution of RMI\_GRANULE\_TRACKING\_SET.

Execution of RMI\_GRANULE\_TRACKING\_SET fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE.

Changing the granularity of a tracking region for which tracking is enabled is permitted only if all Granules within the region have the same state.

Permitted Granule tracking region state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

Figure A2.5: Granule tracking region state transitions

<!-- image -->

The Granule tracking metadata which describes an address range which is populated by DRAM must be located in DRAM.

R0001 The Granule tracking metadata which describes an address range which is populated by a CMEM Interleave Set must be located either in DRAM, or within the address range of that CMEM Interleave Set.

Granule tracking metadata is permitted to be located within the tracking region that it describes.

On execution of RMI\_GRANULE\_TRACKING\_SET, if the implementation requires memory to be donated then the 'donating memory to a Stateful RMI Operation (SRO)' flow is followed. Prior to donation, the state of the memory must be GRAN\_DELEGATED.

On execution of RMI\_GRANULE\_TRACKING\_SET, if the implementation requires memory to be reclaimed then the 'reclaiming memory from a Stateful RMI Operation (SRO)' flow is followed. Following reclamation, the state of the memory is GRAN\_DELEGATED.

See also:

- A2.1 RMM
- A2.3.1 Granule size
- B3.67 PaIsTracked function
- B4.3.2.2 Donating memory to an SRO
- B4.3.2.3 Reclaiming memory from an SRO

- B4.5.19 RMI\_GRANULE\_TRACKING\_GET command
- B4.5.20 RMI\_GRANULE\_TRACKING\_SET command

## A2.3.5 Delegable physical memory


A physical address is delegable

- The address is tracked .
- The address is populated .
- The address is not within a region which is reserved for use by the platform. For example, all or part of a tracking region may be reserved for use by RMSD or by the RMM. Discovery of such reserved regions is out of scope of this specification.

Delegable memory can be delegated by the Host for use to store RMM data, or to be mapped into a Realm.

RMMobjects can only be stored in Delegable conventional memory.

Non-delegable memory cannot be used to store RMM data and cannot be mapped into the Protected IPA space of a Realm.

Delegable device memory is the union of Delegable non-coherent device memory and Delegable coherent device memory.

Delegable memory is the union of Delegable conventional memory and Delegable device memory.

The following diagram summarizes the relationship between categories of delegable memory.

Figure A2.6: Delegable memory

<!-- image -->

The following diagram shows an example of how delegability of memory changes as a result of allocation of tracking metadata storage.

if all of the following are true:

Figure A2.7: Example memory tracking view

<!-- image -->

U = UNDELEGATED

## See also:

- A2.3.2 Views of physical memory
- A2.3.4 Granule tracking region
- B3.58 PaIsDelegable function
- B3.59 PaIsDelegableCohDevMem function
- B3.60 PaIsDelegableConventional function
- B3.62 PaIsDelegableDevMem function
- B3.63 PaIsDelegableNonCohDevMem function

## A2.3.6 Granule state

A Granule state indicates whether a delegable Granule has been delegated to Realm PAS, and if so whether it is in use by the RMM or by a Realm.

The states of a Granule are listed below.

| Name           | Description                               |
|----------------|-------------------------------------------|
| GRAN_CMEM      | Coherent memory device object.            |
| GRAN_DATA      | Realm code or data.                       |
| GRAN_DELEGATED | Delegated for use by the RMM.             |
| GRAN_DEV       | Device memory, mapped into a Realm.       |
| GRAN_INTERNAL  | Used for IMPLEMENTATION DEFINED purposes. |
| GRAN_PDEV      | Physical device object.                   |
| GRAN_RD        | Realm Descriptor object                   |
| GRAN_REC       | Realm Execution Context object.           |


| Name             | Description                       |
|------------------|-----------------------------------|
| GRAN_RTT         | Realm Translation Table.          |
| GRAN_UNDELEGATED | Not delegated for use by the RMM. |
| GRAN_VDEV        | Virtual device object.            |
| GRAN_VSMMU       | Virtual SMMUobject.               |

If the state of a Granule is GRAN\_UNDELEGATED then the RMM does not prevent the GPT entry of the Granule from being changed by another agent to any value except GPT\_REALM.

An NS Granule is a Granule whose GPT entry is GPT\_NS.

See also:

- A2.3.5 Delegable physical memory

## A2.3.6.1 Granule state transitions

- The initial state of all Granules of Delegable memory is GRAN\_UNDELEGATED.

The set of reachable states depends on the Granule category.

- Permitted Granule state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

| From state       | To state         | Events                                 |
|------------------|------------------|----------------------------------------|
| GRAN_UNDELEGATED | GRAN_DELEGATED   | RMI_GRANULE_RANGE_DELEGATE             |
| GRAN_DELEGATED   | GRAN_UNDELEGATED | RMI_GRANULE_RANGE_UNDELEGATE           |
| GRAN_DELEGATED   | GRAN_RD          | RMI_REALM_CREATE                       |
| GRAN_RD          | GRAN_DELEGATED   | RMI_REALM_DESTROY                      |
| GRAN_DELEGATED   | GRAN_DATA        | RMI_RTT_DATA_MAP_INIT RMI_RTT_DATA_MAP |
| GRAN_DATA        | GRAN_DELEGATED   | RMI_RTT_DATA_UNMAP                     |
| GRAN_DELEGATED   | GRAN_REC         | RMI_REC_CREATE                         |
| GRAN_REC         | GRAN_DELEGATED   | RMI_REC_DESTROY                        |
| GRAN_DELEGATED   | GRAN_RTT         | RMI_REALM_CREATE RMI_RTT_CREATE        |
| GRAN_RTT         | GRAN_DELEGATED   | RMI_REALM_DESTROY RMI_RTT_DESTROY      |
| GRAN_DELEGATED   | GRAN_PDEV        | RMI_PDEV_CREATE                        |
| GRAN_PDEV        | GRAN_DELEGATED   | RMI_PDEV_DESTROY                       |
| GRAN_DELEGATED   | GRAN_VDEV        | RMI_VDEV_CREATE                        |
| GRAN_VDEV        | GRAN_DELEGATED   | RMI_VDEV_DESTROY                       |
| GRAN_DELEGATED   | GRAN_DEV         | RMI_RTT_DEV_MAP                        |
| GRAN_DEV         | GRAN_DELEGATED   | RMI_RTT_DEV_UNMAP                      |


| From state     | To state       | Events            |
|----------------|----------------|-------------------|
| GRAN_DELEGATED | GRAN_VSMMU     | RMI_VSMMU_CREATE  |
| GRAN_VSMMU     | GRAN_DELEGATED | RMI_VSMMU_DESTROY |
| GRAN_DELEGATED | GRAN_CMEM      | RMI_CMEM_CREATE   |
| GRAN_CMEM      | GRAN_DELEGATED | RMI_CMEM_DESTROY  |

Permitted Granule state transitions are shown in the following figures. Each arc is labeled with the events which can cause the corresponding state transition.

Figure A2.9: Granule state transitions for Delegable device memory

<!-- image -->

See also:

- B4.5.3 RMI\_CMEM\_CREATE command
- B4.5.4 RMI\_CMEM\_DESTROY command
- B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command
- B4.5.18 RMI\_GRANULE\_RANGE\_UNDELEGATE command
- B4.5.27 RMI\_PDEV\_CREATE command
- B4.5.28 RMI\_PDEV\_DESTROY command
- B4.5.46 RMI\_REALM\_CREATE command
- B4.5.47 RMI\_REALM\_DESTROY command
- B4.5.49 RMI\_REC\_CREATE command
- B4.5.50 RMI\_REC\_DESTROY command
- B4.5.64 RMI\_RTT\_CREATE command
- B4.5.65 RMI\_RTT\_DATA\_MAP command
- B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command
- B4.5.68 RMI\_RTT\_DESTROY command
- B4.5.69 RMI\_RTT\_DEV\_MAP command
- B4.5.70 RMI\_RTT\_DEV\_UNMAP command
- B4.5.82 RMI\_VDEV\_CREATE command
- B4.5.83 RMI\_VDEV\_DESTROY command
- B4.5.95 RMI\_VSMMU\_CREATE command
- B4.5.96 RMI\_VSMMU\_DESTROY command

## A2.3.6.2 Granule delegation

- Transition of Granules from GRAN\_UNDELEGATED to GRAN\_DELEGATED state is called Granule delegation .
- Transition of Granules from GRAN\_DELEGATED to GRAN\_UNDELEGATED state is called Granule undelegation .
- Granule delegation and undelegation implement the Range RMI operation which returns progress address programming model.
- Granule delegation and undelegation implement the RMI operations which can lead to an intermediate state programming model.


- The amount of progress made by a Granule delegation or undelegation operation during a single RMI call is determined by a combination of constraints imposed by the RMM architecture, and IMPLEMENTATION DEFINED properties of the RMM implementation.

The following architectural constraints apply to the tracking region which includes the start of the target PA range:

- If the tracking region is untracked then the command fails with RMI\_ERROR\_TRACKING.
- If start of the target PA range is not aligned to the granularity of the tracking region then the command fails with RMI\_ERROR\_INPUT.
- If the granularity of the tracking region is larger than the total size of the target PA range then the command fails with RMI\_ERROR\_INPUT.

The following architectural constraints apply to the Granule at the start of the target PA range:

- If the state of the Granule is not the expected source state then the command fails with RMI\_ERROR\_INPUT. For example, for Granule delegation the source state is GRAN\_UNDELEGATED.

If none of the above checks failed then the operation starts to operate on the target PA range. The operation terminates when any of the following is true:

- The operation has started to transition one or more contiguous Granules from the source state, but has not completed the work needed for the entry to reach the destination state. For example, for Granule delegation the destination state is GRAN\_DELEGATED. The Granules transition to an intermediate state and the command returns RMI\_INCOMPLETE.

- The operation reaches a tracking region or Granule which fails one of the above checks. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made. If no changes of system state occur before the operation is resumed then the next command will fail the same check at the beginning, and return an error code as described above.
- The operation reaches a tracking region which passes the above checks, but whose size is too large to process for an IMPLEMENTATION DEFINED reason. For example, an implementation may limit the maximum size of the address space which can be processed during a single RMI command, either to ensure that the command's execution time does not exceed an IMPLEMENTATION DEFINED budget, or to limit complexity of the implementation. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made. If no changes of system state occur before the operation is resumed then the next command will fail with RMI\_ERROR\_TRACKING. This indicates that in order to progress the operation, the Host must first transition the tracking region to fine granularity.
- The operation neither encounters a failing check, nor reaches the end of the target PA range, but yields for an IMPLEMENTATION DEFINED reason. For example, this could be due to the command's execution time having exceeded an IMPLEMENTATION DEFINED budget. The command returns RMI\_SUCCESS with out\_top indicating the amount of progress made.
- The operation reaches the end of the target PA range. The command returns RMI\_SUCCESS with out\_top == top .
- On successful execution of a Granule delegation or undelegation command, all of the following are true:
- out\_top &gt; base
- The state of all Granules in the PA range [base, out\_top) transition from the source state to the destination state.
- On failed execution of a Granule delegation or undelegation command, if the result is not RMI\_INCOMPLETE then no Granules in the PA range [base, top) transition from the source state to the destination state.
- Execution of RMI\_GRANULE\_RANGE\_DELEGATE fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE.

See also:

- B4.3.2 Stateful RMI operations
- B4.3.5 Range RMI operations


- B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command
- B4.5.18 RMI\_GRANULE\_RANGE\_UNDELEGATE command

## A2.3.7 Granule ownership

- A Granule whose state is one of the following is owned by a Realm:
- GRAN\_DATA
- GRAN\_DEV
- GRAN\_RD
- GRAN\_REC
- GRAN\_RTT
- GRAN\_VDEV
- GRAN\_VSMMU
- The owner of a Granule is identified by the address of a Realm Descriptor (RD).
- For a Granule whose state is GRAN\_RD, the ownership relation is recursive: the owning Realm is identified by the address of the RD itself.
- A Granule whose state is GRAN\_RTT is one of the following:
- A starting level RTT. The address of this RTT is stored in the RD of the owning Realm.

- A non-starting level RTT. The address of this RTT is stored in its parent RTT, in an RTT entry whose state is RTTE\_TABLE. Recursively following the parent relationship leads to the RD of the owning Realm.
- AGranule whose state is GRAN\_DATA is mapped at a Protected IPA, in an RTT entry whose state is RTTE\_DATA. The Realm which owns the RTT is the owner of the DATA Granule.

A REC has an 'owner' attribute which points to the RD of the owning Realm.

A REC is not mapped at a Protected IPA. Its ownership therefore needs to be recorded explicitly.

A VDEV has an 'owner' attribute which points to the RD of the owning Realm.

- A VDEV is not mapped at a Protected IPA. Its ownership therefore needs to be recorded explicitly.

See also:

- A2.2 Realm
- A2.2.7 Realm Descriptor
- A2.4 Realm Execution Context
- A5.2.1 Realm IPA space
- A5.6 Realm Translation Table
- Chapter A9 Realm device assignment
- B4.5.49 RMI\_REC\_CREATE command
- B4.5.64 RMI\_RTT\_CREATE command
- Wiping is an operation which changes the observable value of a memory location from X to Y , such that the value X cannot be determined from the value Y .
- · B4.5.65 RMI\_RTT\_DATA\_MAP command · B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command A2.3.8 Granule wiping RTMGSL When the state of a Granule has transitioned from P to GRAN\_DELEGATED and then to any other state, any content associated with P has been wiped . XCTGQZ Any sequence of Granule state transitions which passes through the GRAN\_DELEGATED state causes the Granule contents to be wiped. This is necessary to ensure that information does not leak from one Realm to another, or from a Realm to the Host. Note that no agent can observe the contents of a Granule while its state is GRAN\_DELEGATED.
- Wiping of a memory location does not reveal, directly or indirectly, any confidential Realm data.
- Possible implementations of wiping include:
- The RMM (or other platform firmware) writing either random data or zeroes to the memory location
- The MEC of the memory location being changed
- The state of a device, which is observable via MMIO to the memory location, being reset
- Realm software should not assume that the initial contents of uninitialized memory (that is, Realm IPA space which is backed by DATA Granules created using RMI\_RTT\_DATA\_MAP) are zero.

See also:

- Arm CCA Security model [4]
- A2.3.6 Granule state
- B4.5.65 RMI\_RTT\_DATA\_MAP command

## A2.3.9 Granule Protection Table management


GPT unfolding is the operation of creating an L1GPT, by applying the following process:

1. Locate the L0GPT entry which describes the target physical address range.
2. Check that the L0GPT entry is a Block descriptor.

3. Transition the state of all Granules in the L1GPT from GRAN\_UNDELEGATED to GPT\_L1.
4. Populate all entries of the L1GPT with the GPI value taken from the L0GPT Block descriptor.
5. Replace the L0GPT Block descriptor with an L0GPT Table descriptor whose output address points to the L1GPT.

GPT unfolding is performed by execution of RMI\_GPT\_L1\_CREATE.

An L1GPT is homogeneous if all its entries have the same GPI value.

- The function GptL1IsHomogeneous() is used to evaluate whether an L1GPT is homogeneous.
- An L1GPT is self-describing if it is stored within the physical address range which it describes.
- GPT folding is the operation of destroying an L1GPT, by applying the following process:
1. Check that the L1GPT is homogeneous. If the L1GPT is self-describing then this check excludes the GPIs which describe the memory which stores the L1GPT itself.
2. Replace the parent L0GPT Table descriptor with an L0GPT Block descriptor, copying the GPI value from the L1GPT.
3. Transition the state of all Granules in the L1GPT from GPT\_L1 to GRAN\_UNDELEGATED.
- GPT folding is performed by execution of RMI\_GPT\_L1\_DESTROY.
- On execution of RMI\_GPT\_L1\_CREATE, the memory which constitutes the L1GPT is provided via the 'donate memory to a Stateful RMI Operation (SRO)' flow.
- If RMI\_GPT\_L1\_CREATE fails then the Granules which constitute the L1GPT remain in the Non-secure PAS.
- If RMI\_GPT\_L1\_CREATE returns RMI\_INCOMPLETE then the creation operation must be completed before the L1GPT can be destroyed.
- On execution of RMI\_GPT\_L1\_DESTROY, the memory which constitutes the L1GPT is returned via the 'reclaim memory from a Stateful RMI Operation (SRO)' flow.
- If RMI\_GPT\_L1\_DESTROY returns RMI\_INCOMPLETE then the destruction operation must be completed before a new L1GPT which describes the same physical address region can be created.
- Creation or destruction of L1GPTs which describes different physical address regions may be performed concurrently.

See also:


- A5.6.6 RTT folding
- A5.6.7 RTT unfolding
- B3.37 GptL1IsHomogeneous function
- B4.3.2.2 Donating memory to an SRO
- B4.3.2.3 Reclaiming memory from an SRO
- B4.5.15 RMI\_GPT\_L1\_CREATE command
- B4.5.16 RMI\_GPT\_L1\_DESTROY command