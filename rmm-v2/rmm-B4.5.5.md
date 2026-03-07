## B4.5.5 RMI\_CMEM\_POPULATE command

Mark CMEM address range as populated.

See also:

- [A9.11 Coherent memory devices](rmm-A9.11.md)
- [B4.5.9 RMI\_CMEM\_UNPOPULATE command](rmm-B4.5.9.md)

## B4.5.5.1 Interface

## B4.5.5.1.1 Input values

| Name     | Register   | Bits   | Type    | Description             |
|----------|------------|--------|---------|-------------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC40001E7   |
| cmem_ptr | X1         | 63:0   | Address | PA of theCMEM           |
| base     | X2         | 63:0   | Address | Base of target PA range |
| top      | X3         | 63:0   | Address | Top of target PA range  |

## B4.5.5.1.2 Context

The RMI\_CMEM\_POPULATE command operates on the following context.

| Name   | Type    | Value            | Before   | Description   |
|--------|---------|------------------|----------|---------------|
| cmem   | RmmCmem | CmemAt(cmem_ptr) | false    | CMEM          |

## B4.5.5.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                                   |
|---------|------------|--------|-----------|-----------------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                                |
| out_top | X1         | 63:0   | Address   | Top PA of range which was marked as populated |


## B4.5.5.2 Failure conditions

* feat
  * pre: Rmm().static.feat_cmem_cxl != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* cmem_align
  * pre: !AddrIsRmiGranuleAligned(cmem_ptr)
  * post: result.status == RMI_ERROR_INPUT
* cmem_bound
  * pre: !PaIsTracked(cmem_ptr)
  * post: result.status == RMI_ERROR_INPUT
* cmem_gran_state
  * pre: GranuleAt(cmem_ptr).state != GRAN_CMEM
  * post: result.status == RMI_ERROR_INPUT
* cmem_state
  * pre: cmem.state != CMEM_STARTED
  * post: result.status == RMI_ERROR_DEVICE
* base_bound
  * pre: (UInt(base) < UInt(cmem.addr_range.base) || UInt(base) >
  * post: result.status == RMI_ERROR_DEVICE
* top_bound
  * pre: (UInt(top) <= UInt(base) || UInt(top) < UInt(cmem.addr_range.base) || UInt(top) > UInt(cmem.addr_range.top))
  * post: result.status == RMI_ERROR_DEVICE

## B4.5.5.2.1 Failure condition ordering

```
[cmem_gran_state] < [cmem_state, base_bound, [feat] < [cmem_align, cmem_bound, cmem_gran_state]
```

```
top_bound]
```

<!-- image -->

## B4.5.5.3 Success conditions

* pop
  * post: PaRangeIsPopulated(base, out_top)
* state
  * post: GranulesAllState( base, out_top, GRAN_UNDELEGATED)

## B4.5.5.4 Footprint

The RMI\_CMEM\_POPULATE command does not have any footprint.