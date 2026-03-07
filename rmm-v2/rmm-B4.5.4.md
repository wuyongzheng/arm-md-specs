## B4.5.4 RMI\_CMEM\_DESTROY command

Destroy a CMEM.

The RMI\_CMEM\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_CMEM\_DESTROY command may initiate a memory-transferring RMI Operation.

## See also:

- A9.11 Coherent memory devices
- B4.3.4 Object creation and destruction
- B4.5.3 RMI\_CMEM\_CREATE command

## B4.5.4.1 Interface

## B4.5.4.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC40001E6 |
| cmem_ptr | X1         | 63:0   | Address | PA of theCMEM         |

## B4.5.4.1.2 Context

The RMI\_CMEM\_DESTROY command operates on the following context.

| Name     | Type    | Value            | Before   | Description   |
|----------|---------|------------------|----------|---------------|
| cmem_pre | RmmCmem | CmemAt(cmem_ptr) | true     | CMEM          |

## B4.5.4.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.4.2 Failure conditions

* feat
  * pre: Rmm().static.feat_cmem_cxl != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* cmem_align
  * pre: !AddrIsRmiGranuleAligned(cmem_ptr)
  * post: result.status == RMI_ERROR_INPUT
* cmem_tracking
  * pre: !PaIsTrackedFine(cmem_ptr)
  * post: result.status == RMI_ERROR_INPUT
* cmem_gran_state
  * pre: GranuleAt(cmem_ptr).state != GRAN_CMEM
  * post: result.status == RMI_ERROR_INPUT
* cmem_state
  * pre: cmem_pre.state != CMEM_STOPPED
  * post: result.status == RMI_ERROR_DEVICE
* cmem_pdev
  * pre: CmemNumPdevs(cmem_pre) != 0
  * post: result.status == RMI_ERROR_DEVICE

## B4.5.4.2.1 Failure condition ordering

```
[cmem_gran_state] < [cmem_state] [feat] < [cmem_align, cmem_tracking, cmem_gran_state,
```

cmem\_state]

<!-- image -->

## B4.5.4.3 Success conditions

* gran_state
  * post: GranuleAt(cmem_ptr).state == GRAN_DELEGATED
* hb_hdm_dec
  * post: HdmDecoderIsFree(cmem_pre, cmem_pre.hb_hdm_id)
* hb_addr_range
  * post: HdmAddressRangeIsFree(cmem_pre, cmem_pre.addr_range)

## B4.5.4.4 Footprint

| ID    | Value                     |
|-------|---------------------------|
| state | GranuleAt(cmem_ptr).state |