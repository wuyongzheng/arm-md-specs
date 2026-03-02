## B4.5.95 RMI\_VSMMU\_CREATE command

Create a VSMMU.

The RMI\_VSMMU\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_VSMMU\_CREATE command may initiate a memory-transferring RMI Operation.

## See also:

- A9.8 Virtual SMMU
- B4.3.4 Object creation and destruction
- B4.5.96 RMI\_VSMMU\_DESTROY command

## B4.5.95.1 Interface

## B4.5.95.1.1 Input values

| Name       | Register   | Bits   | Type    | Description            |
|------------|------------|--------|---------|------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC400016A  |
| rd         | X1         | 63:0   | Address | PA of the RD           |
| vsmmu_ptr  | X2         | 63:0   | Address | PA of the VSMMU        |
| params_ptr | X3         | 63:0   | Address | PA of VSMMU parameters |

## B4.5.95.1.2 Context

The RMI\_VSMMU\_CREATE command operates on the following context.

| Name      | Type           | Value                         | Before   | Description      |
|-----------|----------------|-------------------------------|----------|------------------|
| realm_pre | RmmRealm       | RealmAt(rd)                   | true     | Realm            |
| realm     | RmmRealm       | RealmAt(rd)                   | false    | Realm            |
| vsmmu     | RmmVsmmu       | VsmmuAt(vsmmu_ptr)            | false    | VSMMU            |
| params    | RmiVsmmuParams | RmiVsmmuParamsAt( params_ptr) | false    | VSMMU parameters |

DRAFT

## B4.5.95.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.95.2 Failure conditions

Condition

ID

| feat   | pre: Rmm().static.feat_vsmmu != FEATURE_TRUE   |
|--------|------------------------------------------------|
|        | post: result.status == RMI_ERROR_NOT_SUPPORTED |

## ID

## Condition

```
DRAFT rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT realm_state pre: realm.state != REALM_NEW post: result.status == RMI_ERROR_REALM vsmmu_align pre: !AddrIsRmiGranuleAligned(vsmmu_ptr) post: result.status == RMI_ERROR_INPUT vsmmu_bound pre: !PaIsDelegableConventionalFine(vsmmu_ptr) post: result.status == RMI_ERROR_INPUT vsmmu_state pre: GranuleAt(vsmmu_ptr).state != GRAN_DELEGATED post: result.status == RMI_ERROR_INPUT params_align pre: !AddrIsRmiGranuleAligned(params_ptr) post: result.status == RMI_ERROR_INPUT params_pas pre: !NonSecureAccessPermitted(params_ptr) post: result.status == RMI_ERROR_INPUT params_valid pre: !RmiVsmmuParamsIsValid(params_ptr) post: result.status == RMI_ERROR_INPUT reg_align pre: (!AddrIsRmiGranuleAligned(params.reg_base) || !AddrIsRmiGranuleAligned(params.reg_top)) post: result.status == RMI_ERROR_INPUT reg_bound pre: (!AddrIsProtected(params.reg_base, realm) || !AddrIsProtected(params.reg_top, realm) || UInt(params.reg_top) <= UInt(params.reg_base)) post: result.status == RMI_ERROR_INPUT
```

## B4.5.95.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [realm_state] [feat] < [rd_align, rd_bound, rd_state, vsmmu_align, vsmmu_bound, vsmmu_state, params_align, params_pas, params_valid, reg_align, reg_bound]
```

<!-- image -->

## B4.5.95.3 Success conditions

```
ID Condition gran_state post: GranuleAt(vsmmu_ptr).state == GRAN_VSMMU state post: vsmmu.state == VSMMU_INACTIVE
```

<!-- image -->