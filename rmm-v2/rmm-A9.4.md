## A9.4 Virtual device object

A virtual device (VDEV) represents the binding between a device function and a Realm.

## A9.4.1 Virtual device attributes


The attributes of a VDEV are summarized in the following table.

| Name           | Type              | Description                                                                                |
|----------------|-------------------|--------------------------------------------------------------------------------------------|
| vdev_id        | Bits64            | Virtual device identifier                                                                  |
| tdi_id         | Bits64            | TDI identifier                                                                             |
| pdev           | Address           | PA of parent PDEV                                                                          |
| realm          | Address           | PA of RD of Realm which owns this VDEV                                                     |
| vdev_state     | RmmVdevState      | VDEV lifecycle state                                                                       |
| dma_state      | RmmVdevDmaState   | DMAstate                                                                                   |
| non_ats_plane  | UInt64            | Index of Plane whose stage 2 permissions are observed by non-ATS requests from the device  |
| op             | RmmVdevOperation  | Operation performed on this VDEV                                                           |
| comm_state     | RmmDevCommState   | Device communication state                                                                 |
| vsmmu          | RmmFeature        | Whether device uses a VSMMU                                                                |
| vsmmu_addr     | Address           | PA of VSMMU. This field is valid if vsmmu is FEATURE_TRUE.                                 |
| vsid           | Bits64             Virtual Stream Identifier. This field is valid if vsmmu is FEATURE_TRUE.             |
| attest_info    | RmmVdevAttestInfo | Attestation information                                                                    |
| meas_digest    | Bits512           | Measurement digest                                                                         |
| report_digest  | Bits512           | Interface report digest                                                                    |
| p2p_bound      | RmmFeature        | Whether VDEV is bound to a P2P peer VDEV                                                   |
| p2p_peer       | Bits64            | VDEV ID of P2P peer VDEV                                                                   |
| num_addr_range | UInt64            | Number of device address ranges                                                            |
| addr_range     | RmmAddrRange[8]   | Device address ranges. These ranges include both coherent and non- coherent device memory. |

A Device identifier is a value which identifies a VDEV within a Realm, and is agreed between the Host and the Realm to which the VDEV is assigned.

The choice of device identifier depends upon the interface provided by the Host to the Realm. For example, if the Host provides a PCIe interface, then identifier is a PCIe (bus, device, function) tuple.

The Host provides the device identifier when executing RMI\_VDEV\_CREATE.

The Realm provides the device identifier when executing any RSI\_VDEV command. See also:


- A9.4.4 Mapping from virtual device ID to VDEV object
- A9.6 Realm management of an assigned virtual device
- B4.5.82 RMI\_VDEV\_CREATE command

## A9.4.2 Virtual device invariants

This section lists invariants which are enforced via checks performed by the RMM on execution of RMI\_VDEV\_CREATE.

Execution of RMI\_VDEV\_CREATE fails if the required Level 2 Stream Table is not present

RFQHHK pdev.num\_vdevs is not greater than pdev.max\_num\_vdevs.

RCVHND vdev.vdev\_id is unique among VDEVs assigned to a Realm.

RLBQZT vdev.tdi\_id is unique among VDEVs within the same segment.

The RMM can track usage of tdi\_id values within a segment either using SW\_RESERVED bits in the SMMU Stream Table Entry, or using an IMPLEMENTATION DEFINED data structure stored within the PDEV object.

RHJYPM vdev.tdi\_id is within the RID range of the parent PDEV.

All entries in vdev.addr\_range are disjoint.

All entries in vdev.addr\_range have the following properties:

- Fall within the union of address ranges for NCOH and COH PDEV streams associated with the parent PDEV.
- Not used by any other VDEV with the same parent PDEV.

## See also:

- [A9.2.2 Physical device invariants](rmm-A9.2.md#a922-physical-device-invariants)
- [B4.5.82 RMI\_VDEV\_CREATE command](rmm-B4.5.82.md)
- [B4.5.83 RMI\_VDEV\_DESTROY command](rmm-B4.5.83.md)

## A9.4.3 Virtual device lifecycle

## A9.4.3.1 States

The states of a VDEV are listed below.


| State            | Description                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------|
| VDEV_NEW         | Initial state of the device interface.                                                                  |
| VDEV_UNLOCKED    | Device interface is unlocked.                                                                           |
| VDEV_LOCKED      | Device interface is locked.                                                                             |
| VDEV_STARTED     | Device interface is started.                                                                            |
| VDEV_ERROR       | Device interface has reported a fatal error.                                                            |
| VDEV_KEY_REFRESH | Waiting for key refresh to be performed on all streams associated with the device interface.            |
| VDEV_KEY_PURGE   | Waiting for purge of inactive keys to be performed on all streams associated with the device interface. |

The platform may require the Host to perform a key refresh then purge inactive keys from all streams associated with a given device when a VDEV is unlocked. This sequence ensures that any transactions, which were either initiated by the VDEV or which target resources of the VDEV, are completed. This in turn can be used to prevent

<!-- image -->

violations of confidentiality or integrity, which could arise if those transactions were delayed in the IO fabric and later released.

See also:

- [A9.3.3.2.3 Stream key refresh](rmm-A9.3.md#a93323-stream-key-refresh)
- [A9.3.3.2.4 Stream key purge](rmm-A9.3.md#a93324-stream-key-purge)

## A9.4.3.2 State transitions

Permitted VDEV state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a VDEV. A transition to the pseudo-state NULL represents destruction of a VDEV.

In this diagram:

- 'RMI\_VDEV\_COMMUNICATE returns COMPLETE' means that the RmiDevCommExitFlags indicate that device communication is complete.
- 'RMI\_VDEV\_COMMUNICATE returns INCOMPLETE' means that the RmiDevCommExitFlags indicate that device communication is not complete.

Figure A9.8: VDEV state transitions

<!-- image -->

While a VDEV is in VDEV\_NEW state, execution of RMI\_VDEV\_COMMUNICATE causes the RMM to initialize the device.

Once device initialization is complete, the VDEV moves to VDEV\_UNLOCKED state.

- On execution of RMI\_VDEV\_UNLOCK, if the state of any Granule within the VDEV's PA ranges is GRAN\_DEV then the command fails with RMI\_ERROR\_GRANULE and returns the PA of the Granule.
- While a VDEV is in VDEV\_UNLOCKED state, execution of RMI\_VDEV\_LOCK causes the RMM to initiate a request to lock the device. The request is sent to the device via subsequent execution of RMI\_VDEV\_COMMUNICATE.

Once the RMI\_VDEV\_LOCK request is complete, the VDEV moves to VDEV\_LOCKED state.

- While a VDEV is in VDEV\_LOCKED state, execution of RMI\_VDEV\_START causes the RMM to initiate a request to start the device. The request is sent to the device via subsequent execution of RMI\_VDEV\_COMMUNICATE.

Once the RMI\_VDEV\_START request is complete, the VDEV moves to VDEV\_STARTED state.

- While a VDEV is in VDEV\_LOCKED state, execution of RMI\_VDEV\_UNLOCK causes the RMM to initiate a request to unlock the device. The request is sent to the device via subsequent execution of RMI\_VDEV\_COMMUNICATE.

Once the RMI\_VDEV\_UNLOCK request is complete, the VDEV moves to VDEV\_UNLOCKED state.

- While a VDEV is in VDEV\_STARTED state, execution of RMI\_VDEV\_UNLOCK causes the RMM to initiate a request to unlock the device. The request is sent to the device via subsequent execution of RMI\_VDEV\_COMMUNICATE.

Once the RMI\_VDEV\_UNLOCK request is complete:

- If the platform requires key refresh on VDEV unlock then the VDEV moves to VDEV\_KEY\_REFRESH state.
- Otherwise the VDEV moves to VDEV\_UNLOCKED state.

The requirement for key refresh on VDEV unlock is discoverable via RMI\_FEATURES.

- While a VDEV is in VDEV\_KEY\_REFRESH state, the Host is expected to perform a key refresh on all PDEV streams which are associated with the VDEV.

Once the key refreshes are complete, execution of RMI\_VDEV\_COMMUNICATE causes the VDEV moves to VDEV\_KEY\_PURGE state.

- While a VDEV is in VDEV\_KEY\_PURGE state, the Host is expected to purge inactive keys from all PDEV streams which are associated with the VDEV.


Once the key purges are complete, execution of RMI\_VDEV\_COMMUNICATE causes the RMM to initiate a request to unlock the device. The request is sent to the device via subsequent execution of RMI\_VDEV\_COMMUNICATE.

Once the unlock request is complete, the VDEV moves to VDEV\_UNLOCKED state.

- On execution of RMI\_VDEV\_COMMUNICATE, if the RMM detects a fatal error (such as an unexpected response or a protocol error) then the VDEV moves to VDEV\_ERROR state.
- While a VDEV is in VDEV\_ERROR state, execution of RMI\_VDEV\_UNLOCK causes the RMM to initiate a request to unlock the device. The request is sent to the device via subsequent execution of RMI\_VDEV\_COMMUNICATE.

Once the lock request is complete, the VDEV moves to VDEV\_UNLOCKED state.

- Execution of RMI\_VDEV\_UNLOCK fails if the VDEV has associated device memory mappings.
- While the state of a VDEV is VDEV\_NEW, VDEV\_UNLOCKED or VDEV\_ERROR, the Host can reclaim resources by executing RMI\_VDEV\_DESTROY.


Permitted VDEV state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a VDEV object. A transition to the pseudo-state NULL represents destruction of a VDEV object.

| From state       | To state         | Events                              |
|------------------|------------------|-------------------------------------|
| NULL             | VDEV_NEW         | RMI_VDEV_CREATE                     |
| VDEV_NEW         | VDEV_NEW         | RMI_VDEV_ABORT RMI_VDEV_COMMUNICATE |
| VDEV_NEW         | VDEV_UNLOCKED    | RMI_VDEV_COMMUNICATE                |
| VDEV_UNLOCKED    | VDEV_LOCKED      | RMI_VDEV_COMMUNICATE                |
| VDEV_LOCKED      | VDEV_STARTED     | RMI_VDEV_COMMUNICATE                |
| VDEV_LOCKED      | VDEV_KEY_REFRESH | RMI_VDEV_COMMUNICATE                |
| VDEV_STARTED     | VDEV_KEY_REFRESH | RMI_VDEV_COMMUNICATE                |
| VDEV_KEY_REFRESH | VDEV_KEY_PURGE   | RMI_VDEV_COMMUNICATE                |
| VDEV_KEY_PURGE   | VDEV_UNLOCKED    | RMI_VDEV_COMMUNICATE                |
| VDEV_ERROR       | VDEV_UNLOCKED    | RMI_VDEV_COMMUNICATE                |
| VDEV_NEW         | NULL             | RMI_VDEV_DESTROY                    |
| VDEV_UNLOCKED    | NULL             | RMI_VDEV_DESTROY                    |

## See also:

- [B4.5.79 RMI\_VDEV\_ABORT command](rmm-B4.5.79.md)
- [B4.5.80 RMI\_VDEV\_COMMUNICATE command](rmm-B4.5.80.md)
- [B4.5.82 RMI\_VDEV\_CREATE command](rmm-B4.5.82.md)
- [B4.5.83 RMI\_VDEV\_DESTROY command](rmm-B4.5.83.md)

## See also:

- [A9.3.3.2.3 Stream key refresh](rmm-A9.3.md#a93323-stream-key-refresh)
- [A9.3.3.2.4 Stream key purge](rmm-A9.3.md#a93324-stream-key-purge)
- [B4.5.14 RMI\_FEATURES command](rmm-B4.5.14.md)
- [B4.5.80 RMI\_VDEV\_COMMUNICATE command](rmm-B4.5.80.md)
- [B4.5.87 RMI\_VDEV\_LOCK command](rmm-B4.5.87.md)
- [B4.5.90 RMI\_VDEV\_START command](rmm-B4.5.90.md)
- [B4.5.91 RMI\_VDEV\_UNLOCK command](rmm-B4.5.91.md)

## A9.4.4 Mapping from virtual device ID to VDEV object

- The RMM does not maintain a mapping from virtual device ID to VDEV object. Conseqeuntly, when a Realm executes an RSI\_VDEV command, passing a virtual device ID, the RMM must request the Host to provide a corresponding VDEV object.
- The following sequence diagram shows how the virtual device ID passed by a Realm is mapped to the corresponding VDEV object.

If the mapping is not completed (because either the Host provided the incorrect VDEV object, or provided no VDEV object), an error is returned to the Realm following the next REC entry.


Figure A9.9: Mapping from virtual device ID to VDEV

<!-- image -->

See also:

- [A4.3.12 REC exit due to VDEV request](rmm-A4.3.md#a4312-rec-exit-due-to-vdev-request)
- [B4.5.81 RMI\_VDEV\_COMPLETE command](rmm-B4.5.81.md)
- [B5.4.19 RSI\_VDEV\_GET\_INFO command](rmm-B5.4.19.md)

## A9.4.4.1 Relationship between VDEV state and TDISP TDI state

- The lifecycle of a VDEV closely resembles the lifecycle of a TDISP TDI. There cannot exist a direct mapping between the two, because changes in TDI state (for example due to Host action) may not be immediately observed by either the RMM or the Realm. However, the two states are sufficiently closely coupled to provide the Realm with important guarantees regarding the TDI state.
- On transition of a VDEV to VDEV\_LOCKED state, the corresponding TDI transitions to CONFIG\_LOCKED state.
- On transition of a VDEV to VDEV\_STARTED state, the corresponding TDI transitions to RUN state.
- On detection by the RMM that a TDI is in ERROR state, the corresponding VDEV transitions to VDEV\_ERROR state.

See also:

- PCI Express 6.0 specification [16]

## A9.4.4.2 Relationship between VDEV state and SMMU enablement

- When the DMA state of a VDEV is VDEV\_DMA\_ENABLED, the SMMU permits traffic from the device to the Realm's Protected IPA space.
- When the DMA state of a VDEV is VDEV\_DMA\_DISABLED, the SMMU blocks traffic from the device to the Realm's Protected IPA space.
- Execution of RMI\_VDEV\_UNLOCK caused the DMA state of the VDEV to become VDEV\_DMA\_DISABLED.


## A9.4.5 Virtual device flows

## A9.4.5.1 Virtual device teardown flow

Teardown of a VDEV is illustrated in the following sequence diagram.

Figure A9.10: VDEV teardown (part 1 of 2)

<!-- image -->

## Chapter A9. Realm device assignment A9.4. Virtual device object

Figure A9.11: VDEV teardown (part 2 of 2)

<!-- image -->

## See also:

- [B4.5.70 RMI\_RTT\_DEV\_UNMAP command](rmm-B4.5.70.md)
- [B4.5.80 RMI\_VDEV\_COMMUNICATE command](rmm-B4.5.80.md)
- [B4.5.83 RMI\_VDEV\_DESTROY command](rmm-B4.5.83.md)
- [B4.5.91 RMI\_VDEV\_UNLOCK command](rmm-B4.5.91.md)