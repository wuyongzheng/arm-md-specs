## B4.5.27 RMI\_PDEV\_CREATE command

Create a PDEV.

The RMI\_PDEV\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_PDEV\_CREATE command may initiate a memory-transferring RMI Operation.

## See also:

- Chapter A9 Realm device assignment
- A9.2.2 Physical device invariants
- B4.3.4 Object creation and destruction

## B4.5.27.1 Interface

## B4.5.27.1.1 Input values

| Name       | Register   | Bits   | Type    | Description           |
|------------|------------|--------|---------|-----------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC4000176 |
| pdev_ptr   | X1         | 63:0   | Address | PA of the PDEV        |
| params_ptr | X2         | 63:0   | Address | PA of PDEV parameters |

## B4.5.27.1.2 Context

The RMI\_PDEV\_CREATE command operates on the following context.

| Name   | Type          | Value            | Before   | Description     |
|--------|---------------|------------------|----------|-----------------|
| rmm    | RmmGlobal     | Rmm()            | false    | RMMglobal state |
| pdev   | RmmPdev       | PdevAt(pdev_ptr) | false    | PDEV            |
| params | RmiPdevParams | RmiPdevParamsAt( | false    | PDEV parameters |


## B4.5.27.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.27.2 Failure conditions

| ID         | Condition                                                                                |
|------------|------------------------------------------------------------------------------------------|
| feat       | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| pdev_align | pre: !AddrIsRmiGranuleAligned(pdev_ptr) post: result.status == RMI_ERROR_INPUT           |
| pdev_bound | pre: !PaIsDelegableConventionalFine(pdev_ptr) post: result.status == RMI_ERROR_INPUT     |

ID

## Condition

```
pdev_state pre: GranuleAt(pdev_ptr).state != GRAN_DELEGATED post: result.status == RMI_ERROR_INPUT params_align pre: !AddrIsRmiGranuleAligned(params_ptr) post: result.status == RMI_ERROR_INPUT params_pas pre: !NonSecureAccessPermitted(params_ptr) post: result.status == RMI_ERROR_INPUT params_valid pre: !RmiPdevParamsIsValid(params_ptr) post: result.status == RMI_ERROR_INPUT flags_supp pre: !RmiPdevFlagsSupported(params.flags) post: result.status == RMI_ERROR_INPUT max_num_vdevs pre: params.max_vdevs_order > post: result.status == RMI_ERROR_INPUT
```

## B4.5.27.2.1 Failure condition ordering

```
[feat] params_align,
```

```
< [pdev_align, pdev_bound, pdev_state, params_pas, params_valid, flags_supp]
```

<!-- image -->

## B4.5.27.3 Success conditions

```
ID Condition gran_state post: GranuleAt(pdev_ptr).state == GRAN_PDEV category post: Equal(pdev.category, params.flags.category) pdev_id post: pdev.pdev_id == params.pdev_id routing_id post: pdev.routing_id == params.routing_id rid_base post: pdev.rid_base == params.rid_base rid_top post: pdev.rid_top == params.rid_top id_index post: pdev.id_index == params.id_index hash_algo post: Equal(pdev.hash_algo, params.hash_algo) spdm post: Equal(pdev.spdm, params.flags.spdm) state post: pdev.state == PDEV_NEW op post: pdev.op == PDEV_OP_NONE comm_state post: pdev.comm_state == DEV_COMM_PENDING max_num_vdevs post: pdev.max_num_vdevs == (2 ^ params.max_vdevs_order) -1 num_vdevs post: pdev.num_vdevs == 0
```


```
rmm.static.max_vdevs_order
```

```
ID Condition params.flags.p2p)
```

```
p2p_enabled post: Equal(pdev.p2p_enabled, pdev_stream_live post: !PdevStreamLive(pdev) cmem_count post: pdev.cmem_count == 0
```

## B4.5.27.4 Footprint

| ID    | Value                     |
|-------|---------------------------|
| state | GranuleAt(pdev_ptr).state |

<!-- image -->