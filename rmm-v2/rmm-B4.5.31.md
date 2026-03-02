## B4.5.31 RMI\_PDEV\_SET\_PUBKEY command

Provide public key associated with a PDEV.

See also:

- Chapter A9 Realm device assignment

## B4.5.31.1 Interface

## B4.5.31.1.1 Input values

| Name       | Register   | Bits   | Type    | Description              |
|------------|------------|--------|---------|--------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC400017B    |
| pdev_ptr   | X1         | 63:0   | Address | PA of the PDEV           |
| params_ptr | X2         | 63:0   | Address | PA of the key parameters |

## B4.5.31.1.2 Context

The RMI\_PDEV\_SET\_PUBKEY command operates on the following context.

| Name   | Type               | Value                             | Before   | Description           |
|--------|--------------------|-----------------------------------|----------|-----------------------|
| pdev   | RmmPdev            | PdevAt(pdev_ptr)                  | false    | PDEV                  |
| params | RmiPublicKeyParams | RmiPublicKeyParamsAt( params_ptr) | false    | Public key parameters |

## B4.5.31.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.31.2 Failure conditions

| ID              | Condition                                                                                |
|-----------------|------------------------------------------------------------------------------------------|
| feat            | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| pdev_align      | pre: !AddrIsRmiGranuleAligned(pdev_ptr) post: result.status == RMI_ERROR_INPUT           |
| pdev_bound      | pre: !PaIsTracked(pdev_ptr) post: result.status == RMI_ERROR_INPUT                       |
| pdev_gran_state | pre: GranuleAt(pdev_ptr).state != GRAN_PDEV post: result.status == RMI_ERROR_INPUT       |
| params_align    | pre: !AddrIsRmiGranuleAligned(params_ptr) post: result.status == RMI_ERROR_INPUT         |

ID

## Condition

| params_pas          | pre: post:   | !NonSecureAccessPermitted(params_ptr) result.status == RMI_ERROR_INPUT                                                 |
|---------------------|--------------|------------------------------------------------------------------------------------------------------------------------|
| key_len_oflow       | pre: post:   | params.key_len > 1024 result.status == RMI_ERROR_INPUT                                                                 |
| metadata_len_of low | pre: post:   | params.metadata_len > 1024 result.status == RMI_ERROR_INPUT                                                            |
| key_invalid         | pre:         | Key is invalid, for example length is invalid for specified signature algorithm.                                       |
| metadata_invali d   | pre: post:   | Metadata is invalid, for example length is invalid for specified signature algorithm. result.status == RMI_ERROR_INPUT |
| pdev_state          | pre: post:   | pdev.state != PDEV_NEEDS_KEY result.status == RMI_ERROR_DEVICE                                                         |

## B4.5.31.2.1 Failure condition ordering

```
[feat] < [pdev_align, pdev_bound, pdev_gran_state, params_pas, key_len_oflow, key_invalid, metadata_invalid] [pdev_gran_state] < [pdev_state]
```

<!-- image -->

## B4.5.31.3 Success conditions

```
params_align, metadata_len_oflow,
```

## Condition

ID

state comm\_state

post:

pdev.state

==

PDEV\_HAS\_KEY

post: pdev.comm\_state == DEV\_COMM\_PENDING

## B4.5.31.4 Footprint

| ID         | Value           |
|------------|-----------------|
| state      | pdev.state      |
| comm_state | pdev.comm_state |