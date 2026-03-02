## A9.2 Physical device object

- A Physical Device

(PDEV) represents a communication channel between the RMM and a physical device.


The physical device represented by a PDEV is one of the following:

- A Root Port.
- An endpoint device whose resources are mapped as special-purpose memory. For example, a PCIe accelerator or a CHI / CXL accelerator.
- An endpoint device whose resources are mapped as conventional memory For example, a CXL type-3 memory expansion device.

## A9.2.1 Physical device attributes


<!-- image -->

The attributes of a PDEV are summarized in the following table.

| Name                         | Type                         | Description                                                                   |
|------------------------------|------------------------------|-------------------------------------------------------------------------------|
| category                     | RmmPdevCategory              | Device category                                                               |
| pdev_id                      | Bits64                       | Device identifier                                                             |
| routing_id                   | Bits64                       | Routing identifier                                                            |
| rid_base                     | Bits16                        Base of requester ID range (inclusive). The value is in PCI BDF format. |
| rid_top                      | Bits16                       | Top of requester ID range (exclusive). The value is in PCI BDF format.        |
| spdm                         | RmmPdevSpdm                  | Whether communication with the device uses SPDM                               |
| signed_meas                  | RmmFeature                   | Whether device supports signed measurements                                   |
| id_index                     | UInt64                       | Device identity index                                                         |
| hash_algo                    | RmmHashAlgorithm             | Algorithm used to generate device digests                                     |
| state                        | RmmPdevState                 | Lifecycle state                                                               |
| op                           | RmmPdevOperation             | Operation performed on this PDEV                                              |
| comm_state                   | RmmDevCommState              | Device communication state                                                    |
| max_num_vdevs                | UInt64                       | Maximum number of VDEVs which can be associated with this PDEV                |
| num_vdevs                    | UInt64                       | Number of VDEVs associated with this PDEV                                     |
| p2p_enabled                  | RmmFeature                   | TRUE if this device can be associated with a Direct P2P IDE stream            |
| negotiation_data_dig Bits512 | negotiation_data_dig Bits512 | Protocol negotiation data digest                                              |
| feat_tse                     | RmmFeature                   | Whether this device supports Target-Side Encryption                           |
| cmem_count                   | UInt64                       | Number of CMEMobjects with which this PDEV is associated                      |

For a device which uses SPDM communication, negotiation\_data\_digest field corresponds to the VCA digest. VCA is a concatenation of the following SPDM requests and responses:



- VERSION\_REQ
- VERSION\_RESP
- CAP\_REQ
- CAP\_RESP
- NEGO\_REQ
- NEGO\_RESP

The following table describes how combinations of PDEV attributes map to different types of devices.

| PDEV attributes   | PDEV attributes   | PDEV attributes         | PDEV attributes                              |
|-------------------|-------------------|-------------------------|----------------------------------------------|
| spdm              | p2p               | category                | Device type                                  |
| 1                 | 0                 | ROOT_PORT               | Root Port                                    |
| 1                 | *                 | ENDPOINT_ACCEL_OFF_CHIP | Off-chip PCIe accelerator with / without P2P |
| *                 | 0                 | ENDPOINT_ACCEL_ON_CHIP  | Integrated PCIe device                       |
| 1                 | *                 | ENDPOINT_ACCEL_OFF_CHIP | Off-chip coherent accelerator                |
| *                 | *                 | ENDPOINT_ACCEL_ON_CHIP  | Integrated coherent accelerator              |
| 1                 | 0                 | ENDPOINT_CMEM           | Off-chip CXL type-3 device                   |

The following table summarizes the meaning of the pdev\_id and routing\_id attributes, for each supported device category.

| category                                                       | pdev_id                                                                                                                                                                                                                                     | routing_id               |
|----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| ENDPOINT_ACCEL_OFF_CHIP or ENDPOINT_ACCEL_ON_CHIP or ROOT_PORT | Address of device entry in PCIe configuration space. The ECAM physical (system) address - the unique CPU-visible system physical address to the start of the target's or RP's PCIe Extended Configuration Space within an ECAM MMIO region. | PCIe segment identifier. |

## See also:

- PCI Express 6.0 specification [16]
- Compute eXpress Link specification [18]
- A9.11 Coherent memory devices
- B3.129 RmiPdevFlagsSupported function

## A9.2.2 Physical device invariants

This section lists invariants which are enforced via checks performed by the RMM on execution of RMI\_PDEV\_CREATE.

| R YDSRN   | On execution of RMI_PDEV_CREATE, TDISP_EN=1 is set at the corresponding Root Port.                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------|
| U YJXZG   | The latest point when the implementation may set TDISP_EN=1 is on creation of the first PDEV attached to that Root Port. |



pdev.max\_num\_vdevs is not greater than ((2 ˆ rmm.static.max\_vdevs\_order) - 1).

Once the state of a PDEV has transitioned to PDEV\_READY, the RMM has established secure communication with the device, which remains in place until the PDEV transitions to PDEV\_STOPPED.

For an integrated PDEV the range (pdev.rid\_base, pdev.rid\_top] falls within the platform-assigned RID range for the corresponding device.

## See also:

- A2.3.2 Views of physical memory
- A2.3.4 Granule tracking region
- A9.4.2 Virtual device invariants
- B4.5.27 RMI\_PDEV\_CREATE command

## A9.2.3 Physical device lifecycle

## A9.2.3.1 States

The states of a PDEV are listed below.

| State          | Description                                                                |
|----------------|----------------------------------------------------------------------------|
| PDEV_NEW       | Initial state of the device.                                               |
| PDEV_NEEDS_KEY | RMMneeds device public key.                                                |
| PDEV_HAS_KEY   | RMMhas device public key.                                                  |
| PDEV_READY     | Secure connection between the RMMand the device has been established.      |
| PDEV_STOPPED    Secure connection between the RMMand the device has been terminated. |
| PDEV_ERROR     | Device has reported a fatal error.                                         |

## A9.2.3.2 State transitions

Permitted PDEV Realm state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a PDEV. A transition to the pseudo-state NULL represents destruction of a PDEV.

In this diagram:

- 'RMI\_PDEV\_COMMUNICATE returns COMPLETE' means that the RmiDevCommExitFlags indicate that device communication is complete.
- 'RMI\_PDEV\_COMMUNICATE returns INCOMPLETE' means that the RmiDevCommExitFlags indicate that device communication is not complete.

<!-- image -->

Figure A9.3: PDEV state transitions

<!-- image -->

## A9.2.3.2.1 State transitions for a device which uses SPDM communication

While a PDEV which uses SPDM communication is in PDEV\_NEW state, execution of RMI\_PDEV\_COMMUNICATE causes the RMM to fetch the device certificate chain. The RMM stores a digest of the device certificate chain for later retrieval by the Realm. The Host is expected to cache the device certificate chain for later retrieval by the Realm.

Once device certificate chain retrieval is complete, the PDEV moves to PDEV\_NEEDS\_KEY state.

While a PDEV which uses SPDM communication is in PDEV\_HAS\_KEY state, execution of RMI\_PDEV\_COMMUNICATE causes the RMM to perform secure SPDM session establishment.

Secure SPDM session establishment includes verification of the signature in the SPDM KEY\_EXCHANGE response.

Once secure SPDM session establishment is complete, the PDEV moves to PDEV\_READY state.

A9.2.3.2.2 State transitions for a device which uses platform communication


While a PDEV which uses platform communication is in PDEV\_NEW state, execution of RMI\_PDEV\_COMMUNICATE causes the RMM to establish a communication channel with the device.

Once device identity evidence retrieval is complete, the PDEV moves to PDEV\_READY state.

## A9.2.3.2.3 State transitions for all devices

- While a device transaction is active for the PDEV, the Host can either:
- Transfer device requests and device responses by executing RMI\_PDEV\_COMMUNICATE. If the return value indicates that the device transaction is complete then the PDEV moves to PDEV\_READY state.
- Abort the device transaction by executing RMI\_PDEV\_ABORT. On successful execution of this command, the PDEV moves to either PDEV\_READY state or PDEV\_ERROR state.
- On execution of RMI\_PDEV\_COMMUNICATE, if the RMM detects a fatal error (such as an unexpected response or a protocol error) then the PDEV moves to PDEV\_ERROR state.
- While a PDEV is in any of the following states, the Host can request the RMM to stop the device by executing RMI\_PDEV\_STOP:
- PDEV\_NEW
- PDEV\_NEEDS\_KEY
- PDEV\_HAS\_KEY
- PDEV\_READY
- PDEV\_ERROR

A device transaction is initiated for the PDEV, with the operation set to PDEV\_OP\_STOP.

- While a PDEV has its operation set to PDEV\_OP\_STOP, the Host can enact the 'stop' device transaction by executing RMI\_PDEV\_COMMUNICATE.

If the return value indicates that the device transaction is complete then the PDEV moves to PDEV\_STOPPED state.

- While a PDEV has its operation set to PDEV\_OP\_STOP, if the device fails to respond or reports an error then the Host can call RMI\_PDEV\_COMMUNICATE, passing RMI\_DEV\_COMM\_ERROR.

On successful execution of this command, the PDEV moves to PDEV\_STOPPED state.

- While a PDEV is in PDEV\_STOPPED state, the Host can reclaim resources by executing RMI\_PDEV\_DESTROY.


This command will fail if the PDEV is associated with any VDEVs.

- Permitted PDEV state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a PDEV object. A transition to the pseudo-state NULL represents destruction of a PDEV object.

| From state     | To state       | Events                              |
|----------------|----------------|-------------------------------------|
| NULL           | PDEV_NEW       | RMI_PDEV_CREATE                     |
| PDEV_NEW       | PDEV_NEW       | RMI_PDEV_ABORT RMI_PDEV_COMMUNICATE |
| PDEV_NEW       | PDEV_NEEDS_KEY | RMI_PDEV_COMMUNICATE                |
| PDEV_NEW       | PDEV_READY     | RMI_PDEV_COMMUNICATE                |
| PDEV_NEEDS_KEY | PDEV_HAS_KEY   | RMI_PDEV_SET_PUBKEY                 |
| PDEV_HAS_KEY   | PDEV_HAS_KEY   | RMI_PDEV_ABORT RMI_PDEV_COMMUNICATE |

| From state     | To state     | Events               |
|----------------|--------------|----------------------|
| PDEV_HAS_KEY   | PDEV_READY   | RMI_PDEV_COMMUNICATE |
| PDEV_NEW       | PDEV_STOPPED | RMI_PDEV_STOP        |
| PDEV_NEEDS_KEY | PDEV_STOPPED | RMI_PDEV_STOP        |
| PDEV_HAS_KEY   | PDEV_STOPPED | RMI_PDEV_STOP        |
| PDEV_ERROR     | PDEV_STOPPED | RMI_PDEV_STOP        |
| PDEV_STOPPED   | NULL         | RMI_PDEV_DESTROY     |

## See also:

- B4.5.25 RMI\_PDEV\_ABORT command
- B4.5.26 RMI\_PDEV\_COMMUNICATE command
- B4.5.27 RMI\_PDEV\_CREATE command
- B4.5.28 RMI\_PDEV\_DESTROY command
- B4.5.31 RMI\_PDEV\_SET\_PUBKEY command
- B4.5.32 RMI\_PDEV\_STOP command

## See also:

- PCI Express 6.0 specification [16]
- A9.5 Communication between RMM and a device


## A9.2.4 Physical device flows

## A9.2.4.1 Physical device setup flow

Setup of a PDEV is illustrated in the following sequence diagram.

Figure A9.4: Setup of a PDEV

<!-- image -->

Establishment of a Secure SPDM session means that the requester (the RMM) has verified that the responder holds the private key which corresponds to the public key in the device leaf certificate. The identity and trustworthiness of the responder are not evaluated until the Realm receives attestation evidence for the device.


Mapping of the PDEV setup flow onto SPDM communication with a TDISP PCIe device is illustrated in the following sequence diagram.

Figure A9.5: Mapping of the PDEV setup flow onto SPDM communication with a TDISP PCIe device

<!-- image -->

Chapter A9. Realm device assignment A9.2. Physical device object

See also:

- PCI Express 6.0 specification [16]
- A9.5 Communication between RMM and a device
- B4.5.26 RMI\_PDEV\_COMMUNICATE command
- B4.5.27 RMI\_PDEV\_CREATE command
- B4.5.31 RMI\_PDEV\_SET\_PUBKEY command

<!-- image -->