## B4.5.2 RMI\_CMEM\_ADD\_PDEV command

Establishes a binding between a CMEM and a PDEV.

See also:

- A9.11 Coherent memory devices
- B4.5.6 RMI\_CMEM\_REMOVE\_PDEV command

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

DRAFT

## B4.5.2.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.2.2 Failure conditions

| ID         | Condition                                                                                      |
|------------|------------------------------------------------------------------------------------------------|
| feat       | pre: Rmm().static.feat_cmem_cxl != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| cmem_align | pre: !AddrIsRmiGranuleAligned(cmem_ptr) post: result.status == RMI_ERROR_INPUT                 |

ID

## Condition

| cmem_bound      | pre: post:   | !PaIsTracked(cmem_ptr) result.status == RMI_ERROR_INPUT                                                             |
|-----------------|--------------|---------------------------------------------------------------------------------------------------------------------|
| cmem_gran_state | pre: post:   | GranuleAt(cmem_ptr).state != GRAN_CMEM result.status == RMI_ERROR_INPUT                                             |
| pdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(pdev_ptr) result.status == RMI_ERROR_INPUT                                                 |
| pdev_bound      | pre: post:   | !PaIsTracked(pdev_ptr) result.status == RMI_ERROR_INPUT                                                             |
| pdev_gran_state | pre: post:   | GranuleAt(pdev_ptr).state != GRAN_PDEV result.status == RMI_ERROR_INPUT                                             |
| index_bound     | pre: post:   | index >= cmem.ilv_ways result.status == RMI_ERROR_INPUT                                                             |
| pdev_state      | pre: post:   | pdev.state != PDEV_READY result.status == RMI_ERROR_DEVICE                                                          |
| pdev_category   | pre: post:   | pdev.category != PDEV_ENDPOINT_CMEM result.status == RMI_ERROR_DEVICE                                               |
| tse             | pre: post:   | (Rmm().static.feat_cmem_tse_req == FEATURE_TRUE && pdev.feat_tse != FEATURE_TRUE) result.status == RMI_ERROR_DEVICE |
| dev_hdm_dec     | pre: post:   | !HdmDecoderIsFree(pdev, params.dev_hdm_id) result.status == RMI_ERROR_DEVICE                                        |
| cmem_state      | pre: post:   | cmem.state != CMEM_STOPPED result.status == RMI_ERROR_DEVICE                                                        |
| index_free      | pre: post:   | DRAFT cmem.pdev[[index]].valid != RMM_FALSE result.status == RMI_ERROR_DEVICE                                       |
| pdev_attr       | pre: post:   | PDEV attributes are not consistent with CMEM attributes. result.status == RMI_ERROR_DEVICE                          |
| cxl_attr        | pre: post:   | Parameters are not consistent with CMEM attributes. result.status == RMI_ERROR_DEVICE                               |

## B4.5.2.2.1 Failure condition ordering

```
[cmem_gran_state] < [cmem_state, index_free] [pdev_gran_state] < [pdev_state, pdev_category] [cmem_gran_state, pdev_gran_state] < [pdev_attr, cxl_attr] [feat] < [cmem_align, cmem_bound, cmem_gran_state, pdev_align, pdev_bound, pdev_gran_state, index_bound]
```

<!-- image -->

## B4.5.2.3 Success conditions

| ID          | Condition                                                |
|-------------|----------------------------------------------------------|
| pdev_valid  | post: cmem.pdev[[index]].valid == RMM_TRUE               |
| pdev_addr   | post: cmem.pdev[[index]].pdev_addr == pdev_ptr           |
| pdev_id     | post: cmem.pdev[[index]].dev_hdm_id == params.dev_hdm_id |
| dev_hdm_dec | post: !HdmDecoderIsFree(pdev, params.dev_hdm_id)         |
| cmem_count  | post: pdev.cmem_count == pdev_pre.cmem_count + 1         |

## B4.5.2.4 Footprint

| ID         | Value              |
|------------|--------------------|
| pdev       | cmem.pdev[[index]] |
| cmem_count | pdev.cmem_count    |

<!-- image -->