## B4.5.7 RMI\_CMEM\_START command

Start a CMEM.

See also:

- A9.11 Coherent memory devices
- B4.5.8 RMI\_CMEM\_STOP command

## B4.5.7.1 Interface

## B4.5.7.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC40001E9 |
| cmem_ptr | X1         | 63:0   | Address | PA of theCMEM         |

## B4.5.7.1.2 Context

The RMI\_CMEM\_START command operates on the following context.

| Name   | Type      | Value            | Before   | Description     |
|--------|-----------|------------------|----------|-----------------|
| rmm    | RmmGlobal | Rmm()            | false    | RMMglobal state |
| cmem   | RmmCmem   | CmemAt(cmem_ptr) | false    | CMEM            |

## B4.5.7.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

DRAFT

## B4.5.7.2 Failure conditions

| ID              | Condition                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------|
| feat            | pre: Rmm().static.feat_cmem_cxl != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| live            | pre: rmm.dynamic.num_realms != 0 post: result.status == RMI_ERROR_GLOBAL                       |
| cmem_align      | pre: !AddrIsRmiGranuleAligned(cmem_ptr) post: result.status == RMI_ERROR_INPUT                 |
| cmem_bound      | pre: !PaIsTracked(cmem_ptr) post: result.status == RMI_ERROR_INPUT                             |
| cmem_gran_state | pre: GranuleAt(cmem_ptr).state != GRAN_CMEM post: result.status == RMI_ERROR_INPUT             |
| cmem_state      | pre: cmem.state != CMEM_STOPPED post: result.status == RMI_ERROR_DEVICE                        |

ID

## Condition

```
cmem_pdev cmem.ilv_ways
```

```
pre: CmemNumPdevs(cmem) != post: result.status == RMI_ERROR_DEVICE
```

## B4.5.7.2.1 Failure condition ordering

```
[cmem_gran_state] < [cmem_state, cmem_pdev] [feat] < [live] [feat] < [cmem_align, cmem_bound, cmem_gran_state]
```

<!-- image -->

## B4.5.7.3 Success conditions

| ID        | Condition                                |
|-----------|------------------------------------------|
| state     | post: cmem.state == CMEM_STARTED         |
| pat_valid | post: rmm.dynamic.pat_valid == RMM_FALSE |

I0074

DRAFT

Following successful execution of RMI\_CMEM\_START, the number of MECs supported by the platform (reported by RMI\_FEATURES) may change.

See also:

- Chapter A11 Realm memory encryption

## B4.5.7.4 Footprint

| ID        | Value                 |
|-----------|-----------------------|
| state     | cmem.state            |
| pat_valid | rmm.dynamic.pat_valid |