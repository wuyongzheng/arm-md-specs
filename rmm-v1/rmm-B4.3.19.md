## B4.3.19 RMI\_RTT\_MAP\_UNPROTECTED command

Creates a mapping from an Unprotected IPA to a Non-secure PA.

## See also:

- A5.5 Realm Translation Table
- B4.3.22 RMI\_RTT\_UNMAP\_UNPROTECTED command

## B4.3.19.1 Interface

## B4.3.19.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                                 |
|--------|------------|--------|---------|-------------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC400015F                                       |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm                           |
| ipa    | X2         | 63:0   | Address | IPA at which the Granule will be mapped in the target Realm |
| level  | X3         | 63:0   | Int64   | RTT level                                                   |
| desc   | X4         | 63:0   | Bits64  | RTTE descriptor                                             |

The layout and encoding of fields in the desc input value match 'Attribute fields in stage 2 VMSAv8-64 Block and Page descriptors' in Arm Architecture Reference Manual for A-Profile architecture [3].

## See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]
- A5.5.11 RTT entry attributes
- B3.56 RttDescriptorIsValidForUnprotected function

## B4.3.19.1.2 Context

The RMI\_RTT\_MAP\_UNPROTECTED command operates on the following context.

| Name      | Type             | Value                             | Before   | Description     |
|-----------|------------------|-----------------------------------|----------|-----------------|
| realm     | RmmRealm         | Realm(rd)                         | false    | Realm           |
| walk      | RmmRttWalkResult | RttWalk( rd, ipa, level)          | false    | RTT walk result |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)   | false    | RTTE index      |
| rtte      | RmmRttEntry      | RttEntryFromDescriptor(desc ↪ → ) | false    | RTT entry       |

## B4.3.19.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description           |
|--------|------------|--------|----------------------|-----------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status |

ID

## B4.3.19.2 Failure conditions

## Condition

```
attr_valid pre: !RttDescriptorIsValidForUnprotected(desc) post: ResultEqual(result, RMI_ERROR_INPUT) rd_align pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_bound pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_state pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT) level_bound pre: !RttLevelIsBlockOrPage(rd, level) post: ResultEqual(result, RMI_ERROR_INPUT) addr_align pre: !AddrIsRttLevelAligned(rtte.addr, level) post: ResultEqual(result, RMI_ERROR_INPUT) addr_bound pre: ((realm.feat_lpa2 == FEATURE_FALSE) && (UInt(rtte.addr) >= 2^48)) post: ResultEqual(result, RMI_ERROR_INPUT) ipa_align pre: !AddrIsRttLevelAligned(ipa, level) post: ResultEqual(result, RMI_ERROR_INPUT) ipa_bound pre: (UInt(ipa) >= (2 ^ Realm(rd).ipa_width) || AddrIsProtected(ipa, Realm(rd))) post: ResultEqual(result, RMI_ERROR_INPUT) rtt_walk pre: walk.level < level post: ResultEqual(result, RMI_ERROR_RTT, rtte_state pre: walk.rtte.state != UNASSIGNED_NS post: ResultEqual(result, RMI_ERROR_RTT,
```

## B4.3.19.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state] [level_bound, ipa_bound] < [rtt_walk,
```

```
rtte_state]
```

<!-- image -->

## B4.3.19.3 Success conditions

```
ID Condition rtte_state walk.rtte.state == ASSIGNED_NS rtte_contents (walk.rtte.MemAttr == rtte.MemAttr && walk.rtte.S2AP == rtte.S2AP && walk.rtte.addr == rtte.addr)
```

```
walk.level) walk.level)
```

## B4.3.19.4 Footprint

| ID   | Value                              |
|------|------------------------------------|
| rtte | RttEntry(walk.rtt_addr, entry_idx) |