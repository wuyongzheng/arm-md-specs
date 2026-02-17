## A2.2 Granule

This section describes the concept of a Granule.

DNBXXX A Granule is a unit of physical memory whose size is 4KB.

IDJGZW A Granule may be used to store one of the following:

- Code or data used by the Host
- Code or data used by software in the Secure Security state
- Code or data used by a Realm
- Data used by the RMM to manage a Realm

The use of a Granule is reflected in its lifecycle state.

DZVRXC A Granule is delegable if it can be delegated by the Host for use by the RMM or by a Realm.

UKHKLP In a typical implementation, all memory which is presented to the Host as RAM is delegable. Examples of non-delegable memory may include the following:

- Memory which is carved out for use by the Root world, the RMM or the Secure world
- Device memory

## See also:

- A2.2.1 Granule attributes
- A2.2.3 Granule lifecycle

## A2.2.1 Granule attributes

This section describes the attributes of a Granule.

- DJPBBC A Granule attribute is a property of a Granule whose value can be observed or modified either by the Host or by a Realm.
- IWVXGK Examples of ways in which a Granule attribute may be observable include the outcome of an RMM command, and whether a memory access generates a fault.

DDVMRF The attributes of a Granule are summarized in the following table.

| Name   | Type            | Description     |
|--------|-----------------|-----------------|
| gpt    | RmmGptEntry     | GPT entry       |
| state  | RmmGranuleState | Lifecycle state |

## See also:

- A2.1 Realm
- A2.1.7 Realm Descriptor
- A2.2.3 Granule lifecycle
- B3.20 GranuleAccessPermitted function
- C1.6 RmmGranule type

## A2.2.2 Granule ownership

- IDMVQM A Granule whose state is neither UNDELEGATED nor DELEGATED is owned by a Realm.

IPRNTM The owner of a Granule is identified by the address of a Realm Descriptor (RD).

- IZXBZM For a Granule whose state is RD, the ownership relation is recursive: the owning Realm is identified by the address of the RD itself.

ITYHTD A Granule whose state is RTT is one of the following:

- A starting level RTT. The address of this RTT is stored in the RD of the owning Realm.
- A non-starting level RTT. The address of this RTT is stored in its parent RTT, in an RTT entry whose state is TABLE. Recursively following the parent relationship leads to the RD of the owning Realm.
- IQCNRM A Granule whose state is DATA is mapped at a Protected IPA, in an RTT entry whose state is ASSIGNED. The Realm which owns the RTT is the owner of the DATA Granule.
- IHHPVB A REC has an 'owner' attribute which points to the RD of the owning Realm.
- XNDNHG A REC is not mapped at a Protected IPA. Its ownership therefore needs to be recorded explicitly.

See also:

- A2.1 Realm
- A2.1.7 Realm Descriptor
- A2.3 Realm Execution Context
- A5.2.1 Realm IPA space
- A5.5 Realm Translation Table
- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.12 RMI\_REC\_CREATE command
- B4.3.15 RMI\_RTT\_CREATE command

## A2.2.3 Granule lifecycle

## A2.2.3.1 States

DMPLGT

The states of a Granule are listed below.

For each state, the corresponding GPT entry value is shown.

| Granule state   | Description                                | GPT entry     |
|-----------------|--------------------------------------------|---------------|
| UNDELEGATED     | Not delegated for use by the RMM.          | Not GPT_REALM |
| DELEGATED       | Delegated for use by the RMM.              | GPT_REALM     |
| RD              | Realm Descriptor.                          | GPT_REALM     |
| REC             | Realm Execution Context.                   | GPT_REALM     |
| REC_AUX         | Realm Execution Context auxiliary Granule. | GPT_REALM     |
| DATA            | Realm code or data.                        | GPT_REALM     |
| RTT             | Realm Translation Table.                   | GPT_REALM     |

IMPGJV If the state of a Granule is UNDELEGATED then the RMM does not prevent the GPT entry of the Granule from being changed by another agent to any value except GPT\_REALM.

DVRSKZ An NS Granule is a Granule whose GPT entry is GPT\_NS.

IZJBTT

IVVGVM

## A2.2.3.2 State transitions

Permitted Granule state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

| From state   | To state    | Events                                  |
|--------------|-------------|-----------------------------------------|
| UNDELEGATED  | DELEGATED   | RMI_GRANULE_DELEGATE                    |
| DELEGATED    | UNDELEGATED | RMI_GRANULE_UNDELEGATE                  |
| DELEGATED    | RD          | RMI_REALM_CREATE                        |
| RD           | DELEGATED   | RMI_REALM_DESTROY                       |
| DELEGATED    | DATA        | RMI_DATA_CREATE RMI_DATA_CREATE_UNKNOWN |
| DATA         | DELEGATED   | RMI_DATA_DESTROY                        |
| DELEGATED    | REC         | RMI_REC_CREATE                          |
| REC          | DELEGATED   | RMI_REC_DESTROY                         |
| DELEGATED    | REC_AUX     | RMI_REC_CREATE                          |
| REC_AUX      | DELEGATED   | RMI_REC_DESTROY                         |
| DELEGATED    | RTT         | RMI_REALM_CREATE RMI_RTT_CREATE         |
| RTT          | DELEGATED   | RMI_REALM_DESTROY RMI_RTT_DESTROY       |

Permitted Granule state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

Figure A2.2: Granule state transitions

<!-- image -->

See also:

- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.5 RMI\_GRANULE\_DELEGATE command
- B4.3.6 RMI\_GRANULE\_UNDELEGATE command
- B4.3.9 RMI\_REALM\_CREATE command
- B4.3.10 RMI\_REALM\_DESTROY command
- B4.3.12 RMI\_REC\_CREATE command
- B4.3.13 RMI\_REC\_DESTROY command
- B4.3.15 RMI\_RTT\_CREATE command
- B4.3.16 RMI\_RTT\_DESTROY command

## A2.2.4 Granule wiping

- RTMGSL When the state of a Granule has transitioned from P to DELEGATED and then to any other state, any content associated with P has been wiped .
- XCTGQZ Any sequence of Granule state transitions which passes through the DELEGATED state causes the Granule contents to be wiped. This is necessary to ensure that information does not leak from one Realm to another, or from a Realm to the Host. Note that no agent can observe the contents of a Granule while its state is DELEGATED.
- DWTWJR Wiping is an operation which changes the observable value of a memory location from X to Y , such that the value X cannot be determined from the value Y .
- RBSXXV Wiping of a memory location does not reveal, directly or indirectly, any confidential Realm data.
- IMRPCQ Wiping is not guaranteed to be implemented as zero filling.
- SVJWYH Realm software should not assume that the initial contents of uninitialized memory (that is, Realm IPA space which is backed by DATA Granules created using RMI\_DATA\_CREATE\_UNKNOWN) are zero.

See also:

- Arm CCA Security model [4]
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.6 RMI\_GRANULE\_UNDELEGATE command