## B4.5.99 RMI\_VSMMU\_FEATURES command

Returns VSMMU features supporte by the RMM.

## B4.5.99.1 Interface

## B4.5.99.1.1 Input values

| Name         | Register   | Bits   | Type    | Description                        |
|--------------|------------|--------|---------|------------------------------------|
| fid          | X0         | 63:0   | UInt64  | FID, value 0xC400020B              |
| features_ptr | X1         | 63:0   | Address | PA of the VSMMU features structure |

## B4.5.99.1.2 Context

The RMI\_VSMMU\_FEATURES command operates on the following context.

| Name     | Type             | Value                              | Before   | Description    |
|----------|------------------|------------------------------------|----------|----------------|
| features | RmiVsmmuFeatures | VsmmuFeaturesAt( ↪ → features_ptr) | false    | VSMMU features |

## B4.5.99.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.99.2 Failure conditions

| ID             | Condition                                                                           |
|----------------|-------------------------------------------------------------------------------------|
| features_align | pre: !AddrIsAligned(features_ptr, 0x100) post: result.status == RMI_ERROR_INPUT     |
| features_pas   | pre: !NonSecureAccessPermitted(features_ptr) post: result.status == RMI_ERROR_INPUT |

DRAFT

## B4.5.99.2.1 Failure condition ordering

The RMI\_VSMMU\_FEATURES command does not have any failure condition orderings.

## B4.5.99.3 Success conditions

| ID       | Condition                                                             |
|----------|-----------------------------------------------------------------------|
| features | post: features is populated with VSMMU features supported by the RMM. |

## B4.5.99.4 Footprint

The RMI\_VSMMU\_FEATURES command does not have any footprint.