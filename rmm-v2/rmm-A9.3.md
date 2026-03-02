## A9.3 Physical device stream object

- DZJKLQ A Physical Device Stream (PDEV stream) represents a category of traffic to an endpoint device.
- IXSYXF A PDEV stream may represent any of the following:
- Traffic between a Root Port an an off-chip endpoint device
- Traffic between the system and an on-chip endpoint device
- Direct peer-to-peer (P2P) traffic between two endpoint devices
- DHLMRX The supported categories of PDEV stream are summarized in the following table.

| Name                 | Description                                                                           |
|----------------------|---------------------------------------------------------------------------------------|
| PDEV_STREAM_COH      | Coherent traffic between an upstream port and an accelerator endpoint device.         |
| PDEV_STREAM_COH_CMEM | Coherent traffic between an upstream port and a CMEMendpoint device.                  |
| PDEV_STREAM_COH_SYS  | Coherent traffic to an endpoint device which is protected by system construction.     |
| PDEV_STREAM_NCOH     | Non-coherent traffic between an upstream port and an endpoint device.                 |
| PDEV_STREAM_NCOH_P2P | Non-coherent traffic between two endpoint devices.                                    |
| PDEV_STREAM_NCOH_SYS | Non-coherent traffic to an endpoint device which is protected by system construction. |
| PDEV_STREAM_NON_TEE  | Non-TEE traffic.                                                                      |

IHGDFC Connection of a PDEV stream is managed by the Host by execution of RMI commands.

IVGNJY Creation of a VDEV is conditional on a sufficient set of PDEV streams having first been established. Satisfaction of this requirement is represented by the return value from the PdevStreamsForVdev() function, which is called by an RMI\_VDEV\_CREATE pre-condition.

DRAFT

- IVFFWG Traffic paths which are protected by system construction may include switches only if these are pass-through.

## See also:

- A9.2 Physical device object
- A9.4 Virtual device object
- A9.10 Peer-to-peer device communication
- B3.81 PdevStreamsForVdev function
- B4.5.34 RMI\_PDEV\_STREAM\_CONNECT command
- B4.5.82 RMI\_VDEV\_CREATE command

## A9.3.1 Physical device stream attributes

DQCFDL The attributes of a PDEV stream are summarized in the following table.

| Name        | Type               | Description   |
|-------------|--------------------|---------------|
| handle      | Bits64             | Stream handle |
| state       | RmmPdevStreamState | Stream state  |
| stream_type | RmmPdevStreamType  | Stream type   |

| Name           | Type             | Description                     |
|----------------|------------------|---------------------------------|
| ide_sid        | UInt64           | IDE stream identifier           |
| num_addr_range | UInt64           | Number of device address ranges |
| addr_range     | RmmAddrRange[16] | Device address range            |

The meaning and validity of some PDEV stream attributes depends on the stream type. This is summarized in the following table.

A blank cell indicates that the corresponding RmiPdevStreamParams attribute is ignored by RMI\_PDEV\_STREAM\_CONNECT.

| stream_type   | pdev_1                | pdev_2                       | ide_sid   | addr_range   | IDE stream type           |
|---------------|-----------------------|------------------------------|-----------|--------------|---------------------------|
| NON_TEE       | Endpoint device       | Root Port                    | Required  |              | PCIe Link IDE stream      |
| NCOH          | Endpoint device       | Root Port                    | Required  | Required     | PCIe Selective IDE stream |
| COH           | Endpoint device       | Root Port                    |           | Required     | CXL.cachemem IDE          |
| COH_CMEM      | Endpoint device       | Root Port                    |           |              | CXL.cachemem IDE          |
| NCOH_P2P      | First endpoint device | DRAFT Second endpoint device | Required  |              | PCIe Selective IDE stream |
| NCOH_SYS      | Endpoint device       |                              |           | Required     | Not Applicable            |
| COH_SYS       | Endpoint device       |                              |           | Required     | Not Applicable            |

IDSZBR

The following table shows the set of PDEV streams which are typically required for each of a set of use cases.

A * indicates that the stream type is optional, depending on the device implementation.

| Use case                        | PDEV stream type   | PDEV stream type   |          |          |          |         |      |
|---------------------------------|--------------------|--------------------|----------|----------|----------|---------|------|
|                                 | NON_TEE            | COH                | COH_CMEM | NCOH_P2P | NCOH_SYS | COH_SYS | NCOH |
| PCIe NON_TEE traffic protection | Y                  | N                  | N        | N        | N        | N       | N    |
| PCIe off-chip                   | *                  | N                  | N        | *        | N        | N       | Y    |
| PCIe on-chip                    | N                  | N                  | N        | N        | Y        | N       | N    |
| CXL / CHI off-chip accelerator  | N                  | Y                  | N        | N        | N        | N       | *    |
| CXL / CHI on-chip accelerator   | N                  | N                  | N        | N        | *        | Y       | N    |
| CXL type-3 memory expansion     | N                  | N                  | *        | N        | N        | N       | N    |

## A9.3.2 Physical device stream invariants

This section lists invariants which are enforced via checks performed by the RMM on execution of RMI\_PDEV\_STREAM\_CONNECT.

RPHXKJ All entries in stream.addr\_range have the following properties:

- Not used by any other PDEV stream.

DRAFT

- If the stream type is NCOH or NCOH\_SYS, fall within the physical address region(s) of the system memory map which are reserved for non-coherent device memory.
- If the stream type is COH or COH\_SYS, fall within the physical address region(s) of the system memory map which are reserved for coherent device memory.

RNVLDN For a stream whose type is NCOH, COH or COH\_CMEM the range [pdev\_1.rid\_base, does not overlap any other device in the same PCIe segment.

pdev\_1.rid\_top)

RQGJQB For a stream whose type is NCOH or NCOH\_P2P the ide\_sid does not match any existing stream in either device.

## See also:

- A2.3.2 Views of physical memory
- A2.3.4 Granule tracking region
- B4.5.34 RMI\_PDEV\_STREAM\_CONNECT command

## A9.3.3 Physical device stream lifecycle

## A9.3.3.1 States

DVZFBD

The states of a PDEV stream are listed below.

<!-- image -->

IVVHZT

| State                      | Description                      |
|----------------------------|----------------------------------|
| PDEV_STREAM_DISCONNECTED   | PDEV_STREAM_DISCONNECTED         |
|                            | Stream is not connected.         |
| PDEV_STREAM_CONNECTING     | PDEV_STREAM_CONNECTING           |
|                            | Stream is connecting.            |
| PDEV_STREAM_CONNECTED      | PDEV_STREAM_CONNECTED            |
|                            | Stream is connected.             |
| PDEV_STREAM_DISCONNECTING  | PDEV_STREAM_DISCONNECTING        |
|                            | Stream is disconnecting.         |
| PDEV_STREAM_KEY_REFRESHING | PDEV_STREAM_KEY_REFRESHING       |
|                            | Stream keys are being refreshed. |
| PDEV_STREAM_KEY_PURGING    | PDEV_STREAM_KEY_PURGING          |
|                            | Stream keys are being purged.    |

## A9.3.3.2 State transitions

Permitted PDEV stream state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

| From state                 | To state                   | Events                      |
|----------------------------|----------------------------|-----------------------------|
| PDEV_STREAM_DISCONNECTED   | PDEV_STREAM_CONNECTING     | RMI_PDEV_STREAM_CONNECT     |
| PDEV_STREAM_CONNECTING     | PDEV_STREAM_CONNECTED      | RMI_PDEV_STREAM_COMPLETE    |
| PDEV_STREAM_CONNECTED      | PDEV_STREAM_DISCONNECTING  | RMI_PDEV_STREAM_DISCONNECT  |
| PDEV_STREAM_DISCONNECTING  | PDEV_STREAM_DISCONNECTED   | RMI_PDEV_STREAM_COMPLETE    |
| PDEV_STREAM_CONNECTED      | PDEV_STREAM_KEY_REFRESHING | RMI_PDEV_STREAM_KEY_REFRESH |
| PDEV_STREAM_KEY_REFRESHING | PDEV_STREAM_CONNECTED      | RMI_PDEV_STREAM_COMPLETE    |
| PDEV_STREAM_CONNECTED      | PDEV_STREAM_KEY_PURGING    | RMI_PDEV_STREAM_KEY_PURGE   |
| PDEV_STREAM_KEY_PURGING    | PDEV_STREAM_CONNECTED      | RMI_PDEV_STREAM_COMPLETE    |

DRAFT

## A9.3.3.2.1 Stream connection

| I WMCXY   | Execution of RMI_PDEV_STREAM_CONNECT initiates connection of the stream.                       |
|-----------|------------------------------------------------------------------------------------------------|
| I TPGZH   | RMI_PDEV_STREAM_CONNECT fails if either PDEV already has the maximum number of streams.        |
| I GYXYM   | RMI_PDEV_STREAM_CONNECT fails if the endpoint PDEV already has a stream of the specified type. |
| I RSCKV   | RMI_PDEV_STREAM_CONNECT fails if the state of either PDEV is not PDEV_READY.                   |
| I GLYZR   | RMI_PDEV_STREAM_CONNECT fails if the operation of either PDEV is not PDEV_OP_NONE.             |

- IXSZZV

On successful execution of RMI\_PDEV\_STREAM\_CONNECT, all of the following are true:

- A stream handle is returned. Note that this is an IMPLEMENTATION DEFINED value which identifies the stream, and is distinct from the hardware stream ID.
- The stream state is PDEV\_STREAM\_CONNECTING.
- For each of the PDEV(s) associated with the stream a device transaction is initiated and the device operation is PDEV\_OP\_CONNECT.
- IVZVBJ Following execution of RMI\_PDEV\_STREAM\_CONNECT, if RMI\_PDEV\_COMMUNICATE with one PDEV sets the RmiDevCommExitFlags::stream\_wait then device communication with the other PDEV must proceed before the the first device communication can proceed.
- IWRLHB Following execution of RMI\_PDEV\_STREAM\_CONNECT, when device communication is complete with either PDEV, the device operation of that PDEV is set to PDEV\_OP\_STREAM\_COMPLETE.
- IDTGGH Following execution of RMI\_PDEV\_STREAM\_CONNECT, when device communication is complete with both PDEVs, execution of RMI\_PDEV\_STREAM\_COMPLETE completes connection of the stream. The stream state transitions to PDEV\_STREAM\_CONNECTED.
- ICNKPG For details of Root Port IDE key programming which is performed during PDEV stream connection, refer to Firmware Interfaces for RME (FIRME) specification [19].

See also:

- Firmware Interfaces for RME (FIRME) specification [19]
- A9.5 Communication between RMM and a device
- B4.5.33 RMI\_PDEV\_STREAM\_COMPLETE command
- B4.5.34 RMI\_PDEV\_STREAM\_CONNECT command

## A9.3.3.2.2 Stream disconnection

- ILFDYY Execution of RMI\_PDEV\_STREAM\_DISCONNECT initiates disconnection of the stream.
- IDHRSY Input values to RMI\_PDEV\_STREAM\_DISCONNECT include the stream handle which was returned by RMI\_PDEV\_STREAM\_CONNECT.
- IMZRXZ RMI\_PDEV\_STREAM\_DISCONNECT fails if the endpoint PDEV has a non-zero number of VDEVs.
- IZJRPJ On successful execution of RMI\_PDEV\_STREAM\_DISCONNECT, all of the following are true:
- The stream state is PDEV\_STREAM\_DISCONNECTING.

DRAFT

- For each of the PDEV(s) associated with the stream a device transaction is initiated and the device operation is PDEV\_OP\_DISCONNECT.
- IZDMQX Following execution of RMI\_PDEV\_STREAM\_DISCONNECT, when device communication is complete with either PDEV, the device operation of that PDEV is set to PDEV\_OP\_STREAM\_COMPLETE.
- IZFWFK Following execution of RMI\_PDEV\_STREAM\_DISCONNECT, when device communication is complete with both PDEVs, execution of RMI\_PDEV\_STREAM\_COMPLETE completes disconnection of the stream. The stream state transitions to PDEV\_STREAM\_DISCONNECTED.

See also:

- B4.5.33 RMI\_PDEV\_STREAM\_COMPLETE command
- B4.5.35 RMI\_PDEV\_STREAM\_DISCONNECT command

## A9.3.3.2.3 Stream key refresh

- ICFHHD Execution of RMI\_PDEV\_STREAM\_KEY\_REFRESH initiates key refresh of a stream.
- IJYRBD Input values to RMI\_PDEV\_STREAM\_KEY\_REFRESH include the stream handle which was returned by RMI\_PDEV\_STREAM\_CONNECT.

IPKWKD On successful execution of RMI\_PDEV\_STREAM\_KEY\_REFRESH, all of the following are true:

- The stream state is PDEV\_STREAM\_KEY\_REFRESHING.
- For each of the PDEV(s) associated with the stream a device transaction is initiated and the device operation is PDEV\_OP\_KEY\_REFRESH.
- IKWPNV Following execution of RMI\_PDEV\_STREAM\_KEY\_REFRESH, when device communication is complete with either PDEV, the device operation of that PDEV is set to PDEV\_OP\_STREAM\_COMPLETE.
- IWJQCZ Following execution of RMI\_PDEV\_STREAM\_KEY\_REFRESH, when device communication is complete with both PDEVs, execution of RMI\_PDEV\_STREAM\_COMPLETE completes key refresh of the stream. The stream state transitions to PDEV\_STREAM\_CONNECTED.
- ISZNMZ PDEV stream key refresh may be required in order to complete unlocking of a VDEV. This requirement is discoverable via RMI\_FEATURES.

See also:

- A9.4.3 Virtual device lifecycle
- B4.5.14 RMI\_FEATURES command
- B4.5.33 RMI\_PDEV\_STREAM\_COMPLETE command
- B4.5.37 RMI\_PDEV\_STREAM\_KEY\_REFRESH command

## A9.3.3.2.4 Stream key purge

- IPCMTZ Execution of RMI\_PDEV\_STREAM\_KEY\_PURGE initiates purge of inactive keys from the stream.
- IVTDCS Input values to RMI\_PDEV\_STREAM\_KEY\_PURGE include the stream handle which was returned by RMI\_PDEV\_STREAM\_CONNECT.
- IMTDQQ On successful execution of RMI\_PDEV\_STREAM\_KEY\_PURGE, all of the following are true:
- The stream state is PDEV\_STREAM\_KEY\_PURGING.
- For each of the PDEV(s) associated with the stream a device transaction is initiated and the device operation is PDEV\_OP\_KEY\_PURGE.
- IKNZRB Following execution of RMI\_PDEV\_STREAM\_KEY\_PURGE, when device communication is complete with either PDEV, the device operation of that PDEV is set to PDEV\_OP\_STREAM\_COMPLETE.
- ICSTJR Following execution of RMI\_PDEV\_STREAM\_KEY\_PURGE, when device communication is complete with both PDEVs, execution of RMI\_PDEV\_STREAM\_COMPLETE completes purge of inactive keys from the stream. The stream state transitions to PDEV\_STREAM\_CONNECTED.

DRAFT

- ILHSTX Purging of inactive keys from streams associated with the device may be required in order to complete unlocking of a VDEV. This requirement is discoverable via RMI\_FEATURES.

See also:

- A9.4.3 Virtual device lifecycle
- B4.5.14 RMI\_FEATURES command
- B4.5.33 RMI\_PDEV\_STREAM\_COMPLETE command
- B4.5.36 RMI\_PDEV\_STREAM\_KEY\_PURGE command

## A9.3.3.3 Physical device stream setup flow

IFGSKS Setup of a PDEV stream between a Root Port and a PCIe off-chip accelerator endpoint device is illustrated in the following sequence diagram.

Figure A9.6: Setup of a PDEV stream between a Root Port and a PCIe off-chip accelerator endpoint device

<!-- image -->

IYWBYW Setup of a PDEV stream between a Root Port and a PCIe on-chip accelerator endpoint device is illustrated in the following sequence diagram.

Figure A9.7: Setup of a PDEV stream between a Root Port and a PCIe on-chip accelerator endpoint device

<!-- image -->