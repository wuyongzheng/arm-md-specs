## A9.5 Communication between RMM and a device

This section describes how the RMM communicates management requests to the device.

See also:

- A9.1.2 Device properties

## A9.5.1 Device requests and responses

- Communication between the RMM and a device consists of a series of device requests sent from the RMM to the device and device responses returned by the device to the RMM.
- A device transaction is a series of one or more (device request, device response) tuples.
- A device transaction is initiated by Host execution of an RMI command.
- At the requester side (that is, at the RMM), a device transaction is associated with either a PDEV or a VDEV, depending on the event which triggered the device transaction:
- If the device transaction was triggered by one of the following RMI commands then the device transaction is associated with the PDEV.
- -RMI\_PDEV\_CREATE
- -RMI\_PDEV\_SET\_PUBKEY
- -RMI\_PDEV\_STOP
- -RMI\_PDEV\_STREAM\_CONNECT
- -RMI\_PDEV\_STREAM\_DISCONNECT
- -RMI\_PDEV\_STREAM\_KEY\_REFRESH
- If the device transaction was triggered by one of the following RMI commands then the device transaction is associated with the VDEV.
- -RMI\_VDEV\_P2P\_BIND
- -RMI\_VDEV\_GET\_INTERFACE\_REPORT
- -RMI\_VDEV\_GET\_MEASUREMENTS
- -RMI\_VDEV\_LOCK
- -RMI\_VDEV\_START
- -RMI\_VDEV\_UNLOCK


- A Realm is expected to request the Host to initiate device transactions (for both state changes and for requesting measurements and interface report) via an RSI\_HOST\_CALL interface. For details, refer to Realm Host Interface specification [20].
- A PDEV is associated with at most one device transaction at a time.
- A VDEV is associated with at most one device transaction at a time.
- The states of a Device communication are listed below.

| State            | Description                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEV_COMM_IDLE    | The RMMis not communicating with the device.                                                                                                                                                                                                                |
| DEV_COMM_PENDING | The RMMhas a device request which is ready to be sent to the device.                                                                                                                                                                                        |
| DEV_COMM_ACTIVE  | The RMMhas initiated a device transaction. One or more device requests associated with this device transaction have been sent from the RMMto the device. The RMMhas not received all the expected device responses associated with this device transaction. |





## See also:

- Secured Messages using SPDM Specification version 1.1.0 [17]
- B4.6.20 RmiDevCommExitFlags type

While the device communication state of a PDEV is either DEV\_COMM\_PENDING or DEV\_COMM\_ACTIVE, the Host can either:

- Transfer device requests and device responses by executing RMI\_PDEV\_COMMUNICATE.

DEV\_COMM\_ERROR

The RMM encountered an error during communication with the device.

Device communication state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

Figure A9.12: Device communication state transitions

<!-- image -->


- Abort the device transaction by executing RMI\_PDEV\_ABORT.

While the device communication state of a VDEV is either DEV\_COMM\_PENDING or DEV\_COMM\_ACTIVE, the Host can either:

- Transfer device requests and device responses by executing RMI\_VDEV\_COMMUNICATE.
- Abort the device transaction by executing RMI\_VDEV\_ABORT.

If a physical device is temporarily unable to service a request for an IMPLEMENTATION DEFINED reason then RMI\_PDEV\_COMMUNICATE or RMI\_VDEV\_COMMUNICATE may return RMI\_BUSY.

When the Host receives RMI\_BUSY from RMI\_VDEV\_COMMUNICATE, it can choose to either:

- Propagate the busy status to the requesting Realm via RHI.
- Hold onto the Realm's request, and retry the RMI command later. While holding on to the request, the Host should indicate via RHI that the request is incomplete.

## See also:

- Realm Host Interface specification [20]
- B4.5.26 RMI\_PDEV\_COMMUNICATE command
- B4.5.80 RMI\_VDEV\_COMMUNICATE command

## A9.5.2 Device communication data structures

## A9.5.2.1 Device communication exit data structure

An RmiDevCommExit object is a data structure which is passed from the RMM to the Host during a device transaction.

The attributes of an RmiDevCommExit object tell the Host the following:

- Whether there is data in the device response buffer which the Host is requested to cache. This is indicated by the RmiDevCommExitFlags::rsp\_cache flag.
- Whether there is data in the device request buffer which the Host is requested to cache. This is indicated by the RmiDevCommExitFlags::req\_cache flag.
- Whether the device request buffer contains a device request which the Host is requested to send to the device. This is indicated by the RmiDevCommExitFlags::req\_send flag.
- Whether the Host is requested to delay sending a device request. This is indicated by the RmiDevCommExit::req\_delay value.
- Whether the RMM is waiting for a response from the device. This is indicated by the RmiDevCommExitFlags::rsp\_wait flag.
- The maximum time which the Host should wait for a response from the device. This is indicated by the RmiDevCommExit::req\_timeout value. The time to wait is measured from the most recent object which had the RmiDevCommExitFlags::rsp\_reset flag set to true.
- Whether the device transaction contains more than one (device request, device response) tuple. This is indicated by the RmiDevCommExitFlags::multi flag.
- Whether the device transaction is waiting for a transaction on another device, to which this device is connected via a PDEV stream, to proceed. This is indicated by the RmiDevCommExitFlags::stream\_wait flag.

Device communication is complete means that none of the following flags are set:

- RmiDevCommExitFlags::req\_send
- RmiDevCommExitFlags::req\_cache
- RmiDevCommExitFlags::rsp\_cache
- RmiDevCommExitFlags::rsp\_reset
- RmiDevCommExitFlags::rsp\_wait
- RmiDevCommExitFlags::stream\_wait
- RmiDevCommExitFlags::req\_send and RmiDevCommExitFlags::rsp\_wait are never set together.


RmiDevCommExitFlags::multi is only set when RmiDevCommExitFlags::req\_send is set.


A device which uses SPDM communication is permitted to respond with ResponseNotReady and a token and timeout value (RDTExponent and RDTM). In this case, the RMM is expected to do the following:

- Construct a RespondIfReady request
- Set RmiDevCommExitFlags::req\_delay according to the RDTExponent and RDTM values

As a result, the Host is expected to wait for the specified amount of time, before it sends the RespondIfReady request to the device.

When initiating a new SPDM request, the RMM is expected to set the RmiDevCommExitFlags::rsp\_reset flag. On subsequent RMI\_xDEV\_COMMUNICATE calls while the SPDM request is still outstanding, the RMM is expected to clear the RmiDevCommExitFlags::rsp\_reset flag.

As a result, the Host is expected to measure the time taken by the SPDM request from the first call in the sequence, when the RmiDevCommExitFlags::rsp\_reset flag was set.

- During communication between the RMM and a device which uses SPDM:
- RmiDevCommExitFlags::req\_send indicates that the Host is requested to send a device request to the device.
- RmiDevCommExitFlags::rsp\_wait indicates that the Host is requested to return a device response to the RMM.



## Chapter A9. Realm device assignment

| I SCJZM   | During communication between the RMMand a device which does not use SPDM:                                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XFBZH   | On return from RMI_PDEV_COMMUNICATE or RMI_VDEV_COMMUNICATE, RmiDevCommExit::req_len is guaranteed to be not greater than the RMI Granule size.                                          |
| R MKMQJ   | On return from RMI_PDEV_COMMUNICATE or RMI_VDEV_COMMUNICATE, RmiDevCommExit::req_cache_offset + RmiDevCommExit::req_cache_len is guaranteed to be not greater than the RMI Granule size. |
| R HCNNN   | On return from RMI_PDEV_COMMUNICATE or RMI_VDEV_COMMUNICATE, RmiDevCommExit::rsp_cache_offset + RmiDevCommExit::rsp_cache_len is guaranteed to be not greater than the RMI Granule size. |
| D VYFKM   | The attributes of an RmiDevCommExit object are summarized in the following table.                                                                                                        |

| Name             | Byte offset   | Type                | Description                                                                                                                       |
|------------------|---------------|---------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| flags            | 0x0           | RmiDevCommExitFlags | Flags indicating action(s) which the Host is requested to perform                                                                 |
| req_cache_offset | 0x8           | UInt64              | If flags.req_cache is true, offset in the device request buffer to the start of data to be cached, in bytes                       |
| req_cache_len    | 0x10          | UInt64              | If flags.req_cache is true, amount of device request data to be cached, in bytes                                                  |
| rsp_cache_offset | 0x18           UInt64        | If flags.rsp_cache is true, offset in the device response buffer to the start of data to be cached, in bytes                      |
| rsp_cache_len    | 0x20          | UInt64              | If flags.rsp_cache is true, amount of device response data to be cached, in bytes                                                 |
| cache_object_id  | 0x28          | RmiDevCommObject    | If flags.req_cache is true and / or flags.rsp_cache is true, identifier for the object to be cached                               |
| protocol         | 0x30          | RmiDevCommProtocol  | If flags.req_send is true, protocol to use                                                                                        |
| req_delay        | 0x38          | UInt64              | If flags.req_send is true, amount of time to wait before sending the request, in microseconds.                                    |
| req_len          | 0x40          | UInt64              | If flags.req_send is true, amount of valid data in request buffer in bytes                                                        |
| rsp_timeout      | 0x48          | UInt64              | Amount of time to wait (measured from the most recent exit which had flags.rsp_reset = true) for device response in microseconds. |

## See also:

- A9.3 Physical device stream object
- B4.5.26 RMI\_PDEV\_COMMUNICATE command
- B4.5.80 RMI\_VDEV\_COMMUNICATE command
- B4.6.19 RmiDevCommExit type

## · B4.6.20 RmiDevCommExitFlags type

## A9.5.2.2 Device communication enter data structure

An RmiDevCommEnter object is a data structure which is passed from the Host to the RMM during a device transaction.


<!-- image -->

<!-- image -->

The attributes of an RmiDevCommEnter object tell the RMM the following:

- Whether the device reported an error.
- Whether the device response buffer contains a device response.
- The location of the device request buffer, into which the RMM can write a device request.

If RmiDevCommEnter::rsp\_len is greater than the RMI Granule size then RMI\_PDEV\_COMMUNICATE or RMI\_VDEV\_COMMUNICATE returns RMI\_ERROR\_INPUT.

The attributes of an RmiDevCommEnter object are summarized in the following table.

| Name     | Byte offset   | Type             | Description                                      |
|----------|---------------|------------------|--------------------------------------------------|
| status   | 0x0           | RmiDevCommStatus | Status of device transaction                     |
| req_addr | 0x8           | Address          | Address of request buffer                        |
| rsp_addr | 0x10          | Address          | Address of response buffer                       |
| rsp_len  | 0x18          | UInt64           | Amount of valid data in response buffer in bytes |

## See also:

- B4.5.26 RMI\_PDEV\_COMMUNICATE command
- B4.5.80 RMI\_VDEV\_COMMUNICATE command
- B4.6.18 RmiDevCommEnter type

## A9.5.3 Host-side device communication flow


- The RMI\_PDEV\_COMMUNICATE command is used to send a PDEV-associated device request from the RMM to a device, and / or to return a device response from the device to the RMM.
- The RMI\_VDEV\_COMMUNICATE command is used to send a VDEV-associated device request from the RMM to a device, and / or to return a device response from the device to the RMM.
- The RMI\_PDEV\_COMMUNICATE and RMI\_VDEV\_COMMUNICATE commands have identical programming models. Hereafter, they are referred to collectively as 'device communication commands'.

For a given physical device, at most one device transaction can be active.

- The RMI\_PDEV\_ABORTcommandor RMI\_VDEV\_ABORTcommandisused to abort an DEV\_COMM\_ACTIVE device transaction.
- At the responder side (that is, at the device), device transactions associated with a PDEV and device transactions associated with its child VDEVs all terminate at the same physical device.

## A9.5.3.1 Communication flow for devices which use SPDM

- The overall flow for communication between the RMM and a device which uses SPDM is as follows:
1. The Host executes an RMI command which causes a device transaction, associated with a specified PDEV or VDEV, to become pending.

The output values of the command include an indication of whether the pending transaction will contain more than one (device request, device response) tuple.

2. The Host calls the appropriate device communication command.

Input values to the command include a device request buffer , which is a pointer to a Granule of NS memory.

3. The RMM writes a device request to the device request buffer and returns to the Host, indicating that data is ready to be sent to the device.
4. The Host sends the device request to the device.

Details of how this is performed are out of scope of this specification. For a PCIe device, this could be done by copying from the device request buffer to a Data Object Exchange (DOE) mailbox.

The device communication state becomes DEV\_COMM\_ACTIVE.

5. The device indicates to the Host that it has responded to the request.

The Host copies the device response to a device response buffer in NS memory. As with sending the request, details of how this is performed are out of scope of this specification.

6. The Host calls the device communication command, providing a pointer to the device response buffer.
7. The return value indicates that either:
- The RMM has another device request to send within the same device transaction (in which case the flow returns to step 2), or
- The device transaction is complete.
8. If the device transaction is incomplete, the Host checks the device state to determine whether an error has occurred.
6. IRSPTF When multiple device transactions destined for the same physical device are DEV\_COMM\_PENDING, the Host is free to choose which of them to transition to DEV\_COMM\_ACTIVE.
7. IQDBZK When a device transaction is DEV\_COMM\_ACTIVE, the Host must not send to that physical device a device request associated with any other device transaction.
8. UBMMVH The SPDM session which is established between the RMM and a device has the following characteristics:
- SPDM heartbeat is not supported
- SPDM key update is not supported
11. UKPPFB In order for its functions to be assignable to Realms, a device must provide the following functionality:


- SPDM version required by PCIe TDISP and IDE\_KM specifications.
- Identity and authentication including key exchange.
- The following sequence illustrates communication with a device which uses SPDM, taking RMI\_VDEV\_LOCK as the example which initiates the communication.

Figure A9.13: Communication with a device which uses SPDM

<!-- image -->

The implementation should set the SPDM DataTransferSize to a value which allows the largest possible secure SPDM payload to fit within an RMI Granule.

See also:

- PCI Express 6.0 specification [16]
- B4.5.26 RMI\_PDEV\_COMMUNICATE command
- B4.5.80 RMI\_VDEV\_COMMUNICATE command

## A9.5.3.2 Communication flow for devices which do not use SPDM

The overall flow for communication between the RMM and a device which does not use SPDM is as follows:

1. The Host executes an RMI command which causes a device transaction, associated with a specified PDEV or VDEV, to become pending.

The output values of the command include an indication of whether the pending transaction will contain more than one (device request, device response) tuple.

2. The Host calls the appropriate device communication command repeatedly, until either:
- The return value indicates that the device transaction is complete.
- The device enters an error state.
4. ILFRNJ When the RMM sends a device request via an IMPLEMENTATION DEFINED channel, the 'req\_send' flag is clear and the 'req\_wait' flag is set in the DevCommExitFlags fieldset. This informs the Host that it should either:
- Register for an IMPLEMENTATION DEFINED notification that the request has been completed, and call RMI\_PDEV\_COMMUNICATE or RMI\_VDEV\_COMMUNICATE when this notification is received, or
- Poll for request completion by periodically calling RMI\_PDEV\_COMMUNICATE or RMI\_VDEV\_COMMUNICATE.
7. INLBWX The following sequence illustrates communication with a device which does not use SPDM, taking RMI\_VDEV\_LOCK as the example which initiates the communication.

<!-- image -->

Figure A9.14: Communication with a device which does not use SPDM

<!-- image -->

For details of communication with the device via the platform, refer to Firmware Interfaces for RME (FIRME) specification [19].

## A9.5.4 Host caching of device attestation evidence

- On execution of a device communication command, the RMM can indicate to the Host that the Host should cache data from the request buffer and / or response buffer, for later retrieval by the Realm.
- If RmiDevCommExitFlags::req\_cache is set then the Host should cache data from the request buffer, with the extent identified by the RmiDevCommExit::req\_cache\_offset and RmiDevCommExit::req\_cache\_len fields.
- If RmiDevCommExitFlags::rsp\_cache is set then the Host should cache data from the response buffer, with the extent identified by the RmiDevCommExit::rsp\_cache\_offset and RmiDevCommExit::rsp\_cache\_len fields.
- The identity of the data which the Host is requested to cache is identified by the RmiDevCommExit::cache\_object\_id field.
- If the device transaction was triggered while the PDEV state was PDEV\_NEW then the RMM may indicate that the Host should cache the following objects:
- Anegotiation data object, indicated by RmiDevCommExit::cache\_object\_id == RMI\_DEV\_NEGOTIATION\_DATA.
- A device identity evidence, indicated by RmiDevCommExit::cache\_object\_id == RMI\_DEV\_IDENTITY.
- Device measurement data, indicated by RmiDevCommExit::cache\_object\_id == RMI\_DEV\_MEASUREMENTS.
- If the device transaction was triggered by RMI\_VDEV\_GET\_MEASUREMENTS then the RMM may indicate that the Host should cache device measurement data, indicated by RmiDevCommExit::cache\_object\_id == RMI\_DEV\_MEASUREMENTS.

For a device which uses SPDM communication, this data consists of the SPDM GET\_MEASUREMENTS request and the corresponding MEASUREMENTS response message, stored in the same sequence used to construct the SPDM measurement transcript. Note that this data does not include the VCA exchange. For a device which uses platform communication, the format of this data is IMPLEMENTATION DEFINED. ITYCWV If the device transaction was triggered by RMI\_VDEV\_GET\_INTERFACE\_REPORT then the RMM may indicate that the Host should cache a device interface report, indicated by RmiDevCommExit::cache\_object\_id == RMI\_DEV\_INTERFACE\_REPORT. See also: · A9.6.1 Realm retrieval of device attestation evidence · B4.5.27 RMI\_PDEV\_CREATE command · B4.5.84 RMI\_VDEV\_GET\_INTERFACE\_REPORT command · B4.5.85 RMI\_VDEV\_GET\_MEASUREMENTS command

- B4.6.19 RmiDevCommExit type

## A9.5.5 Device measurement retrieval

## A9.5.5.1 Device measurement retrieval overview

- Device measurement retrieval is initiated by execution of RMI\_VDEV\_GET\_MEASUREMENTS.
- Following initiation of device measurement retrieval, the Host is expected to call RMI\_VDEV\_COMMUNICATE in order to exchange device requests and device responses with the RMM.
- During all variants of the device measurement retrieval flow, on return from RMI\_VDEV\_COMMUNICATE the RMMmay request the Host to cache measurement data, for later retrieval by the Realm via RHI.

During a device measurement retrieval flow, the Host is expected to concatenate this data into a single 'cached measurement buffer'.

The RMM stores a digest of the measurement data which it requests the Host to cache, which the Realm can request via RSI\_VDEV\_GET\_INFO.

- Device measurement retrieval is permitted regardless of the state of the VDEV. The Realm can use the RsiVdevInfo::lock\_nonce and RsiVdevInfo::meas\_nonce fields to check measurement freshness.

See also:

- A9.5.3 Host-side device communication flow
- B4.5.80 RMI\_VDEV\_COMMUNICATE command
- B4.5.85 RMI\_VDEV\_GET\_MEASUREMENTS command
- B5.4.19 RSI\_VDEV\_GET\_INFO command

## A9.5.5.2 Retrieval of device measurements from a device which uses SPDM

During retrieval of device measurements from a device which uses SPDM, the data which the RMM requests the Host to cache is the SPDM measurement request and response messages.

During retrieval of device measurements from a device which uses SPDM, if the device supports signed measurements then the SPDM\_MEASUREMENTS response includes a device-generated signature over the SPDM measurement transcript, as specified in the SPDM specification; see Security Protocol and Data Model (SPDM) [21].

The following sequence illustrates retrieval of device measurements from a device which uses SPDM.

<!-- image -->

Chapter A9.

Realm device assignment

A9.5.

Communication between RMM and a device

<!-- image -->

Figure A9.15: Retrieval of measurements from a device which uses SPDM

Copyright © 2022-2026 Arm Limited or its affiliates. All rights reserved.


## A9.5.5.3 Retrieval of device measurements from a device which does not use SPDM

For a device which does not use SPDM, the flags returned from RMI\_VDEV\_COMMUNICATE have 'rsp\_wait' set and 'req\_send' clear. This indicates that the Host should either poll for completion of the request by calling RMI\_VDEV\_COMMUNICATE, or that the Host will receive an IMPLEMENTATION DEFINED notification when the request has been completed.

Validate measurement buffer received from Host against measurement digest received from RMM

<!-- image -->

## See also:

- A9.5.3 Host-side device communication flow