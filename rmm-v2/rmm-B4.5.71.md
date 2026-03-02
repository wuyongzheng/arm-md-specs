## B4.5.71 RMI\_RTT\_DEV\_VALIDATE command

Completes a request made by the Realm to validate mappings to device memory from a target IPA range.

The RMI\_RTT\_DEV\_VALIDATE command may initiate a Stateful RMI Operation.

## See also:

- A5.5 VDEV mapping validation
- A9.6.2 Realm validation of device memory mappings
- B4.3.5 Range RMI operations

## B4.5.71.1 Interface

## B4.5.71.1.1 Input values

| Name     | Register   | Bits   | Type    | Description                       |
|----------|------------|--------|---------|-----------------------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000163             |
| rd       | X1         | 63:0   | Address | PA of the RD for the target Realm |
| rec_ptr  | X2         | 63:0   | Address | PA of the target REC              |
| pdev_ptr | X3         | 63:0   | Address | PA of the PDEV                    |
| vdev_ptr | X4         | 63:0   | Address | PA of the VDEV                    |
| base     | X5         | 63:0   | Address | Base of target IPA region         |
| top      | X6         | 63:0   | Address | Top of target IPA region          |

## B4.5.71.1.2 Context

The RMI\_RTT\_DEV\_VALIDATE command operates on the following context.

| Name         | Type             | Value                                                                        | Before   | Description                                                                                                 |
|--------------|------------------|------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------|
| realm        | RmmRealm         | RealmAt(rd)                                                                  | false    | Realm                                                                                                       |
| realm_pre    | RmmRealm         | RealmAt(rd)                                                                  | true     | Realm                                                                                                       |
| rec          | RmmRec           | RecAt(rec_ptr)                                                               | false    | REC                                                                                                         |
| pdev         | RmmPdev          | PdevAt(pdev_ptr)                                                             | false    | PDEV                                                                                                        |
| vdev         | RmmVdev          | VdevAt(vdev_ptr)                                                             | false    | VDEV                                                                                                        |
| pa_pre       | Address          | rec.dev_mem_pa                                                               | true     | Output base address                                                                                         |
| walk         | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY)              | false    | RTT walk result                                                                                             |
| walk_top_pre | Address          | RttSkipEntriesWithRipas( RttAt(walk.rtt_addr), walk.level, base, top, FALSE) | true     | Top IPA of entries which have associated RIPAS values, starting from entry at which the RTT walk terminated |

DRAFT

## B4.5.71.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                               |
|---------|------------|--------|-----------|-------------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                            |
| out_top | X1         | 63:0   | Address   | Top IPA of range whose RIPAS was modified |

The out\_top output value is valid only when the command result is RMI\_SUCCESS.

## B4.5.71.2 Failure conditions

## ID Condition

| rd_align        | pre: post:   | !AddrIsRmiGranuleAligned(rd) result.status == RMI_ERROR_INPUT               |
|-----------------|--------------|-----------------------------------------------------------------------------|
| rd_bound        | pre: post:   | !PaIsTracked(rd) result.status == RMI_ERROR_INPUT                           |
| rd_state        | pre: post:   | GranuleAt(rd).state != GRAN_RD result.status == RMI_ERROR_INPUT             |
| rec_align       | pre: post:   | !AddrIsRmiGranuleAligned(rec_ptr) result.status == RMI_ERROR_INPUT          |
| rec_bound       | pre: post:   | !PaIsTracked(rec_ptr) result.status == RMI_ERROR_INPUT                      |
| rec_gran_state  | pre: post:   | DRAFT GranuleAt(rec_ptr).state != GRAN_REC result.status == RMI_ERROR_INPUT |
| rec_state       | pre: post:   | rec.state == REC_RUNNING result.status == RMI_ERROR_REC                     |
| rec_owner       | pre: post:   | rec.owner != rd result.status == RMI_ERROR_REC                              |
| pdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(pdev_ptr) result.status == RMI_ERROR_INPUT         |
| pdev_bound      | pre: post:   | !PaIsTracked(pdev_ptr) result.status == RMI_ERROR_INPUT                     |
| pdev_gran_state | pre: post:   | GranuleAt(pdev_ptr).state != GRAN_PDEV result.status == RMI_ERROR_INPUT     |
| vdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(vdev_ptr) result.status == RMI_ERROR_INPUT         |
| vdev_bound      | pre: post:   | !PaIsTracked(vdev_ptr) result.status == RMI_ERROR_INPUT                     |
| vdev_gran_state | pre: post:   | GranuleAt(vdev_ptr).state != GRAN_VDEV result.status == RMI_ERROR_INPUT     |
| vdev_pdev       | pre: post:   | vdev.pdev != pdev_ptr result.status == RMI_ERROR_DEVICE                     |
| size_valid      | pre: post:   | UInt(top) <= UInt(base) result.status == RMI_ERROR_INPUT                    |
| base_bound      | pre: post:   | base != rec.dev_mem_addr result.status == RMI_ERROR_INPUT                   |

```
ID Condition
```

```
DRAFT top_bound pre: UInt(top) > UInt(rec.dev_mem_top) post: result.status == RMI_ERROR_INPUT base_align pre: !AddrIsRttLevelAligned(base, walk.level) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) top_gran_align pre: !AddrIsRmiGranuleAligned(top) post: result.status == RMI_ERROR_INPUT no_progress pre: UInt(base) == UInt(walk_top_pre) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) ncoh_attr pre: (rec.dev_mem_flags.coh == DEV_MEM_NON_COHERENT && !RttEntriesInRangeMemAttr( RttAt(walk.rtt_addr), walk.level, base, walk_top_pre, MEMATTR_NON_CACHEABLE)) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) ncoh_pa pre: (rec.dev_mem_flags.coh == DEV_MEM_NON_COHERENT && !RttEntriesInRangeNonCohDevMem( RttAt(walk.rtt_addr), walk.level, base, walk_top_pre)) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) coh_attr pre: (rec.dev_mem_flags.coh == DEV_MEM_COHERENT && !RttEntriesInRangeMemAttr( RttAt(walk.rtt_addr), walk.level, base, walk_top_pre, MEMATTR_PASSTHROUGH)) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) coh_pa pre: (rec.dev_mem_flags.coh == DEV_MEM_COHERENT && !RttEntriesInRangeCohDevMem( RttAt(walk.rtt_addr), walk.level, base, walk_top_pre)) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) linear_map pre: !RttEntriesInRangeOutputContiguous( RttAt(walk.rtt_addr), walk.level, base, walk_top_pre, rec.dev_mem_pa) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) aux_live pre: AddrRangeIsAuxLive(base, top, realm_pre) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
```

## B4.5.71.2.1 Failure condition ordering

## ID

```
[rd_bound, rd_state] < [base_align] [rd_bound, rd_state] < [no_progress] [rec_bound, rec_gran_state] < [rec_state, rec_owner] [pdev_bound, pdev_gran_state, vdev_bound, vdev_gran_state] < [vdev_pdev] [base_bound] < [base_align] [top_gran_align] < [no_progress]
```

<!-- image -->

## B4.5.71.3 Success conditions

## Condition

```
rtte_ripas post: RttEntriesInRangeRipas( RttAt(walk.rtt_addr), walk.level, base, walk_top_pre, RIPAS_DEV) dev_mem_addr post: rec.dev_mem_addr == MinAddress(top, walk_top_pre) dev_mem_pa post: rec.dev_mem_pa == ToAddress( UInt(pa_pre) + (UInt(walk_top_pre) -out_top post: out_top == MinAddress(top, walk_top_pre)
```

## B4.5.71.4 Footprint

## Value

## ID

| rtte         | RttAt(walk.rtt_addr)   |
|--------------|------------------------|
| dev_mem_addr | rec.dev_mem_addr       |
| dev_mem_pa   | rec.dev_mem_pa         |

```
DRAFT UInt(base)))
```