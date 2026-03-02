## B4.3.18 RMI\_RTT\_INIT\_RIPAS command

Set the RIPAS of a target IPA range to RAM, for a Realm in the REALM\_NEW state.

See also:

- A5.2.2 Realm IPA state
- D1.2.3 Initialize memory of New Realm flow

## B4.3.18.1 Interface

## B4.3.18.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                       |
|--------|------------|--------|---------|-----------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000168             |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm |
| base   | X2         | 63:0   | Address | Base of target IPA region         |
| top    | X3         | 63:0   | Address | Top of target IPA region          |

## B4.3.18.1.2 Context

The RMI\_RTT\_INIT\_RIPAS command operates on the following context.

| Name     | Type             | Value                                                                      | Before   | Description                                                                                                 |
|----------|------------------|----------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------|
| realm    | RmmRealm         | Realm(rd)                                                                  | true     | Realm                                                                                                       |
| walk     | RmmRttWalkResult | RttWalk(rd, base, RMM_RTT_PAGE_LEVEL)                                      | false    | RTT walk result                                                                                             |
| walk_top | Address          | RttSkipEntriesWithRipas( Rtt(walk.rtt_addr), walk.level, base, top, FALSE) | false    | Top IPA of entries which have associated RIPAS values, starting from entry at which the RTT walk terminated |

## B4.3.18.1.3 Output values

| Name    | Register   | Bits   | Type                 | Description                               |
|---------|------------|--------|----------------------|-------------------------------------------|
| result  | X0         | 63:0   | RmiCommandReturnCode | Command return status                     |
| out_top | X1         | 63:0   | Address              | Top IPA of range whose RIPAS was modified |

The out\_top output value is valid only when the command result is RMI\_SUCCESS.

When the out\_top output value is valid, it is aligned to the size of the address range described by the RTT entry at the level where the RTT walk terminated.

## ID

## B4.3.18.2 Failure conditions

## Condition

```
rd_align pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_bound pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_state pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT) size_valid pre: UInt(top) <= UInt(base) post: ResultEqual(result, RMI_ERROR_INPUT) top_bound pre: !AddrIsProtected( ToAddress(UInt(top) -RMM_GRANULE_SIZE), realm) post: ResultEqual(result, RMI_ERROR_INPUT) realm_state pre: realm.state != REALM_NEW post: ResultEqual(result, RMI_ERROR_REALM) base_align pre: !AddrIsRttLevelAligned(base, walk.level) post: ResultEqual(result, RMI_ERROR_RTT, walk.level) rtte_state pre: walk.rtte.state != UNASSIGNED post: ResultEqual(result, RMI_ERROR_RTT, walk.level) top_gran_align pre: !AddrIsGranuleAligned(top) post: ResultEqual(result, RMI_ERROR_INPUT) no_progress pre: UInt(base) == UInt(walk_top) post: ResultEqual(result, RMI_ERROR_RTT, walk.level)
```

## B4.3.18.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [realm_state] [rd_bound, rd_state] < [base_align, rtte_state] [rd_bound, rd_state] < [no_progress] [top_gran_align] < [no_progress]
```

<!-- image -->

## B4.3.18.3 Success conditions

ID

## Condition

```
rtte_ripas RttEntriesInRangeRipas( Rtt(walk.rtt_addr), walk.level, base, walk_top, RAM) rim Realm(rd).measurements[0] == realm, base, walk_top, walk.level) out_top out_top == walk_top
```

```
RimExtendRipas(
```

## B4.3.18.4 RMI\_RTT\_INIT\_RIPAS extension of RIM

On successful execution of RMI\_RTT\_INIT\_RIPAS, the new RIM value of the target Realm is calculated by the RMMas follows:

1. Allocate an RmmMeasurementDescriptorRipas data structure.
2. For each RTT entry in the range [base, top) described by the RMI\_RTT\_INIT\_RIPAS input values:
- a. Populate the measurement descriptor:
- Set the desc\_type field to the descriptor type.
- Set the len field to the descriptor length.
- Set the base field to the IPA of the RTT entry.
- Set the top field to Min(ipa + size, top) , where
8. -ipa is the IPA of the RTT entry
9. -size is the size in bytes of the IPA region described by the RTT entry
10. -top is the input value provided to the command
- b. Using the RHA of the target Realm, compute the hash of the measurement descriptor. Set the RIM of the target Realm to this value, zero filling upper bytes if the RHA output is smaller than the size of the RIM.

## See also:

- A7.1.1 Realm Initial Measurement
- B3.46 RimExtendRipas function
- C1.13 RmmMeasurementDescriptorRipas type

## B4.3.18.5 Footprint

| ID   | Value                     |
|------|---------------------------|
| rtte | Rtt(walk.rtt_addr)        |
| rim  | Realm(rd).measurements[0] |