## A9.10 Peer-to-peer device communication

- D0018 Peer-to-peer (P2P) device communication is access from a source device to a memory location within a destination device.

## A9.10.1 Host-routed P2P communication

- D0019 Host-routed P2P communication is a transaction which consists of the following steps:
1. The source device issues an AT request over its default IDE stream to the Root Port.
2. The AT request is handled by the SMMU, which returns the destination physical address to the source device.
3. The source device issues a request over its default IDE stream, using the translated destination physical address.
4. The request reaches the Root Port and is redirected to the destination device over the destination device's default IDE stream.
5. The destination device issues a response over its default IDE stream.
6. The response reaches the Root Complex and is redirected to the source device over the source device's default IDE stream.

I0020 The following diagram illustrates Host-routed P2P communication.


Figure A9.21: Host-routed P2P communication

<!-- image -->

Beyond the Realm attesting and accepting each of the VDEVs, no action is required by either the Realm or the RMMin order to enable Host-routed P2P between two VDEVs.

See also:

- PCI Express 6.0 specification [16]

## A9.10.2 Direct P2P communication

- D0022 Direct P2P communication
- is a transaction which consists of the following steps:
1. The source device issues an AT request over its default IDE stream to the Root Port.
2. The AT request is handled by the SMMU, which returns the destination physical address to the source device.

I0021

I0023

D0025

3. The source device issues a request over a P2P IDE stream between itself and the destination device, using the translated destination physical address.
4. The destination device issues a response over the same P2P IDE stream via which the request was received.

The following diagram illustrates Direct P2P communication.

Figure A9.22: Direct P2P communication

<!-- image -->


## See also:

- PCI Express 6.0 specification [16]

## A9.10.2.1 Direct P2P communication overview

R0024 Direct P2P communication between a two VDEVs is permitted if all of the following are true:

- Both VDEVs are assigned to the same Realm.
- Each VDEV belongs to a different PDEV.
- A P2P IDE stream exists between the two PDEVs.
- A P2P binding exists between the two VDEVs.

## A9.10.2.1.1 P2P IDE stream

A P2P IDE stream is an IDE stream between two PDEVs.

R0026 A P2P IDE stream is enabled if selective stream association registers are configured at each end to include all memory locations (coherent and non-coherent) of the peer device, as follows:

- IDE selective stream assocation registers at physical device A are programmed as follows:
- -RID range includes the RID of physical device B
- -Address range includes all memory locations of physical device B
- IDE selective stream assocation registers at physical device B are programmed as follows:
- -RID range includes the RID of physical device A
- -Address range includes all memory locations of physical device A

I0027

A PDEV can participate in multiple P2P IDE streams.

R0028

Between a given pair of PDEVs, there can exist at most one P2P IDE stream.

- I0029 Creation of a P2P IDE stream is peformed by the RMM in response to requests from the Host. This does not require consent to be provided by the Realm.

- I0030 Destruction of a P2P IDE stream is peformed by the RMM in response to requests from the Host. This does not require consent to be provided by the Realm.

## A9.10.2.1.2 P2P binding

- D0031 A P2P binding is an association between a VDEV and a P2P IDE stream. Existence of a P2P binding means that the VDEV accepts incoming P2P requests over the P2P IDE stream.
- I0032 Creation of a P2P binding is peformed by the RMM in response to requests from the Host. It is conditional on consent having been provided by the Realm to which the VDEVs are assigned.
- I0033 Destruction of a P2P binding is peformed by the RMM in response to requests from the Host. This does not require consent to be provided by the Realm.
- R0034 A VDEV can participate in at most one P2P binding.

## A9.10.2.2 Setup of Direct P2P communication

- I0035 The flow for establishment of Direct P2P communication between two VDEVs is as follows:
1. P2P IDE stream programming
- The Host programs IDE selective stream assocation registers at each physical device.
2. P2P IDE stream validation and enablement
- · The Host requests the RMM to enable the IDE stream, by executing RMI\_PDEV\_STREAM\_CONNECT with a stream type of NCOH\_P2P. The input values of this command include the ID of the IDE stream configured in the previous step. · The RMM checks that the address ranges for the IDE stream fall within the appropriate regions of the system address map. · The RMM checks that the address range programmed in IDE stream for PDEV1 covers the address range of PDEV2 and vice versa. · The RMM checks that the RID range programmed in IDE stream for PDEV1 covers the RID range of PDEV2 and vice versa. · A device transaction is initiated for each of the two PDEVs. · IDE key programming and stream enablement at each physical device are driven by Host execution of RMI\_PDEV\_COMMUNICATE for each PDEV.
3. P2P TDI binding
- The Realm requests the RMM to create a P2P binding between two VDEVs, by executing RSI\_VDEV\_P2P\_BIND. The input values of this command include attestation information for each VDEV.
- This causes a REC exit due to device P2P binding, which identifies the two VDEVs.
- The Host requests the RMM to bind the VDEVs to a given P2P IDE stream, by executing RMI\_VDEV\_P2P\_BIND.
- The RMM checks that the Host's request matches that previously issued by the Realm.
- The RMM checks that the attestation information of each VDEV matches that provide by the Realm.
- Both VDEVs move into VDEV\_COMMUNICATING state.
- Issuance of TDISP commands to create the P2P binding is driven by Host execution of RMI\_VDEV\_COMMUNICATE.
- I0036 At PDEV creation, a 'P2P enabled' flag indicates whether the PDEV can be added to a P2P IDE stream.
- I0037 RSI\_VDEV\_GET\_INFO reports to the Realm whether the device to which the VDEV belongs can participate in a P2P IDE stream.
- I0038 RSI\_VDEV\_GET\_INFO reports to the Realm whether the VDEV is participating in a P2P binding, and if so it identifies the peer VDEV.

## Chapter A9.

## Realm device assignment

## A9.10. Peer-to-peer device communication

Figure A9.23: Creation of a P2P IDE stream

<!-- image -->

Chapter A9. Realm device assignment

I0040 The following sequence diagram shows the flow for creation of a P2P binding. In this diagram, attest\_info is shorthand for the tuple (lock\_nonce, meas\_nonce, report\_nonce) .


Chapter A9. Realm device assignment A9.10. Peer-to-peer device communication

<!-- image -->

Figure A9.24: Creation of a P2P binding

See also:

- A2.3.2 Views of physical memory
- A4.3.14 REC exit due to VDEV P2P binding
- A9.3 Physical device stream object
- A9.5 Communication between RMM and a device
- B4.5.26 RMI\_PDEV\_COMMUNICATE command
- B4.5.34 RMI\_PDEV\_STREAM\_CONNECT command
- B4.5.88 RMI\_VDEV\_P2P\_BIND command
- B5.4.19 RSI\_VDEV\_GET\_INFO command
- B5.4.20 RSI\_VDEV\_P2P\_BIND command

## A9.10.2.3 Teardown of Direct P2P communication

- I0041 Destruction of a P2P binding is initiated by execution of RMI\_VDEV\_P2P\_UNBIND. This causes both VDEVs to move into VDEV\_COMMUNICATING state. Issuance of TDISP commands to remove the P2P binding is driven by Host execution of RMI\_VDEV\_COMMUNICATE.
- I0042 On transition of a VDEV to any state other than VDEV\_LOCKED or VDEV\_STARTED, any P2P binding associated with that VDEV is destroyed.

See also:

- A9.5 Communication between RMM and a device
- B4.5.89 RMI\_VDEV\_P2P\_UNBIND command

