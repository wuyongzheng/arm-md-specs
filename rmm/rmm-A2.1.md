## A2.1 Realm

This section describes the concept of a Realm.

## A2.1.1 Overview

- A Realm is an execution environment which is protected from agents in the Non-secure and Secure Security states, and from other Realms.

## A2.1.2 Realm execution environment

- The execution environment of a Realm is an EL0 + EL1 environment, as described in Arm Architecture Reference Manual for A-Profile architecture [3].

## A2.1.2.1 Realm registers

- On first entry to a Realm VPE, PE state is initialized according to 'PE state on reset to AArch64 state' in Arm Architecture Reference Manual for A-Profile architecture [3], except for GPR and PC values which are specified by the Host during Realm creation.
- Confidentiality is guaranteed for a Realm VPE's general purpose and SIMD / floating point registers.
- Confidentiality is guaranteed for other Realm VPE register state (including stack pointer, program counter and EL0 / EL1 system registers).
- Integrity is guaranteed for a Realm VPE's general purpose and SIMD / floating point registers.
- Integrity is guaranteed for other Realm VPE register state (including stack pointer, program counter and EL0 / EL1 system registers).
- A Realm can use a Host call to pass arguments to the Host and receive results from the Host.

See also:

- A2.3 Realm Execution Context
- A4.5 Host call
- B4.3.9 RMI\_REALM\_CREATE command

## A2.1.2.2 Realm memory

- A Realm is able to determine whether a given IPA is protected or unprotected .
- Confidentiality is guaranteed for memory contents accessed via a protected address. Informally, this means that a change to the contents of such a memory location is not observable by any agent outside the CCA platform .
- Integrity is guaranteed for memory contents accessed via a protected address. Informally, this means that the Realm does not observe the contents of the location to change unless the Realm itself has either written a different value to the location, or provided consent to the RMM for integrity of the location to be violated.

See also:

- A5.2.1 Realm IPA space

## A2.1.2.3 Realm processor features

- The value returned to a Realm from reading a feature register is architecturally valid and describes the set of features which are present in the Realm's execution environment.
- The RMM may suppress a feature which is supported by the underlying hardware platform, if exposing that feature to a Realm could lead to a security vulnerability.

See also:

- A3.1 Realm feature discovery and selection

## A2.1.2.4 IMPDEF system registers

- A Realm read from or write to an IMPLEMENTATION DEFINED system register causes an Unknown exception taken to the Realm.

## A2.1.3 Realm attributes

This section describes the attributes of a Realm.

- A Realm attribute is a property of a Realm whose value can be observed or modified either by the Host or by the Realm.
- An example of a way in which a Realm attribute may be observable is the outcome of an RMM command.
- The attributes of a Realm are summarized in the following table.

| Name            | Type                   | Description                                         |
|-----------------|------------------------|-----------------------------------------------------|
| feat_lpa2       | RmmFeature             | Whether LPA2 is enabled for this Realm              |
| ipa_width       | UInt8                  | IPA width in bits                                   |
| measurements    | RmmRealmMeasurement[5] | Realm measurements                                  |
| hash_algo       | RmmHashAlgorithm       | Algorithm used to compute Realm measurements        |
| rec_index       | UInt64                 | Index of next REC to be created                     |
| rtt_base        | Address                | Realm Translation Table base address                |
| rtt_level_start | Int64                  | RTT starting level                                  |
| rtt_num_start   | UInt64                 | Number of physically contiguous starting level RTTs |
| state           | RmmRealmState          | Lifecycle state                                     |
| vmid            | Bits16                 | Virtual Machine Identifier                          |
| rpv             | Bits512                | Realm Personalization Value                         |
| num_recs        | UInt64                 | Number of RECs owned by this Realm                  |

| D MGGPT   | A Realm Initial Measurement (RIM) is a measurement of the configuration and contents of a Realm at the time of activation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D GRFCS   | A Realm Extensible Measurement (REM) is a measurement value which can be extended during the lifetime of a Realm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| I FMPYL   | Attributes of a Realm include an array of measurement values. The first entry in this array is a RIM. The remaining entries in this array are REMs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| X DNDKV   | During Realm creation, the Host provides ipa_width, rtt_level_start and rtt_num_start values as Realm parameters. According to the VMSA, the rtt_num_start value is architecturally defined as a function of the ipa_width and rtt_level_start values. It would therefore have been possible to design the Realm creation interface such that the Host provided only the ipa_width and rtt_level_start values. However, this would potentially allow a Realm to be successfully created, but with a configuration which did not match the Host's intent. For this reason, it was decided that the Host should specify all three values explicitly, and that Realm creation should fail if the values are not consistent. See Arm Architecture Reference Manual for A-Profile architecture [3] for further details. |
| I QRVTT   | The VMID of a Realm is chosen by the Host. The VMID must be within the range supported by the hardware platform. The RMMensures that every Realm on the system has a unique VMID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| D FTWBK   | A Realm Personalization Value (RPV) is a provided by the Host, to distinguish between Realms which have the same Realm Initial Measurement, but different behavior.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

Possible uses of the RPV include:

- A GUID
- Hash of Realm Owner public key
- Hash of a 'personalisation document' which is provided to the Realm via a side-band (for example, via NS memory) and contains configuration information used by Realm software.
- The RMM treats the RPV as an opaque value.
- The RPV is included in the Realm attestation report as a separate claim.
- The RPV is included in the output of the RSI\_REALM\_CONFIG command.

See also:

- A2.1.5 Realm lifecycle
- A2.3 Realm Execution Context
- A3.1.2 Realm LPA2 and IPA width
- A5.2.1 Realm IPA space
- A5.5 Realm Translation Table
- A7.1 Realm measurements
- A7.2.3.1.3 Realm Personalization Value claim
- B5.3.3 RSI\_FEATURES command
- B5.3.9 RSI\_REALM\_CONFIG command
- C1.16 RmmRealm type

## A2.1.4 Realm liveness

- Realm liveness is a property which means that there exists one or more Granules, other than the RD and the starting level RTTs, which are owned by the Realm.
- If a Realm is live, it cannot be destroyed.
- A Realm is live if any of the following is true:
- The number of RECs owned by the Realm is not zero
- A starting level RTT of the Realm is live
- If a Realm owns a non-zero number of Data Granules, this implies that it has a starting level RTT which is live, and therefore that the Realm itself is live.

See also:

- A2.1.5 Realm lifecycle
- A2.2.2 Granule ownership
- A2.2.3 Granule lifecycle
- A2.3 Realm Execution Context
- A5.5.8 RTTE liveness and RTT liveness
- B3.32 RealmIsLive function
- B4.3.10 RMI\_REALM\_DESTROY command

## A2.1.5 Realm lifecycle

See also:

- Chapter A3 Realm creation
- D1.2 Realm lifecycle flows

## A2.1.5.1 States

The states of a Realm are listed below.

<!-- image -->


<!-- image -->

## See also:

- B6.3.6 PSCI\_SYSTEM\_OFF command
- B6.3.7 PSCI\_SYSTEM\_RESET command
- B4.3.8 RMI\_REALM\_ACTIVATE command

| State            | Description                                             |
|------------------|---------------------------------------------------------|
| REALM_NEW        | Under construction. Not eligible for execution.         |
| REALM_ACTIVE     | Eligible for execution.                                 |
| REALM_SYSTEM_OFF | System has been turned off. Not eligible for execution. |

## A2.1.5.2 State transitions

Permitted Realm state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a Realm object. A transition to the pseudo-state NULL represents destruction of a Realm object.

| From state       | To state         | Events                            |
|------------------|------------------|-----------------------------------|
| NULL             | REALM_NEW        | RMI_REALM_CREATE                  |
| REALM_NEW        | NULL             | RMI_REALM_DESTROY                 |
| REALM_ACTIVE     | NULL             | RMI_REALM_DESTROY                 |
| REALM_SYSTEM_OFF | NULL             | RMI_REALM_DESTROY                 |
| REALM_NEW        | REALM_ACTIVE     | RMI_REALM_ACTIVATE                |
| REALM_ACTIVE     | REALM_SYSTEM_OFF | PSCI_SYSTEM_OFF PSCI_SYSTEM_RESET |

Permitted Realm state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of an RD. A transition to the pseudo-state NULL represents destruction of an RD.

Figure A2.1: Realm state transitions

<!-- image -->

- B4.3.9 RMI\_REALM\_CREATE command
- B4.3.10 RMI\_REALM\_DESTROY command

## A2.1.6 Realm parameters


A Realm parameter is a value which is provided by the Host during Realm creation.

See also:

- A2.1.3 Realm attributes
- A3.1 Realm feature discovery and selection
- B3.33 RealmParams function
- B4.3.9 RMI\_REALM\_CREATE command
- B4.4.12 RmiRealmParams type

## A2.1.7 Realm Descriptor

- A Realm Descriptor (RD) is an RMM data structure which stores attributes of a Realm.
- The size of an RD is one Granule.

See also:

- A2.1.3 Realm attributes
- A2.2.3 Granule lifecycle