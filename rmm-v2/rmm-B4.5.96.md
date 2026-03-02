## B4.5.96 RMI\_VSMMU\_DESTROY command

Destroy a VSMMU.

The RMI\_VSMMU\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_VSMMU\_DESTROY command may initiate a memory-transferring RMI Operation.

## See also:

- A9.8 Virtual SMMU
- B4.3.4 Object creation and destruction
- B4.5.95 RMI\_VSMMU\_CREATE command

## B4.5.96.1 Interface

## B4.5.96.1.1 Input values

| Name      | Register   | Bits   | Type    | Description           |
|-----------|------------|--------|---------|-----------------------|
| fid       | X0         | 63:0   | UInt64  | FID, value 0xC400016B |
| rd        | X1         | 63:0   | Address | PA of the RD          |
| vsmmu_ptr | X2         | 63:0   | Address | PA of the VSMMU       |

## B4.5.96.1.2 Context

The RMI\_VSMMU\_DESTROY command operates on the following context.

<!-- image -->


| Name      | Type     | Value              | Before   | Description   |
|-----------|----------|--------------------|----------|---------------|
| realm_pre | RmmRealm | RealmAt(rd)        | true     | Realm         |
| realm     | RmmRealm | RealmAt(rd)        | false    | Realm         |
| vsmmu     | RmmVsmmu | VsmmuAt(vsmmu_ptr) | false    | VSMMU         |

## B4.5.96.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.96.2 Failure conditions

| ID       | Condition                                                                                   |
|----------|---------------------------------------------------------------------------------------------|
| feat     | pre: Rmm().static.feat_vsmmu != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| rd_align | pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT                    |
| rd_bound | pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT                                |

## ID

## Condition

```
rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT vsmmu_align pre: !AddrIsRmiGranuleAligned(vsmmu_ptr) post: result.status == RMI_ERROR_INPUT vsmmu_tracking pre: !PaIsTrackedFine(vsmmu_ptr) post: result.status == RMI_ERROR_INPUT vsmmu_state pre: GranuleAt(vsmmu_ptr).state != GRAN_VSMMU post: result.status == RMI_ERROR_INPUT vsmmu_live pre: VsmmuIsLive(vsmmu_ptr) post: result.status == RMI_ERROR_DEVICE
```

## B4.5.96.2.1 Failure condition ordering

```
[vsmmu_tracking, vsmmu_state] < [vsmmu_live]
```

<!-- image -->

## B4.5.96.3 Success conditions

## Condition

## ID

```
gran_state post: GranuleAt(vsmmu_ptr).state == GRAN_DELEGATED num_vsmmus post: realm.num_vsmmus == realm_pre.num_vsmmus - 1
```

## B4.5.96.4 Footprint

## Value

GranuleAt(vsmmu\_ptr).state realm.num\_vsmmus


## ID

state num\_vsmmus