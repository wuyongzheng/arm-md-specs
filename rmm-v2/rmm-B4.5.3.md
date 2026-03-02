## B4.5.3 RMI\_CMEM\_CREATE command

Create a CMEM.

The RMI\_CMEM\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_CMEM\_CREATE command may initiate a memory-transferring RMI Operation.

## See also:

- A9.11 Coherent memory devices
- B4.3.4 Object creation and destruction
- B4.5.4 RMI\_CMEM\_DESTROY command

## B4.5.3.1 Interface

## B4.5.3.1.1 Input values

| Name       | Register   | Bits   | Type    | Description           |
|------------|------------|--------|---------|-----------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC40001E5 |
| cmem_ptr   | X1         | 63:0   | Address | PA of theCMEM         |
| params_ptr | X2         | 63:0   | Address | PA of CMEMparameters  |

## B4.5.3.1.2 Context

The RMI\_CMEM\_CREATE command operates on the following context.

| Name   | Type          | Value            | Before   | Description    |
|--------|---------------|------------------|----------|----------------|
| cmem   | RmmCmem       | CmemAt(cmem_ptr) | false    | CMEM           |
| params | RmiCmemParams | RmiCmemParamsAt( | false    | CMEMparameters |

DRAFT

## B4.5.3.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.3.2 Failure conditions

| ID         | Condition                                                                                      |
|------------|------------------------------------------------------------------------------------------------|
| feat       | pre: Rmm().static.feat_cmem_cxl != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| cmem_align | pre: !AddrIsRmiGranuleAligned(cmem_ptr) post: result.status == RMI_ERROR_INPUT                 |
| cmem_bound | pre: !PaIsDelegableConventionalFine(cmem_ptr) post: result.status == RMI_ERROR_INPUT           |

ID

## Condition

```
cmem_state pre: GranuleAt(cmem_ptr).state != GRAN_DELEGATED post: result.status == RMI_ERROR_INPUT params_align pre: !AddrIsRmiGranuleAligned(params_ptr) post: result.status == RMI_ERROR_INPUT params_pas pre: !NonSecureAccessPermitted(params_ptr) post: result.status == RMI_ERROR_INPUT params_valid pre: !RmiCmemParamsIsValid(params_ptr) post: result.status == RMI_ERROR_INPUT flags_supp pre: !RmiCmemFlagsSupported(params.flags) post: result.status == RMI_ERROR_INPUT hb_hdm_dec pre: !HdmDecoderIsFree(cmem, params.hb_hdm_id) post: result.status == RMI_ERROR_DEVICE hb_addr_range pre: !HdmAddressRangeIsFree(cmem, params.addr_range) post: result.status == RMI_ERROR_DEVICE
```

## B4.5.3.2.1 Failure condition ordering

```
[feat] < [cmem_align, cmem_bound, cmem_state, params_align, params_pas, params_valid, flags_supp]
```

<!-- image -->

## B4.5.3.3 Success conditions

DRAFT

```
ID Condition gran_state post: GranuleAt(cmem_ptr).state == GRAN_CMEM chbcr_addr post: cmem.chbcr_addr == params.chbcr_addr hb_hdm_id post: cmem.hb_hdm_id == params.hb_hdm_id addr_range post: RmiAddrRangesEqual(cmem.addr_range, params.addr_range) ilv_gran post: cmem.ilv_gran == params.ilv_gran ilv_ways post: cmem.ilv_ways == params.ilv_ways state post: cmem.state == CMEM_STOPPED num_pdevs post: CmemNumPdevs(cmem) == 0 hb_hdm_dec post: !HdmDecoderIsFree(cmem, params.hb_hdm_id) hb_addr_range post: !HdmAddressRangeIsFree(cmem, params.addr_range)
```

## B4.5.3.4 Footprint

| ID    | Value      |
|-------|------------|
| state | cmem.state |

<!-- image -->