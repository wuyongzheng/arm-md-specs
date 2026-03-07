## B4.5.2 RMI\_CMEM\_ADD\_PDEV command

Establishes a binding between a CMEM and a PDEV.

See also:

- [A9.11 Coherent memory devices](rmm-A9.11.md)
- [B4.5.6 RMI\_CMEM\_REMOVE\_PDEV command](rmm-B4.5.6.md)

## B4.5.2.1 Interface

## B4.5.2.1.1 Input values

| Name       | Register   | Bits   | Type    | Description                |
|------------|------------|--------|---------|----------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC40001E4      |
| cmem_ptr   | X1         | 63:0   | Address | PA of theCMEM              |
| pdev_ptr   | X2         | 63:0   | Address | PA of the PDEV             |
| index      | X3         | 63:0   | UInt64  | Index of PDEV              |
| params_ptr | X4         | 63:0   | Address | PA of CMEM_PDEV parameters |

## B4.5.2.1.2 Context

The RMI\_CMEM\_ADD\_PDEV command operates on the following context.

| Name     | Type              | Value Before                           | Description          |
|----------|-------------------|----------------------------------------|----------------------|
| cmem     | RmmCmem           | CmemAt(cmem_ptr) false                 | CMEM                 |
| pdev_pre | RmmPdev           | PdevAt(pdev_ptr) true                  | PDEV                 |
| pdev     | RmmPdev           | PdevAt(pdev_ptr) false                 | PDEV                 |
| params   | RmiCmemPdevParams | RmiCmemPdevParamsAt( params_ptr) false | CMEM_PDEV parameters |


## B4.5.2.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.2.2 Failure conditions

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
* pdev_align
  * pre: !AddrIsRmiGranuleAligned(pdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_bound
  * pre: !PaIsTracked(pdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_gran_state
  * pre: GranuleAt(pdev_ptr).state != GRAN_PDEV
  * post: result.status == RMI_ERROR_INPUT
* index_bound
  * pre: index >= cmem.ilv_ways
  * post: result.status == RMI_ERROR_INPUT
* pdev_state
  * pre: pdev.state != PDEV_READY
  * post: result.status == RMI_ERROR_DEVICE
* pdev_category
  * pre: pdev.category != PDEV_ENDPOINT_CMEM
  * post: result.status == RMI_ERROR_DEVICE
* tse
  * pre: (Rmm().static.feat_cmem_tse_req == FEATURE_TRUE && pdev.feat_tse != FEATURE_TRUE)
  * post: result.status == RMI_ERROR_DEVICE
* dev_hdm_dec
  * pre: !HdmDecoderIsFree(pdev, params.dev_hdm_id)
  * post: result.status == RMI_ERROR_DEVICE
* cmem_state
  * pre: cmem.state != CMEM_STOPPED
  * post: result.status == RMI_ERROR_DEVICE
* index_free
  * pre: cmem.pdev[[index]].valid != RMM_FALSE
  * post: result.status == RMI_ERROR_DEVICE
* pdev_attr
  * pre: PDEV attributes are not consistent with CMEM attributes.
  * post: result.status == RMI_ERROR_DEVICE
* cxl_attr
  * pre: Parameters are not consistent with CMEM attributes.
  * post: result.status == RMI_ERROR_DEVICE

## B4.5.2.2.1 Failure condition ordering

```
[cmem_gran_state] < [cmem_state, index_free] [pdev_gran_state] < [pdev_state, pdev_category] [cmem_gran_state, pdev_gran_state] < [pdev_attr, cxl_attr] [feat] < [cmem_align, cmem_bound, cmem_gran_state, pdev_align, pdev_bound, pdev_gran_state, index_bound]
```

<!-- image -->

## B4.5.2.3 Success conditions

* pdev_valid
  * post: cmem.pdev[[index]].valid == RMM_TRUE
* pdev_addr
  * post: cmem.pdev[[index]].pdev_addr == pdev_ptr
* pdev_id
  * post: cmem.pdev[[index]].dev_hdm_id == params.dev_hdm_id
* dev_hdm_dec
  * post: !HdmDecoderIsFree(pdev, params.dev_hdm_id)
* cmem_count
  * post: pdev.cmem_count == pdev_pre.cmem_count + 1

## B4.5.2.4 Footprint

| ID         | Value              |
|------------|--------------------|
| pdev       | cmem.pdev[[index]] |
| cmem_count | pdev.cmem_count    |

<!-- image -->