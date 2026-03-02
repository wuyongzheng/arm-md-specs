## A5.5 Realm Translation Table

This section introduces the stage 2 translation table used by a Realm.

## A5.5.1 RTT overview

- A Realm Translation Table (RTT) is an abstraction over an Armv8-A stage 2 translation table used by a Realm.
- The attributes and format of an Armv8-A stage 2 translation table are defined by the Armv8-A Virtual Memory System Architecture (VMSA) Arm Architecture Reference Manual for A-Profile architecture [3].
- The translation granule size of an RTT is 4KB.
- The RMM architecture can only be deployed on a hardware platform which implements a translation granule size of 4KB.
- The contents of an RTT are not directly accessible to the Host.
- The contents of an RTT are manipulated using RMM commands. These commands allow the Host to manipulate the contents of the RTT used by a Realm, subject to constraints imposed by the RMM.
- An RTT entry (RTTE) is an abstraction over an Armv8-A stage 2 translation table descriptor.
- An RTTE contains an output address which can point to one of the following:
- Another RTT
- A DATA Granule which is owned by the Realm
- Non-secure memory which is accessible to both the Realm and the Host

## A5.5.2 RTT structure and configuration

- An RTT tree is a hierarchical data structure composed of RTTs, connected via Table Descriptors.
- An RTT contains an array of RTTEs.
- An RTT level is the depth of an RTT within an RTT tree.
- An RTT does not have an intrinsic 'level' attribute. The level of an RTT is determined by its position within an RTT tree.
- The RTT level of the root of an RTT tree is called the starting level .
- The maximum depth of an RTT tree depends on all of the following:
- whether LPA2 is selected when the Realm is created
- the rtt\_level\_start attribute of the Realm
- the ipa\_width attribute of the Realm.

## See also:

- A2.1.3 Realm attributes
- A3.1.2 Realm LPA2 and IPA width

## A5.5.3 RTT starting level

- The RTT starting level is set when a Realm is created.
- The number of starting level RTTs is architecturally defined as a function of the Realm IPA width and the RTT starting level. See Arm Architecture Reference Manual for A-Profile architecture [3] for further details.
- The address of the first starting level RTT is stored in the RTT base attribute of the owning Realm.


The RTT base attribute is set when a Realm is created.

See also:

- A2.1.3 Realm attributes

## A5.5.4 RTT entry

An RTT entry (RTTE) is an abstraction over an Armv8-A stage 2 translation table descriptor. The attributes and format of an Armv8-A stage 2 translation table descriptor are defined by the Armv8-A Virtual Memory System Architecture (VMSA) Arm Architecture Reference Manual for A-Profile architecture [3].


An RTTE has a state .

The RTTE state values are shown in the following table.

| Name          | Description                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------|
| ASSIGNED      | This RTTE is identified by a Protected IPA. The output address of this RTTE points to a DATA Granule.   |
| ASSIGNED_NS   | This RTTE is identified by an Unprotected IPA. The output address of this RTTE points to an NS Granule. |
| TABLE         | The output address of this RTTE points to the next-level RTT.                                           |
| UNASSIGNED    | This RTTE is identified by a Protected IPA. This RTTE is not associated with any Granule.               |
| UNASSIGNED_NS | This RTTE is identified by an Unprotected IPA. This RTTE is not associated with any Granule.            |

The state of an RTTE in a RTT which is not level 1 or level 2 or level 3 is UNASSIGNED, UNASSIGNED\_NS or TABLE.

The output address of an RTTE whose state is TABLE and which is in a level n RTT is the physical address of a level n+1 RTT.

An RTT whose level n is not the starting RTT level is pointed-to by exactly one TABLE RTTE in a level n-1 RTT.

The following diagram shows an example RTT tree, annotated with RTTE states.

<!-- image -->


The function AddrIsRttLevelAligned() is used to evaluate whether an address is aligned to the address range described by an RTTE at a specified RTT level.

## See also:

- A5.3.1 Host IPA state
- B1.4 Command condition expressions

## A5.5.5 RTT reading

Attributes of an RTTE, including the RTTE state, can be read by calling the RMI\_RTT\_READ\_ENTRY command. The set of RTTE attributes which are returned depends on the state of the RTTE.

See also:

- B4.3.20 RMI\_RTT\_READ\_ENTRY command

## A5.5.6 RTT folding

<!-- image -->

An RTT is homogeneous if its entries satisfy one of the conditions in the following table. If an RTT is homogeneous, the following table specifies the state to which the parent RTTE is set.

| Conditions on child RTT contents                                                                       | Parent RTTE state   |
|--------------------------------------------------------------------------------------------------------|---------------------|
| All of the following are true: • State of all entries is UNASSIGNED • RIPAS of all entries is the same | UNASSIGNED          |
| State of all entries is UNASSIGNED_NS                                                                  | UNASSIGNED_NS       |
| All of the following are true:                                                                         | ASSIGNED            |

- Level is 2 or 3
- State of all entries is ASSIGNED
- Output address of first entry is aligned to size of the address range described by an entry in the parent RTT
- Output addresses of all entries are contiguous
- RIPAS of all entries is the same

All of the following are true:

- Level is 2 or 3
- State of all entries is ASSIGNED\_NS
- Output address of first entry is aligned to size of the address range described by an entry in the parent RTT
- Output addresses of all entries are contiguous
- Attributes of all entries are identical

The function RttIsHomogeneous() is used to evaluate whether an RTT is homogeneous.

RTT folding is the operation of destroying a homogeneous child RTT, and moving information which was stored in the child RTT into the parent RTTE.

On RTT folding, the state of the parent RTTE is determined from the contents of the child RTTEs.

The function RttFold() is used to evaluate the parent RTTE state which results from an RTT folding operation.

On RTT folding, if the state of the parent RTTE is ASSIGNED or ASSIGNED\_NS then the attributes of the parent RTTE are copied from the child RTTEs.

See also:

- A5.5.9 RTT destruction

ASSIGNED\_NS

- B3.62 RttFold function
- B3.63 RttIsHomogeneous function
- B4.3.17 RMI\_RTT\_FOLD command

## A5.5.7 RTT unfolding

- RTT unfolding is the operation of creating a child RTT, and populating it based on the contents of the parent RTTE.
- On RTT unfolding, the state of all RTTEs in the child RTT are set to the state of the parent RTTE.
- On RTT unfolding, if the state of the parent RTTE is ASSIGNED or ASSIGNED\_NS, then the output addresses of RTTEs in the child RTT are set to a contiguous range which starts from the address of the parent RTTE.

See also:

- B4.3.15 RMI\_RTT\_CREATE command

## A5.5.8 RTTE liveness and RTT liveness

- RTTE liveness is a property which means that a physical address is stored in the RTTE.
- An RTTE is live if the RTTE state is ASSIGNED, ASSIGNED\_NS or TABLE.
- The function RttSkipNonLiveEntries() is used to scan an RTT to find the next live RTTE. The resulting IPA is returned to the Host from commands whose successful execution causes a live RTTE to become non-live.
- Identifying the next live RTTE allows the Host to avoid calls to RMI\_RTT\_READ\_ENTRY when unmapping ranges of a Realm's IPA space, for example during Realm destruction.
- RTT liveness is a property which means that there exists another RMM data structure which is referenced by the RTT.
- An RTT is live if, for any of its entries, either of the following is true:
- The RTTE state is ASSIGNED
- The RTTE state is TABLE.
- Note that an RTT can be non-live, even if one of its entries is live. This would be the case for example if the RTT corresponds to an Unprotected IPA range and the state of one of its entries is ASSIGNED\_NS.
- The function RttIsLive() is used to evaluate whether an RTT is live.

See also:

- A5.5.9 RTT destruction
- B3.64 RttIsLive function
- B3.76 RttSkipNonLiveEntries function
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.16 RMI\_RTT\_DESTROY command
- B4.3.22 RMI\_RTT\_UNMAP\_UNPROTECTED command

## A5.5.9 RTT destruction

- RTT destruction is the operation of destroying a child RTT, and discarding information which was stored in the child RTT.
- An RTT cannot be destroyed if it is live.
- An RTT can be destroyed regardless of whether it is homogeneous.
- Following RTT destruction, all of the following are true for the parent RTTE:
- RIPAS is DESTROYED
- RTTE state is UNASSIGNED

## See also:

- A5.2 Realm view of memory management
- A5.5.6 RTT folding
- A5.5.8 RTTE liveness and RTT liveness
- B4.3.16 RMI\_RTT\_DESTROY command

## A5.5.10 RTT walk

An IPA is translated to a PA by walking an RTT tree, starting at the RTT base.

The behaviour of an RTT walk is defined by the Armv8-A Virtual Memory System Architecture (VMSA) Arm Architecture Reference Manual for A-Profile architecture [3].

The inputs to an RTT walk are:

- a Realm Descriptor, which contains the address of the initial RTT
- a target IPA
- a target RTT level.

The RTT walk terminates when either:

- it reaches the target RTT level, or
- it reaches an RTTE whose state is not TABLE.

The result of an RTT walk performed by the RMM is a data structure of type RmmRttWalkResult.

The attributes of an RmmRttWalkResult are summarized in the following table.

| Name     | Type        | Description                        |
|----------|-------------|------------------------------------|
| level    | Int8        | RTT level reached by the walk      |
| rtt_addr | Address     | Address of RTT reached by the walk |
| rtte     | RmmRttEntry | RTTE reached by the walk           |

The function RmmRttWalkResult RttWalk(rd, addr, level) is used to represent an RTT walk.

The input address to an RTT walk is always less than 2^w , where w is the IPA width of the target Realm. See also:

- A2.1.3 Realm attributes
- B1.4 Command condition expressions
- B3.78 RttWalk function
- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.15 RMI\_RTT\_CREATE command
- B4.3.16 RMI\_RTT\_DESTROY command
- B4.3.19 RMI\_RTT\_MAP\_UNPROTECTED command
- B4.3.22 RMI\_RTT\_UNMAP\_UNPROTECTED command
- C1.31 RmmRttWalkResult type

## A5.5.11 RTT entry attributes

The cacheability attributes of an RTT entry which corresponds to a Protected IPA and whose state is ASSIGNED are independent of any stage 1 descriptors and of the state of the stage 1 MMU.

## Chapter A5. Realm memory management A5.5. Realm Translation Table

- The RMM uses FEAT\_S2FWB to ensure that the cacheability attributes of an RTT entry which corresponds to a Protected IPA and whose state is ASSIGNED are independent of stage 1 translation.
- The attributes of an RTT entry which corresponds to a Protected IPA and whose state is ASSIGNED include the following:
- Normal memory
- Inner Write-Back Cacheable
- Inner Shareable
- The following attributes of an RTT entry which corresponds to an Unprotected IPA and whose state is ASSIGNED\_NS are Host-controlled RTT attributes :
- ADDR
- MemAttr[2:0]
- S2AP
- The shareability attributes of an RTT entry which corresponds to an Unprotected IPA and whose state is ASSIGNED\_NS are as follows:
- Inner Shareable if the mapping is cacheable.
- Outer Shareable if the mapping is non-cacheable.
- The shareability attributes of an RTT entry which corresponds to an Unprotected IPA are expected to be controlled by the RMM as follows:
- If LPA2 is enabled at stage 2 then the RMM is expected to set VTCR\_EL2.DS == '1' .
- If LPA2 is not enabled at stage 2 then the RMM is expected to set the value of the SH field in the translation table descriptor based on the value of the MemAttr field.
- In an RTT entry which corresponds to an Unprotected IPA and whose state is ASSIGNED\_NS, MemAttr[3] is RES0 because the RMM uses FEAT\_S2FWB.
- Hardware access flag and dirty bit management is disabled for the stage 2 translation used by a Realm.
- Hardware access flag and dirty bit management may be enabled by software executing within the Realm, for its own stage 1 translation.

See also:

- A5.2.1 Realm IPA space
- B3.56 RttDescriptorIsValidForUnprotected function
- B4.3.19 RMI\_RTT\_MAP\_UNPROTECTED command
- B4.3.20 RMI\_RTT\_READ\_ENTRY command