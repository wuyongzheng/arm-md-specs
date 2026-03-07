## A5.6 Realm Translation Table

This section introduces the stage 2 translation table used by a Realm.

## A5.6.1 RTT overview

- A Realm Translation Table (RTT) is an abstraction over an Armv8-A stage 2 translation table used by a Realm.
- The attributes and format of an Armv8-A stage 2 translation table are defined by the Armv8-A Virtual Memory System Architecture (VMSA) Arm Architecture Reference Manual for A-Profile architecture [3].
- The translation granule size of an RTT is equal to the RMI Granule size.
- The contents of an RTT are not directly accessible to the Host.
- The contents of an RTT are manipulated using RMM commands. These commands allow the Host to manipulate the contents of the RTT used by a Realm, subject to constraints imposed by the RMM.
- An RTT entry (RTTE) is an abstraction over an Armv8-A stage 2 translation table descriptor.
- An RTTE contains an output address which can point to one of the following:
- Another RTT
- A DATA Granule which is owned by the Realm
- Non-secure memory which is accessible to both the Realm and the Host

## A5.6.2 RTT structure and configuration

- An RTT tree is a hierarchical data structure composed of RTTs, connected via Table Descriptors.
- An RTT contains an array of RTTEs.
- An RTT level is the depth of an RTT within an RTT tree.
- An RTT does not have an intrinsic 'level' attribute. The level of an RTT is determined by its position within an RTT tree.
- The RTT level of the root of an RTT tree is called the starting level .
- The maximum depth of an RTT tree depends on all of the following:


- whether LPA2 is selected when the Realm is created
- the rtt\_level\_start attribute of the Realm
- the ipa\_width attribute of the Realm.
- The VMID associated with an RTT tree is chosen by the RMM. The RMM ensures that this is unique among all RTT trees on the system.

See also:

- [A2.2.3 Realm attributes](rmm-A2.2.md#a223-realm-attributes)
- [A3.3 Realm LPA2 and IPA width](rmm-A3.md#a33-realm-lpa2-and-ipa-width)

## A5.6.3 RTT starting level

- The RTT starting level is set when a Realm is created.
- The number of starting level RTTs is architecturally defined as a function of the Realm IPA width and the RTT starting level. See Arm Architecture Reference Manual for A-Profile architecture [3] for further details.
- The address of the first starting level RTT is stored in the RTT base attribute of the owning Realm.


The RTT base attribute is set when a Realm is created.

See also:

- [A2.2.3 Realm attributes](rmm-A2.2.md#a223-realm-attributes)

## A5.6.4 RTT entry

- An RTT entry (RTTE) is an abstraction over an Armv8-A stage 2 translation table descriptor. The attributes and format of an Armv8-A stage 2 translation table descriptor are defined by the Armv8-A Virtual Memory System Architecture (VMSA) Arm Architecture Reference Manual for A-Profile architecture [3].

An RTTE has a state .

The RTTE state values are shown in the following table.

| Name               | Description                                                                                                                                          |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| RTTE_ARCH_DEV      | This RTTE is identified by a Protected IPA. The output address of this RTTE points to an RMMobject which is used to emulate an architectural device. |
| RTTE_AUX_DESTROYED | An auxiliary RTT was destroyed while a corresponding primary RTT entry was live.                                                                     |
| RTTE_DATA          | This RTTE is identified by a Protected IPA. The output address of this RTTE points to a DATA Granule.                                                |
| RTTE_MAPPED_NS      This RTTE is identified by an Unprotected IPA. The output address of this RTTE points to a Granule-aligned address within NS PAS.              |
| RTTE_NARCH_DEV     | This RTTE is identified by a Protected IPA. The output address of this RTTE points to a GRAN_DEV Granule.                                            |
| RTTE_TABLE         | The output address of this RTTE points to the next-level RTT.                                                                                        |
| RTTE_UNMAPPED_NS   | This RTTE is identified by an Unprotected IPA. This RTTE is not associated with any Granule.                                                         |
| RTTE_VOID          | This RTTE is identified by a Protected IPA. This RTTE is not associated with any Granule.                                                            |

- An RTT whose level n is not the starting RTT level is pointed-to by exactly one RTTE\_TABLE RTTE in a level n-1 RTT.

The following diagram shows an example RTT tree, annotated with RTTE states.

<!-- image -->


Figure A5.7: Example RTT tree

The function AddrIsRttLevelAligned() is used to evaluate whether an address is aligned to the address range described by an RTTE at a specified RTT level.

## See also:

- [A5.3.1 Host IPA state](rmm-A5.3.md#a531-host-ipa-state)
- [B1.4 Command condition expressions](rmm-B1.2.md#b14-command-condition-expressions)

## A5.6.5 RTT reading

Attributes of an RTTE, including the RTTE state, can be read by calling the RMI\_RTT\_READ\_ENTRY command. The set of RTTE attributes which are returned depends on the state of the RTTE.

See also:

- [B4.5.74 RMI\_RTT\_READ\_ENTRY command](rmm-B4.5.74.md)

## A5.6.6 RTT folding


An RTT is homogeneous

- if all of the following are true:
- State of all entries is the same.
- RIPAS of all entries is the same, or the RTT describes Unprotected IPA space.
- S2AP fields of all entries are the same.
- Either the state is RTTE\_VOID or RTTE\_UNMAPPED\_NS, or all of the following are true:
- -Level is 2 or 3.
- -Output address of first entry is aligned to size of the address range described by an entry in the parent RTT.
- -Output addresses of all entries are contiguous.
- -Memory attributes of all entries are the same.

The function RttIsHomogeneous() is used to evaluate whether an RTT is homogeneous.


RTT folding is the operation of destroying a homogeneous child RTT, and moving information which was stored in the child RTT into the parent RTTE.

<!-- image -->

- On RTT folding, the state of the parent RTTE is set to the state of the child RTTEs.
- On RTT folding, if the RTT describes Protected IPA space then the RIPAS of the parent RTTE is set to the RIPAS of the child RTTEs.
- On RTT folding, the S2AP fields of the parent RTTE is set to the S2AP fields of the child RTTEs.
- On RTT folding, if the state of the parent RTTE is not RTTE\_VOID or RTTE\_UNMAPPED\_NS then all of the following are true:
- The output address of the parent RTTE is set to the output address of the first child RTTE.
- The memory attributes of the parent RTTE are set to the memory attributes of the child RTTEs.
- The function RttFold() is used to evaluate the parent RTTE state which results from an RTT folding operation.

See also:

- [A5.6.9 RTT destruction](rmm-A5.6.md#a569-rtt-destruction)
- [A10.3.2 Stage 2 Access Permissions within a multi-Plane Realm](rmm-A10.3.md#a1032-stage-2-access-permissions-within-a-multi-plane-realm)
- [B3.182 RttFold function](rmm-B3.md#b3182-rttfold-function)
- [B3.183 RttIsHomogeneous function](rmm-B3.md#b3183-rttishomogeneous-function)
- [B4.5.72 RMI\_RTT\_FOLD command](rmm-B4.5.72.md)

## A5.6.7 RTT unfolding

- RTT unfolding is the operation of creating a child RTT, and populating it based on the contents of the parent RTTE.
- On RTT unfolding, the state of all RTTEs in the child RTT are set to the state of the parent RTTE.
- On RTT unfolding, if the RTT describes Protected IPA space then the RIPAS of all RTTEs in the child RTT are set to the state of the parent RTTE.
- On RTT unfolding, the S2AP fields of all RTTEs in the child RTT are set to the S2AP fields of the parent RTTE.
- On RTT unfolding, if the state of the parent RTTE is not RTTE\_VOID or RTTE\_UNMAPPED\_NS then all of the following are true:
- The output addresses of RTTEs in the child RTT are set to a contiguous range which starts from the address of the parent RTTE.
- The memory attributes of all RTTEs in the child RTT are set to the memory attributes of the parent RTTE.

See also:

- [B4.5.64 RMI\_RTT\_CREATE command](rmm-B4.5.64.md)

## A5.6.8 RTTE liveness and RTT liveness

- RTTE liveness is a property which means that a physical address is stored in the RTTE.
- An RTTE is live if the RTTE state is any of the following:
- RTTE\_DATA
- RTTE\_MAPPED\_NS
- RTTE\_NARCH\_DEV
- RTTE\_TABLE
- RTTE\_ARCH\_DEV
- The function RttSkipNonLiveEntries() is used to scan an RTT to find the next live RTTE. The resulting IPA is returned to the Host from commands whose successful execution causes a live RTTE to become non-live.
- Identifying the next live RTTE allows the Host to avoid calls to RMI\_RTT\_READ\_ENTRY when unmapping ranges of a Realm's IPA space, for example during Realm destruction.



RTT liveness is a property which means that there exists another RMM data structure which is referenced by the RTT.

An RTT is live if, for any of its entries, the RTTE state is any of the following:

- RTTE\_DATA
- RTTE\_NARCH\_DEV
- RTTE\_TABLE
- VSMMU

Note that an RTT can be non-live, even if one of its entries is live. This would be the case for example if the RTT corresponds to an Unprotected IPA range and the state of one of its entries is RTTE\_MAPPED\_NS.

The function RttIsLive() is used to evaluate whether an RTT is live.

See also:

- [A5.6.9 RTT destruction](rmm-A5.6.md#a569-rtt-destruction)
- [B3.184 RttIsLive function](rmm-B3.md#b3184-rttislive-function)
- [B3.199 RttSkipNonLiveEntries function](rmm-B3.md#b3199-rttskipnonliveentries-function)
- [B4.5.67 RMI\_RTT\_DATA\_UNMAP command](rmm-B4.5.67.md)
- [B4.5.68 RMI\_RTT\_DESTROY command](rmm-B4.5.68.md)
- [B4.5.78 RMI\_RTT\_UNPROT\_UNMAP command](rmm-B4.5.78.md)

## A5.6.9 RTT destruction

- RTT destruction is the operation of destroying a child RTT, and discarding information which was stored in the child RTT.
- An RTT cannot be destroyed if it is live.
- An RTT can be destroyed regardless of whether it is homogeneous.

Following RTT destruction within Protected IPA space, all of the following are true for the parent RTTE:

- RIPAS is RIPAS\_DESTROYED
- RTTE state is RTTE\_VOID

Following RTT destruction within Unprotected IPA space, the state of the parent RTTE is RTTE\_UNMAPPED\_NS.

See also:

- [A5.2 Realm view of memory management](rmm-A5.1.md#a52-realm-view-of-memory-management)
- [A5.6.6 RTT folding](rmm-A5.6.md#a566-rtt-folding)
- [A5.6.8 RTTE liveness and RTT liveness](rmm-A5.6.md#a568-rtte-liveness-and-rtt-liveness)
- [B4.5.68 RMI\_RTT\_DESTROY command](rmm-B4.5.68.md)

## A5.6.10 RTT walk

- An IPA is translated to a PA by walking an RTT tree, starting at the RTT base.
- The behaviour of an RTT walk is defined by the Armv8-A Virtual Memory System Architecture (VMSA) Arm Architecture Reference Manual for A-Profile architecture [3].

The inputs to an RTT walk are:

- a Realm Descriptor, which contains the address of the initial RTT
- an RTT tree index
- a target IPA
- a target RTT level.

The RTT walk terminates when either:

- it reaches the target RTT level, or



- it reaches an RTTE whose state is not RTTE\_TABLE.

The result of an RTT walk performed by the RMM is a data structure of type RmmRttWalkResult.

The attributes of an RmmRttWalkResult are summarized in the following table.

| Name     | Type        | Description                        |
|----------|-------------|------------------------------------|
| level    | Int8        | RTT level reached by the walk      |
| rtt_addr | Address     | Address of RTT reached by the walk |
| rtte     | RmmRttEntry | RTTE reached by the walk           |

- The function RmmRttWalkResult RttWalk(rd, addr, level) is used to represent an RTT walk.


The input address to an RTT walk is always less than 2^w , where w is the IPA width of the target Realm.

## See also:

- [A2.2.3 Realm attributes](rmm-A2.2.md#a223-realm-attributes)
- [A10.3.1 Auxiliary RTT](rmm-A10.3.md#a1031-auxiliary-rtt)
- [B1.4 Command condition expressions](rmm-B1.2.md#b14-command-condition-expressions)
- [B3.211 RttWalk function](rmm-B3.md#b3211-rttwalk-function)
- [B4.5.64 RMI\_RTT\_CREATE command](rmm-B4.5.64.md)
- [B4.5.65 RMI\_RTT\_DATA\_MAP command](rmm-B4.5.65.md)
- [B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command](rmm-B4.5.66.md)
- [B4.5.67 RMI\_RTT\_DATA\_UNMAP command](rmm-B4.5.67.md)
- [B4.5.68 RMI\_RTT\_DESTROY command](rmm-B4.5.68.md)
- [B4.5.77 RMI\_RTT\_UNPROT\_MAP command](rmm-B4.5.77.md)
- [B4.5.78 RMI\_RTT\_UNPROT\_UNMAP command](rmm-B4.5.78.md)
- [C2.74 RmmRttWalkResult type](rmm-C2.md#c274-rmmrttwalkresult-type)

## A5.6.11 Stage 2 Access Permissions

This section describes how Stage 2 Access Permissions (S2AP) observed by Auxiliary Planes is managed for Realm IPA space, from the following perspectives:


- How S2AP is encoded in RTT descriptors.
- The programming model for control by the Realm of S2AP for Protected IPA space.
- The programming model for control by the Host of S2AP for Unprotected IPA space.

## See also:

- [Chapter A10 Planes](rmm-A9.11.md#chapter-a10-planes)

## A5.6.11.1 Encoding of Stage 2 Access Permissions in RTT descriptors

- If the Realm uses S2AP direct encoding then S2AP values are encoded directly in RTT entries.

- Indirect permissions' in the Arm Architecture Reference Manual for A-Profile architecture [3].

If the Realm uses S2AP indirect encoding then S2AP is encoded indirectly in RTT entries, as described in 'Stage 2

## See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]
- [A3.13 Support for Stage 2 Access Permissions indirect encoding](rmm-A3.md#a313-support-for-stage-2-access-permissions-indirect-encoding)


## A5.6.11.2 Stage 2 Access Permissions for a Protected IPA

The programming model for control of S2AP for Protected IPA space is based on indirection, as follows:

- The S2AP base value of a Protected IPA is determined by its HIPAS.
- Each Protected IPA has an S2AP overlay index which is controlled by P0, via RSI commands.
- Each { Plane, S2AP overlay index } tuple maps to an S2AP overlay value .
- -For Pn, this mapping is controlled by P0 via RSI commands, subject to constraints imposed by the RMM.
- -For P0, this mapping is architecturally fixed.
- The S2AP which applies to an access from a given Plane to a given IPA are defined by the combination of the S2AP base value and the S2AP overlay value, following the rules for 'Stage 2 Indirect permissions' in the Arm Architecture Reference Manual for A-Profile architecture [3].
- The programming model for control of S2AP for Protected IPA space does not depend on whether the Realm uses S2AP indirect encoding.
- If the Realm uses S2AP direct encoding, the RMM maps from the indirect programming model onto S2AP values which are directly stored in RTT entries.
- For a Protected IPA which is HIPAS\_DATA, the S2AP base value is RW+puX .
- For a Protected IPA which is HIPAS\_NARCH\_DEV, the S2AP base value is RW .
- For a Protected IPA, all S2AP overlay indices map to RW+puX for P0.

See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]
- [A10.3.2 Stage 2 Access Permissions within a multi-Plane Realm](rmm-A10.3.md#a1032-stage-2-access-permissions-within-a-multi-plane-realm)

## A5.6.11.3 Stage 2 Access Permissions for an Unprotected IPA

- The S2AP which applies to a Realm access to an Unprotected IPA is controlled by the Host.
- The programming model for control by the Host of S2AP for Unprotected IPA space depends on whether the Realm uses S2AP indirect encoding.


If the Realm uses S2AP direct encoding then S2AP is controlled as follows:

- The Host provides read and write permissions via the AP field in the descriptor passed to RMI\_RTT\_UNPROT\_MAP to create the mapping in the primary RTT tree.
- The RMM sets XN = '1' in the primary RTT tree.
- Execution of RMI\_RTT\_AUX\_UNPROT\_MAP causes the RW and XN fields to be copied from the primary RTT tree into an auxiliary RTT tree.

If the Realm uses S2AP indirect encoding then S2AP is controlled as follows:

- The Host provides an S2AP base index in the descriptor passed to RMI\_RTT\_UNPROT\_MAP.
- The RMM configures the S2AP overlay index to provide a S2AP overlay value of RW .
- The observed S2AP is defined by the combination of the S2AP base value and the S2AP overlay value, following the rules for 'Stage 2 Indirect permissions' in the Arm Architecture Reference Manual for A-Profile architecture [3].

In this way, the RMM ensures that neither unprivileged execute permission ( uX ) nor privileged execute permission ( pX ) is observed on Realm access to an Unprotected IPA.

See also:

- [A5.6.11.4 Stage 2 base permission values](rmm-A5.6.md#a56114-stage-2-base-permission-values)


- [B4.5.62 RMI\_RTT\_AUX\_UNPROT\_MAP command](rmm-B4.5.62.md)
- [B4.5.77 RMI\_RTT\_UNPROT\_MAP command](rmm-B4.5.77.md)

## A5.6.11.4 Stage 2 base permission values

The mapping from S2AP base index to S2AP base value is as follows:

|   Encoding | Name               | Description   |
|------------|--------------------|---------------|
|          0 | RMI_S2AP_NO_ACCESS | NoAccess      |
|          1 | RMI_S2AP_RO        | RO            |
|          2 | RMI_S2AP_WO        | WO            |
|          3 | RMI_S2AP_RW        | RW            |
|          4 | RMI_S2AP_RW_PUX    | RW+puX        |

## See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]

## A5.6.12 Memory attributes

## A5.6.12.1 Memory attributes for RTTE\_DATA mappings

- The memory type and cacheability attributes which result from Realm access to an IPA which is HIPAS\_DATA are Normal Write-Back.

The shareability attributes which result from Realm access to an IPA which is HIPAS\_DATA are Inner Shareable.

- The memory attributes which result from Realm access to an IPA which is HIPAS\_DATA are independent of any stage 1 descriptors and of the state of the stage 1 MMU.
- The RMM uses FEAT\_S2FWB to ensure that the memory attributes which result from Realm access to an IPA which is HIPAS\_DATA are independent of stage 1 translation.

## See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]
- [B4.5.65 RMI\_RTT\_DATA\_MAP command](rmm-B4.5.65.md)
- [B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command](rmm-B4.5.66.md)

## A5.6.12.2 Memory attributes for RTTE\_NARCH\_DEV mappings

The memory type and cacheability attributes which result from Realm access to an IPA which is HIPAS\_NARCH\_DEV and which maps to a Device non-coherent memory location are controlled by stage 1 translation and constrained to be one of the following:

- Device, with device attributes specified via stage 1 translation
- Normal Non-Cacheable

The RMM uses FEAT\_S2FWB to constrain the memory type and cacheability attributes which result from Realm access to an IPA which is HIPAS\_NARCH\_DEV and which is mapped to a Device non-coherent memory physical location.


The memory type and cacheability attributes which result from Realm access to an IPA which is HIPAS\_NARCH\_DEV and which maps to a Device coherent memory physical location are passed through from stage 1 translation.


The RMM uses FEAT\_S2FWB to pass through from stage 1 translation the memory type and cacheability attributes which result from Realm access to an IPA which is HIPAS\_NARCH\_DEV and which is mapped to a Device coherent memory physical location.

The shareability attributes which result from Realm access to an IPA which is HIPAS\_NARCH\_DEV and which maps to a Device non-coherent memory physical location are Outer Shareable.

The shareability attributes which result from Realm access to an IPA which is HIPAS\_NARCH\_DEV and which maps to a Device coherent memory physical location are Inner Shareable.

## See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]
- [A2.3 Physical memory](rmm-A2.3.md)
- [A9.6.2 Realm validation of device memory mappings](rmm-A9.6.md#a962-realm-validation-of-device-memory-mappings)
- [B4.5.69 RMI\_RTT\_DEV\_MAP command](rmm-B4.5.69.md)

## A5.6.12.3 Memory attributes for RTTE\_MAPPED\_NS mappings

The following attributes of an RTT entry whose state is RTTE\_MAPPED\_NS are Host-controlled Unprotected RTT attributes :

- ADDR
- MemAttr[2:0]
- AP (if the Realm uses S2AP direct encoding) or PIIndex (if the Realm uses S2AP indirect encoding)
- In an RTT entry whose state is RTTE\_MAPPED\_NS, MemAttr[3] is RES0 because the RMM uses FEAT\_S2FWB.
- The shareability attributes which result from Realm access to an IPA which is HIPAS\_MAPPED\_NS are as follows:
- Inner Shareable if the mapping is cacheable.
- Outer Shareable if the mapping is non-cacheable.

The shareability attributes of an RTT entry which corresponds to an Unprotected IPA are expected to be controlled by the RMM as follows:

- If LPA2 is enabled at stage 2 then the RMM is expected to set VTCR\_EL2.DS == '1' .
- If LPA2 is not enabled at stage 2 then the RMM is expected to set the value of the SH field in the translation table descriptor based on the value of the MemAttr field.

## See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]
- [A3.13 Support for Stage 2 Access Permissions indirect encoding](rmm-A3.md#a313-support-for-stage-2-access-permissions-indirect-encoding)
- [B3.173 RttDescriptorIsValidForUnprotected function](rmm-B3.md#b3173-rttdescriptorisvalidforunprotected-function)
- [B4.5.77 RMI\_RTT\_UNPROT\_MAP command](rmm-B4.5.77.md)

## A5.6.12.4 Summary of memory attributes

The following table summarizes the resultant memory attributes for each permitted combination of HIPAS and Granule category.

| HIPAS      | Granule category              | Resultant memory type and cacheability attributes   | Resultant shareability attributes   |
|------------|-------------------------------|-----------------------------------------------------|-------------------------------------|
| HIPAS_DATA | Delegable conventional memory | Normal Write-Back                                   | Inner Shareable                     |





| HIPAS           | Granule category                     | Resultant memory type and cacheability attributes                                        | Resultant shareability attributes                                                               |
|-----------------|--------------------------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| HIPAS_NARCH_DEV | Delegable non-coherent device memory | One of the following: • Device • Normal Non-cacheable (Specified by stage 1 translation) | Outer Shareable                                                                                 |
| HIPAS_NARCH_DEV | Delegable coherent device memory     | Specified by stage 1 translation                                                         | Inner Shareable                                                                                 |
| HIPAS_MAPPED_NS | Delegable conventional memory        | Specified by combination of Host-controlled RTT attributes and stage 1 translation       | • Inner Shareable if the mapping is cacheable • Outer Shareable if the mapping is non-cacheable |

## See also:

- [A2.3.5 Delegable physical memory](rmm-A2.3.md#a235-delegable-physical-memory)

## A5.6.12.5 Hardware access flag and dirty bit management

Hardware access flag and dirty bit management is disabled for the stage 2 translation used by a Realm.

Hardware access flag and dirty bit management may be enabled by software executing within the Realm, for its own stage 1 translation.

