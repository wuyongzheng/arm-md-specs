## A2.2 Realm

This section describes the concept of a Realm.

## A2.2.1 Overview

- DDLRSR A Realm is an execution environment which is protected from agents in the Non-secure and Secure Security states, and from other Realms.

## A2.2.2 Realm execution environment

- ILQYLY The execution environment of a Realm is an EL0 + EL1 environment, as described in Arm Architecture Reference Manual for A-Profile architecture [3].

## A2.2.2.1 Realm registers

- RNJHQK On first entry to a Realm VPE, PE state is initialized according to 'PE state on reset to AArch64 state' in Arm Architecture Reference Manual for A-Profile architecture [3], except for GPR and PC values which are specified by the Host during Realm creation.
- GZFCQX Confidentiality is guaranteed for a Realm VPE's general purpose and SIMD / floating point registers.
- GQHZCS Confidentiality is guaranteed for other Realm VPE register state (including stack pointer, program counter and EL0 / EL1 system registers).
- GXRMHP Integrity is guaranteed for a Realm VPE's general purpose and SIMD / floating point registers.
- GYKRWG Integrity is guaranteed for other Realm VPE register state (including stack pointer, program counter and EL0 / EL1 system registers).
- IGPGFB A Realm can use a Host call to pass arguments to the Host and receive results from the Host.

See also:

- A2.4 Realm Execution Context
- A4.5 Host call
- B4.5.46 RMI\_REALM\_CREATE command

## A2.2.2.2 Realm memory

DRAFT

- ITQMMZ A Realm is able to determine whether a given IPA is protected or unprotected .
- GLQFQH Confidentiality is guaranteed for memory contents accessed via a protected address. Informally, this means that a change to the contents of such a memory location is not observable by any agent outside the CCA platform .
- GQMLCJ Integrity is guaranteed for memory contents accessed via a protected address. Informally, this means that the Realm does not observe the contents of the location to change unless the Realm itself has either written a different value to the location, or provided consent to the RMM for integrity of the location to be violated.

See also:

- A5.2.1 Realm IPA space

## A2.2.2.3 Realm processor features

- RJGHYJ The value returned to a Realm from reading a feature register is architecturally valid and describes the set of features which are present in the Realm's execution environment.
- IKKBDP The RMM may suppress a feature which is supported by the underlying hardware platform, if exposing that feature to a Realm could lead to a security vulnerability.

See also:

- Chapter A3 Feature discovery and configuration

## A2.2.2.4 IMPDEF system registers

- RFQCKH A Realm read from or write to an IMPLEMENTATION DEFINED system register causes an Unknown exception taken to the Realm.

## A2.2.3 Realm attributes

This section describes the attributes of a Realm.

- DJSGFY A Realm attribute is a property of a Realm whose value can be observed or modified either by the Host or by the Realm.
- ITTDVX An example of a way in which a Realm attribute may be observable is the outcome of an RMM command.
- DMHJCK The attributes of a Realm are summarized in the following table.

| Name               | Type                   | Description                                                                                                                                                                                                               |
|--------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| feat_lpa2          | RmmFeature             | Whether LPA2 is enabled for this Realm                                                                                                                                                                                    |
| ipa_width          | UInt8                  | IPA width in bits                                                                                                                                                                                                         |
| rim                | RmmRealmMeasurement    | Realm Initial Measurement                                                                                                                                                                                                 |
| rem                | RmmRealmMeasurement[4] | Realm Extensible Measurement                                                                                                                                                                                              |
| hash_algo          | RmmHashAlgorithm       | Algorithm used to compute Realm measurements                                                                                                                                                                              |
| rec_index          | UInt64                 | Index of next REC to be created                                                                                                                                                                                           |
| rtt_base           | Address[4]             | DRAFT Realm Translation Table base addresses If rtt_tree_per_plane is FEATURE_FALSE then only the first entry is valid. If rtt_tree_per_plane is FEATURE_TRUE then only the first (num_aux_planes + 1) entries are valid. |
| rtt_level_start    | Int64                  | RTT starting level                                                                                                                                                                                                        |
| rtt_num_start      | UInt64                 | Number of physically contiguous starting level RTTs                                                                                                                                                                       |
| state              | RmmRealmState          | Lifecycle state                                                                                                                                                                                                           |
| rpv                | Bits512                | Realm Personalization Value                                                                                                                                                                                               |
| feat_da            | RmmFeature             | Whether Realm device assignment is enabled for this Realm                                                                                                                                                                 |
| feat_ats           | RmmFeature             | Whether Address Translation Service is supported for devices assigned to the Realm                                                                                                                                        |
| ats_plane          | UInt64                 | Index of Plane whose stage 2 permissions are observed by ATS requests from devices assigned to the Realm                                                                                                                  |
| rtt_tree_per_plane | RmmFeature             | Whether this Realm has an RTT tree per Plane                                                                                                                                                                              |
| num_aux_planes     | UInt64                 | Number of auxiliary Planes                                                                                                                                                                                                |
| rtt_s2ap_encoding  | RmmRttS2APEncoding     | S2AP encoding                                                                                                                                                                                                             |
| overlay_perms      | RmmMemPerms[4]         | Memory overlay permissions                                                                                                                                                                                                |
| overlay_locked     | RmmMemPermLocked[16]   | Whether memory overlay value is locked                                                                                                                                                                                    |
| lfa_policy         | RmmLfaPolicy           | Live Firmware Activation policy for components within the Realm's TCB                                                                                                                                                     |
| mec_policy         | RmmMecPolicy           | MEC policy                                                                                                                                                                                                                |

| Name       | Type   | Description                          |
|------------|--------|--------------------------------------|
| num_recs   | UInt64 | Number of RECs owned by this Realm   |
| num_vdevs  | UInt64 | Number of VDEVs owned by this Realm  |
| num_vsmmus | UInt64 | Number of VSMMUs owned by this Realm |

- DMGGPT A Realm Initial Measurement (RIM) is a measurement of the configuration and contents of a Realm at the time of activation.
- DGRFCS A Realm Extensible Measurement (REM) is a measurement value which can be extended during the lifetime of a Realm.
- IFMPYL Attributes of a Realm include an array of measurement values. The first entry in this array is a RIM. The remaining entries in this array are REMs.
- DRAFT XDNDKV During Realm creation, the Host provides ipa\_width, rtt\_level\_start and rtt\_num\_start values as Realm parameters. According to the VMSA, the rtt\_num\_start value is architecturally defined as a function of the ipa\_width and rtt\_level\_start values. It would therefore have been possible to design the Realm creation interface such that the Host provided only the ipa\_width and rtt\_level\_start values. However, this would potentially allow a Realm to be successfully created, but with a configuration which did not match the Host's intent. For this reason, it was decided that the Host should specify all three values explicitly, and that Realm creation should fail if the values are not consistent. See Arm Architecture Reference Manual for A-Profile architecture [3] for further details. DFTWBK A Realm Personalization Value (RPV) is a provided by the Host, to distinguish between Realms which have the same Realm Initial Measurement, but different behavior. SFCNBF Possible uses of the RPV include: · A GUID · Hash of Realm Owner public key · Hash of a 'personalisation document' which is provided to the Realm via a side-band (for example, via NS memory) and contains configuration information used by Realm software. IZFSWC The RMM treats the RPV as an opaque value.
- IBFSRK The RPV is included in the Realm attestation report as a separate claim.
- IMFRXD The RPV is included in the output of the RSI\_REALM\_CONFIG command.
- IGXKDQ If Realm device assignment is not enabled for a Realm then all of the following are true:
- Assignment of a virtual device to the Realm by execution of RMI\_VDEV\_CREATE fails.
- The device assignment feature is reported to the Realm by RSI\_FEATURES as not enabled. Consequently, execution of any RSI\_VDEV command fails.

See also:

- A2.2.5 Realm lifecycle
- A2.4 Realm Execution Context
- A3.3 Realm LPA2 and IPA width
- A5.2.1 Realm IPA space
- A5.6 Realm Translation Table
- A7.1 Realm measurements
- A7.2.3.1.4 Realm Personalization Value claim
- B4.5.82 RMI\_VDEV\_CREATE command
- B5.4.4 RSI\_FEATURES command
- B5.4.16 RSI\_REALM\_CONFIG command
- C2.49 RmmRealm type

## A2.2.4 Realm liveness

- DWTXTJ Realm liveness is a property which means that there exists one or more Granules, other than the RD and the starting level RTTs, which are owned by the Realm.
- IRLSNX In order to destroy a Realm, it must first be terminated. Terminating a Realm causes it to enter REALM\_ZOMBIE state.
- XNJWWV Being in REALM\_ZOMBIE state guarantees that a Realm's activity has been quiesced.
- DPCKRN A Realm is live if any of the following is true:
- The number of RECs owned by the Realm is not zero
- A starting level RTT of the Realm is live
- The number of VDEVs owned by the Realm is not zero
- The number of VSMMUs owned by the Realm is not zero
- IYXBPC A Realm can be both live and in REALM\_ZOMBIE state.
- IVKKPJ If a Realm owns a non-zero number of Data Granules, this implies that it has a starting level RTT which is live, and therefore that the Realm itself is live.
- IPVPQB If a Realm is live, it cannot be destroyed.

## See also:

- A2.2.5 Realm lifecycle
- A2.3.6 Granule state
- A2.3.7 Granule ownership
- A2.4 Realm Execution Context
- A5.6.8 RTTE liveness and RTT liveness
- A9.4 Virtual device object
- A9.8 Virtual SMMU
- B3.99 RealmIsLive function
- B4.5.47 RMI\_REALM\_DESTROY command
- B4.5.48 RMI\_REALM\_TERMINATE command

## A2.2.5 Realm lifecycle

See also:

- Chapter A3 Feature discovery and configuration
- D1.2 Realm lifecycle flows

## A2.2.5.1 States

The states of a Realm are listed below.

| State            | Description                                             |
|------------------|---------------------------------------------------------|
| REALM_NEW        | Under construction. Not eligible for execution.         |
| REALM_ACTIVE     | Eligible for execution.                                 |
| REALM_SYSTEM_OFF | System has been turned off. Not eligible for execution. |
| REALM_ZOMBIE     | Ready for destruction. Not eligible for execution.      |

DRAFT

DGDQPJ

IRRHFG

## A2.2.5.2 State transitions

Permitted Realm state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a Realm object. A transition to the pseudo-state NULL represents destruction of a Realm object.

| From state       | To state         | Events                            |
|------------------|------------------|-----------------------------------|
| NULL             | REALM_NEW        | RMI_REALM_CREATE                  |
| REALM_NEW        | REALM_ACTIVE     | RMI_REALM_ACTIVATE                |
| REALM_ACTIVE     | REALM_SYSTEM_OFF | PSCI_SYSTEM_OFF PSCI_SYSTEM_RESET |
| REALM_NEW        | REALM_ZOMBIE     | RMI_REALM_TERMINATE               |
| REALM_ACTIVE     | REALM_ZOMBIE     | RMI_REALM_TERMINATE               |
| REALM_SYSTEM_OFF | REALM_ZOMBIE     | RMI_REALM_TERMINATE               |
| REALM_ZOMBIE     | NULL             | RMI_REALM_DESTROY                 |

IYCPWW

Permitted Realm state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of an RD. A transition to the pseudo-state NULL represents destruction of an RD.

Figure A2.2: Realm state transitions

<!-- image -->

DRAFT

## See also:

- B6.3.6 PSCI\_SYSTEM\_OFF command
- B6.3.7 PSCI\_SYSTEM\_RESET command
- B4.5.45 RMI\_REALM\_ACTIVATE command
- B4.5.46 RMI\_REALM\_CREATE command
- B4.5.47 RMI\_REALM\_DESTROY command
- B4.5.48 RMI\_REALM\_TERMINATE command

## A2.2.6 Realm parameters

DTGMVZ A Realm parameter is a value which is provided by the Host during Realm creation.

See also:

- A2.2.3 Realm attributes
- Chapter A3 Feature discovery and configuration
- B3.136 RmiRealmParamsAt function
- B4.5.46 RMI\_REALM\_CREATE command
- B4.6.62 RmiRealmParams type

## A2.2.7 Realm Descriptor

- DTNSBY A Realm Descriptor (RD) is an RMM data structure which stores attributes of a Realm.
- DGGKWX The size of an RD is one Granule.

See also:

- A2.2.3 Realm attributes
- A2.3.6 Granule state

<!-- image -->